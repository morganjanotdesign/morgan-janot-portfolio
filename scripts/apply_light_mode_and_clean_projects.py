import os
import base64
import re

files = [
    'standalone.html',
    'portfolio.html',
    '/Users/morganjanot/.gemini/antigravity/brain/df18ad40-ac30-4b7a-b04f-f3de4961c66b/portfolio.html'
]

# 1. Base64 encode the new P04 images
b64_new_p4 = {}
for f in ['3D.webp', 'plan.webp', 'decoupelaser.webp']:
    p = os.path.join('images/project-04', f)
    with open(p, 'rb') as fp:
        b64_new_p4[f] = base64.b64encode(fp.read()).decode('ascii')

print("Loaded base64 for 3D.webp, plan.webp, decoupelaser.webp")

# 2. Build the updated Project 04 Process HTML
def get_p4_process_html(b64_7196, b64_7215, b64_7205, b64_7229, b64_7233):
    return f"""      <!-- SECTION PROCESS : GRAND TITRE PLEINE PAGE & IMAGES DESSOUS -->
      <section class="project-process-section" id="process-section-p04">
        <div class="process-header">
          <div class="process-eyebrow">
            <span class="process-dot" style="background: rgb(227, 6, 19);"></span>
            <span>04 // PROCESSUS &amp; RECHERCHES STRUCTURELLES</span>
          </div>
          <h2 class="process-giant-title">PROCESS</h2>
          <p class="process-lead-text">
            &Eacute;tudes structurales, mod&eacute;lisation volum&eacute;trique 3D, plans techniques, d&eacute;coupe laser et maquettes d&rsquo;atelier en apesanteur.
          </p>
        </div>

        <!-- 1. &Eacute;TUDES CAO, PLANS TECHNIQUES & D&Eacute;COUPE LASER -->
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: clamp(20px, 2.5vw, 36px); margin-bottom: clamp(32px, 4vw, 48px);">
          <div class="scatter-photo-card" style="aspect-ratio: 16/10;">
            <img src="data:image/webp;base64,{b64_new_p4['3D.webp']}" alt="Mod&eacute;lisation 3D treillis g&eacute;om&eacute;trique - Chaise Suspendue" loading="lazy">
          </div>
          <div class="scatter-photo-card" style="aspect-ratio: 16/10;">
            <img src="data:image/webp;base64,{b64_new_p4['plan.webp']}" alt="Plan technique cot&eacute; et gabarits d'assemblage - Chaise Suspendue" loading="lazy">
          </div>
          <div class="scatter-photo-card" style="aspect-ratio: 16/10;">
            <img src="data:image/webp;base64,{b64_new_p4['decoupelaser.webp']}" alt="D&eacute;coupe laser et usinage num&eacute;rique des membrures - Chaise Suspendue" loading="lazy">
          </div>
        </div>

        <!-- 2. MAQUETTES D'ATELIER &amp; PROTOTYPES &Agrave; L'&Eacute;CHELLE -->
        <div class="conception-scatter-stage scatter-5">
          <!-- Colonne 1 : Photos 01 & 03 -->
          <div class="scatter-col">
            <div class="scatter-photo-card aspect-4-3 scatter-p04-1 scatter-item-1">
              <img src="data:image/webp;base64,{b64_7196}" alt="Conception Chaise Suspendue - Maquette atelier 01" loading="lazy">
            </div>
            <div class="scatter-photo-card aspect-4-3 scatter-p04-3 scatter-item-3">
              <img src="data:image/webp;base64,{b64_7215}" alt="Conception Chaise Suspendue - Exploration g&eacute;om&eacute;trique 03" loading="lazy">
            </div>
          </div>

          <!-- Colonne 2 : Photos 02 & 04 -->
          <div class="scatter-col">
            <div class="scatter-photo-card aspect-4-3 scatter-p04-2 scatter-item-2">
              <img src="data:image/webp;base64,{b64_7205}" alt="Conception Chaise Suspendue - Maquette atelier 02" loading="lazy">
            </div>
            <div class="scatter-photo-card aspect-4-3 scatter-p04-4 scatter-item-4">
              <img src="data:image/webp;base64,{b64_7229}" alt="Conception Chaise Suspendue - Exploration g&eacute;om&eacute;trique 04" loading="lazy">
            </div>
          </div>

          <!-- Colonne 3 : Photo 05 (Portrait pleine hauteur) -->
          <div class="scatter-col">
            <div class="scatter-photo-card tall-fill scatter-p04-5 scatter-item-5">
              <img src="data:image/webp;base64,{b64_7233}" alt="Conception Chaise Suspendue - Prototype en situation 05" loading="lazy">
            </div>
          </div>
        </div>
      </section>"""

