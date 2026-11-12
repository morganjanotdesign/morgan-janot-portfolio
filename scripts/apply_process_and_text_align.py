import os

files = [
    'standalone.html',
    'portfolio.html',
    '/Users/morganjanot/.gemini/antigravity/brain/df18ad40-ac30-4b7a-b04f-f3de4961c66b/portfolio.html'
]

css_old = """    /* NOUVELLE COMPOSITION DUO PHOTO / TEXTE PROJET 01 (GRAND FORMAT & ÉPURÉ) */
    .p1-showcase-row {
      display: grid !important;
      align-items: center !important;
      max-width: 1700px !important;
      width: 95% !important;
      margin: clamp(70px, 9vw, 130px) auto !important;
      padding: 0 clamp(16px, 4vw, 48px) !important;
      gap: clamp(40px, 6vw, 96px) !important;
      box-sizing: border-box !important;
    }
    .p1-showcase-row.text-left {
      grid-template-columns: minmax(280px, 360px) 1fr !important;
    }
    .p1-showcase-row.photo-left {
      grid-template-columns: 1fr minmax(280px, 360px) !important;
    }
    .p1-showcase-text {
      display: flex !important;
      flex-direction: column !important;
      justify-content: center !important;
      max-width: 360px !important;
      box-sizing: border-box !important;
    }
    .p1-showcase-text p {
      margin: 0 !important;
      padding: 0 !important;
      font-size: clamp(14px, 1.1vw, 16px) !important;
      line-height: 1.8 !important;
      font-weight: 300 !important;
      color: #d6d6d6 !important;
    }"""

css_new = """    /* NOUVELLE COMPOSITION DUO PHOTO / TEXTE PROJET 01 (TEXTE ALIGNÉ AU BAS & JUSTIFIÉ) */
    .p1-showcase-row {
      display: grid !important;
      align-items: end !important;
      max-width: 1700px !important;
      width: 95% !important;
      margin: clamp(70px, 9vw, 130px) auto !important;
      padding: 0 clamp(16px, 4vw, 48px) !important;
      gap: clamp(40px, 6vw, 96px) !important;
      box-sizing: border-box !important;
    }
    .p1-showcase-row.text-left {
      grid-template-columns: minmax(280px, 360px) 1fr !important;
    }
    .p1-showcase-row.photo-left {
      grid-template-columns: 1fr minmax(280px, 360px) !important;
    }
    .p1-showcase-text {
      display: flex !important;
      flex-direction: column !important;
      justify-content: flex-end !important;
      max-width: 360px !important;
      box-sizing: border-box !important;
    }
    .p1-showcase-text p {
      margin: 0 !important;
      padding: 0 !important;
      font-size: clamp(14px, 1.1vw, 16px) !important;
      line-height: 1.8 !important;
      font-weight: 300 !important;
      color: #d6d6d6 !important;
      text-align: justify !important;
      text-justify: inter-word !important;
      hyphens: auto !important;
      -webkit-hyphens: auto !important;
    }

    /* ALIGNEMENT AU BAS & JUSTIFICATION DES TEXTES CÔTÉ PHOTO (PROJETS 02 & 05) */
    .photo-detail-row {
      display: grid !important;
      align-items: end !important;
    }
    .photo-side-text-col {
      display: flex !important;
      flex-direction: column !important;
      justify-content: flex-end !important;
    }
    .photo-side-text-col p,
    .photo-side-text-col div {
      text-align: justify !important;
      text-justify: inter-word !important;
      hyphens: auto !important;
      -webkit-hyphens: auto !important;
    }

    /* Justification des textes explicatifs et de genèse */
    .project-genesis-box p,
    .project-hero-text p {
      text-align: justify !important;
      text-justify: inter-word !important;
      hyphens: auto !important;
      -webkit-hyphens: auto !important;
    }"""

conception_css_start_anchor = """    /* ==========================================================================
       CONCEPTION ACCORDION MORPH & SCATTERED PHOTOS
       ========================================================================== */"""

conception_css_end_anchor = """    @media (max-width: 900px) {
      .conception-scatter-stage.scatter-5 {
        grid-template-columns: 1fr !important;
      }
      .conception-scatter-stage.scatter-2 {
        grid-template-columns: 1fr !important;
      }
      .scatter-photo-card {
        transform: none !important;
      }
      .scatter-photo-card:hover {
        transform: scale(1.02) !important;
      }
    }"""

