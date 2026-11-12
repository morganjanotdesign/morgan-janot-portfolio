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

print("ALL VERIFICATIONS PASSED PERFECTLY!")
