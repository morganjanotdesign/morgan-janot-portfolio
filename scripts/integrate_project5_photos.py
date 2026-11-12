import base64
import os
import re

standalone_path = "/Users/morganjanot/.gemini/antigravity/scratch/mj-portfolio/standalone.html"
portfolio_path = "/Users/morganjanot/.gemini/antigravity/brain/04838ef3-4249-4209-97cb-1440ffec4bcd/portfolio.html"

uploaded_dir = "/Users/morganjanot/.gemini/antigravity/brain/3f860e7e-8526-4b50-b119-72f2d542be72/.user_uploaded"

img_front_path = os.path.join(uploaded_dir, "media_1790710578440.png")
img_back_path = os.path.join(uploaded_dir, "media_1790710578488.png")
img_threequarter_path = os.path.join(uploaded_dir, "media_1790710578493.png")
img_macro_path = os.path.join(uploaded_dir, "media_1790710578511.jpg")

def get_b64(path, mime):
    with open(path, "rb") as f:
        data = f.read()
    b64_str = base64.b64encode(data).decode('utf-8')
    return f"data:{mime};base64,{b64_str}"

b64_threequarter = get_b64(img_threequarter_path, "image/png")
b64_front = get_b64(img_front_path, "image/png")
b64_back = get_b64(img_back_path, "image/png")
b64_macro = get_b64(img_macro_path, "image/jpeg")

print(f"Loaded base64 for 4 images: lengths = {[len(b64_threequarter), len(b64_front), len(b64_back), len(b64_macro)]}")

with open(standalone_path, "r", encoding="utf-8") as f:
    html = f.read()

# Locate project 05 section
p5_start = html.find('id="view-project-05"')
if p5_start == -1:
    raise Exception("Project 05 section not found in standalone.html!")

p6_start = html.find('id="view-project-06"')
if p6_start == -1:
    raise Exception("Project 06 section not found in standalone.html!")

# Extract SVG illustration for Project 05 to preserve it exactly
p5_chunk = html[p5_start:p6_start]
svg_match = re.search(r'(<div class="frame-illustration">[\s\S]*?</div>)', p5_chunk)
if not svg_match:
    raise Exception("Project 05 SVG not found!")
svg_p5 = svg_match.group(1).strip()

