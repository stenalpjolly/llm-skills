# Aesthetic Profile: Industrial Brutalism & CRT Telemetry

This reference defines the design rules for rigid, declassified, aerospace, and high-density mechanical layouts. Use this profile when the Design Read calls for an **industrial, brutalist, cybernetic, or technical telemetry** visual language.

---

## 1. Visual Archetypes

Pick **ONE** visual archetype and commit to it. Do not mix light Swiss print with dark CRT telemetry in the same project tree.

### 1.A Swiss Industrial Print (Light)
*   **Background:** Matte, unbleached documentation paper (`#F4F4F0` or `#EAE8E3`).
*   **Typography:** Monolithic, heavy sans-serif display type (`Neue Haas Grotesk`, `Archivo Black`, or `Monument Extended` in heavy black weights).
*   **Layout:** High-contrast grids outlined by thick structural borders, with massive uppercase headers and generous asymmetric white space.
*   **Accent:** Aviation/Hazard Red (`#E61919`). This is the **ONLY** accent color, used for strikethroughs, warning borders, or alert states.

### 1.B Tactical Telemetry & CRT Terminal (Dark)
*   **Background:** Matte deactivated CRT black (`#0A0A0A` or `#121212`).
*   **Typography:** Strict Monospace (`JetBrains Mono`, `IBM Plex Mono`, `Space Mono`, or `VT323`).
*   **Layout:** Extremely dense tabular grids, outlined with thin border-grids, featuring live coordinate data, barcodes, and ASCII indicators.
*   **Accents:** Phosphorus Green (`#4AF626`) or amber yellow, used strictly for active status readouts or blinking glyphs. Primary alerts use Hazard Red (`#E61919`).

---

## 2. Corner Radius & Compartmentalization

*   **Corner Radius Absolute Zero:** Corner-radii are banned. The value is strictly set to `rounded-none` / `0`. All interactive buttons, cards, images, and inputs must have perfectly sharp 90-degree corners.
*   **Grid-Line Determinism:** To build perfect, razor-thin dividing lines between sections or cells without declaring messy individual borders, set a contrasting parent background and use `gap: 1px`:
    ```tsx
    <div class="grid grid-cols-1 md:grid-cols-3 gap-[1px] bg-zinc-800 border border-zinc-800">
      <div class="bg-zinc-950 p-6">Cell 1</div>
      <div class="bg-zinc-950 p-6">Cell 2</div>
      <div class="bg-zinc-950 p-6">Cell 3</div>
    </div>
    ```

---

## 3. Utilitarian Symbology & ASCII Art

Replace standard icon glyphs and decorative elements with raw ASCII characters, industrial warnings, and technical markers:

*   **ASCII Framing:** Use brackets, coordinates, and slashes to frame labels or titles:
    `[ SYSTEM STATUS ]`, `< RE-INDEX >`, `// OPERATOR LOGS \\\\`, `>>> DETAILS`.
*   **Industrial Markers:** Treat copyright (`©`), trademark (`™`), and registration (`®`) marks as prominent geometric design features rather than tiny legal text:
    ```html
    <div class="text-mono text-[9px] tracking-widest text-zinc-500 uppercase">
      REV_09.43.1 // SYS_REG ®
    </div>
    ```
*   **Post-Processing Overlays:** Programmatically simulate hardware scanlines on CRT terminals using repeating linear gradients on the background:
    ```css
    .crt-scanlines {
      background-image: repeating-linear-gradient(
        0deg,
        transparent,
        transparent 2px,
        rgba(0, 0, 0, 0.15) 2px,
        rgba(0, 0, 0, 0.15) 4px
      );
    }
    ```
*   **Technical Asset Additions:** Add mechanical elements like repeating vertical lines (re-created via thin borders to simulate barcodes), crosshairs (`+`) at grid intersections, and mock hardware warnings.
