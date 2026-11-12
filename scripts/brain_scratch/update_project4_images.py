import base64
import re

standalone_path = '/Users/morganjanot/.gemini/antigravity/scratch/mj-portfolio/standalone.html'
portfolio_path = '/Users/morganjanot/.gemini/antigravity/brain/04838ef3-4249-4209-97cb-1440ffec4bcd/portfolio.html'

img1_path = '/Users/morganjanot/.gemini/antigravity/scratch/mj-portfolio/src/assets/images/project-04/chair-perspective-16-9.png'
img2_path = '/Users/morganjanot/.gemini/antigravity/scratch/mj-portfolio/src/assets/images/project-04/chair-joint-exploded-16-9.png'

with open(img1_path, 'rb') as f:
    b64_p1 = base64.b64encode(f.read()).decode('utf-8')

with open(img2_path, 'rb') as f:
    b64_p2 = base64.b64encode(f.read()).decode('utf-8')

print(f"Base64 P1 len: {len(b64_p1)}, Base64 P2 len: {len(b64_p2)}")

with open(standalone_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Locate section 04
sec4_start = content.find('id="view-project-04"')
sec5_start = content.find('id="view-project-05"')
assert sec4_start != -1 and sec5_start != -1, "Sections 04 or 05 not found"

sec4_text = content[sec4_start:sec5_start]

# 1. Replace Image 01 in Section 04
# Target: full-screen-image-block for Image 01
img1_block_match = re.search(r'(<!-- 2\. GRANDE IMAGE PLEIN ÉCRAN.*?)(?=<!-- 3\. IMAGES PLUS PETITES)', sec4_text, re.DOTALL)
assert img1_block_match is not None, "Image 01 block not found in sec4"

new_img1_block = f"""<!-- 2. GRANDE IMAGE PLEIN ÉCRAN : VUE PERSPECTIVE SUR NOIR (SANS FOND) -->
      <div class="full-screen-image-block">
        <div class="white-image-box has-image chair-trans-box" style="aspect-ratio: 16/9; max-height: 85vh; background: transparent; box-shadow: none; border: none;">
          <img src="data:image/png;base64,{b64_p1}" alt="Chaise géométrique minimale et assise en tension textile" style="object-fit: contain; filter: drop-shadow(0 24px 48px rgba(0,0,0,0.8));" loading="lazy" />
        </div>
      </div>

      """

sec4_text = sec4_text[:img1_block_match.start()] + new_img1_block + sec4_text[img1_block_match.end():]
print("Replaced Image 01 in Section 04")

# 2. Replace Image 03 placeholder in Section 04 with Photo 2
# Target: the second white-image-box in the gallery-spaced-pair (Image 03)
img3_target = re.search(r'(<div class="white-image-box" style="aspect-ratio: 16/10;">.*?<h4 class="placeholder-title">IMAGE 03</h4>.*?</div>\s*</div>)', sec4_text, re.DOTALL)
assert img3_target is not None, "Image 03 block not found in sec4"

new_img3_block = f"""<div class="white-image-box has-image chair-trans-box" style="aspect-ratio: 16/9; max-height: 75vh; background: transparent; box-shadow: none; border: none;">
          <img src="data:image/png;base64,{b64_p2}" alt="Détail vue éclatée de la traverse et des vis d'assemblage" style="object-fit: contain; filter: drop-shadow(0 20px 40px rgba(0,0,0,0.75));" loading="lazy" />
        </div>
      </div>"""

sec4_text = sec4_text[:img3_target.start()] + new_img3_block + sec4_text[img3_target.end():]
print("Replaced Image 03 in Section 04")

# Re-assemble content
new_content = content[:sec4_start] + sec4_text + content[sec5_start:]

with open(standalone_path, 'w', encoding='utf-8') as f:
    f.write(new_content)
print("Updated standalone.html successfully")

with open(portfolio_path, 'w', encoding='utf-8') as f:
    f.write(new_content)
print("Updated portfolio.html successfully")
