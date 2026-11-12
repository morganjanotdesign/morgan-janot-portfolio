import React, { useEffect } from "react";
import { projects } from "../data/projectsData";
import { FrameIllustration } from "./Illustrations";

/**
 * ProjectsDrawer Component
 * Off-canvas panel on the right side listing all 6 projects with visual thumbnails.
 * Clicking a project navigates to it and closes the drawer.
 */
export default function ProjectsDrawer({ isOpen, onClose, onSelectProject, onNavigate, theme = "dark", onSetTheme }) {
  useEffect(() => {
    const handleKeyDown = (e) => {
      if (e.key === "Escape" && isOpen) {
        onClose();
      }
    };
    window.addEventListener("keydown", handleKeyDown);
    return () => window.removeEventListener("keydown", handleKeyDown);
  }, [isOpen, onClose]);

  return (
    <>
      {/* Backdrop overlay */}
      <div
        onClick={onClose}
        aria-hidden="true"
        className={`fixed inset-0 bg-black/75 backdrop-blur-md z-[250] transition-opacity duration-350 ${
          isOpen ? "opacity-100 pointer-events-auto" : "opacity-0 pointer-events-none"
        }`}
      />

      {/* Slide-out drawer */}
      <aside
        role="dialog"
        aria-modal="true"
        aria-label="Liste des projets"
        aria-hidden={!isOpen}
        className={`
          fixed top-0 right-0 bottom-0 z-[260]
          w-[clamp(350px,38vw,520px)] max-w-full
          bg-[#0a0a0af5] backdrop-blur-2xl
          border-l border-white/10 shadow-[-24px_0_80px_rgba(0,0,0,0.96)]
          flex flex-col
          transition-transform duration-400 ease-[cubic-bezier(0.16,1,0.3,1)]
          ${isOpen ? "translate-x-0" : "translate-x-full"}
        `}
      >
        {/* Header */}
        <div className="flex flex-col justify-center px-6 sm:px-8 py-6 pr-20 border-b border-white/10 relative">
          <div className="flex items-center gap-2 mb-1">
            <span className="inline-block w-2 h-2 rounded-full bg-[#ccff00] shadow-[0_0_10px_#ccff00] animate-pulse" />
            <span className="text-[11px] font-extrabold tracking-[0.18em] text-white/50 uppercase">
              SÉLECTION ÉDITORIALE
            </span>
          </div>
          <h3
            className="text-2xl font-black tracking-[0.08em] uppercase text-white flex items-baseline gap-2"
            style={{ fontFamily: '"Arial Black", "Impact", sans-serif' }}
          >
            PROJETS <span className="text-white/35 text-base font-normal">[ 06 ]</span>
          </h3>
          <p className="text-xs text-white/45 mt-1 tracking-wide">
            Catalogue des pièces & scénographies contemporaines
          </p>
        </div>

        {/* Projects List */}
        <div className="flex-1 overflow-y-auto px-6 sm:px-8 py-4">
          <ul className="flex flex-col gap-3 list-none p-0 m-0">
            {projects.map((proj) => (
              <li key={proj.id}>
                <button
                  type="button"
                  onClick={() => onSelectProject(proj.id)}
                  className="w-full group flex items-center justify-between p-3 sm:p-3.5 rounded-2xl bg-white/[0.035] hover:bg-white/[0.08] border border-white/[0.07] hover:border-white/25 transition-all duration-280 hover:-translate-x-1.5 text-left cursor-pointer shadow-sm hover:shadow-[0_10px_30px_-10px_rgba(255,255,255,0.15)]"
                >
                  <div className="flex items-center gap-3.5">
                    {/* Visual Vector Thumbnail */}
                    <div
                      style={{ backgroundColor: proj.bgColor }}
                      className="w-[58px] h-[48px] rounded-xl flex items-center justify-center p-1.5 flex-shrink-0 shadow-md group-hover:scale-105 transition-transform overflow-hidden"
                    >
                      <FrameIllustration
                        illustrationKey={proj.illustrationKey}
                        strokeColor={proj.strokeColor}
                        className="w-full h-full object-contain group-hover:scale-110 transition-transform duration-300"
                      />
                    </div>

                    <div className="flex flex-col">
                      <div className="flex items-center gap-2">
                        <span className="text-[11px] font-extrabold tracking-widest text-white/50 font-mono">
                          {proj.number}
                        </span>
                        <span className="text-[10px] text-white/30 tracking-widest">
                          2026
                        </span>
                      </div>
                      <span className="text-base font-black text-white tracking-wide group-hover:text-white transition-colors"
                        style={{ fontFamily: '"Arial Black", "Impact", sans-serif' }}
                      >
                        {proj.title}
                      </span>
                      <span className="text-[11px] text-white/50 tracking-wider">
                        {proj.category || "Design de mobilier"}
                      </span>
                    </div>
                  </div>

                  <div className="w-8 h-8 rounded-full bg-white/[0.04] border border-white/[0.08] group-hover:bg-white/20 group-hover:border-white/35 flex items-center justify-center flex-shrink-0 text-white/40 group-hover:text-white group-hover:translate-x-0.5 transition-all duration-200 text-sm">
                    &rarr;
                  </div>
                </button>
              </li>
            ))}
          </ul>
        </div>

        {/* Footer (Bas du menu de droite) */}
        <div className="p-6 border-t border-white/10 flex flex-col gap-4 bg-black/30">
          {/* Bouton pour changer de mode clair ou sombre en bas du menu */}
          <div className="flex flex-col gap-2 pb-2.5 border-b border-white/10">
            <div className="flex items-center justify-between text-[10px] font-black tracking-widest text-white/40 uppercase">
              <span>APPARENCE</span>
              <span className="text-white font-bold">{theme === "light" ? "MODE CLAIR" : "MODE SOMBRE"}</span>
            </div>
            <div className="grid grid-cols-2 gap-1.5 p-1 rounded-xl bg-white/[0.06] border border-white/10">
              <button
                type="button"
                onClick={() => onSetTheme && onSetTheme("dark")}
                className={`flex items-center justify-center gap-2 py-2 px-3 rounded-lg text-xs font-black uppercase tracking-wider transition-all ${
                  theme === "dark"
                    ? "bg-white/20 text-white shadow-sm"
                    : "text-white/40 hover:text-white"
                }`}
              >
                <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round">
                  <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path>
                </svg>
                <span>Sombre</span>
              </button>
              <button
                type="button"
                onClick={() => onSetTheme && onSetTheme("light")}
                className={`flex items-center justify-center gap-2 py-2 px-3 rounded-lg text-xs font-black uppercase tracking-wider transition-all ${
                  theme === "light"
                    ? "bg-white text-black shadow-sm"
                    : "text-white/40 hover:text-white"
                }`}
              >
                <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round">
                  <circle cx="12" cy="12" r="5"></circle>
                  <line x1="12" y1="1" x2="12" y2="3"></line>
                  <line x1="12" y1="21" x2="12" y2="23"></line>
                  <line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line>
                  <line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line>
                  <line x1="1" y1="12" x2="3" y2="12"></line>
                  <line x1="21" y1="12" x2="23" y2="12"></line>
                  <line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line>
                  <line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line>
                </svg>
                <span>Clair</span>
              </button>
            </div>
          </div>

          <div className="flex items-center gap-3">
            <button
              type="button"
              onClick={() => {
                onClose();
                onNavigate("about");
              }}
              className="flex-1 py-2.5 px-3 rounded-xl bg-white/[0.05] hover:bg-white/[0.12] border border-white/10 text-[11px] font-black tracking-widest uppercase text-white transition-all text-center"
              style={{ fontFamily: '"Arial Black", "Impact", sans-serif' }}
            >
              À propos &rarr;
            </button>
            <button
              type="button"
              onClick={() => {
                onClose();
                onNavigate("contact");
              }}
              className="flex-1 py-2.5 px-3 rounded-xl bg-white/[0.05] hover:bg-white/[0.12] border border-white/10 text-[11px] font-black tracking-widest uppercase text-white transition-all text-center"
              style={{ fontFamily: '"Arial Black", "Impact", sans-serif' }}
            >
              Contact &rarr;
            </button>
          </div>
          <span className="text-[10px] tracking-[0.16em] text-white/35 uppercase text-center mt-0.5">
            MORGAN JANOT &mdash; PARIS &copy; 2026
          </span>
        </div>
      </aside>
    </>
  );
}
