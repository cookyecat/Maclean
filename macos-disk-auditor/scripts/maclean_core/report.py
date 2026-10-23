"""Offline HTML and Markdown; untrusted text is never markup or code."""
import html
import json
from pathlib import Path
from .rules import PACKAGE

def render(data,output,share=False):
    def text(v):
        if share:
            # Redact all detailed paths/names, including filenames embedded in error text.
            return '[已脱敏]' if ('/' in str(v) or '\\' in str(v)) else str(v)
        return str(v)
    def esc(v): return html.escape(text(v),quote=True)
    def md(v):
        s=text(v)
        for c in '\\`*_{}[]<>()#+-.!|': s=s.replace(c,'\\'+c)
        return s.replace('\n',' ')
    label={'scan':'扫描报告','plan':'待批准计划','receipt':'执行收据'}[data['kind']]
    completeness='完整' if data.get('complete') else '部分结果／有覆盖缺口'
    body=f'<p>{label}'+(f' · {completeness}' if data['kind']=='scan' else '')+'</p>'
    lines=['# MacLean 报告','',f'记录类型：{md(data["kind"])}',f'完整扫描：{md(data.get("complete","不适用"))}','']
    if data['kind']=='scan':
        if 'discovery_complete' in data:
            detail=('目标发现：'+('完整' if data['discovery_complete'] else '未完成')+'；目录计量：'+('完整' if data['measurement_complete'] else '未完成')+'。文件数与时间限制是扫描工作量限制，与费用和 Token 无关。')
            body+='<p>'+esc(detail)+'</p>';lines += [detail,'']
            limits=data.get('limits',{})
            detail=f"每目标最多 {limits.get('entries_per_target')} 次元数据访问、{limits.get('seconds_per_target')} 秒；整轮最多 {limits.get('seconds_total')} 秒。目录大小来自文件元数据累加，不读取文件正文。"
            body+='<p>'+esc(detail)+'</p>';lines += [detail,'']
        groups=[('现在可处理',lambda t:t['selected'] and t['execution_route']!='after_task'),('等待处理',lambda t:t['execution_route']=='after_task'),('保留',lambda t:t['disposition']=='retain'),('待调查',lambda t:not t['selected'] and t['disposition']=='investigate')]
        for category in ['app','ai','development']:
            title_category={'app':'macOS 应用','ai':'AI 客户端','development':'开发项目与工具'}[category]
            body+=f'<h2>{title_category}</h2>';lines+=['## '+title_category,'']
            for title,match in groups:
                rows=[t for t in data['targets'] if t['category']==category and match(t) and t['logical_bytes']>0]
                body+=f'<h3>{title} ({len(rows)})</h3>';lines+=['### '+title,'']
                for t in rows:
                    check=f'<label><input type="checkbox" value="{esc(t["id"])}" checked>选择此目标</label>' if t['selected'] else ''
                    body+=f'<section>{check}<strong>{esc(t["purpose"])}</strong><p>{esc(t["path"])}</p><p>逻辑 {t["logical_bytes"]} B · 去重分配 {t["allocated_bytes"]} B · 可选文件 {t["eligible_logical_bytes"]} B</p><details><summary>用途、影响与依据</summary>'
                    lines += [f'- {md(t["purpose"])}：{md(t["path"])}；逻辑 {t["logical_bytes"]} B，分配 {t["allocated_bytes"]} B；ID {t["id"]}']
                    for k in ['rule','impact','recovery','inference_cost_effect','sources','gap','issues']:
                        if not t[k]:continue
                        field={'rule':'规则','impact':'删除影响','recovery':'恢复方式','inference_cost_effect':'模型费用判断','sources':'依据索引','gap':'研究缺口','issues':'未处理原因'}[k]
                        value='根据已确认用途，不预期增加付费模型计算' if k=='inference_cost_effect' and t[k]=='no_expected_increase' else t[k]
                        body+=f'<p>{field}：{esc(value)}</p>';lines += [f'  {field}：{md(value)}']
                    body+='</details></section>'
        body+='<details><summary>扫描覆盖（含空位置与失败）</summary><table><tr><th>规则</th><th>位置</th><th>状态</th></tr>'
        lines+=['','## 扫描覆盖','']
        for c in data['coverage']+data['errors']:
            reasons={'entry_limit':'达到条目数量上限','time_limit':'达到时间上限','cancelled':'用户取消'}
            cause=c.get('limit_reason') or c.get('error','')
            state=c['status']+(' · '+reasons.get(cause,str(cause)) if cause else '')
            if c.get('phase'):state=c['phase']+' · '+state
            body+=f'<tr><td>{esc(c.get("rule",""))}</td><td>{esc(c.get("path",""))}</td><td>{esc(state)}</td></tr>'
            lines += [f'- {md(c.get("rule",""))} {md(c.get("path",""))}：{md(state)}']
        body+='</table></details>'
    elif data['kind']=='plan':
        from .fs import digest
        body+=f'<p>计划 SHA-256：{esc(digest(data))}</p><p>目标 {len(data["actions"])} 项 · 封存文件逻辑大小 {data["logical_bytes"]} B</p><p>确认后不可恢复普通诊断历史；只处理此计划批准的文件或原生域。</p>'
        lines += [f'计划 SHA-256：{digest(data)}',f'目标 {len(data["actions"])} 项；逻辑大小 {data["logical_bytes"]} B','']
        for a in data['actions']:
            body+='<section><h2>'+esc(a['purpose'])+'</h2><p>'+esc(a['path'])+'</p><p>'+esc(a['impact'])+'</p><p>恢复：'+esc(a['recovery'])+'</p>'
            if a.get('native'):body+='<p>原生影响域：'+esc(a['native']['domain']['path'])+'；'+esc(a['native']['effect'])+'</p>'
            body+='<details><summary>精确文件清单</summary><ul>'+''.join('<li>'+esc(f['path'])+'</li>' for f in a['files'])+'</ul></details></section>'
            lines += [f'- {md(a["purpose"])}：{md(a["path"])}；{md(a["impact"])}']
        if data['pending']:body+='<details><summary>未纳入计划的对象</summary><pre>'+esc(data['pending'])+'</pre></details>'
    else:
        counts={state:sum(x['status']==state for x in data['results']) for state in ['completed','pending','failed','skipped']}
        body+='<section>'+''.join(f'<p>{state}：{n}</p>' for state,n in counts.items())+'</section>'
        body+=f'<p>普通文件处理量：{data.get("target_processed_logical_bytes",0)} B · 原清单残留量：{data.get("residual_inventory_logical_bytes",0)} B</p><p>'+esc(data['space_note'])+'</p>'
        lines += [f'{state}：{n}' for state,n in counts.items()]
        for volume,v in data['volumes'].items():
            body+=f'<p>卷 {esc(volume)} 空闲变化：{v["free_delta"]} B</p>';lines += [f'卷 {volume} 空闲变化：{v["free_delta"]} B']
        body+='<table><tr><th>对象</th><th>结果</th><th>说明</th></tr>'
        for r in data['results']:
            body+='<tr><td>'+esc(r['path'])+'</td><td>'+esc(r['status'])+'</td><td>'+esc(r.get('reason','已按计划完成'))+'</td></tr>'
            lines += [f'- {md(r["path"])}：{r["status"]}；{md(r.get("reason","已按计划完成"))}']
        body+='</table>'
    out=Path(output);out.mkdir(parents=True,exist_ok=True)
    (out/'report.html').write_text((PACKAGE/'assets/report.html').read_text().replace('{{BODY}}',body),encoding='utf-8')
    (out/'report.md').write_text('\n'.join(lines),encoding='utf-8')
    return {'html':str((out/'report.html').absolute()),'markdown':str((out/'report.md').absolute())}
