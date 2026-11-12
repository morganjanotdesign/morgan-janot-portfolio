import React, { useRef, useState, useEffect } from "react";

/**
 * Vertical Side Navigation (Grand format le long du bord droit)
 * 
 * - Occupies the entire right edge height (h-[86vh])
 * - Displays "PORTFOLIO", "ABOUT", "CONTACT" in massive Arial Black vertical typography
 * - Smooth physical sliding animation of the black indicator bar
 * - Inactive items are shrunk (scale-68) and smoothly grow to base full size on hover
 * - Drives displacement / navigation between Portfolio (grid), About (white page), and Contact (white page)
 */
export default function SideNav({ activeItem = "portfolio", onNavigate }) {
  const railRef = useRef(null);
  const btnRefs = {
    portfolio: useRef(null),
    about: useRef(null),
    contact: useRef(null),
  };

  const [barStyle, setBarStyle] = useState({
    top: 0,
    height: 0,
    opacity: 0,
  });

  const updateBar = () => {
    const activeBtn = btnRefs[activeItem]?.current;
    if (activeBtn) {
      const topOffset = activeBtn.offsetTop;
      const height = activeBtn.offsetHeight;
      setBarStyle({
        top: topOffset,
        height: height,
        opacity: 1,
      });
    }
  };

  useEffect(() => {
    updateBar();
    window.addEventListener("resize", updateBar);
    const t = setTimeout(updateBar, 40);
    return () => {
      window.removeEventListener("resize", updateBar);
      clearTimeout(t);
    };
  }, [activeItem]);

  const items = [
    { id: "portfolio", label: "PORTFOLIO" },
    { id: "about", label: "ABOUT" },
    { id: "contact", label: "CONTACT" },
  ];

  return (
    <nav
      aria-label="Navigation latérale"
      className="fixed right-0 top-[5vh] h-[90vh] z-50 pointer-events-auto select-none flex flex-col items-end"
      style={{ width: "clamp(80px, 7vw, 120px)" }}
    >
      <div
        ref={railRef}
        className="relative w-full h-full flex flex-col justify-between items-end pr-0"
      >
        {/* Animated Sliding Black Bar (se déplace physiquement entre les options) */}
        <div
          className="absolute right-0 top-0 bg-black pointer-events-none"
          style={{
            width: "clamp(10px, 0.9vw, 14px)",
            transform: `translateY(${barStyle.top}px)`,
            height: `${barStyle.height}px`,
            opacity: barStyle.opacity,
            transition: "transform 450ms cubic-bezier(0.16, 1, 0.3, 1), height 450ms cubic-bezier(0.16, 1, 0.3, 1), opacity 300ms ease",
          }}
          aria-hidden="true"
        />

        {/* Vertical Nav Buttons in EN GROS */}
        {items.map((item) => {
          const isActive = activeItem === item.id;
          return (
            <button
              key={item.id}
              ref={btnRefs[item.id]}
              type="button"
              onClick={() => onNavigate && onNavigate(item.id)}
              aria-current={isActive ? "page" : undefined}
              className="group relative flex items-center justify-end cursor-pointer outline-none p-0 pr-4 sm:pr-5 md:pr-6"
            >
              <span
                className={`
                  block origin-right
                  transition-all duration-380 ease-[cubic-bezier(0.16,1,0.3,1)]
                  ${isActive
                    ? "scale-100 opacity-100 text-black"
                    : "scale-[0.68] opacity-35 text-black group-hover:scale-100 group-hover:opacity-100"
                  }
                `}
                style={{
                  writingMode: "vertical-rl",
                  textOrientation: "mixed",
                  fontFamily: '"Arial Black", "Impact", -apple-system, BlinkMacSystemFont, sans-serif',
                  fontSize: "clamp(30px, 3.8vw, 50px)",
                  fontWeight: 900,
                  letterSpacing: "0.18em",
                  textTransform: "uppercase",
                  lineHeight: 1,
                }}
              >
                {item.label}
              </span>
            </button>
          );
        })}
      </div>
    </nav>
  );
}
