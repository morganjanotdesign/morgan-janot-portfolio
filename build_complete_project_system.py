import re, shutil

# Create backup
shutil.copyfile('standalone.html', 'standalone.html.bak')

with open('standalone.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Extract projects info
pattern = r'<article class="project-card" id="(project-0[1-6])"[^>]*>.*?background-color:\s*([^;\"]+);.*?<svg([^>]*)>(.*?)</svg>.*?<div class="frame-category">([^<]+)</div>.*?<h2 class="frame-title">([^<]+)</h2>'
matches = re.findall(pattern, html, re.DOTALL)

pdata = {}
order = []
for m in matches:
    pid = m[0]
    order.append(pid)
    pdata[pid] = {
        'id': pid,
        'bg_color': m[1].strip(),
        'svg_attrs': m[2].strip(),
        'svg_inner': m[3].strip(),
        'category': m[4].strip(),
        'title': m[5].strip()
    }

print("Found", len(pdata), "projects:", order)