css_light_mode_additions = """
    /* ==========================================================================
       HERO BANNER / ROULETTE : SUPPRESSION DE LA BARRE NOIRE EN MODE CLAIR
       & TOUS LES TEXTES EN NOIR LORSQUE LE MODE CLAIR EST ACTIVÉ
       ========================================================================== */
    body.light-mode .hero-banner,
    body.light-mode #hero-banner {
      background-color: #f7f7f9 !important;
      background: #f7f7f9 !important;
      box-shadow: none !important;
      border: none !important;
    }
    body.light-mode .drum-nav,
    body.light-mode #drum-nav {
      background: transparent !important;
    }
    body.light-mode .drum-slot-btn,
    body.light-mode #hero-banner button {
      color: #0d0d11 !important;
      opacity: 0.35 !important;
    }
    body.light-mode .drum-slot-btn:hover,
    body.light-mode #hero-banner button:hover {
      color: #0d0d11 !important;
      opacity: 1 !important;
    }
    body.light-mode .drum-slot-btn:focus-visible {
      outline-color: #0d0d11 !important;
    }
    body.light-mode .drum-slot-center,
    body.light-mode #hero-banner div,
    body.light-mode #hero-banner div span {
      color: #0d0d11 !important;
      text-shadow: none !important;
      filter: none !important;
    }
    body.light-mode .drum-star {
      color: #0d0d11 !important;
    }
    body.light-mode .drum-slot-text {
      color: #0d0d11 !important;
    }
    body.light-mode .drum-slot-center:hover .drum-slot-label,
    body.light-mode .drum-nav:has(.drum-slot-center:hover) .drum-slot-label {
      text-shadow: none !important;
    }

    /* TOP BAR & EN-TÊTE FIXE EN MODE CLAIR */
    body.light-mode .top-bar {
      background-color: rgba(247, 247, 249, 0.96) !important;
      border-bottom-color: rgba(0, 0, 0, 0.08) !important;
    }
    body.light-mode .top-bar *,
    body.light-mode .brand-title,
    body.light-mode .brand-sub,
    body.light-mode .sticky-title,
    body.light-mode .top-menu-btn,
    body.light-mode .top-theme-quick-btn {
      color: #0d0d11 !important;
    }
    body.light-mode .top-menu-btn .menu-bar-icon span {
      background-color: #0d0d11 !important;
    }
    body.light-mode .sticky-roulette-dropdown {
      background-color: #ffffff !important;
      border-color: rgba(0, 0, 0, 0.1) !important;
      box-shadow: 0 16px 40px rgba(0, 0, 0, 0.12) !important;
    }
    body.light-mode .compact-slot-btn,
    body.light-mode .compact-slot-center,
    body.light-mode .compact-star {
      color: #0d0d11 !important;
      text-shadow: none !important;
    }

    /* TOUS LES TEXTES DES PROJETS EN NOIR EN MODE CLAIR */
    body.light-mode .project-header-bar *,
    body.light-mode .project-nav-arrows *,
    body.light-mode .project-counter-pill {
      color: #0d0d11 !important;
      border-color: rgba(0, 0, 0, 0.15) !important;
    }
    body.light-mode .hero-concept-title,
    body.light-mode .project-header-title {
      color: #0d0d11 !important;
    }
    body.light-mode .hero-concept-thesis,
    body.light-mode .project-header-desc,
    body.light-mode .project-desc {
      color: #111118 !important;
    }
    body.light-mode .editorial-tag,
    body.light-mode .editorial-tag-row span {
      color: #33333e !important;
    }
    body.light-mode .hero-narrative-card,
    body.light-mode .project-genesis-box {
      background: rgba(0, 0, 0, 0.035) !important;
      border-left-color: rgba(0, 0, 0, 0.3) !important;
      border-color: rgba(0, 0, 0, 0.12) !important;
    }
    body.light-mode .hero-narrative-card *,
    body.light-mode .project-genesis-box * {
      color: #0d0d11 !important;
    }
    body.light-mode .narrative-header,
    body.light-mode .genesis-eyebrow {
      color: #0d0d11 !important;
    }
    body.light-mode .project-specs-bar {
      background: rgba(0, 0, 0, 0.04) !important;
      border-color: rgba(0, 0, 0, 0.1) !important;
    }
    body.light-mode .project-specs-bar * {
      color: #0d0d11 !important;
    }
    body.light-mode .project-specs-bar .spec-val {
      color: #0d0d11 !important;
    }
    body.light-mode .p1-showcase-text,
    body.light-mode .p1-showcase-text p,
    body.light-mode .photo-side-text-col,
    body.light-mode .photo-side-text-col p,
    body.light-mode .photo-side-text-col div,
    body.light-mode .photo-side-text-col span {
      color: #0d0d11 !important;
    }
    body.light-mode .process-header *,
    body.light-mode .process-giant-title,
    body.light-mode .process-lead-text,
    body.light-mode .process-eyebrow,
    body.light-mode .process-eyebrow span {
      color: #0d0d11 !important;
    }
    body.light-mode .project-footer-card,
    body.light-mode .project-footer-card *,
    body.light-mode .next-teaser-info div {
      color: #0d0d11 !important;
    }
    body.light-mode .project-nav-btn {
      color: #0d0d11 !important;
      border-color: rgba(0, 0, 0, 0.2) !important;
    }
    body.light-mode .white-image-box {
      background-color: #ffffff !important;
      border-color: rgba(0, 0, 0, 0.12) !important;
    }
    body.light-mode .placeholder-inner * {
      color: #0d0d11 !important;
    }

    /* ABOUT & CONTACT EN MODE CLAIR */
    body.light-mode .view-panel#view-about *,
    body.light-mode .view-panel#view-contact * {
      color: #0d0d11 !important;
    }

    /* TIROIR PROJETS EN MODE CLAIR */
    body.light-mode .projects-drawer * {
      color: #0d0d11 !important;
    }
    body.light-mode aside[aria-hidden="true"],
    body.light-mode .persistent-stamp {
      color: rgba(0, 0, 0, 0.45) !important;
    }
"""

