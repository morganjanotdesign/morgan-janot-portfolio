import React, { useState } from "react";
import { FrameIllustration } from "./Illustrations";

/**
 * PortfolioTile Component
 * - Seamless square tile (aspect 1:1, gap: 0)
 * - Léger zoom au survol et retour à la forme initiale quand on quitte
 * - Liseret en pur flou d'arrière-plan sans couleur opaque avec nom du projet
 * - Texte explicatif à GAUCHE pour les cadres de gauche, à DROITE pour les cadres de droite
 */
export default function PortfolioTile({
  project,
  index = 0,
  isHovered,
  onHover,
  onLeave,
  onToggle
}) {
  const [isFocused, setIsFocused] = useState(false);
  const isActive = isHovered || isFocused;

  const handleKeyDown = (e) => {
    if (e.key === "Enter" || e.key === " ") {
      e.preventDefault();
      onToggle();
    }
  };

  const isLeftCol = index % 2 === 0; // Cadre de gauche (colonne 1)

  // Métadonnées spécifiques au cartouche par projet (sans la 3e ligne)
  const cartoucheInfo = {
    "01": {
      tag: "01 — FOG CHAIR // C001 PARIS",
      title: <>* FOG CHAIR <span className="title-bullet">●</span> MODEL-001 *</>
    },
    "02": {
      tag: "02 — CINÉTIQUE & LUMIÈRE // STUDIO",
      title: "* LAMPADAIRE ARTICULÉ *"
    },
    "03": {
      tag: "03 — RECHERCHE FORMELLE // ATELIER JANOT",
      title: "* CANAPÉ GALET *"
    },
    "04": {
      tag: "04 — STRUCTURE GÉOMÉTRIQUE // PARIS",
      title: "* CHAISE SUSPENDUE *"
    },
    "05": {
      tag: "05 — ENCEINTE STÉRÉO // DESIGN PRODUIT",
      title: "* DAA-DAA *"
    },
    "06": {
      tag: "06 — LUMINAIRE // STUDIO PARIS",
      title: "* LEO-11 *"
    }
  }[project.number] || {
    tag: `${project.number} — ${project.category.toUpperCase()}`,
    title: `* ${project.title.toUpperCase()} *`
  };

  return (
    <article
      id={`project-${project.number}`}
      tabIndex={0}
      role="button"
      aria-label={`${project.number} - ${project.title}`}
      aria-expanded={isActive}
      onMouseEnter={onHover}
      onMouseLeave={onLeave}
      onFocus={() => {
        setIsFocused(true);
        onHover();
      }}
      onBlur={() => {
        setIsFocused(false);
        onLeave();
      }}
      onClick={onToggle}
      onKeyDown={handleKeyDown}
      className={`
        relative select-none outline-none aspect-square block cursor-pointer group
        transition-all duration-360 ease-[cubic-bezier(0.16,1,0.3,1)]
        ${isActive
          ? "scale-[1.035] z-25 shadow-[0_16px_38px_-10px_rgba(0,0,0,0.65)]"
          : "scale-100 z-1 shadow-none"
        }
      `}
    >
      {/* Colored Frame */}
      <div
        style={{ backgroundColor: project.bgColor }}
        className={`
          relative w-full h-full aspect-square overflow-hidden cursor-pointer select-none outline-none
          transition-filter duration-250 ease-out
          ${isActive ? "brightness-[1.02]" : "brightness-100"}
        `}
      >
        {/* Background Vector Illustration Layer (Centered, unclipped) */}
        {project.illustrationKey && (
          <div className="absolute inset-0 flex items-center justify-center p-3 sm:p-4 md:p-5 pointer-events-none">
            <FrameIllustration
              illustrationKey={project.illustrationKey}
              strokeColor={project.strokeColor}
              className={`w-[88%] h-[88%] object-contain transition-transform duration-400 ease-out ${
                isActive ? "scale-[1.02]" : "scale-100"
              }`}
            />
          </div>
        )}

        {/* Layer 1: Dark Paper Fibers & Pulp (Multiply) */}
        <div
          aria-hidden="true"
          className="absolute inset-0 pointer-events-none z-[3] opacity-58 mix-blend-multiply transition-opacity duration-350 group-hover:opacity-68"
          style={{
            backgroundImage: `url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 250 250' width='250' height='250'%3E%3Cfilter id='paperFibers' x='0' y='0' width='100%25' height='100%25'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.62' numOctaves='4' result='noise' stitchTiles='stitch'/%3E%3CfeColorMatrix type='matrix' values='3.5 0 0 0 -1.2  0 3.5 0 0 -1.2  0 0 3.5 0 -1.2  0 0 0 1 0' in='noise' result='contrasted'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23paperFibers)'/%3E%3C/svg%3E")`,
            backgroundSize: "200px 200px",
          }}
        />

        {/* Layer 2: Paper Tooth, Relief Highlights & Vignette (Overlay) */}
        <div
          aria-hidden="true"
          className="absolute inset-0 pointer-events-none z-[4] opacity-80 mix-blend-overlay transition-opacity duration-350 group-hover:opacity-95"
          style={{
            backgroundImage: `radial-gradient(ellipse at 50% 40%, rgba(255, 255, 255, 0.15) 0%, rgba(0, 0, 0, 0.30) 100%), url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 250 250' width='250' height='250'%3E%3Cfilter id='paperGrainTooth' x='0' y='0' width='100%25' height='100%25'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.78' numOctaves='3' result='noise' stitchTiles='stitch'/%3E%3CfeColorMatrix type='matrix' values='2.5 0 0 0 -0.7  0 2.5 0 0 -0.7  0 0 2.5 0 -0.7  0 0 0 1 0' in='noise' result='contrasted'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23paperGrainTooth)'/%3E%3C/svg%3E")`,
            backgroundSize: "100% 100%, 160px 160px",
            boxShadow: "inset 0 0 80px rgba(0, 0, 0, 0.22)",
          }}
        />

        {/* LISERET AU SURVOL DU CADRE : PUR EFFET DE FLOU (SANS COULEUR OPAQUE, CONSERVE LA TEINTE NATURELLE DU CADRE) */}
        <div
          className={`
            absolute bottom-0 left-0 right-0 w-full z-25 pointer-events-none
            flex flex-col items-start justify-end px-3.5 py-3 sm:px-4 sm:py-3.5 md:px-5 md:py-4
            bg-white/5 backdrop-blur-md saturate-120 border-none shadow-none
            transition-all duration-300 ease-[cubic-bezier(0.16,1,0.3,1)]
            ${isActive ? "opacity-100 translate-y-0" : "opacity-0 translate-y-full"}
          `}
        >
          <div className="text-[8px] sm:text-[9px] md:text-[10px] font-black uppercase tracking-[0.16em] text-black/90 mb-1 leading-tight">
            {cartoucheInfo.tag}
          </div>
          <h3 className="text-[14px] sm:text-[16px] md:text-[19px] font-black tracking-tight text-black leading-tight m-0 uppercase whitespace-normal break-words">
            {cartoucheInfo.title}
          </h3>
        </div>
      </div>

      {/* Texte explicatif latéral : à GAUCHE pour cadres de gauche, à DROITE pour cadres de droite */}
      <div
        className={`
          hidden min-[950px]:block absolute bottom-2 sm:bottom-2.5 w-[clamp(170px,18vw,250px)] z-30 pointer-events-none
          transition-all duration-280 ease-out
          ${isLeftCol
            ? "right-[calc(100%+clamp(16px,1.8vw,28px))] text-right"
            : "left-[calc(100%+clamp(16px,1.8vw,28px))] text-left"
          }
          ${isActive ? "opacity-100 translate-y-0" : "opacity-0 translate-y-1"}
        `}
      >
        <p className="font-serif text-[clamp(11.5px,0.95vw,14px)] leading-relaxed text-white/75 tracking-[0.01em]">
          {project.description}
        </p>
      </div>
    </article>
  );
}
