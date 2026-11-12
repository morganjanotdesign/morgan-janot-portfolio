import re

with open("/Users/morganjanot/.gemini/antigravity/scratch/mj-portfolio/standalone.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Extract existing SVGs
illustrations = {}
for i in range(1, 7):
    p_id = f"view-project-0{i}"
    pos = html.find(f"id=\"{p_id}\"")
    next_pos = html.find(f"id=\"view-project-0{i+1}\"") if i < 6 else html.find("id=\"view-about\"")
    chunk = html[pos:next_pos]
    svg_match = re.search(r"(<div class=\"frame-illustration\">[\s\S]*?</div>)", chunk)
    if not svg_match:
        raise Exception(f"SVG for project {i} not found!")
    illustrations[i] = svg_match.group(1).strip()

print("All 6 SVGs preserved successfully.")

# 2. Update CSS
css_new = """
    /* =============================================================
       NEW EDITORIAL PROJECT HERO (CARTE COULEUR + TEXTE EXPLICATIF CÔTE À CÔTE)
       ============================================================= */
    .project-hero-dual {
      display: grid;
      grid-template-columns: 1fr;
      gap: clamp(36px, 5vw, 68px);
      align-items: center;
      margin-top: 10px;
      margin-bottom: clamp(70px, 9vw, 130px);
    }
    @media (min-width: 960px) {
      .project-hero-dual {
        grid-template-columns: 1.15fr 1fr;
      }
      .project-hero-dual.reverse-side {
        grid-template-columns: 1fr 1.15fr;
      }
      .project-hero-dual.reverse-side > .hero-card-col {
        order: 2;
      }
      .project-hero-dual.reverse-side > .hero-text-col {
        order: 1;
      }
    }

    .hero-card-col {
      width: 100%;
    }

    .hero-text-col {
      display: flex;
      flex-direction: column;
      justify-content: center;
    }

    .hero-concept-title {
      font-size: clamp(34px, 4.2vw, 58px);
      font-weight: 900;
      letter-spacing: -0.03em;
      line-height: 0.98;
      color: #ffffff;
      margin: 0 0 16px 0;
    }

    .hero-concept-thesis {
      font-size: clamp(15px, 1.35vw, 19px);
      font-weight: 700;
      color: #eeeeee;
      line-height: 1.45;
      margin-bottom: 22px;
    }

    .hero-narrative-card {
      background: rgba(255, 255, 255, 0.035);
      border-left: 3px solid rgba(255, 255, 255, 0.25);
      padding: clamp(18px, 2.5vw, 26px);
      backdrop-filter: blur(12px);
      margin-bottom: 22px;
      border-radius: 0 4px 4px 0;
    }

    .narrative-header {
      display: flex;
      align-items: center;
      gap: 10px;
      font-size: 11px;
      font-weight: 900;
      letter-spacing: 0.22em;
      text-transform: uppercase;
      color: #aaaaaa;
      margin-bottom: 12px;
    }

    .narrative-dot {
      width: 8px;
      height: 8px;
      border-radius: 2px;
    }

    .narrative-body p {
      font-size: clamp(13px, 1.05vw, 15px);
      line-height: 1.75;
      color: #cccccc;
      margin: 0 0 12px 0;
      font-weight: 400;
    }
    .narrative-body p:last-child {
      margin-bottom: 0;
    }

    /* =============================================================
       SPACED-OUT IMAGES: GRANDES PLEIN ÉCRAN & PETITS FORMATS
       ============================================================= */
    .full-screen-image-block {
      width: 100vw;
      position: relative;
      left: 50%;
      right: 50%;
      margin-left: -50vw;
      margin-right: -50vw;
      max-width: 100vw;
      box-sizing: border-box;
      padding: 0 clamp(16px, 3.5vw, 56px);
      margin-top: clamp(70px, 9vw, 130px);
      margin-bottom: clamp(70px, 9vw, 130px);
    }

    .full-screen-image-block .white-image-box {
      width: 100%;
      aspect-ratio: 21/9;
      min-height: 420px;
      max-height: 720px;
    }

    .gallery-spaced-pair {
      display: grid;
      grid-template-columns: 1fr;
      gap: clamp(36px, 5.5vw, 80px);
      align-items: center;
      margin-top: clamp(60px, 8vw, 120px);
      margin-bottom: clamp(60px, 8vw, 120px);
    }
    @media (min-width: 860px) {
      .gallery-spaced-pair.asymmetric-left {
        grid-template-columns: 1.35fr 1fr;
      }
      .gallery-spaced-pair.asymmetric-right {
        grid-template-columns: 1fr 1.35fr;
      }
      .gallery-spaced-pair.equal {
        grid-template-columns: 1fr 1fr;
      }
    }

    .gallery-centered-small {
      max-width: 680px;
      margin-left: auto;
      margin-right: auto;
      margin-top: clamp(60px, 8vw, 120px);
      margin-bottom: clamp(60px, 8vw, 120px);
      width: 100%;
    }
"""

css_marker_start = html.find("/* Grids */")
css_marker_end = html.find(".project-detail-section {")
if css_marker_start != -1 and css_marker_end != -1:
    html = html[:css_marker_start] + css_new + "\n    " + html[css_marker_end:]
    print("CSS updated successfully.")

# Helper to generate white image box HTML without backslash issues
def make_box(title, subtitle, tag, aspect, max_width=None, min_height=None, max_height=None):
    style_parts = [f"aspect-ratio: {aspect};"]
    if max_width:
        style_parts.append(f"max-width: {max_width};")
    if min_height:
        style_parts.append(f"min-height: {min_height};")
    if max_height:
        style_parts.append(f"max-height: {max_height};")
    style_attr = " ".join(style_parts)

    return f"""      <div class="white-image-box" style="{style_attr}">
        <span class="placeholder-crosshair cross-tl"></span>
        <span class="placeholder-crosshair cross-tr"></span>
        <span class="placeholder-crosshair cross-bl"></span>
        <span class="placeholder-crosshair cross-br"></span>
        <div class="placeholder-inner">
          <div class="placeholder-icon">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <rect x="3" y="3" width="18" height="18" rx="2" ry="2"/>
              <circle cx="8.5" cy="8.5" r="1.5"/>
              <polyline points="21 15 16 10 5 21"/>
            </svg>
          </div>
          <span class="placeholder-tag">{tag}</span>
          <h4 class="placeholder-title">{title}</h4>
          <span class="placeholder-sub">{subtitle}</span>
        </div>
      </div>"""

# Pre-generate boxes for each project to avoid backslash inside f-strings
box_p1_2 = make_box('IMAGE 02', 'Cadrage angulaire d\'ensemble &amp; assise basse &bull; 16/10', 'VUE ANGULAIRE MOYENNE', '16/10')
box_p1_3 = make_box('IMAGE 03', 'Gros plan matière &amp; velours de laine bouclée &bull; 1/1', 'PETIT FORMAT CARRÉ D\'ATELIER', '1/1')
box_p1_4 = make_box('IMAGE 04', 'Détail d\'atelier : capitonnage et tension du tissu &bull; 4/3', 'PETITE VUE DÉTAIL CENTRÉE', '4/3')

box_p2_2 = make_box('IMAGE 02', 'Détail mécanique : rotule et pivot à friction sèche &bull; 1/1', 'PETITE VUE DÉTAIL D\'USINAGE', '1/1')
box_p2_3 = make_box('IMAGE 03', 'Lentille optique &amp; faisceau en ambiance nocturne &bull; 4/5', 'PETIT FORMAT PORTRAIT D\'AMBIANCE', '4/5')
box_p2_4 = make_box('IMAGE 04', 'Contrepoids en laiton CNC &amp; équilibre en porte-à-faux &bull; 16/10', 'PETITE VUE ÉQUILIBRE CENTRÉE', '16/10')

box_p3_2 = make_box('IMAGE 02', 'Point d\'attache zénithal &amp; anneau d\'accroche titane &bull; 4/5', 'PETIT FORMAT PORTRAIT D\'ANCRAGE', '4/5')
box_p3_3 = make_box('IMAGE 03', 'Détail d\'atelier : tressage des fibres Dyneema &bull; 16/10', 'VUE MATIÈRE MOYENNE', '16/10')
box_p3_4 = make_box('IMAGE 04', 'Membrane thermoformée &amp; ergonomie en apesanteur &bull; 1/1', 'PETIT CARRÉ D\'ASSEMBLAGE', '1/1')

box_p4_2 = make_box('IMAGE 02', 'Perspective trois-quarts et profilage d\'assise &bull; 16/10', 'VUE D\'ENSEMBLE TROIS-QUARTS', '16/10')
box_p4_3 = make_box('IMAGE 03', 'Gros plan matière : cuir patiné manuellement &bull; 1/1', 'PETITE VUE DÉTAIL MATIÈRE', '1/1')
box_p4_4 = make_box('IMAGE 04', 'L\'orbe sphérique mobile utilisé en accoudoir &bull; 4/5', 'PETIT FORMAT PORTRAIT USAGE', '4/5')

box_p5_2 = make_box('IMAGE 02', 'Détail macro du col soufflé à la volée sans moule &bull; 1/1', 'PETIT CARRÉ MACRO SOUFFLE', '1/1')
box_p5_3 = make_box('IMAGE 03', 'Réfraction lumineuse &amp; pureté du cristal ultraviolet &bull; 1/1', 'PETIT CARRÉ RÉFRACTION', '1/1')
box_p5_4 = make_box('IMAGE 04', 'Signature gravée sous la base &amp; coffret en noyer &bull; 16/10', 'PETITE VUE COFFRET D\'ART', '16/10')

box_p6_2 = make_box('IMAGE 02', 'Jeu d\'ombres portées et filtrage de la lumière zénithale &bull; 4/3', 'VUE FILTRAGE LUMIÈRE 4/3', '4/3')
box_p6_3 = make_box('IMAGE 03', 'Détail d\'usinage : clavetage conique en aluminium sans soudure &bull; 1/1', 'PETIT FORMAT CARRÉ D\'USINAGE', '1/1')
box_p6_4 = make_box('IMAGE 04', 'Le dôme acoustique parabolique et résonance spatiale &bull; 16/9', 'VUE PERSPECTIVE ACOUSTIQUE', '16/9')

projects_data = [
    {
        "num": "01",
        "title": "Fauteuil Nuage",
        "prev_num": "06",
        "next_num": "02",
        "color": "rgb(204, 255, 0)",
        "aspect": "1/1",
        "reverse": False,
        "cartouche_tag": "01 — Architecture d'Assise // Paris",
        "meta_left": "ESTAMPE D'ATELIER",
        "meta_right": "VERT ACIDE",
        "category_tag": "01 // Mobilier Éditorial",
        "badge_text": "* ÉDITION LIMITÉE 12 EX. *",
        "badge_bg": "rgba(204, 255, 0, 0.15)",
        "badge_color": "#ccff00",
        "badge_border": "rgba(204, 255, 0, 0.4)",
        "thesis": "Une assise sculpturale explorant la densité d'un volume gonflé d'air et l'intensité tactile du vert acide.",
        "p1": "Pourquoi ce projet ? Il est né de la volonté de rompre avec l'austérité géométrique du mobilier contemporain. Trop souvent, le confort enveloppant est sacrifié au profit d'angles droits rigides. Le Fauteuil Nuage a été conçu pour donner la sensation d'être suspendu dans une masse d'air compacte, avec un capitonnage continu sans coutures dures.",
        "p2": "La tension chromatique du vert acide vient électriser la douceur de la laine bouclée : la pièce ne s'efface pas dans l'architecture mais agit comme une sculpture vibrante qui capte la lumière et dialogue avec l'espace alentour.",
        "specs": [
            ("Dimensions", "94 &times; 102 &times; H 82 cm"),
            ("Matière", "Laine bouclée &amp; mousse HR"),
            ("Poids", "28 kg"),
            ("Tirage", "12 pièces numérotées"),
        ],
        "full_img": {
            "title": "IMAGE 01 — GRANDE VUE PLEIN ÉCRAN",
            "subtitle": "Perspective monumentale en situation architecturale &bull; Plein écran 21/9",
            "tag": "PLEIN ÉCRAN // FORMAT CINÉMA 21:9",
            "aspect": "21/9"
        },
        "secondary_html": f"""      <!-- Images plus petites et espacées -->
      <div class="gallery-spaced-pair asymmetric-left">
{box_p1_2}
{box_p1_3}
      </div>

      <div class="gallery-centered-small">
{box_p1_4}
      </div>""",
        "next_title": "Lampadaire Articulé",
        "next_color": "rgb(255, 0, 127)",
    },
    {
        "num": "02",
        "title": "Lampadaire Articulé",
        "prev_num": "01",
        "next_num": "03",
        "color": "rgb(255, 0, 127)",
        "aspect": "9/16",
        "reverse": True,
        "cartouche_tag": "02 — Cinétique &amp; Lumière // Studio",
        "meta_left": "PIVOT À FRICTION SÈCHE",
        "meta_right": "CYBER MAGENTA",
        "category_tag": "02 // Design d'Espace",
        "badge_text": "* PROTOTYPE CINÉTIQUE BREVETÉ *",
        "badge_bg": "rgba(255, 0, 127, 0.15)",
        "badge_color": "#ff55a3",
        "badge_border": "rgba(255, 0, 127, 0.4)",
        "thesis": "Un équilibre mécanique parfait entre bras télescopiques en porte-à-faux et faisceau lumineux directionnel.",
        "p1": "Pourquoi ce projet ? La plupart des luminaires domestiques imposent un cône de lumière figé. L'ambition était de concevoir un luminaire cinétique où le balancier défie la pesanteur : un bras de 220 cm orientable d'un simple effleurement du doigt sans aucun ressort parasite.",
        "p2": "Inspiré des outils d'atelier et des balances de précision, le contrepoids en laiton usiné CNC compense exactement la portée du mât. La lentille collimatrice micro-prismatique diffuse un halo doux de 38&deg;, sans aucun éblouissement latéral.",
        "specs": [
            ("Portée", "220 cm (rotation 360&deg;)"),
            ("Matière", "Laiton massif CNC &amp; Carbone"),
            ("Source", "LED COB 2700K (CRI &gt; 98)"),
            ("Commande", "Variateur capacitif"),
        ],
        "full_img": {
            "title": "IMAGE 01 — GRANDE VUE PLEIN ÉCRAN",
            "subtitle": "Envergure cinétique complète et faisceau nocturne &bull; Plein écran 16/9",
            "tag": "PLEIN ÉCRAN // IMMERSION NOCTURNE 16:9",
            "aspect": "16/9"
        },
        "secondary_html": f"""      <!-- Images plus petites et espacées -->
      <div class="gallery-spaced-pair equal">
{box_p2_2}
{box_p2_3}
      </div>

      <div class="gallery-centered-small">
{box_p2_4}
      </div>""",
        "next_title": "Chaise Suspendue",
        "next_color": "rgb(0, 240, 255)",
    },
    {
        "num": "03",
        "title": "Chaise Suspendue",
        "prev_num": "02",
        "next_num": "04",
        "color": "rgb(0, 240, 255)",
        "aspect": "4/3",
        "reverse": False,
        "cartouche_tag": "03 — Structure Géométrique // Paris",
        "meta_left": "ANCRAGE MONOPHONIQUE",
        "meta_right": "LASER AQUA",
        "category_tag": "03 // Structure Géométrique",
        "badge_text": "* ÉTUDE TENSIONNELLE EN APESANTEUR *",
        "badge_bg": "rgba(0, 240, 255, 0.15)",
        "badge_color": "#00f0ff",
        "badge_border": "rgba(0, 240, 255, 0.4)",
        "thesis": "L'abolition des pieds traditionnels au profit d'un treillis autoportant ancré au plafond par des liens invisibles.",
        "p1": "Pourquoi cette recherche ? Pour libérer complètement la surface au sol et éprouver le vide comme matériau structural. En suspendant l'assise au plafond par des filins en fibre Dyneema ultra-résistante, l'objet s'affranchit des contraintes d'appui et réagit aux oscillations du corps pour une sensation de lévitation intégrale.",
        "p2": "L'arceau triangulé en titane microbillé distribue les tensions mécaniques de manière isotrope. La membrane textile thermoformée épouse la posture sans point dur, rappelant l'aéronautique et le gréement nautique de haute mer.",
        "specs": [
            ("Envergure", "78 &times; 82 &times; H 115 cm"),
            ("Câblage", "Dyneema SK78 (&gt; 1 800 kg)"),
            ("Armature", "Titane Ti-6Al-4V microbillé"),
            ("Charge", "260 kg certifiée Bureau Veritas"),
        ],
        "full_img": {
            "title": "IMAGE 01 — GRANDE VUE PLEIN ÉCRAN",
            "subtitle": "Suspension dans un grand volume d'architecture contemporaine &bull; Plein écran 21/9",
            "tag": "PLEIN ÉCRAN // FORMAT CINÉMA 21:9",
            "aspect": "21/9"
        },
        "secondary_html": f"""      <!-- Images plus petites et espacées -->
      <div class="gallery-spaced-pair asymmetric-right">
{box_p3_2}
{box_p3_3}
      </div>

      <div class="gallery-centered-small">
{box_p3_4}
      </div>""",
        "next_title": "Canapé Galet",
        "next_color": "rgb(255, 94, 0)",
    },
    {
        "num": "04",
        "title": "Canapé Galet",
        "prev_num": "03",
        "next_num": "05",
        "color": "rgb(255, 94, 0)",
        "aspect": "16/10",
        "reverse": True,
        "cartouche_tag": "04 — Recherche Formelle // Atelier Janot",
        "meta_left": "VOLUME MONOBLOC",
        "meta_right": "ORANGE FLUO",
        "category_tag": "04 // Recherche Formelle",
        "badge_text": "* MONOLITHE SCULPTURAL &amp; CUIR PATINÉ *",
        "badge_bg": "rgba(255, 94, 0, 0.15)",
        "badge_color": "#ff904d",
        "badge_border": "rgba(255, 94, 0, 0.4)",
        "thesis": "Masse rocheuse adoucie par l'érosion géologique, accueillant un orbe sphérique mobile en cuir naturel ciré.",
        "p1": "Pourquoi ce projet ? La volonté d'échapper à la monotonie rectiligne des canapés modulaires. Le dessin est né de l'observation des roches de granit érodées par l'océan Atlantique : une forme continue qui s'adapte intuitivement aux différentes postures d'assise (formelle, lecture ou méridienne).",
        "p2": "L'orbe mobile en cuir ciré à chaud apporte une ponctuation sculpturale vivante : confectionné en taurillon pleine fleur, il devient au gré des envies un accoudoir ergonomique, un cale-dos amovible ou un objet de contemplation autonome.",
        "specs": [
            ("Dimensions", "L 285 &times; P 138 &times; H 76 cm"),
            ("Cuir", "Taurillon pleine fleur ciré"),
            ("Structure", "Multiplis de hêtre &amp; mousse végétale"),
            ("Poids", "115 kg monobloc"),
        ],
        "full_img": {
            "title": "IMAGE 01 — GRANDE VUE PLEIN ÉCRAN",
            "subtitle": "Mégalithe sculptural dans une pièce de réception baignée de lumière &bull; Plein écran 21/9",
            "tag": "PLEIN ÉCRAN // FORMAT CINÉMA 21:9",
            "aspect": "21/9"
        },
        "secondary_html": f"""      <!-- Images plus petites et espacées -->
      <div class="gallery-spaced-pair asymmetric-left">
{box_p4_2}
{box_p4_3}
      </div>

      <div class="gallery-centered-small">
{box_p4_4}
      </div>""",
        "next_title": "Vase Corolle",
        "next_color": "rgb(200, 75, 255)",
    },
    {
        "num": "05",
        "title": "Vase Corolle",
        "prev_num": "04",
        "next_num": "06",
        "color": "rgb(200, 75, 255)",
        "aspect": "4/5",
        "reverse": False,
        "cartouche_tag": "05 — Cristal Soufflé // Murano",
        "meta_left": "SOUFFLÉ À LA VOLÉE",
        "meta_right": "ULTRAVIOLET",
        "category_tag": "05 // Édition Limitée",
        "badge_text": "* CRISTAL DE MURANO SOUFFLÉ BOUCHE *",
        "badge_bg": "rgba(200, 75, 255, 0.15)",
        "badge_color": "#d97dff",
        "badge_border": "rgba(200, 75, 255, 0.4)",
        "thesis": "Capture instantanée d'un mouvement de rotation liquide figé pour l'éternité dans le cristal incandescent.",
        "p1": "Pourquoi cette pièce ? Elle résulte d'une recherche sur la fugacité du geste de l'artisan. À Murano, le verrier cueille le cristal à 1 200&deg;C et ne dispose que de 40 secondes de force centrifuge manuelle avant que la matière ne se pétrifie en volute florale.",
        "p2": "L'incorporation d'oxydes rares de cobalt et de manganèse confère au cristal une vie optique permanente : sous un éclairage doux, il arbore un pourpre profond ; sous le soleil direct, il s'enflamme de reflets ultraviolets éclatants.",
        "specs": [
            ("Hauteur", "48 cm (&Oslash; max 36 cm)"),
            ("Matière", "Cristal pur 24% PbO soufflé bouche"),
            ("Pigments", "Oxydes minéraux cobalt &amp; manganèse"),
            ("Tirage", "8 pièces uniques signées"),
        ],
        "full_img": {
            "title": "IMAGE 01 — GRANDE VUE PLEIN ÉCRAN",
            "subtitle": "Réfractions solaires et transparence du cristal incandescent &bull; Plein écran 16/9",
            "tag": "PLEIN ÉCRAN // LUMIÈRE &amp; CRISTAL 16:9",
            "aspect": "16/9"
        },
        "secondary_html": f"""      <!-- Images plus petites et espacées -->
      <div class="gallery-spaced-pair equal">
{box_p5_2}
{box_p5_3}
      </div>

      <div class="gallery-centered-small">
{box_p5_4}
      </div>""",
        "next_title": "Arche Radiale",
        "next_color": "rgb(255, 235, 0)",
    },
    {
        "num": "06",
        "title": "Arche Radiale",
        "prev_num": "05",
        "next_num": "01",
        "color": "rgb(255, 235, 0)",
        "aspect": "4/3",
        "reverse": True,
        "cartouche_tag": "06 — Manifeste &amp; Archive // Biennale Milan",
        "meta_left": "INSTALLATION 4.80M",
        "meta_right": "JAUNE FLUO",
        "category_tag": "06 // Manifesto &amp; Archive",
        "badge_text": "* BIENNALE DE MILAN 2025 *",
        "badge_bg": "rgba(255, 235, 0, 0.15)",
        "badge_color": "#ffeb00",
        "badge_border": "rgba(255, 235, 0, 0.4)",
        "thesis": "Installation monumentale en 42 arches concentriques d'aluminium jaune solaire, onde optique immersive.",
        "p1": "Pourquoi cette échelle monumentale ? Présentée à la Biennale de Milan, l'Arche Radiale explore le passage entre sculpture publique et filtre spatial. Quarante-deux profilés d'aluminium cintrés pivotent de 2,5&deg; chacun, créant un phénomène de moiré optique mouvant lorsque le visiteur circule.",
        "p2": "Au-delà de la géométrie visuelle, la courbure parabolique concentre l'onde sonore en son foyer central, créant un dôme acoustique intime et feutré qui isole le marcheur du bruit ambiant.",
        "specs": [
            ("Envergure", "6.40 m &times; H 4.80 m"),
            ("Éléments", "42 arcs aluminium anodisé 25&mu;m"),
            ("Assemblage", "Clavetage conique invisible"),
            ("Acoustique", "Foyer parabolique à 1.40 m"),
        ],
        "full_img": {
            "title": "IMAGE 01 — GRANDE VUE PLEIN ÉCRAN",
            "subtitle": "Immersion totale sous les 42 arches cinétiques à la Biennale &bull; Plein écran 21/9",
            "tag": "PLEIN ÉCRAN // MANIFESTE MONUMENTAL 21:9",
            "aspect": "21/9"
        },
        "secondary_html": f"""      <!-- Images plus petites et espacées -->
      <div class="gallery-spaced-pair equal">
{box_p6_2}
{box_p6_3}
      </div>

      <div class="gallery-centered-small">
{box_p6_4}
      </div>""",
        "next_title": "Fauteuil Nuage",
        "next_color": "rgb(204, 255, 0)",
    }
]

# Generate all 6 project sections
sections_html = []
for p in projects_data:
    idx = int(p["num"])
    svg = illustrations[idx]
    reverse_class = "reverse-side" if p["reverse"] else ""

    # build specs spans
    specs_items = []
    for label, val in p["specs"]:
        specs_items.append(f'<span>{label} : <span class="spec-val">{val}</span></span>')
    specs_joined = '\n        <span class="spec-sep">&bull;</span>\n        '.join(specs_items)

    full_box_html = make_box(p['full_img']['title'], p['full_img']['subtitle'], p['full_img']['tag'], p['full_img']['aspect'])

    sec = f"""    <!-- VIEW DETAIL: PROJET {p['num']} ({p['title'].upper()}) -->
    <section id="view-project-{p['num']}" class="view-panel project-detail-section">
      <!-- Top Navigation Bar -->
      <div class="project-header-bar">
        <button type="button" class="project-nav-btn btn-back-portfolio" data-target="portfolio">
          <span aria-hidden="true">&larr;</span>
          <span class="link-line">Retourner au portfolio</span>
        </button>
        <div class="project-counter-pill">PROJET [ {p['num']} / 06 ]</div>
        <div class="project-nav-arrows">
          <button type="button" class="project-nav-btn prev btn-switch-project" data-target-project="project-{p['prev_num']}" aria-label="Projet précédent">
            <span aria-hidden="true">&larr;</span>
            <span>Précédent</span>
          </button>
          <button type="button" class="project-nav-btn next btn-switch-project" data-target-project="project-{p['next_num']}" aria-label="Projet suivant">
            <span>Suivant</span>
            <span aria-hidden="true">&rarr;</span>
          </button>
        </div>
      </div>

      <!-- 1. HERO DUAL ROW : CARTE COULEUR & TEXTE EXPLICATIF CÔTE À CÔTE -->
      <div class="project-hero-dual {reverse_class}">
        <!-- Carte Couleur Signature avec Texture Papier -->
        <div class="hero-card-col">
          <div class="project-art-frame" style="background-color: {p['color']}; aspect-ratio: {p['aspect']};">
            {svg}
            <div class="project-detail-cartouche">
              <div class="detail-cartouche-tag">{p['cartouche_tag']}</div>
              <h2 class="detail-cartouche-title">* {p['title'].upper()} *</h2>
              <div class="detail-cartouche-meta">
                <span>{p['meta_left']}</span>
                <span style="font-size: 13px;">*</span>
                <span>{p['meta_right']}</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Texte Explicatif : Base du projet, pourquoi & specs -->
        <div class="hero-text-col">
          <div class="editorial-tag-row" style="margin-bottom: 16px;">
            <span class="editorial-tag">{p['category_tag']}</span>
            <span class="chroma-badge" style="background: {p['badge_bg']}; color: {p['badge_color']}; border: 1px solid {p['badge_border']};">
              {p['badge_text']}
            </span>
          </div>

          <h1 class="hero-concept-title">{p['title']}</h1>
          <p class="hero-concept-thesis">{p['thesis']}</p>

          <div class="hero-narrative-card">
            <div class="narrative-header">
              <span class="narrative-dot" style="background: {p['color']};"></span>
              <span>GENÈSE &amp; BASE DU PROJET</span>
            </div>
            <div class="narrative-body">
              <p>{p['p1']}</p>
              <p>{p['p2']}</p>
            </div>
          </div>

          <!-- Fiche technique atelier épurée -->
          <div class="project-specs-bar" style="margin-bottom: 0;">
            {specs_joined}
          </div>
        </div>
      </div>

      <!-- 2. GRANDE IMAGE PLEIN ÉCRAN (QUI FAIT TOUT L'ÉCRAN) -->
      <div class="full-screen-image-block">
{full_box_html}
      </div>

      <!-- 3. IMAGES PLUS PETITES ET ESPACÉES -->
{p['secondary_html']}

      <!-- 4. Universal Next Project Teaser Footer -->
      <div class="project-footer-card" style="margin-top: clamp(80px, 10vw, 150px);">
        <div class="next-teaser-info">
          <div class="next-teaser-swatch" style="background-color: {p['next_color']};"></div>
          <div>
            <div style="font-size: 11px; font-weight: 900; letter-spacing: 0.2em; text-transform: uppercase; color: #888888; margin-bottom: 4px;">
              Projet Suivant &bull; {p['next_num']}
            </div>
            <div style="font-size: clamp(18px, 1.8vw, 24px); font-weight: 900; color: #ffffff;">
              {p['next_title']}
            </div>
          </div>
        </div>
        <button type="button" class="project-nav-btn next btn-switch-project" data-target-project="project-{p['next_num']}" style="font-size: 13px;">
          <span>Découvrir la pièce</span>
          <span aria-hidden="true">&rarr;</span>
        </button>
      </div>
    </section>
"""
    sections_html.append(sec)

all_sections_html = "\n" + "\n".join(sections_html) + "\n"

# Replace the sections block in html
start_target = html.find("<!-- VIEW DETAIL: PROJET 01 (FAUTEUIL NUAGE) -->")
end_target = html.find("<!-- VIEW 2: ABOUT (ACCESSIBLE VIA ROULETTE WITH * ABOUT *) -->")

if start_target == -1 or end_target == -1:
    raise Exception(f"Markers not found: start_target={start_target}, end_target={end_target}")

html = html[:start_target] + all_sections_html + "    " + html[end_target:]

with open("/Users/morganjanot/.gemini/antigravity/scratch/mj-portfolio/standalone.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Saved standalone.html successfully! New size:", len(html))
