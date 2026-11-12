# encoding: UTF-8
require "json"

vecs = JSON.parse(File.read("/Users/morganjanot/.gemini/antigravity/scratch/normalized_vectors.json"))

projects = [
  {
    id: 1,
    number: "01",
    title: "Pesce Lounge",
    category: "Direction artistique",
    description: "Édition limitée & exploration de formes biomorphiques en mousse expansée teintée.",
    bg: "#e9722b",
    stroke: "#eb6209",
    key: "tile1_orange"
  },
  {
    id: 2,
    number: "02",
    title: "Arco Cantilever",
    category: "Design d'espace",
    description: "Luminaire architectural télescopique & dispositif cinétique pour galerie d'art.",
    bg: "#914792",
    stroke: "#812383",
    key: "tile2_purple"
  },
  {
    id: 3,
    number: "03",
    title: "Bauhaus Sling",
    category: "Mobilier éditorial",
    description: "Assise suspendue en cuir sellier tendu & piétement géométrique en acier brossé.",
    bg: "#68b42d",
    stroke: "#2c8934",
    key: "tile3_green"
  },
  {
    id: 4,
    number: "04",
    title: "Modular Ribbon",
    category: "Scénographie",
    description: "Système modulaire curviligne & îlot d'assises conçu pour la Biennale de Milan.",
    bg: "#775732",
    stroke: "#724b10",
    key: "tile4_brown"
  },
  {
    id: 5,
    number: "05",
    title: "Biomorphic Bloom",
    category: "Recherche matière",
    description: "Sculpture fonctionnelle en résine coulée translucide & recherche formelle.",
    bg: "#46a0d1",
    stroke: "#27629f",
    key: "tile5_blue"
  },
  {
    id: 6,
    number: "06",
    title: "Atelier Rouge",
    category: "Manifesto & Archive",
    description: "Laboratoire d'expérimentation typographique, posters grands formats et archives.",
    bg: "#d83d46",
    stroke: "#b2242c",
    key: nil
  }
]

tiles_html = projects.map do |p|
  ill_svg = ""
  arrow_svg = ""
  if p[:key] && vecs[p[:key]]
    item = vecs[p[:key]]

    ill_svg = %Q{
      <div class="tile-illustration absolute inset-0 w-full h-full flex items-center justify-start p-4 sm:p-6 md:p-8 pl-6 sm:pl-10 md:pl-14 pointer-events-none">
        <svg viewBox="#{item['viewBox']}" class="w-auto h-[88%] sm:h-[90%] md:h-[93%] max-w-[88%] object-contain" xmlns="http://www.w3.org/2000/svg" fill="none" stroke="#{p[:stroke]}" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round">
          <path d="#{item['d']}" />
        </svg>
      </div>
    }

    arrow_svg = %Q{
      <div class="tile-arrow absolute bottom-8 right-8 sm:bottom-10 sm:right-12 md:bottom-12 md:right-14 z-20 pointer-events-none">
        <svg viewBox="0 0 104 204" class="w-10 sm:w-12 md:w-14 lg:w-16 h-auto text-black" fill="none" stroke="#000000" stroke-width="18" stroke-linecap="butt" stroke-linejoin="miter" xmlns="http://www.w3.org/2000/svg">
          <line x1="52" y1="6" x2="52" y2="186" />
          <polyline points="94,140 52,186 10,140" />
        </svg>
      </div>
    }
  end

  %Q{
    <article
      tabindex="0"
      role="button"
      aria-label="#{p[:number]} — #{p[:title]}: #{p[:category]}"
      aria-expanded="false"
      class="portfolio-tile relative w-full overflow-hidden select-none outline-none aspect-[440/342] min-h-[460px] sm:min-h-[520px] md:min-h-[540px] lg:min-h-[620px]"
      data-id="#{p[:id]}"
      style="background-color: #{p[:bg]};"
    >
      #{ill_svg}
      #{arrow_svg}
      
      <!-- Emerging Project Content in Black -->
      <div class="tile-content absolute bottom-8 left-8 sm:bottom-10 sm:left-10 md:bottom-12 md:left-12 z-20 pointer-events-none max-w-[85%] md:max-w-[70%]">
        <div class="tile-category text-[11px] md:text-xs font-black uppercase tracking-[0.24em] text-black/80 mb-1.5">
          #{p[:number]} &mdash; #{p[:category]}
        </div>
        <h2 class="tile-title text-2xl sm:text-3xl md:text-4xl lg:text-5xl font-black tracking-tight text-black mb-2 leading-[1.05]">
          #{p[:title]}
        </h2>
        <p class="tile-desc text-xs sm:text-sm md:text-base text-black/85 font-medium leading-relaxed max-w-sm line-clamp-3 md:line-clamp-none">
          #{p[:description]}
        </p>
      </div>
    </article>
  }
