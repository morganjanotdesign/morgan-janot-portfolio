import React, { useState, useEffect, useRef } from "react";

/**
 * DrumHero / RouletteHero Component (Alternative Éditoriale)
 * - L'élément actif avec astérisques est TOUJOURS au milieu (* SECTION *)
 * - Ligne du haut : section précédente (ex: CONTACT quand on est sur PORTFOLIO)
 * - Ligne du milieu : section active (ex: * PORTFOLIO *)
 * - Ligne du bas : section suivante (ex: ABOUT quand on est sur PORTFOLIO)
 * - Clic direct sur le mot du haut ou du bas pour faire glisser au centre
 * - Molette sur le sélecteur, flèches clavier (↑ / ↓), touch swipe
 * - Flou immersif sur le reste de la page au survol des 3 mots
 * - Aucun élément fléché (pure typographie minimale)
 */
export default function RouletteHero({
  currentView,
  onNavigate,
  onHoverStateChange
}) {
  const cycle = ["portfolio", "about", "contact"];
  const [activeIdx, setActiveIdx] = useState(0);
  const [isRolling, setIsRolling] = useState(null); // 'up' | 'down' | null
  const [isCenterHovered, setIsCenterHovered] = useState(false);
  const lastWheelTime = useRef(0);
  const hoverTimer = useRef(null);

  useEffect(() => {
    const idx = cycle.indexOf(currentView);
    if (idx !== -1) {
      setActiveIdx(idx);
    }
  }, [currentView]);

  const prevIdx = (activeIdx - 1 + cycle.length) % cycle.length;
  const nextIdx = (activeIdx + 1) % cycle.length;
  const currentKey = cycle[activeIdx];
  const prevKey = cycle[prevIdx];
  const nextKey = cycle[nextIdx];

  const rollTo = (direction, newIdx) => {
    if (isRolling) return;
    setIsRolling(direction);

    setTimeout(() => {
      setActiveIdx(newIdx);
      onNavigate(cycle[newIdx]);

      setTimeout(() => {
        setIsRolling(null);
      }, 50);
    }, 380);
  };

  const handlePrev = () => {
    if (hoverTimer.current) clearTimeout(hoverTimer.current);
    rollTo("down", (activeIdx - 1 + cycle.length) % cycle.length);
  };

  const handleNext = () => {
    if (hoverTimer.current) clearTimeout(hoverTimer.current);
    rollTo("up", (activeIdx + 1) % cycle.length);
  };

  const handleHoverPrev = () => {
    if (hoverTimer.current) clearTimeout(hoverTimer.current);
    hoverTimer.current = setTimeout(() => {
      handlePrev();
    }, 180);
  };

  const handleHoverNext = () => {
    if (hoverTimer.current) clearTimeout(hoverTimer.current);
    hoverTimer.current = setTimeout(() => {
      handleNext();
    }, 180);
  };

  const handleHoverLeave = () => {
    if (hoverTimer.current) clearTimeout(hoverTimer.current);
  };

  // Navigation au clavier (flèches haut / bas)
  useEffect(() => {
    const handleKeyDown = (e) => {
      if (e.target && (e.target.tagName === "INPUT" || e.target.tagName === "TEXTAREA")) return;
      if (e.key === "ArrowDown" || e.key === "ArrowRight") {
        handleNext();
      } else if (e.key === "ArrowUp" || e.key === "ArrowLeft") {
        handlePrev();
      }
    };
    window.addEventListener("keydown", handleKeyDown);
    return () => window.removeEventListener("keydown", handleKeyDown);
  }, [activeIdx, isRolling]);

  // Défilement molette ciblé sur le sélecteur
  const handleWheel = (e) => {
    const now = Date.now();
    if (now - lastWheelTime.current < 400) return;
    if (Math.abs(e.deltaY) > 15) {
      lastWheelTime.current = now;
      if (e.deltaY > 0) {
        handleNext();
      } else {
        handlePrev();
      }
    }
  };

  return (
    <section id="hero-banner" className="hero-banner w-full min-h-[30vh] sm:min-h-[34vh] flex flex-col items-center justify-center pt-24 pb-8 sm:pt-32 sm:pb-10 text-center relative select-none z-50">
      <div
        onWheel={handleWheel}
        onMouseEnter={() => onHoverStateChange && onHoverStateChange(true)}
        onMouseLeave={() => {
          handleHoverLeave();
          if (onHoverStateChange) onHoverStateChange(false);
        }}
        className={`group relative inline-flex flex-col items-center justify-center px-8 py-2 cursor-default transform transition-transform duration-420 ease-[cubic-bezier(0.16,1,0.3,1)] ${
          isCenterHovered ? "scale-[1.02]" : "scale-[0.82]"
        }`}
        aria-label="Menu principal de navigation"
      >
        {/* LIGNE HAUT : PRÉCÉDENT */}
        <button
          type="button"
          onClick={handlePrev}
          onMouseEnter={handleHoverPrev}
          onMouseLeave={handleHoverLeave}
          aria-label={`Passer à ${prevKey.toUpperCase()}`}
          className={`flex items-center justify-center text-white/28 hover:text-white uppercase font-black tracking-[0.1em] text-[clamp(20px,3.2vw,38px)] px-6 py-2 transition-all duration-320 ease-[cubic-bezier(0.16,1,0.3,1)] outline-none hover:scale-104 cursor-pointer [perspective:600px] [transform:rotateX(12deg)] ${
            isRolling === "down" ? "translate-y-[38px] !opacity-100 !text-white" : ""
          } ${isRolling === "up" ? "-translate-y-[24px] opacity-0" : ""}`}
          style={{ fontFamily: '"Arial Black", "Impact", sans-serif' }}
        >
          {prevKey.toUpperCase()}
        </button>

        {/* LIGNE MILIEU : TOUJOURS L'ÉLÉMENT SÉLECTIONNÉ AVEC ASTÉRISQUES (ZONE D'ACTIVATION DU ZOOM) */}
        <div
          onMouseEnter={() => setIsCenterHovered(true)}
          onMouseLeave={() => setIsCenterHovered(false)}
          className={`flex items-center justify-center gap-4 sm:gap-6 text-white uppercase font-black tracking-[0.08em] text-[clamp(38px,6vw,76px)] leading-none my-1 transition-all duration-320 ease-[cubic-bezier(0.16,1,0.3,1)] cursor-default drop-shadow-[0_0_28px_rgba(255,255,255,0.35)] ${
            isRolling === "up" ? "-translate-y-[26px] opacity-30" : ""
          } ${isRolling === "down" ? "translate-y-[26px] opacity-30" : ""}`}
          style={{ fontFamily: '"Arial Black", "Impact", sans-serif' }}
        >
          <span className="text-[clamp(36px,5.8vw,72px)] select-none text-white">*</span>
          <span>{currentKey.toUpperCase()}</span>
          <span className="text-[clamp(36px,5.8vw,72px)] select-none text-white">*</span>
        </div>

        {/* LIGNE BAS : SUIVANT */}
        <button
          type="button"
          onClick={handleNext}
          onMouseEnter={handleHoverNext}
          onMouseLeave={handleHoverLeave}
          aria-label={`Passer à ${nextKey.toUpperCase()}`}
          className={`flex items-center justify-center text-white/28 hover:text-white uppercase font-black tracking-[0.1em] text-[clamp(20px,3.2vw,38px)] px-6 py-2 transition-all duration-320 ease-[cubic-bezier(0.16,1,0.3,1)] outline-none hover:scale-104 cursor-pointer [perspective:600px] [transform:rotateX(-12deg)] ${
            isRolling === "up" ? "-translate-y-[38px] !opacity-100 !text-white" : ""
          } ${isRolling === "down" ? "translate-y-[24px] opacity-0" : ""}`}
          style={{ fontFamily: '"Arial Black", "Impact", sans-serif' }}
        >
          {nextKey.toUpperCase()}
        </button>
      </div>
    </section>
  );
}
