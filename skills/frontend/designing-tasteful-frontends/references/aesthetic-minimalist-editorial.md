# Aesthetic Profile: Minimalist Editorial & Workspace UI

This reference defines the design rules for highly refined, ultra-minimalist, document-style web interfaces reminiscent of premium productivity tools (Notion, Linear, Craft). Use this profile when the Design Read calls for a **clean, editorial, minimalist, or workspace** visual language.

---

## 1. The Warm Monochrome & Spot Pastel Palette

Color is treated as an extremely scarce resource. It is deployed exclusively to convey semantic meaning or highlight focused actions.

*   **Canvas / Page Background:** Reject harsh pure white. Use warm bone, off-white, or unbleached paper tones:
    *   *Light Mode:* `#F7F6F3` or `#FBFBFA` or `#F9F9F8`.
    *   *Dark Mode:* `#121212` or `#18181B`.
*   **Surfaces (Cards/Panels):** Pure white `#FFFFFF` (light mode) or `#1E1E24` (dark mode) to pop cleanly against the warm background.
*   **Structural Lines & Dividers:** Very thin, low-contrast lines: `border border-zinc-200/60` or `rgba(0,0,0,0.06)`.
*   **Spot Pastels:** Only highly desaturated, washed-out pastels are permitted for badges, tag backgrounds, or inline code highlights:
    *   *Pale Red:* `#FDEBEC` (Text: `#9F2F2D`)
    *   *Pale Blue:* `#E1F3FE` (Text: `#1F6C9F`)
    *   *Pale Green:* `#EDF3EC` (Text: `#346538`)
    *   *Pale Yellow:* `#FBF3DB` (Text: `#956400`)

---

## 2. Flat Layouts & Editorial Spacing

*   **Crisp Corners:** corner-radii must be tight and geometric: `rounded-md` (6px) or `rounded-lg` (8px) maximum. Banned: `rounded-3xl`, `rounded-full` for large panels, and pill buttons.
*   **No Drop Shadows:** Standard drop shadows are completely banned. Card boundaries are defined purely by borders (`1px solid #EAEAEA` or `border-zinc-200`) and whitespace.
*   **Accordions & Lists:** FAQ or detail accordions are stripped of box containers. Separate items using only a thin bottom border (`border-b border-zinc-200`). Use clean, sharp `+` and `−` symbols for toggle states.
*   **Macro-Whitespace:** Allow sections to breathe. Use huge vertical padding (`py-24` or `py-32` in Tailwind) while keeping content containers tightly constrained (`max-w-4xl` or `max-w-5xl` centered).

---

## 3. Micro-UIs & Technical Framing

*   **Keystroke Indicators (`<kbd>`):** Render keyboard shortcuts as physical, raised mechanical keys. Use monospaced typography, tight borders, and light background fills:
    ```html
    <kbd class="font-mono text-[11px] font-medium px-1.5 py-0.5 bg-zinc-100 border border-zinc-200 rounded shadow-sm text-zinc-600 dark:bg-zinc-800 dark:border-zinc-700 dark:text-zinc-400">
      ⌘ K
    </kbd>
    ```
*   **Faux OS Chrome:** When demonstrating software mockups, wrap the visual in a crisp container with a white top bar containing three small, light-gray circles (replicating macOS window controls):
    ```html
    <div class="border border-zinc-200 rounded-lg overflow-hidden bg-white">
      <div class="flex items-center gap-1.5 px-4 py-2 border-b border-zinc-100 bg-zinc-50">
        <span class="w-2.5 h-2.5 rounded-full bg-zinc-200"></span>
        <span class="w-2.5 h-2.5 rounded-full bg-zinc-200"></span>
        <span class="w-2.5 h-2.5 rounded-full bg-zinc-200"></span>
      </div>
      <div class="p-6">
        <!-- Mockup Content -->
      </div>
    </div>
    ```
