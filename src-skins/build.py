import sys
A='/data/p6/pub/guizang-ppt-skill/assets/'
t=open(A+'template.html',encoding='utf-8').read()
fonts='<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Space+Grotesk:wght@400;500;700&family=JetBrains+Mono:wght@400;500&family=Ma+Shan+Zheng&family=ZCOOL+XiaoWei&display=swap" rel="stylesheet">\n'
i=t.index('<style>')
common=open('common.css').read()
for k,name in [('business','商务汇报风'),('tech','科技发布会风'),('guochao','国潮东方风')]:
    css=open(k+'.css').read()
    s=t[:i]+fonts+t[i:]
    s=s.replace('</style>',common+css+'</style>',1)
    s=s.replace('<title>[必填] 替换为 PPT 标题 · Deck Title</title>','<title>[必填] 替换为 PPT 标题 · Deck Title</title>\n<!-- 大飞AIPPT · '+name+'模板（基于 guizang-ppt-skill template.html 扩展） -->',1)
    open(A+f'template-{k}.html','w',encoding='utf-8').write(s)
    print(k,len(s))
