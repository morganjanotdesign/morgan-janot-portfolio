import React from "react";

/**
 * AboutView Component
 * 
 * Avant-garde editorial presentation with the unified art direction:
 * - Tactile paper texture & Klein Blue atelier frame
 * - Modernist vector sculpture illustration & frosted cartouche
 * - Chromatic swatches & editorial quote
 */
export default function AboutView({ onNavigate }) {
  return (
    <section className="relative w-full min-h-screen bg-black text-white pt-24 pb-28 px-6 sm:px-12 md:px-16 lg:px-24">
      <div className="max-w-[1240px] mx-auto">
        <div className="grid grid-cols-1 lg:grid-cols-[1fr_420px] gap-12 lg:gap-20 items-start">
          
          {/* Left Column: Text, Manifesto, Grid */}
          <div>
            <div className="flex items-center flex-wrap gap-4 mb-6">
              <span className="text-xs font-black uppercase tracking-[0.24em] text-neutral-400">
                01 &mdash; À Propos
              </span>
              <span className="inline-flex items-center text-[11px] font-black uppercase tracking-[0.18em] px-2.5 py-1 rounded-sm bg-[rgba(0,51,255,0.22)] text-[#7099ff] border border-[rgba(0,51,255,0.4)]">
                * ATELIER &amp; PRATIQUE *
              </span>
            </div>

            <h1 className="text-4xl sm:text-6xl md:text-7xl lg:text-8xl font-black tracking-tight leading-[0.95] mb-8 select-none">
              Morgan Janot
            </h1>

            <p className="text-xl sm:text-2xl md:text-3xl font-bold leading-snug mb-8 text-neutral-200 max-w-2xl">
              Direction artistique, scénographie contemporaine et design d'objets sculpturaux basés à Paris.
            </p>

            <div className="space-y-4 text-base sm:text-lg text-neutral-400 leading-relaxed max-w-2xl mb-10">
              <p>
                Ma pratique explore la tension entre la rigueur géométrique, la radicalité chromatique et la recherche de formes organiques. Chaque pièce est pensée comme un objet sculptural doté d'une présence physique forte.
              </p>
              <p>
                J'accompagne des maisons de création, des institutions culturelles et des galeries indépendantes dans la conception d'espaces immersifs, d'éditions de mobilier et d'identités graphiques contemporaines.
              </p>
            </div>

            {/* Manifesto Quote Card */}
            <blockquote className="relative flex flex-col p-6 sm:p-7 bg-white/[0.04] backdrop-blur-md border-l-[3px] border-[#ccff00] my-9">
              <p className="font-serif italic text-base sm:text-xl text-neutral-100 mb-3 leading-relaxed">
                « L'objet sculptural comme point de convergence entre rigueur graphique, radicalité chromatique et matière tactile. »
              </p>
              <cite className="text-xs font-extrabold uppercase tracking-[0.16em] text-neutral-400 not-italic">
                &mdash; Morgan Janot, Note d'atelier
              </cite>
            </blockquote>

            {/* 3-Column Information Grid with Chromatic Swatches */}
            <div className="grid grid-cols-1 sm:grid-cols-3 gap-8 pt-9 border-t border-white/20 mb-12">
              <div>
                <h2 className="text-xs font-black uppercase tracking-[0.2em] text-neutral-400 mb-4 flex items-center">
                  <span className="w-2 h-2 rounded-[1px] bg-[#ccff00] mr-2 inline-block"></span>
                  Domaines
                </h2>
                <ul className="space-y-2 text-sm sm:text-base font-bold text-white">
                  <li>Direction Artistique</li>
                  <li>Design d'Espace</li>
                  <li>Mobilier Éditorial</li>
                  <li>Scénographie d'Exposition</li>
                  <li>Recherche Formelle</li>
                </ul>
              </div>

              <div>
                <h2 className="text-xs font-black uppercase tracking-[0.2em] text-neutral-400 mb-4 flex items-center">
                  <span className="w-2 h-2 rounded-[1px] bg-[#b4b9c0] mr-2 inline-block"></span>
                  Expositions
                </h2>
                <ul className="space-y-2 text-sm sm:text-base font-bold text-white">
                  <li>Biennale de Milan (2025)</li>
                  <li>Pavillon de l'Arsenal (2024)</li>
                  <li>Galerie Contemporaine (2023)</li>
                  <li>Salone del Mobile (2022)</li>
                </ul>
              </div>

              <div>
                <h2 className="text-xs font-black uppercase tracking-[0.2em] text-neutral-400 mb-4 flex items-center">
                  <span className="w-2 h-2 rounded-[1px] bg-[#00e5ff] mr-2 inline-block"></span>
                  Collaborations
                </h2>
                <ul className="space-y-2 text-sm sm:text-base font-bold text-white">
                  <li>Maisons de luxe</li>
                  <li>Institutions culturelles</li>
                  <li>Éditeurs de design</li>
                  <li>Collectifs d'architectes</li>
                </ul>
              </div>
            </div>

            {/* Back to Portfolio Link */}
            <div className="mt-12">
              <button
                type="button"
                onClick={() => onNavigate("portfolio")}
                className="inline-flex items-center gap-3 text-sm font-black uppercase tracking-widest text-white hover:opacity-60 transition-opacity"
              >
                <span>&larr;</span>
                <span className="border-b-2 border-white pb-0.5">Retourner au portfolio</span>
              </button>
            </div>
          </div>

          {/* Right Column: Atelier Art Frame (Echoing the Portfolio Project Frames) */}
          <div className="lg:sticky lg:top-24">
            <aside className="flex flex-col" aria-label="Estampe d'atelier Morgan Janot">
              <div className="relative w-full aspect-[420/500] min-h-[420px] bg-[#0033e6] overflow-hidden shadow-2xl transition-all duration-300 hover:-translate-y-1.5 hover:scale-[1.015] group">
                {/* Paper Fiber Texture Layer 1 (Multiply) */}
                <div 
                  className="absolute inset-0 pointer-events-none z-[3] mix-blend-multiply opacity-60"
                  style={{
                    backgroundImage: `url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 250 250' width='250' height='250'%3E%3Cfilter id='paperFibers' x='0' y='0' width='100%25' height='100%25'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.62' numOctaves='4' result='noise' stitchTiles='stitch'/%3E%3CfeColorMatrix type='matrix' values='3.5 0 0 0 -1.2  0 3.5 0 0 -1.2  0 0 3.5 0 -1.2  0 0 0 1 0' in='noise' result='contrasted'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23paperFibers)'/%3E%3C/svg%3E")`,
                    backgroundSize: '200px 200px'
                  }}
                />
                {/* Paper Tooth & Vignette Layer 2 (Overlay) */}
                <div 
                  className="absolute inset-0 pointer-events-none z-[4] mix-blend-overlay opacity-80"
                  style={{
                    backgroundImage: `radial-gradient(ellipse at 50% 40%, rgba(255, 255, 255, 0.15) 0%, rgba(0, 0, 0, 0.30) 100%), url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 250 250' width='250' height='250'%3E%3Cfilter id='paperGrainTooth' x='0' y='0' width='100%25' height='100%25'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.78' numOctaves='3' result='noise' stitchTiles='stitch'/%3E%3CfeColorMatrix type='matrix' values='2.5 0 0 0 -0.7  0 2.5 0 0 -0.7  0 0 2.5 0 -0.7  0 0 0 1 0' in='noise' result='contrasted'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23paperGrainTooth)'/%3E%3C/svg%3E")`,
                    backgroundSize: '100% 100%, 160px 160px',
                    boxShadow: 'inset 0 0 80px rgba(0, 0, 0, 0.22)'
                  }}
                />

                {/* Vector Drawing */}
                <div className="absolute inset-0 flex items-center justify-center p-6 pointer-events-none transition-transform duration-300 group-hover:scale-[1.02]">
                  <svg viewBox="0 0 460 560" preserveAspectRatio="xMinYMid meet" fill="none" stroke="rgb(0, 18, 120)" strokeWidth="13" strokeLinecap="round" strokeLinejoin="round" className="w-auto h-[88%] max-w-[90%]">
                    <path d="M 230 40 C 310 40 370 100 370 170 C 370 230 320 275 250 285 L 250 330 C 330 340 390 380 390 440 C 390 500 320 520 230 520 C 140 520 70 500 70 440 C 70 380 130 340 210 330 L 210 285 C 140 275 90 230 90 170 C 90 100 150 40 230 40 Z M 160 170 C 160 130 190 100 230 100 C 270 100 300 130 300 170 C 300 210 270 240 230 240 C 190 240 160 210 160 170 Z M 140 440 C 140 410 180 385 230 385 C 280 385 320 410 320 440 C 320 470 280 485 230 485 C 180 485 140 470 140 440 Z" />
                  </svg>
                </div>

                {/* Signature Frosted Cartouche */}
                <div className="absolute bottom-0 inset-x-0 p-6 sm:p-7 bg-white/15 backdrop-blur-md z-20 flex flex-col items-start shadow-sm">
                  <span className="text-[11px] font-black uppercase tracking-[0.2em] text-black/85 mb-1">
                    00 — Recherche formelle
                  </span>
                  <h3 className="text-2xl sm:text-3xl font-black tracking-tight text-black leading-none mb-1.5">
                    Totem Sculptural
                  </h3>
                  <div className="flex items-center gap-2 text-[10px] font-black uppercase tracking-widest text-black/70">
                    <span>ESTAMPE D'ATELIER</span>
                    <span className="text-xs text-black">*</span>
                    <span>PARIS 2026</span>
                  </div>
                </div>
              </div>

              <div className="pt-3.5">
                <p className="font-serif text-sm text-neutral-400 leading-normal">
                  Étude de volumes géométriques en tension — Monolithe en chêne noirci et laque Klein. Atelier Paris 4<sup>e</sup>.
                </p>
              </div>
            </aside>
          </div>

        </div>
      </div>
    </section>
  );
}
