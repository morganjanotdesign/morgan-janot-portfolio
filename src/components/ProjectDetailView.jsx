import React, { useState } from "react";
import { FrameIllustration } from "./Illustrations";
import { projects } from "../data/projectsData";

import imgFloating from "../assets/images/project-01/15.webp";
import imgPortrait from "../assets/images/project-01/12.webp";
import imgStack from "../assets/images/project-01/13.webp";
import imgConception1 from "../assets/images/project-01/1.webp";
import imgConception2 from "../assets/images/project-01/2.webp";
import imgConception3 from "../assets/images/project-01/3.webp";
import imgConception4 from "../assets/images/project-01/4.webp";
import imgConception5 from "../assets/images/project-01/5.webp";

import imgConcreteBase from "../assets/images/project-02/Gemini_Generated_Image_hpc2n0hpc2n0hpc2.webp";
import imgUpperArticulation from "../assets/images/project-02/Gemini_Generated_Image_ntm565ntm565ntm5.webp";
import imgJointCloseup from "../assets/images/project-02/Gemini_Generated_Image_np88z9np88z9np88.webp";
import imgJointArm from "../assets/images/project-02/bla.webp";
import imgBallJoint from "../assets/images/project-02/usm-creative-since-1965-keyvisual-04-5mch2z.webp";

import imgSuspendedChairPerspective from "../assets/images/project-04/Gemini_Generated_Image_bbgjp7bbgjp7bbgj.webp";
import imgSuspendedChairJoint from "../assets/images/project-04/Gemini_Generated_Image_thwtruthwtruthwt.webp";
import imgP4_3D from "../assets/images/project-04/3D.webp";
import imgP4_Plan from "../assets/images/project-04/plan.webp";
import imgP4_Laser from "../assets/images/project-04/decoupelaser.webp";
import imgP4Conception1 from "../assets/images/project-04/IMG_7196.webp";
import imgP4Conception2 from "../assets/images/project-04/IMG_7205.webp";
import imgP4Conception3 from "../assets/images/project-04/IMG_7215.webp";
import imgP4Conception4 from "../assets/images/project-04/IMG_7229.webp";
import imgP4Conception5 from "../assets/images/project-04/IMG_7233.webp";

import imgSpeakerThreeQuarter from "../assets/images/project-05/enceinte1.webp";
import imgSpeakerFront from "../assets/images/project-05/enceinte2bis.webp";
import imgSpeakerBack from "../assets/images/project-05/enceinte3.webp";
import imgSpeakerMacro from "../assets/images/project-05/enceinte4.webp";
import imgSpeakerInsitu from "../assets/images/project-05/Untitled.webp";
import imgSpeakerHand from "../assets/images/project-05/main.webp";
import imgSpeakerWheels from "../assets/images/project-05/wheels_transparent.webp";

import imgLeoFloating from "../assets/images/project-06/f.webp";
import imgLeoInsitu from "../assets/images/project-06/fi.webp";

/**
 * ProcessSection Component
 * Large full-page PROCESS heading with scattered photography stage directly underneath.
 */
function ProcessSection({
  tag = "01 // PROCESSUS & RECHERCHES",
  tagDotColor = "rgba(255, 255, 255, 0.8)",
  id = undefined,
  description = "Recherches de formes, exploration des principes d’assemblage et maquettes d’atelier.",
  children,
}) {
  return (
    <section className="project-process-section" id={id}>
      <div className="process-header">
        <h2 className="process-giant-title">PROCESS</h2>
        {description && (
          <p className="process-lead-text">{description}</p>
        )}
      </div>

      <div className="process-content-wrapper w-full">
        {children}
      </div>
    </section>
  );
}

/**
 * WhiteImageBox Component
 * Clean modernist container for photography.
 * When an image is passed, displays pure full-bleed photo without any overlaid rectangles or corner ticks.
 * When empty, displays crosshairs and placeholder typography.
 */
function WhiteImageBox({
  title = "IMAGE 01",
  subtitle = "",
  tag = "EMPLACEMENT PHOTO",
  aspectRatio = "16/10",
  imageSrc = null,
  imageAlt = "",
  className = "",
  style = {},
  imageStyle = {},
  objectFit = "cover",
  children,
}) {
  const isImage = Boolean(imageSrc);
  return (
    <div
      className={`relative ${isImage ? "!bg-transparent !shadow-none hover:!shadow-none !border-none p-0" : "bg-white text-black shadow-2xl p-6 sm:p-8 hover:-translate-y-1 hover:shadow-[0_24px_50px_rgba(0,0,0,0.6)]"} overflow-hidden flex flex-col items-center justify-center transition-all duration-300 cursor-pointer select-none group ${className}`}
      style={{ aspectRatio, ...style }}
    >
      {/* If an image is present, display it purely without any overlaid rectangles or corner ticks */}
      {imageSrc ? (
        <img
          src={imageSrc}
          alt={imageAlt || title}
          className={`absolute inset-0 w-full h-full ${objectFit === "contain" ? "object-contain" : "object-cover"} z-10 transition-transform duration-700 ease-out group-hover:scale-[1.03]`}
          style={imageStyle}
          loading="lazy"
        />
      ) : children ? (
        children
      ) : (
        <>
          {/* Corner crosshairs only for placeholders */}
          <span className="absolute top-3.5 left-3.5 w-3 h-3 z-20 pointer-events-none before:content-[''] before:absolute before:top-1.5 before:left-0 before:w-3 before:h-[1.5px] before:bg-black/35 after:content-[''] after:absolute after:left-1.5 after:top-0 after:w-[1.5px] after:h-3 after:bg-black/35" />
          <span className="absolute top-3.5 right-3.5 w-3 h-3 z-20 pointer-events-none before:content-[''] before:absolute before:top-1.5 before:left-0 before:w-3 before:h-[1.5px] before:bg-black/35 after:content-[''] after:absolute after:left-1.5 after:top-0 after:w-[1.5px] after:h-3 after:bg-black/35" />
          <span className="absolute bottom-3.5 left-3.5 w-3 h-3 z-20 pointer-events-none before:content-[''] before:absolute before:top-1.5 before:left-0 before:w-3 before:h-[1.5px] before:bg-black/35 after:content-[''] after:absolute after:left-1.5 after:top-0 after:w-[1.5px] after:h-3 after:bg-black/35" />
          <span className="absolute bottom-3.5 right-3.5 w-3 h-3 z-20 pointer-events-none before:content-[''] before:absolute before:top-1.5 before:left-0 before:w-3 before:h-[1.5px] before:bg-black/35 after:content-[''] after:absolute after:left-1.5 after:top-0 after:w-[1.5px] after:h-3 after:bg-black/35" />

          <div className="flex flex-col items-center justify-center text-center gap-2 pointer-events-none px-4">
            <div className="w-10 h-10 rounded-full border border-black/20 flex items-center justify-center text-black/70 mb-1 group-hover:scale-110 transition-transform">
              <svg
                width="20"
                height="20"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                strokeWidth="2"
                strokeLinecap="round"
                strokeLinejoin="round"
              >
                <rect x="3" y="3" width="18" height="18" rx="2" ry="2" />
                <circle cx="8.5" cy="8.5" r="1.5" />
                <polyline points="21 15 16 10 5 21" />
              </svg>
            </div>
            <span className="text-[10px] font-black uppercase tracking-[0.22em] text-neutral-400">
              {tag}
            </span>
            <h4 className="text-xl sm:text-2xl font-black tracking-tight text-black m-0">
              {title}
            </h4>
            {subtitle && (
              <span className="text-xs font-semibold text-neutral-500 tracking-wide">
                {subtitle}
              </span>
            )}
          </div>
        </>
      )}
    </div>
  );
}

/**
 * ProjectDetailView Component
 * Renders bespoke editorial monograph layouts for each of the 6 projects:
 * - Carte couleur & Texte explicatif (genèse, pourquoi, intention de départ) côte à côte
 * - Grande image qui fait tout l'écran (full-bleed 100vw, format cinéma 21/9 ou 16/9)
 * - Images plus petites et largement espacées (formats 16/10, 1/1, 4/5, 4/3)
 */
