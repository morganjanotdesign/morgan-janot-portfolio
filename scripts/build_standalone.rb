# encoding: UTF-8
require "json"

paths = JSON.parse(File.read("/Users/morganjanot/.gemini/antigravity/scratch/extracted_svgs/svg_paths.json"))

projects = [
  {
    id: 1,
    number: "01",
    title: "Pesce Lounge",
    category: "Direction artistique",
    description: "Édition limitée & exploration de formes biomorphiques en mousse expansée.",
    bg: "#e9722b",
    stroke: "#eb6209",
    has_ill: true,
    viewBox: "0 0 440 340"
  },
  {
    id: 2,
    number: "02",
    title: "Arco Cantilever",
    category: "Design d'espace",
    description: "Luminaire architectural télescopique & dispositif d'éclairage cinétique.",
    bg: "#914792",
    stroke: "#812383",
    has_ill: true,
    viewBox: "0 0 439 340"
  },
  {
    id: 3,
    number: "03",
    title: "Bauhaus Sling",
    category: "Mobilier éditorial",
    description: "Assise suspendue en cuir sellier tendu & piétement tubulaire en acier brossé.",
    bg: "#68b42d",
    stroke: "#2c8934",
    has_ill: true,
    viewBox: "0 0 440 342"
  },
  {
    id: 4,
    number: "04",
    title: "Modular Ribbon",
    category: "Scénographie",
    description: "Système modulaire curviligne & îlot d'assises pour la Biennale de Milan.",
    bg: "#775732",
    stroke: "#724b10",
    has_ill: true,
    viewBox: "0 0 439 342"
  },
  {
    id: 5,
    number: "05",
    title: "Biomorphic Bloom",
    category: "Recherche matière",
    description: "Sculpture fonctionnelle en résine coulée translucide & recherche formelle.",
    bg: "#46a0d1",
    stroke: "#27629f",
    has_ill: true,
    viewBox: "0 0 440 342"
  },
  {
    id: 6,
    number: "06",
    title: "Atelier Rouge",
    category: "Manifesto & Archive",
    description: "Laboratoire d'expérimentation typographique, posters et archives graphiques.",
    bg: "#d83d46",
    stroke: "#b2242c",
    has_ill: false,
    viewBox: "0 0 439 342"
  }
]

tiles_html = projects.map do |p|
  ill_svg = ""
  arrow_svg = ""
  if p[:has_ill]
    main_d = paths["tile#{p[:id]}_main_d"]
    arrow_d = paths["tile#{p[:id]}_arrow_d"]

    ill_svg = %Q{
      <div class="tile-illustration absolute inset-0 w-full h-full pointer-events-none">
        <svg viewBox="#{p[:viewBox]}" class="w-full h-full" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="none">
          <path fill="#{p[:stroke]}" fill-rule="evenodd" d="#{main_d}" />
        </svg>
      </div>
    }

    arrow_svg = %Q{
      <div class="tile-arrow absolute inset-0 w-full h-full pointer-events-none">
        <svg viewBox="#{p[:viewBox]}" class="w-full h-full" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="none">
          <path fill="#{p[:stroke]}" fill-rule="evenodd" d="#{arrow_d}" />
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
      class="portfolio-tile relative w-full h-full overflow-hidden select-none outline-none"
      data-id="#{p[:id]}"
      style="background-color: #{p[:bg]};"
    >
      #{ill_svg}
      #{arrow_svg}
      
      <!-- Emerging Project Content -->
      <div class="tile-content absolute bottom-6 left-6 md:bottom-10 md:left-10 z-20 pointer-events-none max-w-[85%] md:max-w-[75%]">
        <div class="tile-category text-[11px] md:text-xs font-semibold uppercase tracking-[0.22em] text-white/85 mb-1.5">
          #{p[:number]} &mdash; #{p[:category]}
        </div>
        <h2 class="tile-title text-2xl sm:text-3xl md:text-4xl font-extrabold tracking-tight text-white mb-2 leading-[1.05]">
          #{p[:title]}
        </h2>
        <p class="tile-desc text-xs sm:text-sm text-white/90 font-normal leading-relaxed max-w-sm">
          #{p[:description]}
        </p>
        <div class="tile-link mt-3 inline-flex items-center gap-2 text-[11px] font-bold uppercase tracking-wider text-white border-b border-white/50 pb-0.5">
          <span>Découvrir le projet</span>
          <span class="text-sm font-normal">&rarr;</span>
        </div>
      </div>
    </article>
  }
