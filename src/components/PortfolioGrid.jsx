import React, { useState, useEffect } from "react";
import PortfolioTile from "./PortfolioTile";
import { projects } from "../data/projectsData";

/**
 * PortfolioGrid Component
 * - 2-column by 3-row layout of frames (seamless mosaic, square 1:1, gap: 0)
 * - Léger zoom au survol, liseret dans le cadre, texte à gauche (colonne gauche) ou à droite (colonne droite)
 * - Retour à la forme initiale quand on quitte le cadre
 */
export default function PortfolioGrid({ onSelectProject }) {
  const [activeTileId, setActiveTileId] = useState(null);

  useEffect(() => {
    const handleKeyDown = (e) => {
      if (e.key === "Escape") {
        setActiveTileId(null);
      }
    };
    window.addEventListener("keydown", handleKeyDown);
    return () => window.removeEventListener("keydown", handleKeyDown);
  }, []);

  const activeProject = projects.find((p) => p.id === activeTileId);

  return (
    <section className="relative w-full px-4 sm:px-6 md:px-10 pb-28 flex flex-col items-center">
      <div className="relative w-full max-w-[clamp(340px,36.8vw,520px)] mx-auto">
        <div className="grid grid-cols-2 gap-0 w-full mx-auto relative">
          {projects.map((project, index) => (
            <PortfolioTile
              key={project.id}
              project={project}
              index={index}
              isHovered={activeTileId === project.id}
              onHover={() => setActiveTileId(project.id)}
              onLeave={() => setActiveTileId(null)}
              onToggle={() => {
                if (onSelectProject) {
                  onSelectProject(`project-${project.number}`);
                } else {
                  setActiveTileId((prev) => (prev === project.id ? null : project.id));
                }
              }}
            />
          ))}
        </div>

        {/* Caption mobile (< 950px) */}
        {activeProject && (
          <div className="block min-[950px]:hidden w-full max-w-[clamp(280px,80vw,440px)] mx-auto mt-5 text-center min-h-[48px] transition-opacity duration-250">
            <p className="font-serif text-[13px] leading-relaxed text-white/75">
              {activeProject.description}
            </p>
          </div>
        )}
      </div>
    </section>
  );
}
