import os
import shutil
import re

standalone_path = 'standalone.html'
portfolio_artifact_path = '/Users/morganjanot/.gemini/antigravity/brain/df18ad40-ac30-4b7a-b04f-f3de4961c66b/portfolio.html'

with open(standalone_path, 'r', encoding='utf-8') as f:
    html = f.read()

p1_view_start = html.find('id="view-project-01"')
assert p1_view_start != -1, "view-project-01 not found"
p2_view_start = html.find('id="view-project-02"')
assert p2_view_start != -1, "view-project-02 not found"

sec1 = html[p1_view_start:p2_view_start]

# 1. Remove neon orange chroma-badge in hero editorial tags
chroma_badge_pat = r'<span class="chroma-badge"[^>]*?>\s*\* MODÈLE 001 &bull; ÉDITION ORIGINALE \*\s*</span>'
sec1, n_rep = re.subn(chroma_badge_pat, '', sec1, count=1)
print(f"1. Removed chroma-badge: {n_rep} occurrences removed")

# 2. Make narrative dot neutral
narrative_dot_pat = r'<span class="narrative-dot" style="background: rgb\(255, 94, 0\);"></span>'
new_narrative_dot = '<span class="narrative-dot" style="background: rgba(255, 255, 255, 0.6);"></span>'
sec1, n_rep = re.subn(narrative_dot_pat, new_narrative_dot, sec1, count=1)
print(f"2. Neutralized narrative-dot: {n_rep} occurrences updated")

# 3. Extract existing base64 strings for photo 2 and photo 3
imgs_in_sec1 = re.findall(r'<img[^>]+src="(data:image/[^;]+;base64,[^"]+)"', sec1)
assert len(imgs_in_sec1) >= 3, f"Expected at least 3 images in sec1, found {len(imgs_in_sec1)}"
b64_p1_img2 = imgs_in_sec1[1]
b64_p1_img3 = imgs_in_sec1[2]

# 4. Replace Photo 02 and Photo 03 blocks with:
#    - significantly enlarged images (1.85fr, max-height 92vh / 94vh, max-width 1440px)
#    - reduced side text (font-size: clamp(13px, 1.05vw, 15px), max-width 440px, subtle gray color)
#    - complete removal of orange titles and neon orange styling
old_photos_pat = r'<!-- 3\. PHOTO 02 : CHAISE MODULABLE AVEC TEXTE EXPLICATIF.*?(?=<!-- 5\. Universal Next Project Teaser)'

new_photos_block = f"""<!-- 3. PHOTO 02 : CHAISE MODULABLE EN GRAND AVEC TEXTE RÉDUIT À CÔTÉ -->
      <div class="gallery-spaced-pair photo-with-side-text" style="grid-template-columns: 1.85fr 1fr; gap: clamp(36px, 6vw, 90px); align-items: center; max-width: 1440px; margin: clamp(60px, 8vw, 120px) auto; padding: 0 clamp(16px, 4vw, 48px);">
        <!-- Photo 02 à gauche (grand format) -->
        <div class="white-image-box has-image chair-trans-box" style="aspect-ratio: 1/1; max-height: 92vh; background: transparent !important; background-color: transparent !important; box-shadow: none !important; border: none !important; display: flex; align-items: center; justify-content: center;">
          <img src="{b64_p1_img2}" alt="Fog Chair Modèle 001 - Vue trois-quarts en élévation sans fond" style="position: static !important; max-width: 100%; max-height: 92vh; width: 100%; height: auto; object-fit: contain; filter: drop-shadow(0 28px 50px rgba(0, 0, 0, 0.9));">
        </div>
        <!-- Texte explicatif à droite (format réduit, sans titre orange) -->
        <div class="photo-side-text-col" style="display: flex; flex-direction: column; justify-content: center; max-width: 440px;">
          <div style="font-size: clamp(13px, 1.05vw, 15px); line-height: 1.75; font-weight: 300; color: #d0d0d0;">
            <p style="margin: 0; padding: 0; color: #d0d0d0;">
              Le projet prend la forme d’une chaise modulable inspirée du principe des jeux de construction. Son assemblage simple invite l’utilisateur à participer à la création de son mobilier. Le geste de construire fait ainsi partie de l’expérience de l’objet : on assemble, on expérimente et on transforme.
            </p>
          </div>
        </div>
      </div>

      <!-- 4. PHOTO 03 : TROIS CONFIGURATIONS EN GRAND AVEC TEXTE RÉDUIT -->
      <div class="gallery-spaced-pair photo-with-side-text" style="grid-template-columns: 1fr 1.85fr; gap: clamp(36px, 6vw, 90px); align-items: center; max-width: 1440px; margin: clamp(60px, 8vw, 120px) auto; padding: 0 clamp(16px, 4vw, 48px);">
        <!-- Texte explicatif à gauche (format réduit, sans titre orange) -->
        <div class="photo-side-text-col" style="display: flex; flex-direction: column; justify-content: center; max-width: 440px; justify-self: end;">
          <div style="font-size: clamp(13px, 1.05vw, 15px); line-height: 1.75; font-weight: 300; color: #d0d0d0;">
            <p style="margin: 0; padding: 0; color: #d0d0d0;">
              Un même ensemble de pièces permet de composer trois configurations de chaise. Déclinable en plusieurs coloris, le projet offre différentes possibilités pour s’adapter aux intérieurs et aux préférences de chacun. La chaise devient un mobilier évolutif, avec lequel on retrouve le plaisir de jouer à l’âge adulte.
            </p>
          </div>
        </div>
        <!-- Photo 03 à droite (grand format) -->
        <div class="white-image-box has-image chair-trans-box" style="aspect-ratio: 4/5; max-height: 94vh; background: transparent !important; background-color: transparent !important; box-shadow: none !important; border: none !important; display: flex; align-items: center; justify-content: center;">
          <img src="{b64_p1_img3}" alt="Fog Chair Modèle 001 - Trio de chaises en équilibre (Tangerine, Vert Acide, Magenta) sans fond" style="position: static !important; max-width: 100%; max-height: 94vh; width: 100%; height: auto; object-fit: contain; filter: drop-shadow(0 32px 60px rgba(0, 0, 0, 0.92));">
        </div>
      </div>

      """

sec1, n_rep = re.subn(old_photos_pat, new_photos_block, sec1, count=1, flags=re.DOTALL)
assert n_rep == 1, f"Failed to replace photo 2 and 3 blocks, n_rep={n_rep}"
print("3. Replaced Photo 02 and Photo 03 with enlarged layouts and reduced side texts.")

html = html[:p1_view_start] + sec1 + html[p2_view_start:]

# Check if any orange text remains in sec1
updated_sec1 = html[p1_view_start:html.find('id="view-project-02"')]
remaining_orange_texts = re.findall(r'color:\s*(?:#ff8533|#ff5e00|orange)', updated_sec1, re.I)
print("Remaining orange text colors in project 1:", remaining_orange_texts)
assert len(remaining_orange_texts) == 0, f"Found remaining orange text colors: {remaining_orange_texts}"

with open(standalone_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated standalone.html successfully.")

if os.path.exists(os.path.dirname(portfolio_artifact_path)):
    shutil.copyfile(standalone_path, portfolio_artifact_path)
    print(f"Copied to artifact {portfolio_artifact_path} ({os.path.getsize(portfolio_artifact_path):,} bytes)")

