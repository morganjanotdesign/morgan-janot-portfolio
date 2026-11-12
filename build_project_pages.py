import re

with open('standalone.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Extract SVG and color data for all 6 projects
pattern = r'<article class="project-card" id="(project-0[1-6])"[^>]*>.*?background-color:\s*([^;\"]+);.*?<svg([^>]*)>(.*?)</svg>.*?<div class="frame-category">([^<]+)</div>.*?<h2 class="frame-title">([^<]+)</h2>'
matches = re.findall(pattern, content, re.DOTALL)

projects_data = {}
for m in matches:
    pid = m[0]
    bg_color = m[1].strip()
    svg_attrs = m[2].strip()
    svg_inner = m[3].strip()
    cat = m[4].strip()
    title = m[5].strip()
    projects_data[pid] = {
        'id': pid,
        'bg_color': bg_color,
        'svg_attrs': svg_attrs,
        'svg_inner': svg_inner,
        'category': cat,
        'title': title
    }

print("Extracted", len(projects_data), "projects")
for pid, d in projects_data.items():
    print(pid, ":", d['title'], "-", d['bg_color'])