end.join("\n")

mj_data = vecs["mj_black"]

make_html = lambda do |tailwind_src|
%Q{<!DOCTYPE html>
<html lang="fr" class="bg-black">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>MJ — Morgan Janot | Portfolio</title>
  <meta name="description" content="Portfolio personnel & direction artistique de Morgan Janot. Composition visuelle interactive 2x3.">
  <script src="#{tailwind_src}"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
  <style>
    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }
    html, body {
      background-color: #000;
      color: #000;
      font-family: "Plus Jakarta Sans", "Arial Black", -apple-system, BlinkMacSystemFont, sans-serif;
      overflow-x: hidden;
      overflow-y: auto;
      -webkit-font-smoothing: antialiased;
    }

    /* Grid physics and perspective */
    .portfolio-grid {
      perspective: 1200px;
    }

    .portfolio-tile {
      cursor: pointer;
      transform: translate3d(0, 0, 0) scale(1);
      transition: transform 500ms cubic-bezier(0.16, 1, 0.3, 1),
                  box-shadow 500ms cubic-bezier(0.16, 1, 0.3, 1),
                  opacity 400ms cubic-bezier(0.16, 1, 0.3, 1),
                  filter 400ms cubic-bezier(0.16, 1, 0.3, 1);
      will-change: transform, box-shadow;
      z-index: 10;
    }

    /* Active lifted state: zooms over neighbors */
    .portfolio-tile.is-active,
    .portfolio-grid:not(.is-touch) .portfolio-tile:hover {
      transform: translate3d(0, -8px, 0) scale(1.025);
      z-index: 30;
      box-shadow: 0 30px 60px -12px rgba(0, 0, 0, 0.5), 0 0 0 1px rgba(255, 255, 255, 0.2);
    }

    /* Sibling tiles when one is active: NO scaling, no shrinking, so zero gaps! */
    .portfolio-grid.has-active .portfolio-tile:not(.is-active):not(:hover) {
      opacity: 0.95;
      filter: brightness(0.96);
      transform: none !important;
    }

    /* Raw Illustrator illustration animation */
    .tile-illustration {
      transform: translate3d(0, 0, 0) scale(1) rotate(0deg);
      transition: transform 550ms cubic-bezier(0.16, 1, 0.3, 1);
      will-change: transform;
    }
    .portfolio-tile.is-active .tile-illustration,
    .portfolio-grid:not(.is-touch) .portfolio-tile:hover .tile-illustration {
      transform: translate3d(8px, -4px, 0) scale(1.02) rotate(-0.5deg);
    }

    /* Arrow: DOWNWARD, HIDDEN AT REST, APPEARS WITH TEXT ON HOVER */
    .tile-arrow {
      opacity: 0;
      transform: translate3d(0, -20px, 0);
      transition: opacity 450ms cubic-bezier(0.16, 1, 0.3, 1),
                  transform 500ms cubic-bezier(0.16, 1, 0.3, 1);
      will-change: opacity, transform;
    }
    .portfolio-tile.is-active .tile-arrow,
    .portfolio-grid:not(.is-touch) .portfolio-tile:hover .tile-arrow {
      opacity: 1;
      transform: translate3d(0, 0, 0);
      transition-delay: 100ms;
    }

    /* Emerging text animations */
    .tile-content {
      opacity: 0;
      transform: translate3d(0, 20px, 0);
      transition: opacity 400ms cubic-bezier(0.16, 1, 0.3, 1),
                  transform 450ms cubic-bezier(0.16, 1, 0.3, 1);
      will-change: opacity, transform;
    }
    .portfolio-tile.is-active .tile-content,
    .portfolio-grid:not(.is-touch) .portfolio-tile:hover .tile-content {
      opacity: 1;
      transform: translate3d(0, 0, 0);
    }

    .tile-category, .tile-title, .tile-desc {
      opacity: 0;
      transform: translate3d(0, 14px, 0);
      transition: opacity 450ms cubic-bezier(0.16, 1, 0.3, 1),
                  transform 450ms cubic-bezier(0.16, 1, 0.3, 1);
    }

    .portfolio-tile.is-active .tile-category,
    .portfolio-grid:not(.is-touch) .portfolio-tile:hover .tile-category {
      opacity: 1;
      transform: translate3d(0, 0, 0);
      transition-delay: 50ms;
    }
    .portfolio-tile.is-active .tile-title,
    .portfolio-grid:not(.is-touch) .portfolio-tile:hover .tile-title {
      opacity: 1;
      transform: translate3d(0, 0, 0);
      transition-delay: 100ms;
    }
    .portfolio-tile.is-active .tile-desc,
    .portfolio-grid:not(.is-touch) .portfolio-tile:hover .tile-desc {
      opacity: 1;
      transform: translate3d(0, 0, 0);
      transition-delay: 150ms;
    }

    /* Vertical Side Navigation */
    .vertical-nav {
      writing-mode: vertical-rl;
      text-orientation: mixed;
      font-family: "Arial Black", "Plus Jakarta Sans", sans-serif;
    }

    /* Focus visible */
    .portfolio-tile:focus-visible {
      outline: none;
      box-shadow: 0 0 0 4px #000000, 0 30px 60px -12px rgba(0,0,0,0.5);
      z-index: 35;
    }

    /* Reduced Motion */
    @media (prefers-reduced-motion: reduce) {
      .portfolio-tile,
      .tile-illustration,
      .tile-arrow,
      .tile-content,
      .tile-category,
      .tile-title,
      .tile-desc {
        transform: none !important;
        transition: opacity 250ms ease-in-out !important;
      }
    }
  </style>
