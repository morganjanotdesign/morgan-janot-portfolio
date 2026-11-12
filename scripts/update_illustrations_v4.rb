# encoding: UTF-8
require "json"

vecs = JSON.parse(File.read("/Users/morganjanot/.gemini/antigravity/scratch/normalized_vectors.json"))

jsx_content = <<~JSX
/**
 * Vector illustrations extracted directly from the original Adobe Illustrator PDF.
 * Pure mathematical Bézier curves for infinite resolution (zero pixelation).
 */
import React from "react";

export const VECTORS = #{JSON.pretty_generate(vecs)};

/**
 * Editorial Serif Logo "MJ" from the Illustrator master file
 */
export function MjLogo({ className = "w-28 sm:w-32 md:w-36 h-auto" }) {
  const data = VECTORS.mj_black;
  return (
    <svg
      viewBox={data.viewBox}
      className={`select-none ${className}`}
      fill="currentColor"
      xmlns="http://www.w3.org/2000/svg"
      aria-label="MJ Logo"
    >
      <path d={data.d} />
    </svg>
  );
}

/**
 * Raw Illustrator Vector Drawing for each Tile
 * Enlarged and anchored to the left of the tile
 */
export function TileIllustration({ tileId, strokeColor, className = "" }) {
  const keyMap = {
    1: "tile1_orange",
    2: "tile2_purple",
    3: "tile3_green",
    4: "tile4_brown",
    5: "tile5_blue"
  };

  const key = keyMap[tileId];
  if (!key || !VECTORS[key]) return null;
  const item = VECTORS[key];

  return (
    <div className={`absolute inset-0 w-full h-full flex items-center justify-start p-4 sm:p-6 md:p-8 pl-6 sm:pl-10 md:pl-14 ${className}`}>
      <svg
        viewBox={item.viewBox}
        className="w-auto h-[88%] sm:h-[90%] md:h-[93%] max-w-[88%] object-contain pointer-events-none drop-shadow-sm select-none"
        xmlns="http://www.w3.org/2000/svg"
        fill="none"
        stroke={strokeColor}
        strokeWidth="4.5"
        strokeLinecap="round"
        strokeLinejoin="round"
      >
        <path d={item.d} />
      </svg>
    </div>
  );
}

/**
 * Downward Vertical Arrow extracted directly from Illustrator master model (media_1790631437401.pdf)
 * Features vertical shaft pointing down and bold orthogonal chevron.
 */
export function TileArrow({ className = "w-10 sm:w-12 md:w-14 lg:w-16 h-auto" }) {
  return (
    <svg
      viewBox="0 0 104 204"
      className={`pointer-events-none select-none text-black ${className}`}
      fill="none"
      stroke="currentColor"
      strokeWidth="18"
      strokeLinecap="butt"
      strokeLinejoin="miter"
      xmlns="http://www.w3.org/2000/svg"
      aria-hidden="true"
    >
      <line x1="52" y1="6" x2="52" y2="186" />
      <polyline points="94,140 52,186 10,140" />
    </svg>
  );
}
JSX

File.write("/Users/morganjanot/.gemini/antigravity/scratch/mj-portfolio/src/components/Illustrations.jsx", jsx_content)
puts "Updated Illustrations.jsx with downward vector arrow!"
