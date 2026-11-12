import os
import base64
import re

def to_base64_uri(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    if ext == '.png':
        mime = 'image/png'
    elif ext in ['.jpg', '.jpeg']:
        mime = 'image/jpeg'
    elif ext == '.webp':
        mime = 'image/webp'
    else:
        mime = 'image/png'
    with open(file_path, 'rb') as f:
        data = f.read()
    b64 = base64.b64encode(data).decode('ascii')
    return f'data:{mime};base64,{b64}'

# 1. Base64 URIs
b64_p1_img2 = to_base64_uri('src/assets/images/project-01/12.png')
b64_p1_img3 = to_base64_uri('src/assets/images/project-01/13.png')

b64_p2_img4 = to_base64_uri('src/assets/images/project-02/Gemini_Generated_Image_np88z9np88z9np88.jpg')
b64_p2_img5 = to_base64_uri('src/assets/images/project-02/Gemini_Genemage_45c55i45c55i45c5.jpg')

b64_p5_img2_insitu = to_base64_uri('src/assets/images/project-05/Untitled.png')
b64_p5_img4_wheels = to_base64_uri('src/assets/images/project-05/wheels_transparent.png')

with open('standalone.html', 'r', encoding='utf-8') as f:
    html = f.read()

# -------------------------------------------------------------
# A. Add Universal Hover Zoom styles into <style>
# -------------------------------------------------------------
zoom_css = """    /* Universal subtle hover zoom on all photos */
    .white-image-box {
      overflow: hidden;
    }
    .white-image-box.chair-trans-box,
    .white-image-box.lamp-trans-box,
    .white-image-box.speaker-trans-box,
    .leo-native-wrap {
      overflow: visible;
    }
    .project-detail-section img {
      transition: transform 0.6s cubic-bezier(0.25, 1, 0.5, 1), filter 0.6s ease !important;
      will-change: transform;
    }
    .white-image-box:hover img,
    .full-screen-image-block:hover img,
    .leo-native-wrap:hover img,
    .photo-with-side-text:hover img,
    .gallery-spaced-pair:hover img,
    .project-detail-section img:hover {
      transform: scale(1.035) !important;
    }
"""

if '/* Universal subtle hover zoom on all photos */' not in html:
    style_idx = html.find('</style>')
    assert style_idx != -1
    html = html[:style_idx] + zoom_css + html[style_idx:]
    print("Added universal hover zoom CSS")

# -------------------------------------------------------------
# B. Update Project 01: Make photo 2 and 3 individual large blocks
# -------------------------------------------------------------
p1_start = html.find('id="view-project-01"')
p2_start = html.find('id="view-project-02"')
sec1 = html[p1_start:p2_start]

old_p1_duo_pattern = r'<!-- 3\. IMAGES DUO ESPACÉES SUR FOND NOIR PUR.*?(?=<!-- 5\. Universal Next Project Teaser)'
m_p1 = re.search(old_p1_duo_pattern, sec1, re.DOTALL)
assert m_p1 is not None, "Project 01 duo block not found"

new_p1_blocks = f"""<!-- 3. PHOTO 02 EN GRAND FORMAT : VUE EN ÉLÉVATION 3/4 SUR FOND NOIR (SANS FOND BLANC) -->
      <div class="full-screen-image-block" style="margin-top: clamp(60px, 8vw, 120px); margin-bottom: clamp(60px, 8vw, 120px);">
        <div class="white-image-box has-image chair-trans-box" style="aspect-ratio: 1/1; max-width: 960px; max-height: 85vh; margin: 0 auto; background: transparent !important; background-color: transparent !important; box-shadow: none !important; border: none !important; display: flex; align-items: center; justify-content: center;">
          <img src="{b64_p1_img2}" alt="Fog Chair Modèle 001 - Vue trois-quarts en élévation sur piètement courbé" style="position: static !important; max-width: 960px; max-height: 85vh; width: 100%; height: auto; object-fit: contain; filter: drop-shadow(0 25px 45px rgba(0, 0, 0, 0.85));">
        </div>
      </div>

      <!-- 4. PHOTO 03 EN GRAND FORMAT : TOTEM TRICOLORE EN ÉQUILIBRE SUR FOND NOIR (SANS FOND BLANC) -->
      <div class="full-screen-image-block" style="margin-top: clamp(60px, 8vw, 120px); margin-bottom: clamp(60px, 8vw, 120px);">
        <div class="white-image-box has-image chair-trans-box" style="aspect-ratio: 4/5; max-width: 900px; max-height: 90vh; margin: 0 auto; background: transparent !important; background-color: transparent !important; box-shadow: none !important; border: none !important; display: flex; align-items: center; justify-content: center;">
          <img src="{b64_p1_img3}" alt="Fog Chair Modèle 001 - Trio de chaises en équilibre sculptural" style="position: static !important; max-width: 900px; max-height: 90vh; width: 100%; height: auto; object-fit: contain; filter: drop-shadow(0 30px 55px rgba(0, 0, 0, 0.9));">
        </div>
      </div>

      """

sec1_updated = sec1[:m_p1.start()] + new_p1_blocks + sec1[m_p1.end():]
html = html[:p1_start] + sec1_updated + html[p2_start:]
print("Updated Project 01 photos 2 and 3 in grand format")

# -------------------------------------------------------------
# C. Update Project 02: Make photo 5 en plus grand
# -------------------------------------------------------------
p2_start = html.find('id="view-project-02"')
p3_start = html.find('id="view-project-03"')
sec2 = html[p2_start:p3_start]

old_p2_duo_pattern = r'<!-- 5\. DUO GÉOMÉTRIQUE D\'ATELIER.*?(?=<!-- 5\. Universal Next Project Teaser)'
m_p2 = re.search(old_p2_duo_pattern, sec2, re.DOTALL)
assert m_p2 is not None, "Project 02 duo block not found"

new_p2_blocks = f"""<!-- 5. PHOTO 04 : DÉTAIL ROTULE FACETTÉE (16/9) -->
      <div class="gallery-spaced-pair" style="max-width: 900px; margin: clamp(60px, 8vw, 120px) auto;">
        <div class="white-image-box has-image" style="aspect-ratio: 16/9; width: 100%;">
          <img src="{b64_p2_img4}" alt="Gros plan sur la rotule à facettes et l'anneau passe-câble" loading="lazy" />
        </div>
      </div>

      <!-- 6. PHOTO 05 EN PLUS GRAND : CUBE CONNECTEUR PLEIN ÉCRAN (16/9) -->
      <div class="full-screen-image-block" style="margin-top: clamp(60px, 8vw, 120px); margin-bottom: clamp(60px, 8vw, 120px);">
        <div class="white-image-box has-image" style="aspect-ratio: 16/9; max-height: 85vh;">
          <img src="{b64_p2_img5}" alt="Cube connecteur géométrique à facettes usiné avec filetages" loading="lazy" />
        </div>
      </div>

      """

sec2_updated = sec2[:m_p2.start()] + new_p2_blocks + sec2[m_p2.end():]
html = html[:p2_start] + sec2_updated + html[p3_start:]
print("Updated Project 02 photo 5 in grand format")

# -------------------------------------------------------------
# D. Update Project 05: Swap photo 2 and photo 4 & transparent wheels
# -------------------------------------------------------------
p5_start = html.find('id="view-project-05"')
p6_start = html.find('id="view-project-06"')
sec5 = html[p5_start:p6_start]

# Replace Photo 2 in sec5: alt="Enceintes acoustiques en situation réelle sur table basse circulaire en chrome et tapis bleu cobalt"
p2_pat = r'(<img\s+[^>]*?alt="Enceintes acoustiques en situation réelle sur table basse circulaire en chrome et tapis bleu cobalt"[^>]*?src=")[^"]+("[^>]*?>)'
m5_2 = re.search(p2_pat, sec5)
if not m5_2:
    p2_pat = r'(<img\s+[^>]*?src=")[^"]+("[^>]*?alt="Enceintes acoustiques en situation réelle sur table basse circulaire en chrome et tapis bleu cobalt"[^>]*?>)'
    m5_2 = re.search(p2_pat, sec5)
assert m5_2 is not None, "P5 photo 2 not found"

sec5 = sec5[:m5_2.start()] + m5_2.group(1) + b64_p5_img2_insitu + m5_2.group(2) + sec5[m5_2.end():]
print("Replaced Project 05 Photo 02 with Untitled.png (in-situ)")

# Replace Photo 4 in sec5: alt="Roues en uréthane bleu cobalt translucide 70mm 78A à l'origine du concept des modules acoustiques"
p4_pat = r'(<img\s+[^>]*?alt="Roues en uréthane bleu cobalt translucide 70mm 78A à l\'origine du concept des modules acoustiques"[^>]*?src=")[^"]+("[^>]*?>)'
m5_4 = re.search(p4_pat, sec5)
if not m5_4:
    p4_pat = r'(<img\s+[^>]*?src=")[^"]+("[^>]*?alt="Roues en uréthane bleu cobalt translucide 70mm 78A à l\'origine du concept des modules acoustiques"[^>]*?>)'
    m5_4 = re.search(p4_pat, sec5)
assert m5_4 is not None, "P5 photo 4 not found"

sec5 = sec5[:m5_4.start()] + m5_4.group(1) + b64_p5_img4_wheels + m5_4.group(2) + sec5[m5_4.end():]
print("Replaced Project 05 Photo 04 with wheels_transparent.png (wheels)")

html = html[:p5_start] + sec5 + html[p6_start:]

# -------------------------------------------------------------
# Save to standalone.html and portfolio.html
# -------------------------------------------------------------
with open('standalone.html', 'w', encoding='utf-8') as f:
    f.write(html)

portfolio_path = '/Users/morganjanot/.gemini/antigravity/brain/df18ad40-ac30-4b7a-b04f-f3de4961c66b/portfolio.html'
with open(portfolio_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Successfully written standalone.html and portfolio.html!")
