import React, { useState } from "react";
import LogoDef from "./LogoDef";

/**
 * Header Component
 * - Top-left: Logo STUDIO def (symbole) (persistent).
 * - Center: "* PORTFOLIO *" (sticky title that appears when scrolled down).
 * - Top-right: "//" minimal icon.
 */
const projectTitleMap = {
  "project-01": "FOG CHAIR",
  "project-02": "LAMPADAIRE ARTICULÉ",
  "project-03": "CANAPÉ GALET",
  "project-04": "CHAISE SUSPENDUE",
  "project-05": "DAA-DAA",
  "project-06": "LEO-11"
};

export default function Header({ currentView, isScrolled, onNavigate, isDrawerOpen, onToggleDrawer, theme = "dark", onToggleTheme }) {
  const [isDropdownOpen, setIsDropdownOpen] = useState(false);
  const isProjectView = currentView.startsWith("project-");
  const cycle = ["portfolio", "about", "contact"];
  const currentIdx = cycle.indexOf(currentView) >= 0 ? cycle.indexOf(currentView) : 0;
  const prevSection = cycle[(currentIdx - 1 + cycle.length) % cycle.length];
  const nextSection = cycle[(currentIdx + 1) % cycle.length];

  return (
    <header
      className={`
        fixed top-0 left-0 w-full h-[70px] z-50 pointer-events-none
        flex items-center justify-between px-6 sm:px-10 md:px-12
        transition-all duration-300
        ${isProjectView
          ? "bg-black/85 backdrop-blur-md"
          : isScrolled
            ? currentView === "portfolio"
              ? "bg-black/80 backdrop-blur-md"
              : "bg-white/90 backdrop-blur-md"
            : "bg-transparent"
        }
      `}
    >
      {/* Top Left: Logo STUDIO (symbole logodef) */}
      <button
        type="button"
        onClick={() => onNavigate("portfolio")}
        aria-label="Retour au Portfolio"
        className={`
          pointer-events-auto cursor-pointer outline-none select-none
          inline-flex items-center justify-center
          transition-opacity duration-300 hover:opacity-60
          ${currentView === "portfolio" || isProjectView ? "text-white" : "text-black"}
        `}
      >
        <LogoDef className="h-9 sm:h-12 w-auto max-w-[90px]" />
      </button>

      {/* Center: On project page, only the small project name between asterisks (no roulette) with click returning to portfolio.
          On other pages, sticky title and floating roulette dropdown when scrolled. */}
      <div
        className="sticky-center-wrapper pointer-events-auto relative flex flex-col items-center"
        onMouseEnter={() => !isProjectView && setIsDropdownOpen(true)}
        onMouseLeave={() => !isProjectView && setIsDropdownOpen(false)}
      >
        {isProjectView ? (
          <button
            type="button"
            onClick={() => {
              onNavigate("portfolio");
              window.scrollTo({ top: 0, behavior: "smooth" });
            }}
            aria-label="Retour au portfolio"
            className="cursor-pointer select-none font-black uppercase tracking-[0.16em] text-xs sm:text-sm md:text-base text-white opacity-100 translate-y-0 transition-all duration-200 hover:opacity-70 hover:scale-[1.03]"
            style={{ fontFamily: '"Arial Black", "Impact", sans-serif' }}
          >
            * {projectTitleMap[currentView] || "PORTFOLIO"} *
          </button>
        ) : (
          <>
            <div
              onClick={() => {
                if (currentView === "portfolio") {
                  window.scrollTo({ top: 0, behavior: "smooth" });
                } else {
                  onNavigate("portfolio");
                  window.scrollTo({ top: 0, behavior: "smooth" });
                }
              }}
              role="button"
              tabIndex={0}
              aria-label="Section actuelle"
              className={`
                cursor-pointer select-none
                font-black uppercase tracking-[0.1em] text-lg sm:text-xl
                transition-all duration-380 ease-[cubic-bezier(0.16,1,0.3,1)]
                ${currentView === "portfolio" ? "text-white" : "text-black"}
                ${isScrolled
                  ? "opacity-100 translate-y-0"
                  : "opacity-0 -translate-y-2 pointer-events-none"
                }
              `}
              style={{ fontFamily: '"Arial Black", "Impact", sans-serif' }}
            >
              * {currentView.toUpperCase()} *
            </div>

            {/* Floating Roulette Dropdown */}
            {isScrolled && isDropdownOpen && (
              <div
                className="absolute top-[calc(100%+8px)] left-1/2 -translate-x-1/2 z-50 bg-[#0c0c0cf5] backdrop-blur-2xl rounded-2xl px-6 py-3 shadow-[0_16px_40px_rgba(0,0,0,0.85)] flex flex-col items-center gap-1 min-w-[200px] border-none outline-none"
                style={{ fontFamily: '"Arial Black", "Impact", sans-serif' }}
              >
                <button
                  type="button"
                  onClick={() => onNavigate(prevSection)}
                  className="text-xs tracking-[0.16em] uppercase text-white/50 hover:text-white py-1 transition-colors"
                >
                  {prevSection}
                </button>
                <div className="text-xl tracking-[0.14em] uppercase text-white font-black py-0.5">
                  * {currentView} *
                </div>
                <button
                  type="button"
                  onClick={() => onNavigate(nextSection)}
                  className="text-xs tracking-[0.16em] uppercase text-white/50 hover:text-white py-1 transition-colors"
                >
                  {nextSection}
                </button>
              </div>
            )}
          </>
        )}
      </div>

      {/* Top Right: Theme Toggle & // Menu Icon */}
      <div className="flex items-center gap-2 pointer-events-auto">
        <button
          type="button"
          onClick={onToggleTheme}
          aria-label={theme === "light" ? "Passer en mode sombre" : "Passer en mode clair"}
          title={theme === "light" ? "Mode sombre" : "Mode clair"}
          className={`w-10 h-10 rounded-full flex items-center justify-center cursor-pointer transition-all duration-300 ${
            theme === "light"
              ? "bg-black/5 hover:bg-black/10 text-[#0d0d11] border border-black/10"
              : "bg-white/10 hover:bg-white/20 text-white border border-white/15"
          }`}
        >
          {theme === "light" ? (
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.2" strokeLinecap="round" strokeLinejoin="round">
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
          ) : (
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.2" strokeLinecap="round" strokeLinejoin="round">
              <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path>
            </svg>
          )}
        </button>

        <div
          onClick={onToggleDrawer}
          role="button"
          tabIndex={0}
          aria-label={isDrawerOpen ? "Fermer la liste des projets" : "Ouvrir la liste des projets"}
          aria-expanded={isDrawerOpen}
          className={`relative w-11 h-11 rounded-full flex items-center justify-center cursor-pointer transition-all duration-300 ${
            isDrawerOpen
              ? "bg-white/15 hover:bg-white/25 border border-white/20"
              : "hover:bg-white/10"
          }`}
        >
          <div
            className={`relative w-6 h-6 flex items-center justify-center transition-transform duration-500 ease-[cubic-bezier(0.16,1,0.3,1)] ${
              isDrawerOpen ? "rotate-180" : "rotate-0"
            }`}
          >
            <span
              className={`absolute w-[2.5px] h-[18px] rounded-[2px] transition-all duration-500 ease-[cubic-bezier(0.16,1,0.3,1)] ${
                isDrawerOpen
                  ? "translate-x-0 rotate-45 !bg-white"
                  : "-translate-x-[4px] -skew-x-[24deg] " + (currentView === "portfolio" || isProjectView ? "bg-white" : "bg-black")
              }`}
            />
            <span
              className={`absolute w-[2.5px] h-[18px] rounded-[2px] transition-all duration-500 ease-[cubic-bezier(0.16,1,0.3,1)] ${
                isDrawerOpen
                  ? "translate-x-0 -rotate-45 !bg-white"
                  : "translate-x-[4px] -skew-x-[24deg] " + (currentView === "portfolio" || isProjectView ? "bg-white" : "bg-black")
              }`}
            />
          </div>
        </div>
      </div>
    </header>
  );
}