for path in files:
    if not os.path.exists(path):
        print(f"Skipping non-existent: {path}")
        continue
    
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Update CSS: insert css_light_mode_additions before </style>
    style_end_pos = content.find('</style>')
    if style_end_pos != -1:
        # Check if our additions are already there
        if '/* HERO BANNER / ROULETTE : SUPPRESSION DE LA BARRE NOIRE EN MODE CLAIR' not in content:
            content = content[:style_end_pos] + css_light_mode_additions + "\n" + content[style_end_pos:]
            print(f"Added light mode CSS in {path}")
        else:
            # Replace existing block if needed
            print(f"Light mode CSS block already present in {path}")
    
    # 2. In Project 06: Remove process-section-p06
    p6_pos = content.find('id="process-section-p06"')
    if p6_pos != -1:
        sec_start = content.rfind('<section', 0, p6_pos)
        sec_end = content.find('</section>', p6_pos) + len('</section>')
        # Also clean up surrounding whitespace/comments
        comment_start = content.rfind('<!--', 0, sec_start)
        if comment_start != -1 and 'PROCESS' in content[comment_start:sec_start]:
            actual_start = comment_start
        else:
            actual_start = sec_start
        content = content[:actual_start] + content[sec_end:]
        print(f"Removed process-section-p06 from {path}")
    else:
        print(f"process-section-p06 not found in {path}")
    
    # 3. In Project 04: Extract existing 5 maquettes base64 and update process-section-p04
    p4_pos = content.find('id="process-section-p04"')
    if p4_pos != -1:
        sec_start = content.rfind('<section', 0, p4_pos)
        sec_end = content.find('</section>', p4_pos) + len('</section>')
        p4_sec_text = content[sec_start:sec_end]
        
        # Extract b64 for each maquette
        def extract_b64(alt_keyword):
            m = re.search(r'src="data:image/webp;base64,([^"]+)"[^>]*alt="[^"]*' + alt_keyword, p4_sec_text)
            if not m:
                m = re.search(r'alt="[^"]*' + alt_keyword + r'[^"]*"[^>]*src="data:image/webp;base64,([^"]+)"', p4_sec_text)
            return m.group(1) if m else None

        b64_7196 = extract_b64("01")
        b64_7215 = extract_b64("03")
        b64_7205 = extract_b64("02")
        b64_7229 = extract_b64("04")
        b64_7233 = extract_b64("05")
        
        # If any is missing from section text, read directly from file on disk
        def b64_from_disk(fname):
            with open(os.path.join('images/project-04', fname), 'rb') as fp:
                return base64.b64encode(fp.read()).decode('ascii')
        
        if not b64_7196: b64_7196 = b64_from_disk('IMG_7196.webp')
        if not b64_7215: b64_7215 = b64_from_disk('IMG_7215.webp')
        if not b64_7205: b64_7205 = b64_from_disk('IMG_7205.webp')
        if not b64_7229: b64_7229 = b64_from_disk('IMG_7229.webp')
        if not b64_7233: b64_7233 = b64_from_disk('IMG_7233.webp')
        
        new_p4_html = get_p4_process_html(b64_7196, b64_7215, b64_7205, b64_7229, b64_7233)
        
        comment_start = content.rfind('<!--', 0, sec_start)
        if comment_start != -1 and 'PROCESS' in content[comment_start:sec_start]:
            actual_start = comment_start
        else:
            actual_start = sec_start
            
        content = content[:actual_start] + new_p4_html + content[sec_end:]
        print(f"Updated process-section-p04 in {path}")
    else:
        print(f"process-section-p04 not found in {path}")
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Saved {path}")

print("HTML files update complete!")
