/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        tileOrange: "#e9722b",
        tilePurple: "#914792",
        tileGreen: "#68b42d",
        tileBrown: "#775732",
        tileBlue: "#46a0d1",
        tileRed: "#d83d46"
      }
    },
  },
  plugins: [],
}
