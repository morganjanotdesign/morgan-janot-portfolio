import re

with open('standalone.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract projects
pattern = r'<article class="project-card" id="(project-0[1-6])"[^>]*>.*?background-color:\s*([^;\"]+);.*?<svg([^>]*)>(.*?)</svg>.*?<div class="frame-category">([^<]+)</div>.*?<h2 class="frame-title">([^<]+)</h2>'
matches = re.findall(pattern, content, re.DOTALL)

projects = []
for m in matches:
    projects.append({
        'id': m[0],
        'bg_color': m[1].strip(),
        'svg_attrs': m[2].strip(),
        'svg_inner': m[3].strip(),
        'category': m[4].strip(),
        'title': m[5].strip()
    })

print(f"Loaded {len(projects)} projects.")
