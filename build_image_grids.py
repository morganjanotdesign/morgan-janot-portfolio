import re

with open('standalone.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Verify regex matches for 6 projects
pattern = r'<article class="project-card" id="(project-0[1-6])"[^>]*>.*?background-color:\s*([^;\"]+);.*?<svg([^>]*)>(.*?)</svg>.*?<div class="frame-category">([^<]+)</div>.*?<h2 class="frame-title">([^<]+)</h2>'
matches = re.findall(pattern, content, re.DOTALL)
print("Matches found:", len(matches))
