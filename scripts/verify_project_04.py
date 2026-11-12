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
if validator.errors:
    print('Errors:', validator.errors[:10])

# 2. Check p tags in view-project-04
p4_match = re.search(r'<section id="view-project-04".*?</section>', html_content, re.DOTALL)
assert p4_match is not None
p4_html = p4_match.group(0)
ps = re.findall(r'<p[^>]*>(.*?)</p>', p4_html, re.DOTALL)
print(f'Project 04 p tags count: {len(ps)}')
assert len(ps) == 3, f"Expected exactly 3 p tags, got {len(ps)}"
for i, p in enumerate(ps):
    print(f'  p[{i}]: {p[:60]}...')

# 3. Check I18N
fr_matches = re.findall(r"'project-04':\s*\[\s*\"(.*?)\",\s*\"(.*?)\",\s*\"(.*?)\"\s*\]", html_content, re.DOTALL)
print(f'Total I18N project-04 blocks with 3 strings: {len(fr_matches)}')
assert len(fr_matches) == 2, f"Expected 2 I18N blocks (FR and EN), got {len(fr_matches)}"

print('FR texts:')
for idx, text in enumerate(fr_matches[0]):
    print(f'  [{idx}]: {text[:60]}...')

print('EN texts:')
for idx, text in enumerate(fr_matches[1]):
    print(f'  [{idx}]: {text[:60]}...')

print('ALL CHECKS PASSED!')