new_project_05 = f"""    <!-- VIEW DETAIL: PROJET 05 (ENCEINTES ACOUSTIQUES) -->
    <section id="view-project-05" class="view-panel project-detail-section">
      <!-- Top Navigation Bar -->
      <div class="project-header-bar">
        <button type="button" class="project-nav-btn btn-back-portfolio" data-target="portfolio">
          <span aria-hidden="true">&larr;</span>
          <span class="link-line">Retourner au portfolio</span>
        </button>
        <div class="project-counter-pill">PROJET [ 05 / 06 ]</div>
        <div class="project-nav-arrows">
          <button type="button" class="project-nav-btn prev btn-switch-project" data-target-project="project-04" aria-label="Projet précédent">
            <span aria-hidden="true">&larr;</span>
            <span>Précédent</span>
          </button>
          <button type="button" class="project-nav-btn next btn-switch-project" data-target-project="project-06" aria-label="Projet suivant">
            <span>Suivant</span>
            <span aria-hidden="true">&rarr;</span>
          </button>
        </div>
      </div>

      <!-- 1. HERO DUAL ROW : CARTE COULEUR & TEXTE EXPLICATIF CÔTE À CÔTE -->
      <div class="project-hero-dual ">
        <!-- Carte Couleur Signature avec Texture Papier -->
        <div class="hero-card-col">
          <div class="project-art-frame" style="background-color: rgb(200, 75, 255); aspect-ratio: 4/5;">
            {svg_p5}
            <div class="project-detail-cartouche">
              <div class="detail-cartouche-tag">05 — Design Produit // Son Haute-Fidélité</div>
              <h2 class="detail-cartouche-title">* ENCEINTES ACOUSTIQUES *</h2>
              <div class="detail-cartouche-meta">
                <span>STÉRÉO BI-AMPLIFIÉE</span>
                <span style="font-size: 13px;">*</span>
                <span>ALUMINIUM BROSSÉ &amp; BLEU COBALT</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Texte Explicatif : Base du projet, pourquoi & specs -->
        <div class="hero-text-col">
          <div class="editorial-tag-row" style="margin-bottom: 16px;">
            <span class="editorial-tag">05 // Studio Acoustique</span>
            <span class="chroma-badge" style="background: rgba(200, 75, 255, 0.15); color: #d97dff; border: 1px solid rgba(200, 75, 255, 0.4);">
              * CYLINDRES DÉCOUPLÉS &amp; PIÈTEMENT CRUCIFORME *
            </span>
          </div>

          <h1 class="hero-concept-title">Enceintes Acoustiques</h1>
          <p class="hero-concept-thesis">Un système d'écoute stéréophonique sculpturale alliant deux modules acoustiques bleu cobalt, un plateau d'amplification analogique et un piètement cruciforme autoportant.</p>

          <div class="hero-narrative-card">
            <div class="narrative-header">
              <span class="narrative-dot" style="background: rgb(200, 75, 255);"></span>
              <span>GENÈSE &amp; BASE DU PROJET</span>
            </div>
            <div class="narrative-body">
              <p>Pourquoi cette pièce ? Elle repense la présence spatiale et sculpturale de l'enceinte de monitoring. Loin des coffrages monolithiques cubiques, le système désolidarise les deux chambres acoustiques cylindriques pour projeter un champ stéréophonique d'une clarté chirurgicale.</p>
              <p>Chaque cylindre laqué bleu cobalt intègre un haut-parleur large bande à membrane texturée haute fidélité. La base circulaire en noir mat accueille les potentiomètres de réglage analogique à crans, tandis que le piètement cruciforme en aluminium brossé assure un découplage mécanique absolu avec la surface d'appui.</p>
            </div>
          </div>

          <!-- Fiche technique atelier épurée -->
          <div class="project-specs-bar" style="margin-bottom: 0;">
            <span>Configuration : <span class="spec-val">Stéréo 2 voies bi-amplifiée</span></span>
            <span class="spec-sep">&bull;</span>
            <span>Matériaux : <span class="spec-val">Aluminium brossé, cylindres ABS bleu cobalt</span></span>
            <span class="spec-sep">&bull;</span>
            <span>Contrôles : <span class="spec-val">Potentiomètres analogiques à crans</span></span>
            <span class="spec-sep">&bull;</span>
            <span>Acoustique : <span class="spec-val">Découplage mécanique par piètement croix</span></span>
          </div>
        </div>
      </div>

      <!-- 2. GRANDE IMAGE PLEIN ÉCRAN : VUE PERSPECTIVE TROIS-QUARTS DÉTOURÉE (16:9) -->
      <div class="full-screen-image-block">
        <div class="white-image-box has-image" style="aspect-ratio: 16/9; max-height: 80vh; background-color: #ffffff; display: flex; align-items: center; justify-content: center;">
          <img src="{b64_threequarter}" alt="Enceintes acoustiques stéréophoniques, vue trois-quarts perspective" style="object-fit: contain !important; padding: clamp(24px, 4vw, 56px);" loading="lazy" />
        </div>
      </div>

      <!-- 3. DUO SYMÉTRIQUE : VUE DE FACE CONTRE-PLONGÉE & VUE ARRIÈRE CONNECTIQUES (16:10) -->
      <div class="gallery-spaced-pair equal" style="grid-template-columns: 1fr 1fr; gap: clamp(36px, 5.5vw, 80px); align-items: center;">
        <!-- Photo 2 : Vue de face contre-plongée -->
        <div class="white-image-box has-image" style="aspect-ratio: 16/10; background-color: #ffffff; display: flex; align-items: center; justify-content: center;">
          <img src="{b64_front}" alt="Enceintes acoustiques, vue de face en contre-plongée" style="object-fit: contain !important; padding: clamp(20px, 3vw, 44px);" loading="lazy" />
        </div>
        <!-- Photo 3 : Vue arrière connectiques et câbles -->
        <div class="white-image-box has-image" style="aspect-ratio: 16/10; background-color: #ffffff; display: flex; align-items: center; justify-content: center;">
          <img src="{b64_back}" alt="Enceintes acoustiques, vue arrière connectiques et chambres acoustiques" style="object-fit: contain !important; padding: clamp(20px, 3vw, 44px);" loading="lazy" />
        </div>
      </div>

      <!-- 4. IMAGE CENTRÉE MACRO : CÔNES D'ENCEINTES & POTENTIOMÈTRES ANALOGIQUES (16:9) -->
      <div class="gallery-centered-small" style="max-width: 960px; margin: clamp(48px, 6vw, 80px) auto 0;">
        <div class="white-image-box has-image" style="aspect-ratio: 16/9; background-color: #000000; overflow: hidden; display: flex; align-items: center; justify-content: center;">
          <img src="{b64_macro}" alt="Gros plan macro sur les membranes des haut-parleurs et potentiomètres analogiques" style="object-fit: cover !important; padding: 0 !important; width: 100%; height: 100%;" loading="lazy" />
        </div>
      </div>

      <!-- 4. Universal Next Project Teaser Footer -->
      <div class="project-footer-card" style="margin-top: clamp(80px, 10vw, 150px);">
        <div class="next-teaser-info">
          <div class="next-teaser-swatch" style="background-color: rgb(255, 235, 0);"></div>
          <div>
            <div style="font-size: 11px; font-weight: 900; letter-spacing: 0.2em; text-transform: uppercase; color: #888888; margin-bottom: 4px;">
              Projet Suivant &bull; 06
            </div>
            <div style="font-size: clamp(18px, 1.8vw, 24px); font-weight: 900; color: #ffffff;">
              Arche Radiale
            </div>
          </div>
        </div>
        <button type="button" class="project-nav-btn next btn-switch-project" data-target-project="project-06" style="font-size: 13px;">
          <span>Découvrir la pièce</span>
          <span aria-hidden="true">&rarr;</span>
        </button>
      </div>
    </section>
"""

sec_p5_start = html.rfind("<section", 0, p5_start)
sec_p5_end = html.find("</section>", p5_start) + len("</section>")

html = html[:sec_p5_start] + new_project_05.strip() + "\n\n    " + html[sec_p5_end:]

with open(standalone_path, "w", encoding="utf-8") as f:
    f.write(html)
print(f"Updated {standalone_path}! New size: {len(html)}")

try:
    if os.path.exists(portfolio_path):
        with open(portfolio_path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Updated {portfolio_path}! New size: {len(html)}")
except PermissionError:
    print(f"Note: Cannot write to legacy {portfolio_path} (cross-conversation sandbox restriction).")

# Also write to current conversation brain directory
current_portfolio = "/Users/morganjanot/.gemini/antigravity/brain/3f860e7e-8526-4b50-b119-72f2d542be72/portfolio.html"
with open(current_portfolio, "w", encoding="utf-8") as f:
    f.write(html)
print(f"Updated current conversation copy: {current_portfolio}! New size: {len(html)}")
