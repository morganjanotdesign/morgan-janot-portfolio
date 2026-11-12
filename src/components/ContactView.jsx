import React from "react";

/**
 * ContactView Component
 * 
 * Avant-garde editorial presentation with the unified art direction:
 * - Tactile stationery card with paper grain
 * - Live studio status & geolocation
 * - Frosted social chips with color dots
 * - Official 6-swatch studio palette strip
 */
export default function ContactView({ onNavigate }) {
  const swatches = [
    { num: "01", color: "rgb(255, 94, 0)", name: "Orange Fluo (Fog Chair)" },
    { num: "02", color: "rgb(180, 185, 192)", name: "Gris Minéral (Lampadaire Articulé)" },
    { num: "03", color: "rgb(0, 140, 70)", name: "Vert Studio Profond (Canapé Galet)" },
    { num: "04", color: "rgb(227, 6, 19)", name: "Rouge Suisse (Chaise Suspendue)" },
    { num: "05", color: "rgb(0, 130, 255)", name: "Bleu Cobalt Fluo (DAA-DAA)" },
    { num: "06", color: "rgb(255, 235, 0)", name: "Jaune Fluo (Arche Radiale)" },
  ];

  return (
    <section className="relative w-full min-h-screen bg-black text-white pt-24 pb-28 px-6 sm:px-12 md:px-16 lg:px-24">
      <div className="max-w-4xl mx-auto">
        {/* Breadcrumb / Category */}
        <div className="flex items-center flex-wrap gap-4 mb-6">
          <span className="text-xs font-black uppercase tracking-[0.24em] text-neutral-400">
            02 &mdash; Contact
          </span>
          <span className="inline-flex items-center text-[11px] font-black uppercase tracking-[0.18em] px-2.5 py-1 rounded-sm bg-[rgba(255,94,0,0.22)] text-[#ff914d] border border-[rgba(255,94,0,0.4)]">
            * STUDIO &amp; INVITATION *
          </span>
        </div>

        {/* Main Title */}
        <h1 className="text-4xl sm:text-6xl md:text-7xl lg:text-8xl font-black tracking-tight leading-[0.95] mb-8 select-none">
          Travaillons ensemble.
        </h1>

        <p className="text-xl sm:text-2xl md:text-3xl font-bold leading-snug mb-12 text-neutral-200 max-w-3xl">
          Pour une collaboration, une commande de mobilier ou une demande d'exposition, contactez le studio directement.
        </p>

        {/* Tactile Stationery Card */}
        <div className="relative bg-[#0d0d10] border border-white/15 p-7 sm:p-12 mb-12 shadow-2xl overflow-hidden">
          {/* Paper Fiber Texture Layer 1 */}
          <div 
            className="absolute inset-0 pointer-events-none z-[1] mix-blend-multiply opacity-35"
            style={{
              backgroundImage: `url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 250 250' width='250' height='250'%3E%3Cfilter id='paperFibers' x='0' y='0' width='100%25' height='100%25'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.62' numOctaves='4' result='noise' stitchTiles='stitch'/%3E%3CfeColorMatrix type='matrix' values='3.5 0 0 0 -1.2  0 3.5 0 0 -1.2  0 0 3.5 0 -1.2  0 0 0 1 0' in='noise' result='contrasted'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23paperFibers)'/%3E%3C/svg%3E")`,
              backgroundSize: '200px 200px'
            }}
          />
          {/* Paper Tooth Layer 2 */}
          <div 
            className="absolute inset-0 pointer-events-none z-[2] mix-blend-overlay opacity-60"
            style={{
              backgroundImage: `radial-gradient(ellipse at 50% 30%, rgba(255, 255, 255, 0.08) 0%, rgba(0, 0, 0, 0.35) 100%), url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 250 250' width='250' height='250'%3E%3Cfilter id='paperGrainTooth' x='0' y='0' width='100%25' height='100%25'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.78' numOctaves='3' result='noise' stitchTiles='stitch'/%3E%3CfeColorMatrix type='matrix' values='2.5 0 0 0 -0.7  0 2.5 0 0 -0.7  0 0 2.5 0 -0.7  0 0 0 1 0' in='noise' result='contrasted'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23paperGrainTooth)'/%3E%3C/svg%3E")`,
              backgroundSize: '100% 100%, 160px 160px'
            }}
          />

          <div className="relative z-10">
            {/* Status Bar */}
            <div className="flex items-center justify-between flex-wrap gap-4 pb-6 mb-8 border-b border-white/10">
              <div className="inline-flex items-center gap-2.5">
                <span className="w-2.5 h-2.5 rounded-full bg-[#ccff00] shadow-[0_0_10px_#ccff00] animate-pulse"></span>
                <span className="text-[11px] font-black uppercase tracking-[0.18em] text-[#ccff00]">
                  * STUDIO OUVERT &mdash; NOUVEAUX PROJETS (2026) *
                </span>
              </div>
              <div className="text-[11px] font-extrabold uppercase tracking-[0.2em] text-neutral-400">
                PARIS 48.8566&deg; N &bull; 2.3522&deg; E
              </div>
            </div>

            {/* Direct Email */}
            <div className="mb-10">
              <div className="text-xs font-black uppercase tracking-[0.2em] text-neutral-400 mb-2">
                Email direct du Studio
              </div>
              <a
                href="mailto:bonjour@morganjanot.com"
                className="text-2xl sm:text-4xl md:text-5xl font-black text-white hover:text-[#00e5ff] transition-colors underline decoration-4 underline-offset-8 break-all"
              >
                bonjour@morganjanot.com
              </a>
            </div>

            {/* Phone & Address */}
            <div className="grid grid-cols-1 md:grid-cols-2 gap-8 mb-10">
              <div>
                <div className="text-xs font-black uppercase tracking-[0.2em] text-neutral-400 mb-2 flex items-center">
                  <span className="w-2 h-2 rounded-[1px] bg-[rgb(255,94,0)] mr-2 inline-block"></span>
                  Téléphone
                </div>
                <a
                  href="tel:+33142685000"
                  className="text-lg sm:text-2xl font-bold text-white hover:text-[#ff3b00] transition-colors"
                >
                  +33 (0)1 42 68 50 00
                </a>
              </div>

              <div>
                <div className="text-xs font-black uppercase tracking-[0.2em] text-neutral-400 mb-2 flex items-center">
                  <span className="w-2 h-2 rounded-[1px] bg-[rgb(0,245,255)] mr-2 inline-block"></span>
                  Atelier &amp; Studio
                </div>
                <address className="text-lg sm:text-2xl font-bold text-white not-italic leading-snug">
                  12, rue de Turenne<br />
                  75004 Paris, France
                </address>
              </div>
            </div>

            {/* Social Chips */}
            <div className="pt-8 border-t border-white/10">
              <div className="text-xs font-black uppercase tracking-[0.2em] text-neutral-400 mb-4">
                Réseaux &amp; Archives Numériques
              </div>
              <div className="flex flex-wrap gap-4">
                <a
                  href="https://instagram.com"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="inline-flex items-center gap-2.5 px-5 py-3 bg-white/[0.08] backdrop-blur-md border border-white/15 text-xs font-black uppercase tracking-widest text-white hover:-translate-y-0.5 hover:bg-white/15 transition-all"
                >
                  <span className="w-2 h-2 rounded-full bg-[rgb(0,204,102)]"></span>
                  <span>* INSTAGRAM *</span>
                  <span className="text-sm">&nearr;</span>
                </a>
                <a
                  href="https://linkedin.com"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="inline-flex items-center gap-2.5 px-5 py-3 bg-white/[0.08] backdrop-blur-md border border-white/15 text-xs font-black uppercase tracking-widest text-white hover:-translate-y-0.5 hover:bg-white/15 transition-all"
                >
                  <span className="w-2 h-2 rounded-full bg-[rgb(0,245,255)]"></span>
                  <span>* LINKEDIN *</span>
                  <span className="text-sm">&nearr;</span>
                </a>
                <a
                  href="https://behance.net"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="inline-flex items-center gap-2.5 px-5 py-3 bg-white/[0.08] backdrop-blur-md border border-white/15 text-xs font-black uppercase tracking-widest text-white hover:-translate-y-0.5 hover:bg-white/15 transition-all"
                >
                  <span className="w-2 h-2 rounded-full bg-[rgb(255,235,0)]"></span>
                  <span>* BEHANCE *</span>
                  <span className="text-sm">&nearr;</span>
                </a>
              </div>
            </div>

          </div>
        </div>

        {/* Studio Palette Strip (Reminder of the 6 Iconic Project Colors) */}
        <div className="p-6 bg-white/[0.03] border border-white/10 flex flex-col gap-3.5 mb-12">
          <div className="flex items-center justify-between flex-wrap gap-2 text-[11px] font-black uppercase tracking-[0.2em] text-neutral-400">
            <span>NUANCIER D'ATELIER &bull; S&Eacute;RIE 2026</span>
            <span>6 TEINTES OFFICIELLES</span>
          </div>
          <div className="grid grid-cols-3 sm:grid-cols-6 gap-2.5">
            {swatches.map((s) => (
              <div
                key={s.num}
                className="relative h-10 flex items-end p-2 cursor-default transition-transform hover:-translate-y-0.5 hover:scale-105"
                style={{ backgroundColor: s.color }}
                title={s.name}
              >
                <span className="text-[10px] font-black tracking-wider text-black/85">
                  {s.num}
                </span>
              </div>
            ))}
          </div>
        </div>

        {/* Back Link */}
        <div>
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
    </section>
  );
}
