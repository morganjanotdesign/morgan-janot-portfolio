import html.parser
import re

with open('portfolio.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# 1. HTML validity parser
class HTMLValidator(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.self_closing = {'img', 'br', 'hr', 'input', 'meta', 'link'}
        self.errors = []

    def handle_starttag(self, tag, attrs):
        if tag not in self.self_closing:
            self.stack.append(tag)

    def handle_endtag(self, tag):
        if tag in self.self_closing:
            return
        if not self.stack:
            self.errors.append(f'Unexpected end tag: </{tag}>')
            return
        last = self.stack.pop()
        if last != tag:
            self.errors.append(f'Mismatched tag: expected </{last}>, found </{tag}>')

validator = HTMLValidator()
validator.feed(html_content)
print(f'HTML Validator errors: {len(validator.errors)}')
assert len(validator.errors) == 0, f"HTML errors: {validator.errors}"

# 2. Check p tags in view-project-03
p3_match = re.search(r'<section id="view-project-03".*?</section>', html_content, re.DOTALL)
assert p3_match is not None
p3_html = p3_match.group(0)
ps = re.findall(r'<p[^>]*>(.*?)</p>', p3_html, re.DOTALL)
print(f'Project 03 DOM p tags count: {len(ps)}')
assert len(ps) == 4, f"Expected exactly 4 p tags, got {len(ps)}"
for i, p in enumerate(ps):
    print(f'  p[{i}]: {p[:60]}...')

# 3. Check I18N project-03 in FR and EN
matches = re.findall(r"'project-03':\s*\[(.*?)\]", html_content, re.DOTALL)
assert len(matches) == 2, f"Expected 2 project-03 I18N blocks, found {len(matches)}"

fr_items = re.findall(r'"(.*?)"', matches[0])
print(f"FR project-03 verified with {len(fr_items)} items:")
assert len(fr_items) == 4, f"Expected 4 FR items, got {len(fr_items)}"
for i, item in enumerate(fr_items):
    print(f"  [{i}]: {item[:60]}...")

en_items = re.findall(r'"(.*?)"', matches[1])
print(f"EN project-03 verified with {len(en_items)} items:")
assert len(en_items) == 4, f"Expected 4 EN items, got {len(en_items)}"
for i, item in enumerate(en_items):
    print(f"  [{i}]: {item[:60]}...")

# 4. Check all projects match between DOM and I18N
print("Checking all projects DOM vs I18N consistency:")
for i in range(1, 7):
    pid = f"project-0{i}"
    proj_view_match = re.search(r'<section id="view-' + pid + r'".*?</section>', html_content, re.DOTALL)
    assert proj_view_match is not None
    dom_ps = re.findall(r'<p[^>]*>', proj_view_match.group(0))
    p_i18n = re.findall(r"'" + pid + r"':\s*\[(.*?)\]", html_content, re.DOTALL)
    assert len(p_i18n) == 2, f"Expected 2 I18N blocks for {pid}"
    fr_count = len(re.findall(r'"(.*?)"', p_i18n[0]))
    en_count = len(re.findall(r'"(.*?)"', p_i18n[1]))
    assert len(dom_ps) == fr_count == en_count, f"Mismatch for {pid}: DOM={len(dom_ps)}, FR={fr_count}, EN={en_count}"
    print(f"  {pid}: {len(dom_ps)} DOM p tags == {fr_count} FR items == {en_count} EN items (OK)")

# 5. Check legacy portfolio elements are permanently locked & hidden
legacy_ids = [
    'top-bar',
    'portfolio-bg-year',
    'project-hover-desc-left',
    'project-hover-desc-right',
    'intro-curtain',
    'projects-drawer',
    'drawer-overlay',
    'portfolio-mobile-desc',
]
for lid in legacy_ids:
    m = re.search(r'<[a-zA-Z0-9]+\s+[^>]*id="' + re.escape(lid) + r'"[^>]*>', html_content)
    assert m is not None, f"Legacy element #{lid} tag not found"
    tag_str = m.group(0)
    assert 'hidden' in tag_str and 'display:none !important' in tag_str, f"Legacy element #{lid} is missing inline hidden lock: {tag_str}"
print(f"Legacy elements inline HTML lock verified for {len(legacy_ids)} IDs (OK)")

assert '#top-bar,' in html_content and 'display: none !important;' in html_content, "Missing global CSS lock for #top-bar and legacy elements"
print("Global CSS lock for legacy portfolio elements verified (OK)")

# 6. Check index.html == portfolio.html and no base64 WebP bloat
with open('index.html', 'r', encoding='utf-8') as f_idx:
    index_content = f_idx.read()
assert html_content == index_content, "index.html and portfolio.html are out of sync!"
assert 'data:image/webp;base64,' not in html_content, "Found unoptimized base64 WebP data URI in HTML!"
print("index.html and portfolio.html sync + external WebP optimization verified (OK)")

print("ALL VERIFICATIONS PASSED PERFECTLY!")
