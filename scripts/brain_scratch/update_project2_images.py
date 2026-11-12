import base64
import re

standalone_path = '/Users/morganjanot/.gemini/antigravity/scratch/mj-portfolio/standalone.html'
portfolio_path = '/Users/morganjanot/.gemini/antigravity/brain/04838ef3-4249-4209-97cb-1440ffec4bcd/portfolio.html'

img1_path = '/Users/morganjanot/.gemini/antigravity/scratch/mj-portfolio/src/assets/images/project-02/lamp-concrete-base-full-16-9.jpg'
img2_path = '/Users/morganjanot/.gemini/antigravity/scratch/mj-portfolio/src/assets/images/project-02/lamp-upper-articulation-16-9.png'

with open(img1_path, 'rb') as f:
    b64_img1 = base64.b64encode(f.read()).decode('utf-8')

with open(img2_path, 'rb') as f:
    b64_img2 = base64.b64encode(f.read()).decode('utf-8')

print(f"B64 img1 len: {len(b64_img1)}, B64 img2 len: {len(b64_img2)}")

with open(standalone_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update CSS to include .lamp-trans-box
css_target = ".chair-trans-box {"
css_replacement = ".chair-trans-box, .speaker-trans-box, .lamp-trans-box {"
if css_target in content:
    content = content.replace(css_target, css_replacement)
    print("Updated CSS with .lamp-trans-box")

# 2. Locate Section 02
sec2_start = content.find('id="view-project-02"')
sec3_start = content.find('id="view-project-03"')
assert sec2_start != -1 and sec3_start != -1, "Sections not found"

sec2_text = content[sec2_start:sec3_start]

# 3. Replace Photo 1 in sec2
# Find the first full-screen-image-block in sec2
p1_match = re.search(r'(<!-- 2\. GRANDE IMAGE PLEIN ÉCRAN : SOCLE BÉTON.*?)(?=<!-- 3\. PHOTO 2)', sec2_text, re.DOTALL)
assert p1_match is not None, "Photo 1 block not found in sec2"

new_p1_block = f"""<!-- 2. GRANDE IMAGE PLEIN ÉCRAN : SOCLE BÉTON & ÉLÉVATION COMPLÈTE (16:9) -->
      <div class="full-screen-image-block">
        <div class="white-image-box has-image" style="aspect-ratio: 16/9; max-height: 80vh;">
          <img src="data:image/jpeg;base64,{b64_img1}" alt="Lampadaire articulé avec socle en béton brut et câble orange" loading="lazy" />
        </div>
      </div>

      """

sec2_text = sec2_text[:p1_match.start()] + new_p1_block + sec2_text[p1_match.end():]
print("Replaced Photo 1 block in sec2")

# 4. Replace Photo 3 in sec2
# Find the Photo 3 block in sec2
p3_match = re.search(r'(<!-- 4\. PHOTO 3 : EN DESSOUS DE LA PHOTO 2.*?)(?=<!-- 5\. DUO GÉOMÉTRIQUE)', sec2_text, re.DOTALL)
assert p3_match is not None, "Photo 3 block not found in sec2"

new_p3_block = f"""<!-- 4. PHOTO 03 : EN DESSOUS DE LA PHOTO 02 (GRANDE VUE PLEIN ÉCRAN 16:9 - SANS FOND) -->
      <div class="full-screen-image-block" style="margin-top: clamp(60px, 8vw, 120px); margin-bottom: clamp(60px, 8vw, 120px);">
        <div class="white-image-box has-image lamp-trans-box" style="aspect-ratio: 16/9; max-height: 85vh; background: transparent; box-shadow: none; border: none;">
          <img src="data:image/png;base64,{b64_img2}" alt="Bras articulé télescopique et passage de câble orange" style="object-fit: contain; filter: drop-shadow(0 20px 40px rgba(0,0,0,0.75));" loading="lazy" />
        </div>
      </div>

      """

sec2_text = sec2_text[:p3_match.start()] + new_p3_block + sec2_text[p3_match.end():]
print("Replaced Photo 3 block in sec2")

# Re-assemble content
new_content = content[:sec2_start] + sec2_text + content[sec3_start:]

with open(standalone_path, 'w', encoding='utf-8') as f:
    f.write(new_content)
print("Updated standalone.html successfully")

with open(portfolio_path, 'w', encoding='utf-8') as f:
    f.write(new_content)
print("Updated portfolio.html successfully")