export default function ProjectDetailView({ projectId, onNavigate, onSelectProject }) {
  const currentIndex = projects.findIndex(
    (p) => `project-${p.number}` === projectId || p.number === projectId || p.id.toString() === projectId
  );
  const activeIndex = currentIndex !== -1 ? currentIndex : 0;
  const project = projects[activeIndex];

  const prevIndex = (activeIndex - 1 + projects.length) % projects.length;
  const nextIndex = (activeIndex + 1) % projects.length;
  const prevProject = projects[prevIndex];
  const nextProject = projects[nextIndex];

  // Helper for universal tactile paper grain texture overlay
  const PaperGrain = () => (
    <>
      <div
        aria-hidden="true"
        className="absolute inset-0 pointer-events-none z-[3] opacity-60 mix-blend-multiply"
        style={{
          backgroundImage: `url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 250 250' width='250' height='250'%3E%3Cfilter id='paperFibers' x='0' y='0' width='100%25' height='100%25'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.62' numOctaves='4' result='noise' stitchTiles='stitch'/%3E%3CfeColorMatrix type='matrix' values='3.5 0 0 0 -1.2  0 3.5 0 0 -1.2  0 0 3.5 0 -1.2  0 0 0 1 0' in='noise' result='contrasted'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23paperFibers)'/%3E%3C/svg%3E")`,
          backgroundSize: "200px 200px",
        }}
      />
      <div
        aria-hidden="true"
        className="absolute inset-0 pointer-events-none z-[4] opacity-80 mix-blend-overlay"
        style={{
          backgroundImage: `radial-gradient(ellipse at 50% 40%, rgba(255, 255, 255, 0.15) 0%, rgba(0, 0, 0, 0.30) 100%), url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 250 250' width='250' height='250'%3E%3Cfilter id='paperGrainTooth' x='0' y='0' width='100%25' height='100%25'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.78' numOctaves='3' result='noise' stitchTiles='stitch'/%3E%3CfeColorMatrix type='matrix' values='2.5 0 0 0 -0.7  0 2.5 0 0 -0.7  0 0 2.5 0 -0.7  0 0 0 1 0' in='noise' result='contrasted'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23paperGrainTooth)'/%3E%3C/svg%3E")`,
          backgroundSize: "100% 100%, 160px 160px",
          boxShadow: "inset 0 0 80px rgba(0, 0, 0, 0.22)",
        }}
      />
    </>
  );

  return (
    <article className="w-full max-w-[1360px] mx-auto px-6 sm:px-12 md:px-16 pt-8 pb-32 box-border">
      {/* Top Navigation Bar */}
      <div className="flex items-center justify-between flex-wrap gap-4 pb-6 mb-12 border-b border-white/15">
        <button
          type="button"
          onClick={() => onNavigate("portfolio")}
          className="inline-flex items-center gap-2 text-xs font-black uppercase tracking-widest text-white hover:opacity-60 transition-opacity"
        >
          <span>&larr;</span>
          <span className="border-b-2 border-white pb-0.5">Retourner au portfolio</span>
        </button>

        <div className="text-[11px] font-black uppercase tracking-[0.22em] text-neutral-400 bg-white/5 border border-white/10 px-3.5 py-1.5 rounded-sm">
          PROJET [ {project.number} / 06 ]
        </div>

        <div className="flex items-center gap-5">
          <button
            type="button"
            onClick={() => onSelectProject(`project-${prevProject.number}`)}
            className="inline-flex items-center gap-1.5 text-xs font-black uppercase tracking-wider text-white hover:opacity-60 transition-opacity"
          >
            <span>&larr;</span>
            <span>Précédent</span>
          </button>
          <button
            type="button"
            onClick={() => onSelectProject(`project-${nextProject.number}`)}
            className="inline-flex items-center gap-1.5 text-xs font-black uppercase tracking-wider text-white hover:opacity-60 transition-opacity"
          >
            <span>Suivant</span>
            <span>&rarr;</span>
          </button>
        </div>
      </div>

      {/* =========================================================================
          PROJET 01: FOG CHAIR — MODÈLE 001 (#ff5e00 - Orange Fluo / Tangerine)
         ========================================================================= */}
      {activeIndex === 0 && (
        <section>
          {/* 1. HERO DUAL ROW: CARTE COULEUR & TEXTE EXPLICATIF CÔTE À CÔTE */}
          <div className="grid grid-cols-1 lg:grid-cols-[1.15fr_1fr] gap-10 lg:gap-16 items-center mb-24 sm:mb-32">
            {/* Carte Couleur Signature */}
            <div className="relative w-full aspect-square bg-[#ff5e00] overflow-hidden shadow-2xl group">
              <FrameIllustration illustrationKey={project.illustrationKey} strokeColor={project.strokeColor} />
              <PaperGrain />
              <div className="absolute bottom-0 inset-x-0 p-6 sm:p-8 bg-white/16 backdrop-blur-md z-20 flex flex-col items-start">
                <span className="text-[11px] font-black uppercase tracking-widest text-black/85 mb-1">
                  01 — Fog Chair // C001 Paris
                </span>
                <h2 className="text-2xl sm:text-4xl font-black tracking-tight text-black leading-none mb-1.5">
                  * FOG CHAIR <span className="title-bullet">●</span> MODEL-001 *
                </h2>
                <div className="flex items-center gap-2 text-[10px] font-black uppercase tracking-widest text-black/70">
                  <span>CHAISE MODÈLE 001</span>
                  <span>*</span>
                  <span>TANGERINE ÉLECTRIQUE</span>
                </div>
              </div>
            </div>

            {/* Texte Explicatif : Base du projet & Pourquoi */}
            <div className="flex flex-col justify-center">

              <h1 className="text-4xl sm:text-6xl font-black tracking-tight leading-[0.98] mb-4 text-white">
                Fog Chair &bull; Modèle 001
              </h1>
              <p className="text-base sm:text-lg font-bold text-neutral-200 mb-6 leading-snug">
                Comment réintégrer le jeu dans notre quotidien grâce au mobilier modulable ?
              </p>

              <div className="space-y-3 text-sm text-neutral-300 leading-relaxed font-normal">
                <p style={{ textAlign: "justify", textJustify: "inter-word", hyphens: "auto" }}>
                  Ce projet répond à un brief : s’inspirer d’une culture pour concevoir un produit. J’ai choisi celle des jeux de construction, comme les Lego ou les Kapla, qui permettent de créer librement et d’inventer son propre univers. Mon enquête révèle que huit personnes interrogées sur dix ressentaient cette liberté en jouant. Pourtant, la majorité a arrêté autour de 13 ans et évoque aujourd’hui le manque de temps et de matériel comme principaux freins. Ce constat m’a amené à l’hypothèse suivante : réintroduire le jeu de construction à l’âge adulte pourrait permettre de retrouver un espace de créativité, d’expression et de liberté au quotidien.
                </p>
              </div>
            </div>
          </div>

          {/* 2. PHOTO 01 : PERSPECTIVE ISOMÉTRIQUE EN GRAND FORMAT GÉANT */}
          <div className="w-full my-20 sm:my-32 max-w-[1600px] mx-auto px-4 sm:px-6 flex items-center justify-center">
            <img
              src={imgFloating}
              alt="Fog Chair Modèle 001 - Vue perspective isométrique aérienne en suspension sans fond"
              className="p1-no-shadow-img w-full max-w-[1500px] h-auto max-h-[95vh] object-contain transition-transform duration-500 hover:scale-[1.035] cursor-pointer !filter-none !shadow-none"
              style={{ filter: "none", boxShadow: "none" }}
            />
          </div>

          {/* 3. PHOTO 02 : VUE TROIS-QUARTS EN GRAND AVEC TEXTE D'EXPÉRIENCE À CÔTÉ */}
          <div className="grid grid-cols-1 lg:grid-cols-[1fr_minmax(280px,360px)] gap-10 lg:gap-20 items-end my-20 sm:my-32 max-w-[1700px] mx-auto w-[95%] px-4 sm:px-6">
            <div className="w-full order-1 flex items-center justify-center">
              <img
                src={imgPortrait}
                alt="Fog Chair Modèle 001 - Vue trois-quarts en élévation sans fond"
                className="w-full max-w-[1300px] h-auto max-h-[92vh] object-contain transition-transform duration-500 hover:scale-[1.035] cursor-pointer"
                style={{ filter: "drop-shadow(0 32px 70px rgba(0,0,0,0.95))" }}
              />
            </div>
            <div className="flex flex-col justify-end self-end text-white order-2 max-w-[360px]">
              <div className="text-xs sm:text-sm font-light text-neutral-300 leading-relaxed">
                <p className="m-0 text-justify" style={{ textAlign: "justify", textJustify: "inter-word", hyphens: "auto" }}>
                  Le projet prend la forme d’une chaise modulable inspirée du principe des jeux de construction. Son assemblage simple invite l’utilisateur à participer à la création de son mobilier. Le geste de construire fait ainsi partie de l’expérience de l’objet : on assemble, on expérimente et on transforme.
                </p>
              </div>
            </div>
          </div>

          {/* 4. PHOTO 03 : TROIS CONFIGURATIONS EN FORMAT GÉANT AVEC TEXTE À CÔTÉ */}
          <div className="grid grid-cols-1 lg:grid-cols-[minmax(280px,360px)_1fr] gap-10 lg:gap-20 items-end my-20 sm:my-32 max-w-[1700px] mx-auto w-[95%] px-4 sm:px-6">
            <div className="flex flex-col justify-end self-end text-white order-2 lg:order-1 max-w-[360px]">
              <div className="text-xs sm:text-sm font-light text-neutral-300 leading-relaxed">
                <p className="m-0 text-justify" style={{ textAlign: "justify", textJustify: "inter-word", hyphens: "auto" }}>
                  Un même ensemble de pièces permet de composer trois configurations de chaise. Déclinable en plusieurs coloris, le projet offre différentes possibilités pour s’adapter aux intérieurs et aux préférences de chacun. La chaise devient un mobilier évolutif, avec lequel on retrouve le plaisir de jouer à l’âge adulte.
                </p>
              </div>
            </div>
            <div className="w-full order-1 lg:order-2 flex items-center justify-center">
              <img
                src={imgStack}
                alt="Fog Chair Modèle 001 - Trio de chaises en équilibre (Tangerine, Vert Acide, Magenta) sans fond"
                className="w-full max-w-[1300px] h-auto max-h-[92vh] object-contain transition-transform duration-500 hover:scale-[1.035] cursor-pointer"
                style={{ filter: "drop-shadow(0 32px 70px rgba(0,0,0,0.95))" }}
              />
            </div>
          </div>

          {/* 5. SECTION PROCESS : GRAND TITRE PLEINE PAGE & IMAGES DESSOUS */}
          <ProcessSection
            tag="01 // PROCESSUS & RECHERCHES D'ATELIER"
            tagDotColor="rgb(255, 94, 0)"
            id="process-section-p01"
            description="Recherches de formes, exploration des principes d’assemblage et maquettes d’atelier. Décomposition des étapes de prototypage physique."
          >
            {/* DUO 01 : PHOTOS 01 & 02 + ZONE DE TEXTE EXPLICATIF */}
            <div className="process-duo-row">
              <div className="process-duo-photos">
                <div className="process-photo-box">
                  <img
                    src={imgConception1}
                    alt="Conception Fog Chair - Exploration maquette 01"
                    loading="lazy"
                  />
                </div>
                <div className="process-photo-box">
                  <img
                    src={imgConception2}
                    alt="Conception Fog Chair - Exploration maquette 02"
                    loading="lazy"
                  />
                </div>
              </div>
              <div className="process-duo-text-col">
                <h3 className="process-step-title">Gabarits d'étude et cintrage des profilés</h3>
                <p className="process-step-desc">
                  Découpage initial des gabarits en mousse et confection des premiers modules tubulaires. Cette phase d'étude sur table permet d'éprouver le rayon de courbure des cylindres, l'inclinaison de l'assise et la prise en main des éléments avant assemblage mécanique définitif.
                </p>
              </div>
            </div>

            {/* DUO 02 : PHOTOS 03 & 04 + ZONE DE TEXTE EXPLICATIF (REVERSE) */}
            <div className="process-duo-row reverse">
              <div className="process-duo-photos">
                <div className="process-photo-box">
                  <img
                    src={imgConception3}
                    alt="Conception Fog Chair - Exploration maquette 03"
                    loading="lazy"
                  />
                </div>
                <div className="process-photo-box">
                  <img
                    src={imgConception4}
                    alt="Conception Fog Chair - Exploration maquette 04"
                    loading="lazy"
                  />
                </div>
              </div>
              <div className="process-duo-text-col">
                <h3 className="process-step-title">Entrelacement textile et liaisons articulées</h3>
                <p className="process-step-desc">
                  Mise sous tension des profilés rembourrés de laine et test de maintien de l'assise. L'expérimentation vérifie la stabilité des points de serrage métalliques sous contrainte de compression et assure une répartition homogène de la charge corporelle.
                </p>
              </div>
            </div>

            {/* DUO 03 : PHOTO 05 (PROTOTYPE FINAL D'ATELIER) + ZONE DE TEXTE DE SYNTHÈSE */}
            <div className="process-duo-row">
              <div className="process-duo-photos single-photo">
                <div className="process-photo-box tall">
                  <img
                    src={imgConception5}
                    alt="Conception Fog Chair - Exploration maquette 05"
                    loading="lazy"
                  />
                </div>
              </div>
              <div className="process-duo-text-col">
                <h3 className="process-step-title">Validation des proportions échelle 1</h3>
                <p className="process-step-desc">
                  Assemblage complet de la maquette physique finale avec son piètement arrière thermolaqué. Validation des jeux d'assemblage, de la texture tactile de la laine tangerine et de la silhouette architecturale sculpturale dans l'espace habitable.
                </p>
              </div>
            </div>
          </ProcessSection>
        </section>
      )}

      {/* =========================================================================
          PROJET 02: LAMPADAIRE ARTICULÉ (#b4b9c0 - Gris Minéral / Béton Brut)
         ========================================================================= */}
      {activeIndex === 1 && (
        <section>
          {/* 1. HERO DUAL ROW: TEXTE À GAUCHE, CARTE COULEUR À DROITE */}
          <div className="grid grid-cols-1 lg:grid-cols-[1fr_1.15fr] gap-10 lg:gap-16 items-center mb-24 sm:mb-32">
            {/* Texte Explicatif */}
            <div className="flex flex-col justify-center order-2 lg:order-1">

              <h1 className="text-4xl sm:text-6xl font-black tracking-tight leading-[0.98] mb-4 text-white">
                Lampadaire Articulé
              </h1>
              <p className="text-base sm:text-lg font-bold text-neutral-200 mb-6 leading-snug">
                Un système d'éclairage cinétique né du dialogue entre la masse brute du béton, la finesse des profilés chromés et la tension graphique d'un câble orange.
              </p>

              <div className="mb-6">
                <div className="space-y-3 text-sm text-neutral-300 leading-relaxed font-normal">
                  <p>
                    Pourquoi ce projet ? Ce lampadaire explore la liberté de mouvement dans l'espace habité. Plutôt qu'un luminaire figé, il est pensé comme une grue cinétique légère : un piétement ancré dans un bloc de béton brut, relié à des segments tubulaires télescopiques orientables grâce à des connecteurs géométriques usinés.
                  </p>
                  <p>
                    Le câble électrique orange vif n'est pas dissimulé : il traverse les articulations via des anneaux de guidage et devient un élément graphique majeur, traçant une onde colorée dans l'espace qui contraste avec l'épure métallique et la rugosité minérale du socle.
                  </p>
                </div>
              </div>
            </div>

            {/* Carte Couleur Totem */}
            <div className="relative w-full aspect-[9/16] min-h-[480px] bg-[#b4b9c0] overflow-hidden shadow-2xl group order-1 lg:order-2">
              <FrameIllustration illustrationKey={project.illustrationKey} strokeColor={project.strokeColor} />
              <PaperGrain />
              <div className="absolute bottom-0 inset-x-0 p-6 sm:p-8 bg-white/16 backdrop-blur-md z-20 flex flex-col items-start">
                <span className="text-[11px] font-black uppercase tracking-widest text-black/85 mb-1">
                  02 — Cinétique &amp; Lumière // Studio
                </span>
                <h2 className="text-2xl sm:text-4xl font-black tracking-tight text-black leading-none mb-1.5">
                  * LAMPADAIRE ARTICULÉ *
                </h2>
                <div className="flex items-center gap-2 text-[10px] font-black uppercase tracking-widest text-black/70">
                  <span>ROTULES GÉOMÉTRIQUES &amp; SOCLE BÉTON</span>
                  <span>*</span>
                  <span>GRIS MINÉRAL</span>
                </div>
              </div>
            </div>
          </div>

          {/* 2. GRANDE IMAGE PLEIN ÉCRAN : SOCLE BÉTON & ÉLÉVATION COMPLÈTE (16:9) */}
          <div className="w-[100vw] relative left-1/2 right-1/2 -ml-[50vw] -mr-[50vw] max-w-[100vw] px-4 sm:px-12 my-20 sm:my-32 box-border">
            <WhiteImageBox
              title="IMAGE 01 — GRANDE VUE PLEIN ÉCRAN"
              aspectRatio="16/9"
              style={{ maxHeight: "80vh" }}
              imageSrc={imgConcreteBase}
              imageAlt="Lampadaire articulé avec socle en béton brut et câble orange"
            />
          </div>

          {/* 3. PHOTO 02 (ROTULE SPHÉRIQUE USM) & TEXTE EXPLICATIF LÉGER EN BLANC À CÔTÉ */}
          <div className="grid grid-cols-1 lg:grid-cols-[1fr_1.15fr] gap-10 lg:gap-16 items-end my-20 sm:my-32 max-w-6xl mx-auto w-full px-4 sm:px-6">
            <div className="w-full">
              <WhiteImageBox
                title="IMAGE 02 — ARTICULATION & ROTULE USM"
                aspectRatio="786/1024"
                imageSrc={imgBallJoint}
                imageAlt="Détail macro rotule sphérique chromée usinée"
              />
            </div>
            <div className="flex flex-col justify-end self-end text-white">
              <div className="text-base sm:text-lg font-light text-white leading-relaxed space-y-3" style={{ textAlign: "justify", textJustify: "inter-word" }}>
                <p className="text-white font-light m-0 text-justify" style={{ textAlign: "justify", textJustify: "inter-word" }}>Rotule sphérique usinée au micron en laiton nickelé et acier chromé poli miroir.</p>
                <p className="text-white font-light m-0 text-justify" style={{ textAlign: "justify", textJustify: "inter-word" }}>Ses six taraudages multidirectionnels articulent les profilés tubulaires légers.</p>
                <p className="text-white font-light m-0 text-justify" style={{ textAlign: "justify", textJustify: "inter-word" }}>Une friction mécanique calibrée fige le faisceau lumineux sans jeu ni serrage visible.</p>
                <p className="text-white font-light m-0 text-justify" style={{ textAlign: "justify", textJustify: "inter-word" }}>L'emprunt au mobilier modulaire suisse appliqué à la cinétique d'éclairage.</p>
              </div>
            </div>
          </div>

          {/* 4. PHOTO 03 : EN DESSOUS DE LA PHOTO 02 (GRANDE VUE PLEIN ÉCRAN 16:9 - SANS FOND) */}
          <div className="w-[100vw] relative left-1/2 right-1/2 -ml-[50vw] -mr-[50vw] max-w-[100vw] px-4 sm:px-12 my-20 sm:my-32 box-border">
            <WhiteImageBox
              title="IMAGE 03 — BRAS ARTICULÉ & PASSAGE DE CÂBLE"
              aspectRatio="16/9"
              objectFit="contain"
              className="!bg-transparent !shadow-none !border-none !max-w-[1024px] !mx-auto"
              style={{ maxHeight: "576px", backgroundColor: "transparent" }}
              imageStyle={{ filter: "drop-shadow(0 20px 40px rgba(0,0,0,0.75))" }}
              imageSrc={imgUpperArticulation}
              imageAlt="Bras articulé télescopique et passage de câble orange"
            />
          </div>

          {/* 5. PHOTO 04 : DÉTAIL ROTULE FACETTÉE (DÉTOURÉE & AGRANDIE) */}
          <div className="max-w-4xl sm:max-w-5xl mx-auto my-16 sm:my-28 w-full flex justify-center">
            <WhiteImageBox
              title="IMAGE 04 — DÉTAIL ROTULE FACETTÉE"
              aspectRatio="1/1"
              objectFit="contain"
              className="!bg-transparent !shadow-none !border-none max-w-[780px] w-full"
              style={{ maxHeight: "75vh" }}
              imageSrc={imgJointCloseup}
              imageAlt="Gros plan sur la rotule à facettes et l'anneau passe-câble détouré"
            />
          </div>

          {/* 6. PHOTO 05 EN PLUS GRAND : BRAS ARTICULÉ & CÂBLE ORANGE PLEIN ÉCRAN (16/9) */}
          <div className="w-[100vw] relative left-1/2 right-1/2 -ml-[50vw] -mr-[50vw] max-w-[100vw] px-4 sm:px-12 my-20 sm:my-32 box-border">
            <WhiteImageBox
              title="IMAGE 05 — BRAS ARTICULÉ & CÂBLE ORANGE"
              aspectRatio="16/9"
              className="p2-last-photo-box !shadow-none !border-none !bg-transparent hover:!shadow-none"
              style={{ maxHeight: "85vh", boxShadow: "none", border: "none", background: "transparent" }}
              imageSrc={imgJointArm}
              imageAlt="Bras articulé avec câble orange - Vue d'ensemble technique"
              objectFit="contain"
            />
          </div>
        </section>
      )}

      {/* =========================================================================
          PROJET 03: CANAPÉ GALET (#008c46 - Vert Studio Profond)
         ========================================================================= */}
      {activeIndex === 2 && (
        <section>
          {/* 1. HERO DUAL ROW: TEXTE À GAUCHE, CARTE COULEUR À DROITE */}
          <div className="grid grid-cols-1 lg:grid-cols-[1fr_1.15fr] gap-10 lg:gap-16 items-center mb-24 sm:mb-32">
            <div className="flex flex-col justify-center order-2 lg:order-1">

              <h1 className="text-4xl sm:text-6xl font-black tracking-tight leading-[0.98] mb-4 text-white">
                Canapé Galet
              </h1>
              <p className="text-base sm:text-lg font-bold text-neutral-200 mb-6 leading-snug">
                Masse rocheuse adoucie par l'érosion géologique, accueillant un orbe sphérique mobile en cuir naturel ciré.
              </p>

              <div className="mb-6">
                <div className="space-y-3 text-sm text-neutral-300 leading-relaxed font-normal">
                  <p>
                    Pourquoi ce projet ? La volonté d'échapper à la monotonie rectiligne des canapés modulaires. Le dessin est né de l'observation des roches de granit érodées par l'océan Atlantique : une forme continue qui s'adapte intuitivement aux différentes postures d'assise (formelle, lecture ou méridienne).
                  </p>
                  <p>
                    L'orbe mobile en cuir ciré à chaud apporte une ponctuation sculpturale vivante : confectionné en taurillon pleine fleur, il devient au gré des envies un accoudoir ergonomique, un cale-dos amovible ou un objet de contemplation autonome.
                  </p>
                </div>
              </div>
            </div>

            <div className="relative w-full aspect-[16/10] bg-[#008c46] overflow-hidden shadow-2xl group order-1 lg:order-2">
              <FrameIllustration illustrationKey={project.illustrationKey} strokeColor={project.strokeColor} />
              <PaperGrain />
              <div className="absolute bottom-0 inset-x-0 p-6 sm:p-8 bg-white/16 backdrop-blur-md z-20 flex flex-col items-start">
                <span className="text-[11px] font-black uppercase tracking-widest text-black/85 mb-1">
                  03 — Recherche Formelle // Atelier Janot
                </span>
                <h2 className="text-2xl sm:text-4xl font-black tracking-tight text-black leading-none mb-1.5">
                  * CANAPÉ GALET *
                </h2>
                <div className="flex items-center gap-2 text-[10px] font-black uppercase tracking-widest text-black/70">
                  <span>VOLUME MONOBLOC</span>
                  <span>*</span>
                  <span>VERT PROFOND</span>
                </div>
              </div>
            </div>
          </div>

          {/* 2. GRANDE IMAGE PLEIN ÉCRAN */}
          <div className="w-[100vw] relative left-1/2 right-1/2 -ml-[50vw] -mr-[50vw] max-w-[100vw] px-4 sm:px-12 my-20 sm:my-32 box-border">
            <WhiteImageBox
              title="IMAGE 01 — GRANDE VUE PLEIN ÉCRAN"
              subtitle="Mégalithe sculptural dans une pièce de réception baignée de lumière • Plein écran 21/9"
              tag="PLEIN ÉCRAN // FORMAT CINÉMA 21:9"
              aspectRatio="21/9"
              style={{ minHeight: "420px", maxHeight: "720px" }}
            />
          </div>

          {/* 3. IMAGES PLUS PETITES ET ESPACÉES */}
          <div className="grid grid-cols-1 lg:grid-cols-[1.35fr_1fr] gap-10 lg:gap-16 items-center my-16 sm:my-28">
            <WhiteImageBox
              title="IMAGE 02"
              subtitle="Perspective trois-quarts et profilage d'assise • 16/10"
              tag="VUE D'ENSEMBLE TROIS-QUARTS"
              aspectRatio="16/10"
            />
            <WhiteImageBox
              title="IMAGE 03"
              subtitle="Gros plan matière : cuir patiné manuellement • 1/1"
              tag="PETITE VUE DÉTAIL MATIÈRE"
              aspectRatio="1/1"
            />
          </div>

          <div className="max-w-[580px] mx-auto my-16 sm:my-28 w-full">
            <WhiteImageBox
              title="IMAGE 04"
              subtitle="L'orbe sphérique mobile utilisé en accoudoir • 4/5"
              tag="PETIT FORMAT PORTRAIT USAGE"
              aspectRatio="4/5"
            />
          </div>
        </section>
      )}

      {/* =========================================================================
          PROJET 04: CHAISE SUSPENDUE (#e30613 - Rouge Suisse)
         ========================================================================= */}
      {activeIndex === 3 && (
        <section>
          {/* 1. HERO DUAL ROW: CARTE À GAUCHE, TEXTE À DROITE */}
          <div className="grid grid-cols-1 lg:grid-cols-[1.15fr_1fr] gap-10 lg:gap-16 items-center mb-24 sm:mb-32">
            <div className="relative w-full aspect-[4/3] bg-[#e30613] overflow-hidden shadow-2xl group">
              <FrameIllustration illustrationKey={project.illustrationKey} strokeColor={project.strokeColor} />
              <PaperGrain />
              <div className="absolute bottom-0 inset-x-0 p-6 sm:p-8 bg-white/16 backdrop-blur-md z-20 flex flex-col items-start">
                <span className="text-[11px] font-black uppercase tracking-widest text-black/85 mb-1">
                  04 — Structure Géométrique // Paris
                </span>
                <h2 className="text-2xl sm:text-4xl font-black tracking-tight text-black leading-none mb-1.5">
                  * CHAISE SUSPENDUE *
                </h2>
                <div className="flex items-center gap-2 text-[10px] font-black uppercase tracking-widest text-black/70">
                  <span>ANCRAGE MONOPHONIQUE</span>
                  <span>*</span>
                  <span>ROUGE SUISSE</span>
                </div>
              </div>
            </div>

            <div className="flex flex-col justify-center">

              <h1 className="text-4xl sm:text-6xl font-black tracking-tight leading-[0.98] mb-4 text-white">
                Chaise Suspendue
              </h1>
              <p className="text-base sm:text-lg font-bold text-neutral-200 mb-6 leading-snug">
                L'abolition des pieds traditionnels au profit d'un treillis autoportant ancré au plafond par des liens invisibles.
              </p>

              <div className="mb-6">
                <div className="space-y-3 text-sm text-neutral-300 leading-relaxed font-normal">
                  <p>
                    Pourquoi cette recherche ? Pour libérer complètement la surface au sol et éprouver le vide comme matériau structural. En suspendant l'assise au plafond par des filins en fibre Dyneema ultra-résistante, l'objet s'affranchit des contraintes d'appui et réagit aux oscillations du corps pour une sensation de lévitation intégrale.
                  </p>
                  <p>
                    L'arceau triangulé en titane microbillé distribue les tensions mécaniques de manière isotrope. La membrane textile thermoformée épouse la posture sans point dur, rappelant l'aéronautique et le gréement nautique de haute mer.
                  </p>
                </div>
              </div>
            </div>
          </div>

          {/* 2. GRANDE IMAGE PLEIN ÉCRAN : VUE PERSPECTIVE COMPLÈTE SUR NOIR (SANS FOND) */}
          <div className="w-[100vw] relative left-1/2 right-1/2 -ml-[50vw] -mr-[50vw] max-w-[100vw] px-4 sm:px-12 my-20 sm:my-32 box-border">
            <WhiteImageBox
              title="IMAGE 01 — VUE PERSPECTIVE PLEIN ÉCRAN"
              aspectRatio="16/9"
              imageSrc={imgSuspendedChairPerspective}
              imageAlt="Chaise géométrique minimale et assise en tension textile"
              objectFit="contain"
              className="!bg-transparent !shadow-none !border-none"
              style={{ minHeight: "420px", maxHeight: "85vh", backgroundColor: "transparent" }}
              imageStyle={{ filter: "drop-shadow(0 24px 48px rgba(0,0,0,0.8))" }}
            />
          </div>

          {/* 3. IMAGES PLUS PETITES ET ESPACÉES */}
          <div className="grid grid-cols-1 lg:grid-cols-[1fr_1.35fr] gap-10 lg:gap-16 items-center my-16 sm:my-28">
            <WhiteImageBox
              title="IMAGE 02"
              subtitle="Point d'attache zénithal & anneau d'accroche titane • 4/5"
              tag="PETIT FORMAT PORTRAIT D'ANCRAGE"
              aspectRatio="4/5"
            />
            <WhiteImageBox
              title="IMAGE 03 — DÉTAIL D'ASSEMBLAGE & VISSERIE"
              aspectRatio="16/9"
              imageSrc={imgSuspendedChairJoint}
              imageAlt="Détail vue éclatée de la traverse et des vis d'assemblage"
              objectFit="contain"
              className="!bg-transparent !shadow-none !border-none"
              style={{ minHeight: "360px", maxHeight: "75vh", backgroundColor: "transparent" }}
              imageStyle={{ filter: "drop-shadow(0 20px 40px rgba(0,0,0,0.75))" }}
            />
          </div>

          <div className="max-w-[580px] mx-auto my-16 sm:my-28 w-full">
            <WhiteImageBox
              title="IMAGE 04"
              subtitle="Membrane thermoformée & ergonomie en apesanteur • 1/1"
              tag="PETIT CARRÉ D'ASSEMBLAGE"
              aspectRatio="1/1"
            />
          </div>

          {/* 4. SECTION PROCESS : GRAND TITRE PLEINE PAGE & IMAGES DESSOUS */}
          <ProcessSection
            tag="04 // PROCESSUS & RECHERCHES STRUCTURELLES"
            tagDotColor="rgb(227, 6, 19)"
            id="process-section-p04"
            description="Études structurales, modélisation volumétrique 3D, plans techniques, découpe laser et maquettes d’expérimentation à l'échelle."
          >
            {/* DUO 01 : 3D & PLANS TECHNIQUES + ZONE DE TEXTE EXPLICATIF */}
            <div className="process-duo-row">
              <div className="process-duo-photos">
                <div className="process-photo-box">
                  <img
                    src={imgP4_3D}
                    alt="Modélisation 3D treillis géométrique - Chaise Suspendue"
                    loading="lazy"
                  />
                </div>
                <div className="process-photo-box">
                  <img
                    src={imgP4_Plan}
                    alt="Plan technique coté et gabarits d'assemblage - Chaise Suspendue"
                    loading="lazy"
                  />
                </div>
              </div>
              <div className="process-duo-text-col">
                <h3 className="process-step-title">Modélisation volumétrique et épures techniques</h3>
                <p className="process-step-desc">
                  Calcul précis des vecteurs de tension et définition des axes d'accroche par modélisation tridimensionnelle. Les plans techniques cotent les rayons de courbure de l'arceau principal et déterminent le centre de gravité exact de l'assise suspendue pour éliminer tout basculement.
                </p>
              </div>
            </div>

            {/* DUO 02 : DÉCOUPE LASER & PREMIÈRE MAQUETTE ATELIER + ZONE DE TEXTE EXPLICATIF (REVERSE) */}
            <div className="process-duo-row reverse">
              <div className="process-duo-photos">
                <div className="process-photo-box">
                  <img
                    src={imgP4_Laser}
                    alt="Découpe laser et usinage numérique des membrures - Chaise Suspendue"
                    loading="lazy"
                  />
                </div>
                <div className="process-photo-box">
                  <img
                    src={imgP4Conception1}
                    alt="Conception Chaise Suspendue - Maquette atelier 01"
                    loading="lazy"
                  />
                </div>
              </div>
              <div className="process-duo-text-col">
                <h3 className="process-step-title">Usinage des platines et assemblage des membrures</h3>
                <p className="process-step-desc">
                  Découpe laser des platines de fixation pour un assemblage à tolérance zéro. Réalisation des premières maquettes en atelier pour vérifier la rigidité intrinsèque de l'arceau triangulé face aux déformations axiales avant passage aux profilés définitifs.
                </p>
              </div>
            </div>

            {/* DUO 03 : MAQUETTES ATELIER 02 & 03 (TENSION & HAUBANAGE) + ZONE DE TEXTE EXPLICATIF */}
            <div className="process-duo-row">
              <div className="process-duo-photos">
                <div className="process-photo-box">
                  <img
                    src={imgP4Conception2}
                    alt="Conception Chaise Suspendue - Maquette atelier 02"
                    loading="lazy"
                  />
                </div>
                <div className="process-photo-box">
                  <img
                    src={imgP4Conception3}
                    alt="Conception Chaise Suspendue - Exploration géométrique 03"
                    loading="lazy"
                  />
                </div>
              </div>
              <div className="process-duo-text-col">
                <h3 className="process-step-title">Haubanage croisé et équilibre dynamique</h3>
                <p className="process-step-desc">
                  Intégration des câbles haute résistance et réglage des longueurs de suspente. La triangulation dynamique transforme la structure rigide en un système auto-tendu, capable d'absorber les mouvements de l'utilisateur tout en maintenant une posture d'assise ergonomique et stable.
                </p>
              </div>
            </div>

            {/* DUO 04 : PROTOTYPE SUSPENDU ÉCHELLE 1 + ZONE DE TEXTE EXPLICATIF (REVERSE) */}
            <div className="process-duo-row reverse">
              <div className="process-duo-photos">
                <div className="process-photo-box">
                  <img
                    src={imgP4Conception4}
                    alt="Conception Chaise Suspendue - Exploration géométrique 04"
                    loading="lazy"
                  />
                </div>
                <div className="process-photo-box">
                  <img
                    src={imgP4Conception5}
                    alt="Conception Chaise Suspendue - Prototype en situation 05"
                    loading="lazy"
                  />
                </div>
              </div>
              <div className="process-duo-text-col">
                <h3 className="process-step-title">Prototype suspendu à l'échelle et éprouvette d'usage</h3>
                <p className="process-step-desc">
                  Suspension du prototype final en conditions réelles d'atelier. Validation de la résistance sous charge, contrôle de l'absence de flèche parasite et appréciation de la légèreté visuelle : l'assise semble léviter dans la pièce, libérant intégralement la continuité du sol.
                </p>
              </div>
            </div>
          </ProcessSection>
        </section>
      )}

      {/* =========================================================================
          PROJET 05: DAA-DAA (#0082ff - Bleu Cobalt Fluo)
         ========================================================================= */}
      {activeIndex === 4 && (
        <section>
          {/* 1. HERO DUAL ROW: CARTE À GAUCHE, TEXTE À DROITE */}
          <div className="grid grid-cols-1 lg:grid-cols-[1.15fr_1fr] gap-10 lg:gap-16 items-center mb-24 sm:mb-32">
            <div className="relative w-full aspect-[4/5] min-h-[440px] bg-[#0082ff] overflow-hidden shadow-2xl group">
              <FrameIllustration illustrationKey={project.illustrationKey} strokeColor={project.strokeColor} />
              <PaperGrain />
              <div className="absolute bottom-0 inset-x-0 p-6 sm:p-8 bg-white/16 backdrop-blur-md z-20 flex flex-col items-start">
                <span className="text-[11px] font-black uppercase tracking-widest text-black/85 mb-1">
                  05 — Enceinte Stéréo // Design Produit
                </span>
                <h2 className="text-2xl sm:text-4xl font-black tracking-tight text-black leading-none mb-1.5">
                  * DAA-DAA *
                </h2>
                <div className="flex items-center gap-2 text-[10px] font-black uppercase tracking-widest text-black/70">
                  <span>STÉRÉO BI-AMPLIFIÉE</span>
                  <span>*</span>
                  <span>ALUMINIUM BROSSÉ &amp; BLEU COBALT</span>
                </div>
              </div>
            </div>

            <div className="flex flex-col justify-center">

              <h1 className="text-4xl sm:text-6xl font-black tracking-tight leading-[0.98] mb-4 text-white">
                DAA-DAA
              </h1>
              <p className="text-base sm:text-lg font-bold text-neutral-200 mb-6 leading-snug">
                Un système d'écoute stéréophonique sculptural né du dialogue entre deux modules acoustiques bleu cobalt, un plateau d'amplification analogique et un piètement cruciforme autoportant.
              </p>

              <div className="mb-6">
                <div className="space-y-3 text-sm text-neutral-300 leading-relaxed font-normal">
                  <p>
                    Pourquoi DAA-DAA ? Ce projet repense la présence spatiale et sculpturale de l'enceinte de monitoring. Loin des coffrages monolithiques cubiques, DAA-DAA désolidarise les deux chambres acoustiques cylindriques pour projeter un champ stéréophonique d'une clarté chirurgicale.
                  </p>
                  <p>
                    Chaque cylindre laqué bleu cobalt intègre un haut-parleur large bande à membrane texturée haute fidélité. La base circulaire en noir mat accueille les potentiomètres de réglage analogique à crans, tandis que le piètement cruciforme en aluminium brossé assure un découplage mécanique absolu avec la surface d'appui.
                  </p>
                </div>
              </div>
            </div>
          </div>

          {/* 2. PHOTO 1 : PERSPECTIVE TROIS-QUARTS & TEXTE EXPLICATIF RÉDUIT CÔTE À CÔTE */}
          <div className="grid grid-cols-1 lg:grid-cols-[2.2fr_1fr] gap-6 lg:gap-14 items-center my-16 sm:my-28 max-w-[1520px] mx-auto w-full px-4 sm:px-6">
            <div className="w-full flex items-center justify-center">
              <WhiteImageBox
                title="IMAGE 01 — GRANDE VUE PERSPECTIVE"
                aspectRatio="1/1"
                imageSrc={imgSpeakerThreeQuarter}
                imageAlt="Enceintes acoustiques stéréophoniques, vue trois-quarts perspective sans fond blanc"
                objectFit="contain"
                className="!bg-transparent !shadow-none !border-none !w-full"
                imageStyle={{ padding: "0", filter: "drop-shadow(0 24px 48px rgba(0,0,0,0.75))" }}
                style={{ backgroundColor: "transparent", maxHeight: "84vh", width: "100%" }}
              />
            </div>
            <div className="flex flex-col justify-center text-white max-w-sm">
              <div className="text-xs sm:text-sm font-normal text-white/90 leading-relaxed space-y-2" style={{ textAlign: "justify", textJustify: "inter-word" }}>
                <p className="text-white/90 m-0 text-justify" style={{ textAlign: "justify", textJustify: "inter-word" }}>Disposition stéréophonique active articulée autour de deux modules en aluminium massif.</p>
                <p className="text-white/90 m-0 text-justify" style={{ textAlign: "justify", textJustify: "inter-word" }}>Orientation angulaire calculée pour une directivité spatiale optimale au point d'écoute.</p>
                <p className="text-white/90 m-0 text-justify" style={{ textAlign: "justify", textJustify: "inter-word" }}>Une géométrie pure qui neutralise les résonances internes et affirme sa présence sculpturale.</p>
              </div>
            </div>
          </div>

          {/* 3. DUO IN-SITU & USAGE : SALON CONTEMPORAIN ET ÉCHELLE HUMAINE (4:5) */}
          <div className="grid grid-cols-1 md:grid-cols-2 gap-10 md:gap-16 items-center my-16 sm:my-28">
            <WhiteImageBox
              title="IMAGE 02 — IN-SITU SALON"
              aspectRatio="4/5"
              imageSrc={imgSpeakerInsitu}
              imageAlt="Enceintes acoustiques en situation réelle sur table basse circulaire en chrome et tapis bleu cobalt"
              objectFit="cover"
              className="!bg-transparent !shadow-none !border-none"
            />
            <WhiteImageBox
              title="IMAGE 03 — INTERACTION TACTILE"
              aspectRatio="4/5"
              imageSrc={imgSpeakerHand}
              imageAlt="Détail du geste ergonomique réglant les commandes analogiques de l'enceinte"
              objectFit="cover"
              className="!bg-transparent !shadow-none !border-none"
            />
          </div>

          {/* 4. PHOTO 4 (ROUES URÉTHANE) & TEXTE EXPLICATIF 4 LIGNES À DROITE EN BLANC */}
          <div className="grid grid-cols-1 md:grid-cols-[1.15fr_1fr] gap-10 md:gap-16 items-end my-20 sm:my-32 max-w-6xl mx-auto w-full px-4 sm:px-6">
            <div className="w-full">
              <WhiteImageBox
                title="IMAGE 04 — INSPIRATION ROUES URÉTHANE"
                aspectRatio="1/1"
                imageSrc={imgSpeakerWheels}
                imageAlt="Roues en uréthane bleu cobalt translucide 70mm 78A à l'origine du concept des modules acoustiques"
                objectFit="contain"
                className="!bg-transparent !shadow-none !border-none"
                imageStyle={{ padding: "clamp(10px, 2vw, 24px)", filter: "drop-shadow(0 20px 45px rgba(0, 110, 255, 0.35))" }}
                style={{ backgroundColor: "transparent" }}
              />
            </div>
            <div className="flex flex-col justify-end self-end text-white">
              <div className="text-base sm:text-lg font-normal text-white leading-relaxed space-y-1" style={{ textAlign: "justify", textJustify: "inter-word" }}>
                <p className="text-white m-0 text-justify" style={{ textAlign: "justify", textJustify: "inter-word" }}>Roues de skateboard en uréthane coulé 78A détournées de leur fonction.</p>
                <p className="text-white m-0 text-justify" style={{ textAlign: "justify", textJustify: "inter-word" }}>Leur translucidité bleu cobalt a défini le gabarit des modules acoustiques.</p>
                <p className="text-white m-0 text-justify" style={{ textAlign: "justify", textJustify: "inter-word" }}>La matière absorbe naturellement les micro-vibrations de la membrane.</p>
                <p className="text-white m-0 text-justify" style={{ textAlign: "justify", textJustify: "inter-word" }}>Une collision formelle entre culture de la glisse et haute-fidélité.</p>
              </div>
            </div>
          </div>

          {/* 5. PHOTO 5 : VUE ARRIÈRE CONNECTIQUES & TEXTE EXPLICATIF RÉDUIT CÔTE À CÔTE */}
          <div className="grid grid-cols-1 lg:grid-cols-[2.2fr_1fr] gap-6 lg:gap-14 items-center my-16 sm:my-28 max-w-[1520px] mx-auto w-full px-4 sm:px-6">
            <div className="w-full flex items-center justify-center">
              <WhiteImageBox
                title="IMAGE 05 — VUE ARRIÈRE CONNECTIQUES"
                aspectRatio="3/4"
                imageSrc={imgSpeakerBack}
                imageAlt="Enceintes acoustiques, grande vue arrière connectique et chambres acoustiques sans fond blanc"
                objectFit="contain"
                className="!bg-transparent !shadow-none !border-none !w-full"
                imageStyle={{ padding: "0", filter: "drop-shadow(0 24px 48px rgba(0,0,0,0.75))" }}
                style={{ backgroundColor: "transparent", maxHeight: "84vh", width: "100%" }}
              />
            </div>
            <div className="flex flex-col justify-center text-white max-w-sm">
              <div className="text-xs sm:text-sm font-normal text-white/90 leading-relaxed space-y-2" style={{ textAlign: "justify", textJustify: "inter-word" }}>
                <p className="text-white/90 m-0 text-justify" style={{ textAlign: "justify", textJustify: "inter-word" }}>Panneau dorsal intégrant borniers massifs en cuivre pur et entrées analogiques symétriques.</p>
                <p className="text-white/90 m-0 text-justify" style={{ textAlign: "justify", textJustify: "inter-word" }}>Évents laminaires arrière calibrés pour une décompression fluide et sans turbulence.</p>
                <p className="text-white/90 m-0 text-justify" style={{ textAlign: "justify", textJustify: "inter-word" }}>Le dos usiné fait également office de dissipateur thermique pour l'étage d'amplification.</p>
              </div>
            </div>
          </div>

          {/* 6. PHOTO 6 AGRANDIE : GRAND FORMAT MACRO CÔNES & COMMANDES (16:9) */}
          <div className="w-[100vw] relative left-1/2 right-1/2 -ml-[50vw] -mr-[50vw] max-w-[100vw] px-4 sm:px-12 my-20 sm:my-32 box-border">
            <WhiteImageBox
              title="IMAGE 06 — MACRO COMMANDES PLEIN ÉCRAN"
              aspectRatio="16/9"
              imageSrc={imgSpeakerMacro}
              imageAlt="Gros plan macro sur les membranes des haut-parleurs et potentiomètres analogiques sans fond blanc"
              objectFit="contain"
              className="!bg-transparent !shadow-none"
              imageStyle={{ padding: "clamp(6px, 1vw, 20px)", filter: "drop-shadow(0 20px 40px rgba(0,0,0,0.75))" }}
              style={{ minHeight: "420px", maxHeight: "85vh", backgroundColor: "transparent" }}
            />
          </div>

          {/* 7. PHOTO 7 : VUE FRONTALE CONTRE-PLONGÉE & TEXTE EXPLICATIF RÉDUIT CÔTE À CÔTE */}
          <div className="grid grid-cols-1 lg:grid-cols-[2.2fr_1fr] gap-6 lg:gap-14 items-center my-16 sm:my-28 max-w-[1520px] mx-auto w-full px-4 sm:px-6">
            <div className="w-full flex items-center justify-center">
              <WhiteImageBox
                title="IMAGE 07 — VUE FRONTALE CONTRE-PLONGÉE"
                aspectRatio="1/1"
                imageSrc={imgSpeakerFront}
                imageAlt="Enceintes acoustiques, grande vue de face en contre-plongée sans fond blanc"
                objectFit="contain"
                className="!bg-transparent !shadow-none !border-none !w-full"
                imageStyle={{ padding: "0", filter: "drop-shadow(0 24px 48px rgba(0,0,0,0.75))" }}
                style={{ backgroundColor: "transparent", maxHeight: "84vh", width: "100%" }}
              />
            </div>
            <div className="flex flex-col justify-center text-white max-w-sm">
              <div className="text-xs sm:text-sm font-normal text-white/90 leading-relaxed space-y-2" style={{ textAlign: "justify", textJustify: "inter-word" }}>
                <p className="text-white/90 m-0 text-justify" style={{ textAlign: "justify", textJustify: "inter-word" }}>Prise de vue frontale en contre-plongée soulignant la posture puissante de l'enceinte.</p>
                <p className="text-white/90 m-0 text-justify" style={{ textAlign: "justify", textJustify: "inter-word" }}>Alignement coaxial des transducteurs assurant une cohérence de phase absolue sur tout le spectre.</p>
                <p className="text-white/90 m-0 text-justify" style={{ textAlign: "justify", textJustify: "inter-word" }}>Le contraste aluminium brossé et translucidité cobalt dialogue avec la lumière ambiante.</p>
              </div>
            </div>
          </div>
        </section>
      )}

      {/* =========================================================================
          PROJET 06: LEO-11 (#ffeb00 - Jaune Fluo)
         ========================================================================= */}
      {(activeIndex === 5 || activeIndex === 6) && (
        <section>
          {/* 1. HERO DUAL ROW: TEXTE À GAUCHE, CARTE COULEUR À DROITE */}
          <div className="grid grid-cols-1 lg:grid-cols-[1fr_1.15fr] gap-10 lg:gap-16 items-center mb-24 sm:mb-32">
            <div className="flex flex-col justify-center order-2 lg:order-1">

              <h1 className="text-4xl sm:text-6xl font-black tracking-tight leading-[0.98] mb-4 text-white">
                LEO-11
              </h1>
              <p className="text-base sm:text-lg font-bold text-neutral-200 mb-6 leading-snug">
                Lampe d'ambiance sculpturale : tension entre ossature filaire en acier et diffusion graphique texturée.
              </p>

              <div className="mb-6">
                <div className="space-y-3 text-sm text-neutral-300 leading-relaxed font-normal">
                  <p>
                    Conception du luminaire LEO-11, né d'une recherche sur l'élévation des volumes lumineux et la transparence des structures métalliques. Une cage filaire cubique en acier élève un parallélépipède sérigraphié dont le papier diffuse une lumière chaude et graphique.
                  </p>
                  <p>
                    Le câble d'alimentation traverse librement la base géométrique en suspension, assumant le dessin technique du passage de courant comme un vecteur d'équilibre visuel dans l'espace.
                  </p>
                </div>
              </div>
            </div>

            <div className="relative w-full aspect-[4/3] bg-[#ffeb00] overflow-hidden shadow-2xl group order-1 lg:order-2">
              <FrameIllustration illustrationKey={project.illustrationKey} strokeColor={project.strokeColor} />
              <PaperGrain />
              <div className="absolute bottom-0 inset-x-0 p-6 sm:p-8 bg-white/16 backdrop-blur-md z-20 flex flex-col items-start">
                <span className="text-[11px] font-black uppercase tracking-widest text-black/85 mb-1">
                  06 — Luminaire // Studio Paris
                </span>
                <h2 className="text-2xl sm:text-4xl font-black tracking-tight text-black leading-none mb-1.5">
                  * LEO-11 *
                </h2>
                <div className="flex items-center gap-2 text-[10px] font-black uppercase tracking-widest text-black/70">
                  <span>LUMINAIRE D'AMBIANCE</span>
                  <span>*</span>
                  <span>JAUNE FLUO</span>
                </div>
              </div>
            </div>
          </div>

          {/* 2. PREMIÈRE IMAGE : VUE PERSPECTIVE AÉRIENNE EN SUSPENSION (RÉSOLUTION NATIVE 1024x576) */}
          <div className="w-[100vw] relative left-1/2 right-1/2 -ml-[50vw] -mr-[50vw] max-w-[100vw] px-4 sm:px-12 my-16 sm:my-24 box-border">
            <div className="relative w-full max-w-[1280px] mx-auto bg-black flex items-center justify-center">
              <img
                src={imgLeoFloating}
                alt="LEO-11 - Luminaire d'ambiance, vue perspective en suspension sur fond noir"
                className="w-full max-w-[1280px] h-auto max-h-[720px] object-contain transition-transform duration-700 ease-out hover:scale-[1.03]"
                loading="eager"
              />
            </div>
          </div>

          {/* 3. DEUXIÈME IMAGE : VUE EN SITUATION IN SITU SUR SOCLE EN BOIS MASSIF */}
          <div className="w-[100vw] relative left-1/2 right-1/2 -ml-[50vw] -mr-[50vw] max-w-[100vw] px-4 sm:px-12 my-16 sm:my-24 box-border">
            <div className="relative w-full max-w-[1280px] mx-auto bg-black flex items-center justify-center">
              <img
                src={imgLeoInsitu}
                alt="LEO-11 - Luminaire d'ambiance en situation in situ sur bloc de bois brut"
                className="w-full max-w-[1280px] h-auto max-h-[720px] object-contain transition-transform duration-700 ease-out hover:scale-[1.03]"
                loading="eager"
              />
            </div>
          </div>
        </section>
      )}

      {/* Universal Next Project Teaser Footer */}
      <div className="flex items-center justify-between flex-wrap gap-6 p-7 bg-white/5 border border-white/10 hover:border-white/25 hover:bg-white/[0.07] transition-all duration-300 mt-28 sm:mt-36">
        <div className="flex items-center gap-5">
          <div
            className="w-11 h-11 relative overflow-hidden flex-shrink-0 shadow-md"
            style={{ backgroundColor: nextProject.bgColor }}
          >
            <div
              className="absolute inset-0 opacity-50 mix-blend-multiply"
              style={{
                backgroundImage: `url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 250 250' width='250' height='250'%3E%3Cfilter id='paperFibers' x='0' y='0' width='100%25' height='100%25'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.62' numOctaves='4' result='noise' stitchTiles='stitch'/%3E%3CfeColorMatrix type='matrix' values='3.5 0 0 0 -1.2  0 3.5 0 0 -1.2  0 0 3.5 0 -1.2  0 0 0 1 0' in='noise' result='contrasted'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23paperFibers)'/%3E%3C/svg%3E")`,
                backgroundSize: "100px 100px",
              }}
            />
          </div>
          <div>
            <div className="text-[11px] font-black uppercase tracking-[0.2em] text-neutral-400 mb-1">
              Projet Suivant &bull; {nextProject.number}
            </div>
            <div className="text-xl sm:text-2xl font-black text-white">
              {nextProject.title}
            </div>
          </div>
        </div>

        <button
          type="button"
          onClick={() => onSelectProject(`project-${nextProject.number}`)}
          className="inline-flex items-center gap-2 text-xs font-black uppercase tracking-widest text-white hover:opacity-60 transition-opacity"
        >
          <span>Découvrir la pièce</span>
          <span>&rarr;</span>
        </button>
      </div>
    </article>
  );
}
