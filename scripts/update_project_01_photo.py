import os
import base64
import re
from PIL import Image

def main():
    src_path = '/Users/morganjanot/Desktop/perso/portfolio /portfolio/PROJET /01/new.JPG'
    assert os.path.exists(src_path), f"File not found: {src_path}"

    print(f"Loading {src_path}...")
    im = Image.open(src_path)

    # 1. Convert to WebP and save
    os.makedirs('images/project-01', exist_ok=True)
    os.makedirs('images_webp/project-01', exist_ok=True)

    dest_paths = [
        'images/project-01/new.webp',
        'images_webp/project-01/new.webp',
        '/Users/morganjanot/Desktop/perso/portfolio /portfolio/PROJET /01/new.webp'
    ]

    for dest in dest_paths:
        im.save(dest, 'WEBP', quality=88, method=6)
        print(f"Saved {dest} ({os.path.getsize(dest):,} bytes)")

    with open('images/project-01/new.webp', 'rb') as f:
        new_b64 = 'data:image/webp;base64,' + base64.b64encode(f.read()).decode('utf-8')

    # 2. Read portfolio.html
    with open('portfolio.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the target wireframe box in Section 3 of view-project-01
    target_wireframe = """              <div class="proj-wireframe-box proj-ratio-4-3">
                <svg viewBox="0 0 100 100" preserveAspectRatio="none" class="proj-wireframe-svg" aria-label="Recherche et croquis de conception">
                  <rect x="0.5" y="0.5" width="99" height="99" fill="#ffffff" stroke="#000000" stroke-width="1.2" vector-effect="non-scaling-stroke"/>
                  <line x1="0" y1="0" x2="100" y2="100" stroke="#000000" stroke-width="1.2" vector-effect="non-scaling-stroke"/>
                  <line x1="100" y1="0" x2="0" y2="100" stroke="#000000" stroke-width="1.2" vector-effect="non-scaling-stroke"/>
                </svg>
              </div>"""

    replacement_media = f"""              <div class="proj-media proj-ratio-4-3">
                <img src="{new_b64}" alt="Recherches de formes et croquis de conception" class="proj-img is-cover" loading="lazy" decoding="async">
              </div>"""

    assert target_wireframe in content, "Target wireframe box not found in portfolio.html"
    assert content.count(target_wireframe) == 1, "Target wireframe box appears more than once"

    content = content.replace(target_wireframe, replacement_media, 1)

    with open('portfolio.html', 'w', encoding='utf-8') as f:
        f.write(content)

    print("SUCCESS: portfolio.html updated cleanly with new.webp in cadre vide 1 of Project 1!")

if __name__ == '__main__':
    main()