process_css_replacement = """    /* ==========================================================================
       SECTION PROCESS : GROS TITRE EN PLEINE PAGE & IMAGES DESSOUS
       ========================================================================== */
    .project-process-section {
      max-width: 1560px;
      margin: clamp(100px, 12vw, 180px) auto clamp(70px, 9vw, 130px) auto;
      padding: 0 clamp(16px, 4vw, 48px);
      box-sizing: border-box;
    }

    .process-header {
      margin-bottom: clamp(36px, 5vw, 64px);
      display: flex;
      flex-direction: column;
      gap: clamp(14px, 2vw, 24px);
    }

    .process-eyebrow {
      display: flex;
      align-items: center;
      gap: 12px;
      font-size: 11px;
      font-weight: 900;
      letter-spacing: 0.24em;
      text-transform: uppercase;
      color: rgba(255, 255, 255, 0.45);
    }
    body.light-mode .process-eyebrow {
      color: #777785 !important;
    }

    .process-dot {
      width: 8px;
      height: 8px;
      border-radius: 2px;
      display: inline-block;
    }

    /* Gros titre en pleine page : PROCESS */
    .process-giant-title {
      margin: 0;
      padding: 0;
      font-family: "Arial Black", "Impact", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      font-size: clamp(64px, 14vw, 180px);
      font-weight: 900;
      letter-spacing: -0.04em;
      line-height: 0.88;
      text-transform: uppercase;
      color: #ffffff;
      user-select: none;
    }
    body.light-mode .process-giant-title {
      color: #0d0d11 !important;
    }

    .process-lead-text {
      margin: 0;
      font-size: clamp(15px, 1.2vw, 18px);
      font-weight: 300;
      line-height: 1.7;
      color: #c4c4cc;
      max-width: 780px;
    }
    body.light-mode .process-lead-text {
      color: #4a4a55 !important;
    }

    /* SCATTERED DISPERSED STAGE : Disposition Aléatoire & Vivante */
    .conception-scatter-stage {
      display: grid;
      gap: clamp(24px, 3.2vw, 44px);
      align-items: center;
      position: relative;
      box-sizing: border-box;
      padding: clamp(16px, 2vw, 32px) 0;
      opacity: 1 !important;
    }
    .conception-scatter-stage.scatter-5 {
      grid-template-columns: 1fr 1fr 1.05fr;
    }
    .conception-scatter-stage.scatter-2 {
      grid-template-columns: 1fr 1fr;
    }
    .scatter-col {
      display: flex;
      flex-direction: column;
      gap: clamp(24px, 3.2vw, 40px);
    }

    /* Carte Photo Dispersée Individuelle */
    .scatter-photo-card {
      position: relative;
      border-radius: 6px;
      overflow: hidden;
      background-color: #121214;
      border: 1px solid rgba(255, 255, 255, 0.12);
      box-shadow: 0 16px 45px rgba(0, 0, 0, 0.75);
      transition: transform 0.45s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.45s ease, border-color 0.4s ease;
      cursor: pointer;
      will-change: transform;
      opacity: 1 !important;
      visibility: visible !important;
    }
    .scatter-photo-card.aspect-4-3 {
      aspect-ratio: 4 / 3;
    }
    .scatter-photo-card.tall-fill {
      height: 100%;
      min-height: 380px;
    }
    .scatter-photo-card img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
      transition: transform 0.6s cubic-bezier(0.16, 1, 0.3, 1);
    }

    /* Effet tactile au survol : la photo se redresse, s'agrandit et s'élève vers l'utilisateur */
    .scatter-photo-card:hover {
      transform: rotate(0deg) scale(1.06) translateY(-12px) !important;
      z-index: 40 !important;
      border-color: rgba(255, 255, 255, 0.4) !important;
      box-shadow: 0 35px 80px rgba(0, 0, 0, 0.95), 0 0 0 1px rgba(255, 255, 255, 0.2) !important;
    }
    .scatter-photo-card:hover img {
      transform: scale(1.02);
    }

    /* DISPERSION ORGANIQUE POUR PROJET 01 (5 PHOTOS) */
    .scatter-p01-1 { transform: rotate(-3.2deg) translateY(-8px); }
    .scatter-p01-2 { transform: rotate(2.8deg) translateY(14px); }
    .scatter-p01-3 { transform: rotate(-2.2deg) translateY(-12px); }
    .scatter-p01-4 { transform: rotate(3.5deg) translateY(10px); }
    .scatter-p01-5 { transform: rotate(-1.5deg) translateY(-4px); }

    /* DISPERSION ORGANIQUE POUR PROJET 04 (5 PHOTOS) */
    .scatter-p04-1 { transform: rotate(-2.8deg) translateY(-6px); }
    .scatter-p04-2 { transform: rotate(3.2deg) translateY(16px); }
    .scatter-p04-3 { transform: rotate(-3.6deg) translateY(6px); }
    .scatter-p04-4 { transform: rotate(2.2deg) translateY(-10px); }
    .scatter-p04-5 { transform: rotate(-1.2deg) translateY(2px); }

    /* DISPERSION ORGANIQUE POUR PROJET 06 (2 PHOTOS) */
    .scatter-p06-1 { transform: rotate(-2.6deg) translateY(-6px); }
    .scatter-p06-2 { transform: rotate(2.8deg) translateY(12px); }

    @media (max-width: 900px) {
      .conception-scatter-stage.scatter-5,
      .conception-scatter-stage.scatter-2 {
        grid-template-columns: 1fr !important;
      }
      .scatter-photo-card {
        transform: none !important;
      }
    }"""

