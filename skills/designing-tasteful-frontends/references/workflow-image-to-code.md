# Workflow Profile: Image-First Design-to-Code Pipeline

This reference defines the execution pipeline for translating visual mockups and generated design references into clean, pixel-perfect frontend code. Use this workflow when building **highly visual pages** (landing pages, marketing sites, portfolios) where visual fidelity and custom art-direction are the primary metrics.

---

## 1. The Mandatory Three-Step Workflow

When tasked with a visual frontend project, you are forbidden from starting with freeform coding. If image generation tools are available in the environment, you must execute the following sequence:

```text
+------------------------+      +------------------------+      +------------------------+
|  1. IMAGE GENERATION   | ---> |   2. DEEP ANALYSIS     | ---> |   3. IMPLEMENTATION    |
| (Mockups per section)  |      |  (Extract Design Map)  |      |  (Clean RSC + Motion)  |
+------------------------+      +------------------------+      +------------------------+
```

### 1.A Step 1: Generate Section Mockups
*   Generate dedicated mockup images for individual page sections (e.g., hero, bento feature grid, CTA, footer).
*   Avoid compressing the entire page into a single unreadable vertical scroll. Prefer large, high-resolution, section-specific images.
*   If details or typography on a generated image are blurry, **regenerate** that specific section as a fresh standalone image instead of guessing the design.

### 1.B Step 2: Deep Extraction & Analysis
Before writing any code, inspect the generated mockups and compile a detailed design extraction map:
*   **Exact Copy:** Extract all readable headlines, subheadlines, CTA button labels, and section titles.
*   **Typography Scale:** Analyze font weight ratios, display-to-body contrast, line heights, and letter-spacing (tracking).
*   **Spacing Rhythm:** Map section-to-section padding, column gutters, card paddings, and distance between headings and CTAs.
*   **Color Palette:** Identify the exact background colors, surface card colors, and accent colors.
*   **Component Borders:** Note corner-radii (radii scales), divider strokes, and shadow depths.

### 1.C Step 3: Faithful Coding Translation
Translate the extracted design map into React and Tailwind. Keep the layout highly faithful to the approved image reference, only inventing details when the images leave a specific interaction state ambiguous.

---

## 2. Structural & Layout Guardrails

*   **Responsive First-View:** The hero section and immediate fold area must fit cleanly on a small laptop screen. Do not overstuff the above-the-fold area with multiple competing features, nested cards, or crowded text. Let it breathe.
*   **Anti-Nested Box Rule:** Avoid default box-in-box structures (e.g., cards inside larger cards wrapped in outer bordered sections). Use open, borderless layouts and whitespace to compartmentalize content wherever possible.
*   **Fixed Media Frames:** Images and photos inside the website should sit in controlled, consistent, implementation-friendly frames with fixed aspect ratios (e.g., `aspect-video` or `aspect-[4/3]`). Avoid random image dimensions.
*   **Social Proof Logos:** Trusted-by logo walls must live directly below the hero section (never inside it). Use real SVG paths (from Simple Icons or Devicon) rather than plain text names. Ensure logos adapt cleanly to both light and dark mode.
