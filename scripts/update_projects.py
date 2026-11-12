import re

with open("/Users/morganjanot/.gemini/antigravity/scratch/mj-portfolio/standalone.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Extract existing illustrations
illustrations = {}
for i in range(1, 7):
    p_id = f"view-project-0{i}"
    pos = html.find(f"id=\"{p_id}\"")
    next_pos = html.find("id=\"view-project-0" + str(i+1) + "\"") if i < 6 else html.find("id=\"view-about\"")
    chunk = html[pos:next_pos]
    svg_match = re.search(r"(<div class=\"frame-illustration\">[\s\S]*?</div>)", chunk)
    if svg_match:
        illustrations[i] = svg_match.group(1).strip()
    else:
        raise Exception(f"Illustration for project {i} not found!")

print("All 6 illustrations extracted successfully!")

# Define CSS updates
new_css = """
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
       SPACED-OUT IMAGES: GRANDES PLEIN ÉCRAN & PETITES FORMATS
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

# Replace old grid CSS
css_old_start = html.find("/* Grids */")
css_old_end = html.find(".project-detail-section {")
if css_old_start != -1 and css_old_end != -1:
    html = html[:css_old_start] + new_css + "\n    " + html[css_old_end:]
    print("CSS replaced successfully!")
else:
    print("Could not find CSS markers, looking for alternative insertion point")

print("Proceeding to build HTML for 6 projects...")
