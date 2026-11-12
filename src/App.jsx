import React, { useState, useEffect } from "react";
import Header from "./components/Header";
import RouletteHero from "./components/RouletteHero";
import PortfolioGrid from "./components/PortfolioGrid";
import AboutView from "./components/AboutView";
import ContactView from "./components/ContactView";
import ProjectDetailView from "./components/ProjectDetailView";
import ProjectsDrawer from "./components/ProjectsDrawer";

/**
 * Landing Page Root Component
 * - Top bar with MORGAN JANOT, sticky title and // menu mark
 * - Side drawer listing all 6 projects when clicking //
 * - Universal 3D Roulette Hero across all pages
 * - Dedicated project detail pages with 6 distinct editorial layouts
 * - Minimalist About and Contact pages
 */
export default function App() {
  const [currentView, setCurrentView] = useState("portfolio");
  const [isScrolled, setIsScrolled] = useState(false);
  const [isBlurred, setIsBlurred] = useState(false);
  const [isDrawerOpen, setIsDrawerOpen] = useState(false);
  const [theme, setTheme] = useState(() => {
    try {
      return localStorage.getItem("mj_theme") || "dark";
    } catch (e) {
      return "dark";
    }
  });

  useEffect(() => {
    if (theme === "light") {
      document.body.classList.add("light-mode");
      document.documentElement.classList.add("light-mode");
    } else {
      document.body.classList.remove("light-mode");
      document.documentElement.classList.remove("light-mode");
    }
    try {
      localStorage.setItem("mj_theme", theme);
    } catch (e) {}
  }, [theme]);

  const toggleTheme = () => {
    setTheme((prev) => (prev === "light" ? "dark" : "light"));
  };

  // Sync with browser hash
  useEffect(() => {
    const handleHash = () => {
      const hash = window.location.hash.replace("#", "").toLowerCase();
      if (hash === "about" || hash === "contact" || hash === "portfolio") {
        setCurrentView(hash);
      } else if (hash.startsWith("project-")) {
        setCurrentView(hash);
      }
    };
    handleHash();
    window.addEventListener("hashchange", handleHash);
    return () => window.removeEventListener("hashchange", handleHash);
  }, []);

  // Track scroll position to slide the category title to top bar
  // Attend que la roulette principale disparaisse complètement de l'écran avant de faire apparaître portfolio en haut
  useEffect(() => {
    const handleScroll = () => {
      const hero = document.getElementById("hero-banner");
      if (hero) {
        const rect = hero.getBoundingClientRect();
        setIsScrolled(rect.bottom <= 70);
      } else {
        const scrollY = window.scrollY || window.pageYOffset;
        setIsScrolled(scrollY > 280);
      }
    };
    window.addEventListener("scroll", handleScroll, { passive: true });
    handleScroll();
    return () => window.removeEventListener("scroll", handleScroll);
  }, []);

  const handleNavigate = (view) => {
    setCurrentView(view);
    window.location.hash = view;
    window.scrollTo({ top: 0, behavior: "smooth" });
  };

  const handleSelectProject = (projectId) => {
    setIsDrawerOpen(false);
    setCurrentView(projectId);
    window.location.hash = projectId;
    window.scrollTo({ top: 0, behavior: "smooth" });
  };

  const isProjectView = currentView.startsWith("project-");

  return (
    <div className={`relative w-full min-h-screen ${theme === "light" ? "bg-[#f7f7f9] text-[#0d0d11]" : "bg-black text-white"} overflow-x-hidden select-none`}>
      {/* Sticky Top Bar: MORGAN JANOT on left, sticky title in center, // on right */}
      <Header
        currentView={currentView}
        isScrolled={isScrolled}
        onNavigate={handleNavigate}
        isDrawerOpen={isDrawerOpen}
        onToggleDrawer={() => setIsDrawerOpen((prev) => !prev)}
        theme={theme}
        onToggleTheme={toggleTheme}
      />

      {/* Projects Off-Canvas Drawer (List of all 6 projects) */}
      <ProjectsDrawer
        isOpen={isDrawerOpen}
        onClose={() => setIsDrawerOpen(false)}
        onSelectProject={handleSelectProject}
        onNavigate={handleNavigate}
        theme={theme}
        onSetTheme={setTheme}
      />

      {/* Universal Hero Section with Infinite 3D Roulette (Hidden or compact when in project view) */}
      {!isProjectView && (
        <RouletteHero
          currentView={currentView}
          onNavigate={handleNavigate}
          onHoverStateChange={setIsBlurred}
        />
      )}

      {/* Page Content (Blurs softly while interacting with roulette, unblurs and reveals on exit) */}
      <div
        className={`w-full transition-all duration-400 ease-[cubic-bezier(0.16,1,0.3,1)] ${
          isBlurred ? "filter blur-[14px] brightness-75 pointer-events-none scale-[0.995]" : "filter blur-0 brightness-100 scale-100"
        } ${isProjectView ? "pt-24" : ""}`}
      >
        {currentView === "portfolio" && <PortfolioGrid onSelectProject={handleSelectProject} />}
        {currentView === "about" && <AboutView onNavigate={handleNavigate} />}
        {currentView === "contact" && <ContactView onNavigate={handleNavigate} />}
        {isProjectView && (
          <ProjectDetailView
            projectId={currentView}
            onNavigate={handleNavigate}
            onSelectProject={handleSelectProject}
          />
        )}
      </div>

      {/* Persistent Bottom-Right Margin Hallmark Stamp: LYON 2026® */}
      <aside
        aria-hidden="true"
        className="fixed bottom-8 sm:bottom-12 right-4 sm:right-7 z-40 pointer-events-none select-none text-[11px] sm:text-xs uppercase tracking-[0.22em] text-white/70 whitespace-nowrap"
        style={{
          fontFamily: '"Playfair Display", Didot, "Times New Roman", serif',
          transform: "rotate(90deg)",
          transformOrigin: "100% 100%",
        }}
      >
        <span>LYON 2026</span>
        <sup className="text-[0.6em] font-bold align-super ml-0.5 opacity-85">&reg;</sup>
      </aside>
    </div>
  );
}
