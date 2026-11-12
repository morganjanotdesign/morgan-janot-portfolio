import os
import shutil
import re

standalone_path = 'standalone.html'
portfolio_artifact_path = '/Users/morganjanot/.gemini/antigravity/brain/df18ad40-ac30-4b7a-b04f-f3de4961c66b/portfolio.html'

with open(standalone_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update landing grid card id="project-01" caption
p1_card_start = html.find('id="project-01"')
assert p1_card_start != -1, "project-01 card not found"
p1_card_end = html.find('</article>', p1_card_start)
assert p1_card_end != -1, "project-01 </article> not found"

card_chunk = html[p1_card_start:p1_card_end]
desc_pattern = r'<p class="project-desc">.*?</p>'
new_card_desc = '<p class="project-desc">Comment réintégrer le jeu dans notre quotidien grâce au mobilier modulable ?</p>'
updated_card_chunk, n_rep = re.subn(desc_pattern, new_card_desc, card_chunk, count=1, flags=re.DOTALL)
assert n_rep == 1, f"Failed to replace card desc, n_rep={n_rep}"

html = html[:p1_card_start] + updated_card_chunk + html[p1_card_end:]
print("1. Updated landing page project-01 card caption successfully.")

# 2. Update view-project-01
p1_view_start = html.find('id="view-project-01"')
assert p1_view_start != -1, "view-project-01 not found"
p2_view_start = html.find('id="view-project-02"')
assert p2_view_start != -1, "view-project-02 not found"

sec1 = html[p1_view_start:p2_view_start]

# 2a. Update hero-concept-thesis
old_thesis_pat = r'<p class="hero-concept-thesis">.*?</p>'
new_thesis = '<p class="hero-concept-thesis">\n            Comment réintégrer le jeu dans notre quotidien grâce au mobilier modulable ?\n          </p>'
sec1, n_rep = re.subn(old_thesis_pat, new_thesis, sec1, count=1, flags=re.DOTALL)
assert n_rep == 1, f"Failed to replace hero thesis, n_rep={n_rep}"
print("2a. Updated hero thesis successfully.")

# 2b. Update narrative body
old_narrative_pat = r'<div class="narrative-body">.*?</div>\s*</div>\s*<!-- Fiche technique'
new_narrative = """<div class="narrative-body">
              <p>
                Ce projet répond à un brief : s’inspirer d’une culture pour concevoir un produit. J’ai choisi celle des jeux de construction, comme les Lego ou les Kapla, qui permettent de créer librement et d’inventer son propre univers. Mon enquête révèle que huit personnes interrogées sur dix ressentaient cette liberté en jouant. Pourtant, la majorité a arrêté autour de 13 ans et évoque aujourd’hui le manque de temps et de matériel comme principaux freins. Ce constat m’a amené à l’hypothèse suivante : réintroduire le jeu de construction à l’âge adulte pourrait permettre de retrouver un espace de créativité, d’expression et de liberté au quotidien.
              </p>
            </div>
          </div>

          <!-- Fiche technique"""
sec1, n_rep = re.subn(old_narrative_pat, new_narrative, sec1, count=1, flags=re.DOTALL)
assert n_rep == 1, f"Failed to replace narrative body, n_rep={n_rep}"
print("2b. Updated narrative body successfully.")

# 2c. Extract existing base64 strings for photo 2 and photo 3
imgs_in_sec1 = re.findall(r'<img[^>]+src="(data:image/[^;]+;base64,[^"]+)"', sec1)
assert len(imgs_in_sec1) >= 3, f"Expected at least 3 images in sec1, found {len(imgs_in_sec1)}"
b64_p1_img2 = imgs_in_sec1[1]
b64_p1_img3 = imgs_in_sec1[2]

# 2d. Replace Photo 02 and Photo 03 blocks with side-by-side photo + text
old_photos_pat = r'<!-- 3\. PHOTO 02 EN GRAND FORMAT.*?(?=<!-- 5\. Universal Next Project Teaser)'
new_photos_block = f"""<!-- 3. PHOTO 02 : CHAISE MODULABLE AVEC TEXTE EXPLICATIF À CÔTÉ -->
      <div class="gallery-spaced-pair photo-with-side-text" style="grid-template-columns: 1.15fr 1fr; gap: clamp(36px, 6vw, 80px); align-items: center; max-width: 1200px; margin: clamp(60px, 8vw, 120px) auto; padding: 0 clamp(16px, 4vw, 48px);">
        <!-- Photo 02 à gauche -->
        <div class="white-image-box has-image chair-trans-box" style="aspect-ratio: 1/1; background: transparent !important; background-color: transparent !important; box-shadow: none !important; border: none !important; display: flex; align-items: center; justify-content: center;">
          <img src="{b64_p1_img2}" alt="Fog Chair Modèle 001 - Vue trois-quarts en élévation sans fond" style="position: static !important; max-width: 100%; max-height: 80vh; width: 100%; height: auto; object-fit: contain; filter: drop-shadow(0 25px 45px rgba(0, 0, 0, 0.85));">
        </div>
        <!-- Texte explicatif à droite -->
        <div class="photo-side-text-col" style="display: flex; flex-direction: column; justify-content: center;">
          <span style="font-size: 11px; font-weight: 900; letter-spacing: 0.22em; text-transform: uppercase; color: #ff8533; margin-bottom: 16px;">
            01 // EXPÉRIENCE &amp; GESTE CONSTRUCTIF
          </span>
          <div style="font-size: clamp(16px, 1.3vw, 20px); line-height: 1.7; font-weight: 300; color: #ffffff;">
            <p style="margin: 0; padding: 0; color: #ffffff;">
              Le projet prend la forme d’une chaise modulable inspirée du principe des jeux de construction. Son assemblage simple invite l’utilisateur à participer à la création de son mobilier. Le geste de construire fait ainsi partie de l’expérience de l’objet : on assemble, on expérimente et on transforme.
            </p>
          </div>
        </div>
      </div>

      <!-- 4. PHOTO 03 : TROIS CONFIGURATIONS AVEC TEXTE EXPLICATIF -->
      <div class="gallery-spaced-pair photo-with-side-text" style="grid-template-columns: 1fr 1.15fr; gap: clamp(36px, 6vw, 80px); align-items: center; max-width: 1200px; margin: clamp(60px, 8vw, 120px) auto; padding: 0 clamp(16px, 4vw, 48px);">
        <!-- Texte explicatif à gauche -->
        <div class="photo-side-text-col" style="display: flex; flex-direction: column; justify-content: center;">
          <span style="font-size: 11px; font-weight: 900; letter-spacing: 0.22em; text-transform: uppercase; color: #ff8533; margin-bottom: 16px;">
            01 // MODULARITÉ &amp; 3 CONFIGURATIONS
          </span>
          <div style="font-size: clamp(16px, 1.3vw, 20px); line-height: 1.7; font-weight: 300; color: #ffffff;">
            <p style="margin: 0; padding: 0; color: #ffffff;">
              Un même ensemble de pièces permet de composer trois configurations de chaise. Déclinable en plusieurs coloris, le projet offre différentes possibilités pour s’adapter aux intérieurs et aux préférences de chacun. La chaise devient un mobilier évolutif, avec lequel on retrouve le plaisir de jouer à l’âge adulte.
            </p>
          </div>
        </div>
        <!-- Photo 03 à droite -->
        <div class="white-image-box has-image chair-trans-box" style="aspect-ratio: 4/5; background: transparent !important; background-color: transparent !important; box-shadow: none !important; border: none !important; display: flex; align-items: center; justify-content: center;">
          <img src="{b64_p1_img3}" alt="Fog Chair Modèle 001 - Trio de chaises en équilibre (Tangerine, Vert Acide, Magenta) sans fond" style="position: static !important; max-width: 100%; max-height: 85vh; width: 100%; height: auto; object-fit: contain; filter: drop-shadow(0 30px 55px rgba(0, 0, 0, 0.9));">
        </div>
      </div>

      """

sec1, n_rep = re.subn(old_photos_pat, new_photos_block, sec1, count=1, flags=re.DOTALL)
assert n_rep == 1, f"Failed to replace photo 2 and 3 blocks, n_rep={n_rep}"
print("2c. Replaced Photo 02 and Photo 03 with side-by-side text layout successfully.")

html = html[:p1_view_start] + sec1 + html[p2_view_start:]

# 3. Add responsive style for mobile screens if not present
responsive_css = """    @media (max-width: 860px) {
      .gallery-spaced-pair.photo-with-side-text {
        grid-template-columns: 1fr !important;
      }
    }
"""
if '.gallery-spaced-pair.photo-with-side-text' not in html:
    style_end = html.find('</style>')
    assert style_end != -1, "</style> not found"
    html = html[:style_end] + responsive_css + html[style_end:]
    print("3. Added responsive CSS for photo-with-side-text.")

# 4. Verify file validity
assert html.endswith('</html>\n') or html.endswith('</html>'), "HTML structure compromised"
print(f"File validation: starts with <!DOCTYPE: {html.startswith('<!DOCTYPE')}, ends with </html>: {html.strip().endswith('</html>')}")
print(f"Total HTML length: {len(html):,} chars")

with open(standalone_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated standalone.html successfully.")

# 5. Sync to portfolio.html artifact
if os.path.exists(os.path.dirname(portfolio_artifact_path)):
    shutil.copyfile(standalone_path, portfolio_artifact_path)
    print(f"Copied to artifact {portfolio_artifact_path} ({os.path.getsize(portfolio_artifact_path):,} bytes)")

