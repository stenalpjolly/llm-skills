# Aesthetic Profile: Soft Tactile & High-End Agency UI

This reference defines the design rules for expensive, tactile, Apple-esque, and Linear-tier digital experiences. Use this profile when the Design Read calls for a **premium consumer, health, modern SaaS, or luxury portfolio** visual language.

---

## 1. The "Double-Bezel" (Doppelrand) Architecture

Never place cards, inputs, images, or primary containers flatly on the background. They must look like physical, machined hardware plates sitting in aluminum or glass trays using nested enclosures.

```text
+-------------------------------------------------------------+
| OUTER SHELL (bg-black/5 or bg-white/5, rounded-[2rem])      |
|  +-------------------------------------------------------+  |
|  | INNER CORE (bg-surface, rounded-[calc(2rem-0.375rem)])|  |
|  |                                                       |  |
|  |  Content Area                                         |  |
|  +-------------------------------------------------------+  |
+-------------------------------------------------------------+
```

### 1.A Outer Shell Styling
*   **Radii:** Exaggerated, soft squircle corners (`rounded-[2rem]` or `rounded-[2.5rem]`).
*   **Borders:** Micro-hairline borders using low-opacity rings or borders (`border border-white/10` or `ring-1 ring-black/5`).
*   **Fill:** Muted, low-opacity fills (`bg-black/5` in light mode, `bg-white/5` in dark mode).
*   **Padding:** Strict uniform padding (`p-1.5` or `p-2`) to act as a physical channel.

### 1.B Inner Core Styling
*   **Radii:** Mathematically calculated concentric radius to match the outer shell perfectly:
    $$\text{Inner Radius} = \text{Outer Radius} - \text{Outer Padding}$$
    *   *Tailwind implementation:* `rounded-[calc(2rem-0.375rem)]` (if padding is `p-1.5` / `0.375rem`) or `rounded-[calc(2rem-0.5rem)]` (if padding is `p-2` / `0.5rem`).
*   **Highlights:** A subtle inner white highlight at the top edge to simulate glass refraction: `shadow-[inset_0_1px_1px_rgba(255,255,255,0.15)]` (dark mode) or `shadow-[inset_0_1px_1px_rgba(255,255,255,0.6)]` (light mode).

---

## 2. Button-in-Button CTA Architecture

Interactive buttons must feel haptic and responsive. When using primary pill CTAs with trailing action indicators (e.g., arrows `↗` or `→`), do not let the icon float naked next to the label.

*   **Structure:** Nest the trailing icon inside its own distinct circular container flush with the main button's right inner padding:
    ```tsx
    <button className="group relative flex items-center gap-4 rounded-full bg-zinc-900 px-6 py-3 text-sm font-medium text-white transition-all duration-300 hover:bg-zinc-800 active:scale-[0.98] dark:bg-white dark:text-zinc-950 dark:hover:bg-zinc-100">
      <span>Get Started</span>
      <span className="flex h-8 w-8 items-center justify-center rounded-full bg-white/10 text-white transition-transform duration-500 group-hover:translate-x-1 group-hover:-translate-y-[1px] dark:bg-black/10 dark:text-black">
        ↗
      </span>
    </button>
    ```
*   **Hover Interaction:** On hover, scale the button slightly and translate the nested icon diagonally to create kinetic tension. Scale the button down to `scale-[0.98]` on `:active` to simulate a physical push.

---

## 3. Custom Spring Motion Dynamics

Reject standard browser linear and ease-in-out animations. All active movement must simulate physical mass, friction, and spring tension.

*   **Tailwind Transitions:** Use a heavy, fluid cubic-bezier curve:
    `ease-[cubic-bezier(0.32,0.72,0,1)]` paired with long durations (`duration-700` or `duration-1000`).
*   **Motion (Framer Motion) Physics:** Standardize on a premium spring configuration:
    ```ts
    const springTransition = {
      type: "spring",
      stiffness: 100,
      damping: 20,
      mass: 1
    };
    ```
*   **Staggered Entry Reveals:** Avoid mounting lists or grids instantly. Fade and translate them upward from a mask with progressive delay offsets (`delay-75`, `delay-100`, `delay-150`).
