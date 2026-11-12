import os
import base64
import re
from PIL import Image

def main():
    p1 = '/Users/morganjanot/Desktop/perso/portfolio /portfolio/PROJET /04/bonne photo/new1.jpg'
    p2 = '/Users/morganjanot/Desktop/perso/portfolio /portfolio/PROJET /04/bonne photo/new2.jpg'

    assert os.path.exists(p1), f"File not found: {p1}"
    assert os.path.exists(p2), f"File not found: {p2}"

    print(f"Loading {p1} and {p2}...")
    im1 = Image.open(p1)
    im2 = Image.open(p2)

    # 1. Convert to WebP and save on disk
    os.makedirs('images/project-04', exist_ok=True)
    os.makedirs('images_webp/project-04', exist_ok=True)

    dest_paths = [
        ('images/project-04/1.webp', im1),
        ('images/project-04/new1.webp', im1),
        ('images_webp/project-04/1.webp', im1),
        ('/Users/morganjanot/Desktop/perso/portfolio /portfolio/PROJET /04/bonne photo/new1.webp', im1),
        ('images/project-04/2.webp', im2),
        ('images/project-04/new2.webp', im2),
        ('images_webp/project-04/2.webp', im2),
        ('/Users/morganjanot/Desktop/perso/portfolio /portfolio/PROJET /04/bonne photo/new2.webp', im2),
    ]

    for path, img in dest_paths:
        img.save(path, 'WEBP', quality=88, method=6)
        print(f"Saved {path} ({os.path.getsize(path):,} bytes)")

    # 2. Read base64 of new webp files
    with open('images/project-04/1.webp', 'rb') as f:
        new1_b64 = 'data:image/webp;base64,' + base64.b64encode(f.read()).decode('utf-8')

    with open('images/project-04/2.webp', 'rb') as f:
        new2_b64 = 'data:image/webp;base64,' + base64.b64encode(f.read()).decode('utf-8')

    # 3. Read portfolio.html
    with open('portfolio.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Find view-project-04 section
    p4_match = re.search(r'(<section id="view-project-04".*?</section>)', content, re.DOTALL)
    assert p4_match is not None, "view-project-04 not found"
    p4_content = p4_match.group(1)

    imgs = re.findall(r'<img[^>]*src="([^"]*)"', p4_content)
    assert len(imgs) >= 2, f"Expected at least 2 images in project-04, found {len(imgs)}"

    old_img0 = imgs[0]
    old_img1 = imgs[1]

    assert content.count(old_img0) == 1, "old_img0 does not appear uniquely in portfolio.html"
    assert content.count(old_img1) == 1, "old_img1 does not appear uniquely in portfolio.html"

    # Replace in portfolio.html
    content = content.replace(old_img0, new1_b64, 1)
    content = content.replace(old_img1, new2_b64, 1)

    with open('portfolio.html', 'w', encoding='utf-8') as f:
        f.write(content)

    print("SUCCESS: portfolio.html updated with new1 and new2 WebP images!")

if __name__ == '__main__':
    main()