end.join("\n")

html = %Q{<!DOCTYPE html>
<html lang="fr" class="bg-black">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>MJ — Morgan Janot | Portfolio</title>
  <meta name="description" content="Portfolio personnel & direction artistique de Morgan Janot. Composition visuelle interactive 2x3.">
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <style>
    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }
    body {
      font-family: "Plus Jakarta Sans", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      background-color: #000;
      color: #fff;
      overflow-x: hidden;
      -webkit-font-smoothing: antialiased;
    }

    /* Grid physics and perspective */
    .portfolio-grid {
      perspective: 1200px;
    }

    .portfolio-tile {
      cursor: pointer;
      min-height: 280px;
      transform: translate3d(0, 0, 0) scale(1);
      transition: transform 520ms cubic-bezier(0.16, 1, 0.3, 1),
                  box-shadow 520ms cubic-bezier(0.16, 1, 0.3, 1),
                  opacity 450ms cubic-bezier(0.16, 1, 0.3, 1),
                  filter 450ms cubic-bezier(0.16, 1, 0.3, 1);
      will-change: transform, box-shadow;
      z-index: 10;
    }

    @media (min-width: 768px) {
      .portfolio-tile {
        min-height: 0;
      }
    }

    /* Active lifted state */
    .portfolio-tile.is-active,
    .portfolio-grid:not(.is-touch) .portfolio-tile:hover {
      transform: translate3d(0, -9px, 0) scale(1.024);
      z-index: 30;
      box-shadow: 0 30px 60px -12px rgba(0, 0, 0, 0.45), 0 0 0 1px rgba(255, 255, 255, 0.15);
    }

    /* Sibling tiles dimming when one is active */
    .portfolio-grid.has-active .portfolio-tile:not(.is-active):not(:hover) {
      opacity: 0.88;
      filter: brightness(0.93) saturate(0.92);
      transform: scale(0.995);
    }

    /* Illustration animation */
    .tile-illustration {
      transform: translate3d(0, 0, 0) scale(1) rotate(0deg);
      transition: transform 550ms cubic-bezier(0.16, 1, 0.3, 1);
      will-change: transform;
    }
    .portfolio-tile.is-active .tile-illustration,
    .portfolio-grid:not(.is-touch) .portfolio-tile:hover .tile-illustration {
      transform: translate3d(8px, -4px, 0) scale(1.03) rotate(-0.5deg);
    }

    /* Arrow animation */
    .tile-arrow {
      transform: translate3d(0, 0, 0) scale(1);
      transition: transform 520ms cubic-bezier(0.16, 1, 0.3, 1);
      will-change: transform;
    }
    .portfolio-tile.is-active .tile-arrow,
    .portfolio-grid:not(.is-touch) .portfolio-tile:hover .tile-arrow {
      transform: translate3d(14px, 0, 0) scale(1.04);
    }

    /* Emerging text animations */
    .tile-content {
      opacity: 0;
      transform: translate3d(0, 22px, 0);
      transition: opacity 400ms cubic-bezier(0.16, 1, 0.3, 1),
                  transform 450ms cubic-bezier(0.16, 1, 0.3, 1);
      will-change: opacity, transform;
    }
    .portfolio-tile.is-active .tile-content,
    .portfolio-grid:not(.is-touch) .portfolio-tile:hover .tile-content {
      opacity: 1;
      transform: translate3d(0, 0, 0);
    }

    .tile-category, .tile-title, .tile-desc, .tile-link {
      opacity: 0;
      transform: translate3d(0, 14px, 0);
      transition: opacity 450ms cubic-bezier(0.16, 1, 0.3, 1),
                  transform 450ms cubic-bezier(0.16, 1, 0.3, 1);
    }

    .portfolio-tile.is-active .tile-category,
    .portfolio-grid:not(.is-touch) .portfolio-tile:hover .tile-category {
      opacity: 1;
      transform: translate3d(0, 0, 0);
      transition-delay: 40ms;
    }
    .portfolio-tile.is-active .tile-title,
    .portfolio-grid:not(.is-touch) .portfolio-tile:hover .tile-title {
      opacity: 1;
      transform: translate3d(0, 0, 0);
      transition-delay: 90ms;
    }
    .portfolio-tile.is-active .tile-desc,
    .portfolio-grid:not(.is-touch) .portfolio-tile:hover .tile-desc {
      opacity: 1;
      transform: translate3d(0, 0, 0);
      transition-delay: 140ms;
    }
    .portfolio-tile.is-active .tile-link,
    .portfolio-grid:not(.is-touch) .portfolio-tile:hover .tile-link {
      opacity: 1;
      transform: translate3d(0, 0, 0);
      transition-delay: 190ms;
    }

    /* Focus visible */
    .portfolio-tile:focus-visible {
      outline: none;
      box-shadow: 0 0 0 4px #ffffff, 0 25px 50px -12px rgba(0,0,0,0.5);
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
      .tile-desc,
      .tile-link {
        transform: none !important;
        transition: opacity 250ms ease-in-out !important;
      }
    }
  </style>