</head>
<body class="bg-black text-black m-0 p-0 selection:bg-black selection:text-white">

  <!-- Editorial Floating Header: MJ Monogram in Center -->
  <header class="fixed top-0 left-0 w-full z-40 pointer-events-none px-6 py-5 md:px-10 md:py-7">
    <div class="relative w-full flex items-center justify-center">
      <a href="/" class="pointer-events-auto group transition-transform duration-300 hover:scale-105 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-black rounded" aria-label="MJ - Accueil">
        <svg viewBox="#{mj_data['viewBox']}" class="w-24 sm:w-28 md:w-32 h-auto text-black drop-shadow-[0_2px_8px_rgba(0,0,0,0.15)]" fill="#000000">
          <path d="#{mj_data['d']}" />
        </svg>
      </a>
    </div>
  </header>

  <!-- Vertical Side Navigation (Right edge, matching PDF model) -->
  <nav aria-label="Navigation latérale" class="fixed right-0 top-1/2 -translate-y-1/2 z-50 vertical-nav select-none pointer-events-auto">
    <div id="side-nav-items" class="flex items-center gap-7 sm:gap-9 md:gap-11 pr-0 py-4">
      
      <!-- PORTFOLIO: Active with right black bar -->
      <button
        type="button"
        id="nav-portfolio"
        class="nav-item active group relative flex items-center pr-3 md:pr-3.5 transition-all duration-300 uppercase tracking-[0.2em] cursor-pointer outline-none text-black text-sm sm:text-base md:text-lg font-black"
      >
        <span>PORTFOLIO</span>
        <span class="active-bar absolute right-0 top-0 bottom-0 w-2 md:w-2.5 bg-black" aria-hidden="true"></span>
      </button>

      <!-- ABOUT: Smaller by default, normal size on hover -->
      <button
        type="button"
        id="nav-about"
        class="nav-item group relative flex items-center pr-3 md:pr-3.5 transition-all duration-300 uppercase tracking-[0.2em] cursor-pointer outline-none text-black/60 text-xs sm:text-sm font-bold scale-90 opacity-60 hover:scale-100 hover:opacity-100 hover:text-black hover:font-black hover:text-sm sm:hover:text-base md:hover:text-lg"
      >
        <span>ABOUT</span>
        <span class="active-bar hidden absolute right-0 top-0 bottom-0 w-2 md:w-2.5 bg-black" aria-hidden="true"></span>
      </button>

      <!-- CONTACT: Smaller by default, normal size on hover -->
      <button
        type="button"
        id="nav-contact"
        class="nav-item group relative flex items-center pr-3 md:pr-3.5 transition-all duration-300 uppercase tracking-[0.2em] cursor-pointer outline-none text-black/60 text-xs sm:text-sm font-bold scale-90 opacity-60 hover:scale-100 hover:opacity-100 hover:text-black hover:font-black hover:text-sm sm:hover:text-base md:hover:text-lg"
      >
        <span>CONTACT</span>
        <span class="active-bar hidden absolute right-0 top-0 bottom-0 w-2 md:w-2.5 bg-black" aria-hidden="true"></span>
      </button>

    </div>
  </nav>

  <!-- 2-Column Responsive Flowing Grid with Natural Initial Proportions -->
  <main id="portfolio-grid" class="portfolio-grid relative w-full grid grid-cols-1 md:grid-cols-2 gap-0 overflow-hidden bg-black">
    #{tiles_html}
  </main>

  <script>
    (function() {
      const grid = document.getElementById("portfolio-grid");
      const tiles = document.querySelectorAll(".portfolio-tile");
      let activeTile = null;

      const isTouch = "ontouchstart" in window || navigator.maxTouchPoints > 0;
      if (isTouch) {
        grid.classList.add("is-touch");
      }

      function setActiveTile(tile) {
        if (activeTile && activeTile !== tile) {
          activeTile.classList.remove("is-active");
          activeTile.setAttribute("aria-expanded", "false");
        }
        activeTile = tile;
        if (tile) {
          tile.classList.add("is-active");
          tile.setAttribute("aria-expanded", "true");
          grid.classList.add("has-active");
        } else {
          grid.classList.remove("has-active");
        }
      }

      tiles.forEach(tile => {
        tile.addEventListener("mouseenter", () => {
          if (!isTouch) {
            grid.classList.add("has-active");
          }
        });

        tile.addEventListener("mouseleave", () => {
          if (!isTouch) {
            grid.classList.remove("has-active");
          }
        });

        tile.addEventListener("click", (e) => {
          if (tile.classList.contains("is-active")) {
            setActiveTile(null);
          } else {
            setActiveTile(tile);
          }
        });

        tile.addEventListener("keydown", (e) => {
          if (e.key === "Enter" || e.key === " ") {
            e.preventDefault();
            if (tile.classList.contains("is-active")) {
              setActiveTile(null);
            } else {
              setActiveTile(tile);
            }
          }
        });

        tile.addEventListener("focus", () => {
          setActiveTile(tile);
        });
        tile.addEventListener("blur", () => {
          if (activeTile === tile) {
            setActiveTile(null);
          }
        });
      });

      window.addEventListener("keydown", (e) => {
        if (e.key === "Escape") {
          setActiveTile(null);
        }
      });

      document.addEventListener("click", (e) => {
        if (!e.target.closest(".portfolio-tile")) {
          setActiveTile(null);
        }
      });

      // Side Navigation tabs
      const navItems = document.querySelectorAll(".nav-item");
      navItems.forEach(item => {
        item.addEventListener("click", () => {
          navItems.forEach(n => {
            n.classList.remove("active", "text-black", "font-black", "scale-100", "opacity-100", "text-sm", "sm:text-base", "md:text-lg");
            n.classList.add("text-black/60", "font-bold", "scale-90", "opacity-60", "text-xs", "sm:text-sm");
            const bar = n.querySelector(".active-bar");
            if (bar) bar.classList.add("hidden");
          });
          item.classList.add("active", "text-black", "font-black", "scale-100", "opacity-100", "text-sm", "sm:text-base", "md:text-lg");
          item.classList.remove("text-black/60", "font-bold", "scale-90", "opacity-60", "text-xs", "sm:text-sm");
          const bar = item.querySelector(".active-bar");
          if (bar) bar.classList.remove("hidden");
        });
      });
    })();
  </script>
</body>
</html>
}
end

standalone_html = make_html.call("https://cdn.tailwindcss.com")
artifact_html = make_html.call("https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js")

File.write("/Users/morganjanot/.gemini/antigravity/scratch/mj-portfolio/standalone.html", standalone_html, encoding: "UTF-8")
File.write("/Users/morganjanot/.gemini/antigravity/brain/04838ef3-4249-4209-97cb-1440ffec4bcd/portfolio.html", artifact_html, encoding: "UTF-8")
puts "Successfully built standalone.html and portfolio.html v4!"