for path in files:
    if not os.path.exists(path):
        continue
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Replace showcase CSS
    if css_old in content:
        content = content.replace(css_old, css_new)
        print(f'Showcase CSS replaced in {path}')
    else:
        print(f'Warning: css_old not found in {path}')

    # 2. Replace conception accordion CSS with process CSS
    start_c_css = content.find(conception_css_start_anchor)
    if start_c_css != -1:
        end_c_css = content.find(conception_css_end_anchor, start_c_css)
        if end_c_css != -1:
            end_c_css += len(conception_css_end_anchor)
            content = content[:start_c_css] + process_css_replacement + content[end_c_css:]
            print(f'Process CSS replaced in {path}')
        else:
            print(f'Warning: conception_css_end_anchor not found in {path}')
    else:
        print(f'Warning: conception_css_start_anchor not found in {path}')

    # 3. Replace each of the 3 accordion HTML blocks
    blocks = [
        ('conception-accordion-p01', '01', 'rgb(255, 94, 0)', '01 // PROCESSUS &amp; RECHERCHES D&#39;ATELIER', 'Recherches de formes, exploration des principes d’assemblage et maquettes d’atelier. Décomposition des modules et expérimentation de la modularité à l\'échelle.'),
        ('conception-accordion-p04', '04', 'rgb(227, 6, 19)', '04 // PROCESSUS &amp; RECHERCHES STRUCTURELLES', 'Recherches de formes, exploration des principes d’assemblage et maquettes d’atelier. Expérimentations sur la géométrie et la résistance des éléments structurels.'),
        ('conception-accordion-p06', '06', 'rgb(255, 235, 0)', '06 // PROCESSUS &amp; MODÉLISATION 3D', 'Études de structure filaire, modélisation volumétrique 3D et calage des proportions de la cage en acier.')
    ]

    for bid, pnum, color, eyebrow, desc in blocks:
        old_div_start = f'<div class="conception-accordion-block" id="{bid}">'
        pos_start = content.find(old_div_start)
        if pos_start == -1:
            print(f'Warning: {bid} not found in {path}')
            continue
        
        scatter_pos = content.find('<div class="conception-scatter-stage', pos_start)
        assert scatter_pos != -1, f'Scatter stage not found in {bid}'
        
        end_tag = '        </div>\n      </div>\n'
        pos_end = content.find(end_tag, scatter_pos)
        assert pos_end != -1, f'End tag not found in {bid}'
        
        scatter_html = content[scatter_pos:pos_end].rstrip()
        
        new_block_html = f'''      <!-- SECTION PROCESS : GRAND TITRE PLEINE PAGE & IMAGES DESSOUS -->
      <section class="project-process-section" id="process-section-p{pnum}">
        <div class="process-header">
          <div class="process-eyebrow">
            <span class="process-dot" style="background: {color};"></span>
            <span>{eyebrow}</span>
          </div>
          <h2 class="process-giant-title">PROCESS</h2>
          <p class="process-lead-text">
            {desc}
          </p>
        </div>

        {scatter_html}
      </section>\n'''

        content = content[:pos_start] + new_block_html + content[pos_end + len(end_tag):]
        print(f'Replaced {bid} in {path}')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Successfully updated {path}!')
print('All HTML files processed successfully!')
