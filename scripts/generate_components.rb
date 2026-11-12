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
    <div className={`relative flex items-center justify-center w-full h-full p-8 sm:p-12 md:p-16 ${className}`}>
      <svg
        viewBox={item.viewBox}
        className="w-full h-full max-h-[80%] max-w-[85%] object-contain pointer-events-none drop-shadow-sm select-none"
        xmlns="http://www.w3.org/2000/svg"
        fill="none"
        stroke={strokeColor}
        strokeWidth="4"
        strokeLinecap="round"
        strokeLinejoin="round"
      >
        <path d={item.d} />
      </svg>
    </div>
  );
}

/**
 * Precision Vector Graphic Arrow
 */
export function TileArrow({ strokeColor, className = "" }) {
  return (
    <svg
      viewBox="0 0 160 50"
      className={`pointer-events-none select-none ${className}`}
      fill="none"
      stroke={strokeColor}
      strokeWidth="4.5"
      strokeLinecap="round"
      strokeLinejoin="round"
      xmlns="http://www.w3.org/2000/svg"
    >
      <line x1="8" y1="25" x2="148" y2="25" />
      <polyline points="122,10 150,25 122,40" />
    </svg>
  );
}
JSX

File.write("/Users/morganjanot/.gemini/antigravity/scratch/mj-portfolio/src/components/Illustrations.jsx", jsx_content)
puts "Wrote Illustrations.jsx successfully (#{jsx_content.length} chars)"