</head>
<body class="bg-black text-white m-0 p-0 overflow-x-hidden selection:bg-white selection:text-black">

  <!-- Editorial Floating Header -->
  <header class="absolute top-0 left-0 w-full z-40 pointer-events-none px-6 py-5 md:px-10 md:py-7">
    <div class="relative w-full flex items-center justify-between">
      <!-- Balance spacer -->
      <div class="w-16 md:w-32 hidden sm:block"></div>

      <!-- Center MJ Monogram sitting precisely on top line split -->
      <a href="/" class="pointer-events-auto absolute left-1/2 -translate-x-1/2 top-0 group transition-transform duration-300 hover:scale-105 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-white rounded" aria-label="MJ - Accueil">
        <svg viewBox="0 0 131 76" class="w-24 sm:w-28 md:w-32 h-auto text-white drop-shadow-[0_2px_8px_rgba(0,0,0,0.18)]" fill="currentColor">
          <path fill-rule="evenodd" d="#{paths['mj_logo_d']}" />
        </svg>
      </a>

      <!-- Right Navigation Links -->
      <nav aria-label="Navigation principale" class="pointer-events-auto ml-auto flex items-center gap-7 sm:gap-9 md:gap-11">
        <a href="#about" class="text-white font-bold text-sm sm:text-base md:text-[17px] tracking-wide hover:opacity-75 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-white/80 rounded transition-all duration-200 select-none drop-shadow-[0_1px_4px_rgba(0,0,0,0.2)]">About</a>
        <a href="#contact" class="text-white font-bold text-sm sm:text-base md:text-[17px] tracking-wide hover:opacity-75 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-white/80 rounded transition-all duration-200 select-none drop-shadow-[0_1px_4px_rgba(0,0,0,0.2)]">Contact</a>
      </nav>
    </div>
  </header>

  <!-- 2x3 Seamless Composition Grid -->
  <main id="portfolio-grid" class="portfolio-grid relative w-full min-h-screen md:h-screen grid grid-cols-1 md:grid-cols-2 grid-rows-6 md:grid-rows-3 gap-0 overflow-hidden bg-black">
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
        // Mouse hover
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

        // Click / Touch toggle
        tile.addEventListener("click", (e) => {
          if (tile.classList.contains("is-active")) {
            setActiveTile(null);
          } else {
            setActiveTile(tile);
          }
        });

        // Keyboard navigation
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

        // Focus & Blur
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
    })();
  </script>
</body>
</html>
}

File.write("/Users/morganjanot/.gemini/antigravity/scratch/mj-portfolio/standalone.html", html, encoding: "UTF-8")
File.write("/Users/morganjanot/.gemini/antigravity/brain/04838ef3-4249-4209-97cb-1440ffec4bcd/portfolio.html", html, encoding: "UTF-8")
puts "Successfully generated standalone.html and portfolio.html (#{html.bytesize} bytes)!"
