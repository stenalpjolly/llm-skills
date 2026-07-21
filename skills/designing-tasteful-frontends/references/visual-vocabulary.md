# The Visual Vocabulary: Architectural Layouts & Motion Paradigms

This reference document defines a high-end visual vocabulary. Use these pattern names and structures to design custom layouts and choreograph premium motion.

---

## 1. Hero Paradigms
*   **Asymmetric Split Hero:** Headline and subtext offset heavily on one side; primary visual asset (image or interactive canvas) on the other. Uses generous negative space.
*   **Editorial Manifesto Hero:** Monolithic display typography acting as a poster-like statement. Visual assets are omitted or placed far below the fold.
*   **Kinetic-Type Hero:** The typography *is* the asset. Text animates dynamically (scroll-driven scaling, weight shifts, or characters dodging the cursor).
*   **Scroll-Pinned Hero:** The hero section pins at the top of the viewport. As the user scrolls, the background media scales down or fades, revealing content scrolling up from behind.
*   **Inline-Image Behemoth:** Embeds small, highly stylized, pill-shaped photographic loops directly *inside* the massive display headline. Acts as visual punctuation.

---

## 2. Layout & Container Systems
*   **Prism Bento Grid:** Asymmetric grid of varying tile sizes (e.g., a `col-span-8` bento card containing a visual asset next to two stacked `col-span-4` text cards). Must be gapless and mathematically interlinked.
*   **Split-Screen Scroll:** The viewport is split 50/50. As the user scrolls, the left side moves down while the right side slides up in opposite directions.
*   **Sticky-Stack Sections:** Sections stick to the top of the viewport and stack physically on top of each other, creating a vertical layer effect on scroll.
*   **Double-Bezel Enclosure (Doppelrand):** A high-end card framing technique simulating physical hardware.
    *   *Outer Shell:* `bg-black/5` or `bg-white/5` with a thin border `border border-white/10` or `ring-1 ring-black/5`, padding `p-1.5` or `p-2`, and a soft outer radius `rounded-[2rem]`.
    *   *Inner Core:* The content panel, styled with a distinct background, an inner highlight `shadow-[inset_0_1px_1px_rgba(255,255,255,0.15)]`, and a mathematically smaller curve radius `rounded-[calc(2rem-0.375rem)]`.

---

## 3. Navigation & Interactive Elements
*   **Fluid Island Nav:** Floating glass navigation pill detached from the viewport top (`mt-6 mx-auto w-max rounded-full backdrop-blur-md bg-white/15 dark:bg-black/20 border border-white/10`).
*   **Button-in-Button CTA:** A primary pill button where the trailing icon (e.g., `↗`) is nested in its own distinct circular wrapper, flush with the button's right padding.
*   **Magnetic Button:** An interactive element that detects cursor coordinates and fluidly translates/pulls toward the cursor using spring physics.
*   **Staggered Mask Link Reveal:** Off-canvas or hamburger menus reveal navigation links by sliding them up out of invisible mask boxes (`translate-y-12 opacity-0` to `translate-y-0 opacity-100`) with staggered delays.

---

## 4. Canonical Code Skeletons

### 4.A GSAP Horizontal-Pan (Scroll-Hijack)
Pins a section and translates a track horizontally as the user scrolls vertically. Essential for portfolio slide galleries:

```tsx
"use client";
import { useRef, useEffect } from "react";
import { gsap } from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
import { useReducedMotion } from "motion/react";

gsap.registerPlugin(ScrollTrigger);

export function HorizontalPan({ children }: { children: React.ReactNode }) {
  const wrap = useRef<HTMLDivElement>(null);
  const track = useRef<HTMLDivElement>(null);
  const reduce = useReducedMotion();

  useEffect(() => {
    if (reduce || !wrap.current || !track.current) return;
    const ctx = gsap.context(() => {
      const distance = track.current!.scrollWidth - window.innerWidth;
      gsap.to(track.current, {
        x: -distance,
        ease: "none",
        scrollTrigger: {
          trigger: wrap.current,
          start: "top top", // Pin wrapper at top of viewport
          end: () => `+=${distance}`, // Vertical scroll height matches horizontal distance
          pin: true,
          scrub: 1,
          invalidateOnRefresh: true,
        },
      });
    }, wrap);
    return () => ctx.revert();
  }, [reduce]);

  return (
    <section ref={wrap} className="relative overflow-hidden">
      <div ref={track} className="flex h-[100dvh] items-center">
        {children}
      </div>
    </section>
  );
}
```

### 4.B Motion Scroll-Reveal Stagger (Lightweight Alternative)
Use this lightweight Motion (formerly Framer Motion) component for clean, entry-on-scroll animations that do not require complex pinning or scrubbing:

```tsx
"use client";
import { motion, useReducedMotion } from "motion/react";

interface RevealStaggerProps {
  items: React.ReactNode[];
  className?: string;
}

export function RevealStagger({ items, className = "grid gap-6" }: RevealStaggerProps) {
  const reduce = useReducedMotion();

  return (
    <ul className={className}>
      {items.map((item, i) => (
        <motion.li
          key={i}
          initial={reduce ? false : { opacity: 0, y: 24 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true, amount: 0.2 }}
          transition={{
            duration: 0.6,
            delay: i * 0.06,
            ease: [0.16, 1, 0.3, 1], // Custom cubic-bezier spring simulation
          }}
        >
          {item}
        </motion.li>
      ))}
    </ul>
  );
}
```
Use this for testimonial walls, logo rows, and feature grids. Do not mix GSAP and Motion within the same component subtree.

---

## 5. Component Hierarchies, Shadows & Overlay Paradigms

### 5.A Three-Tier Button System (Tailwind)
Interactive actions should convey strict importance hierarchies. Do not place identical button styles side-by-side.

```tsx
// Tier 1: Primary Action Button (Solid fill, prominent contrast, exactly one per primary hero/card)
export function PrimaryButton({ children, ...props }: React.ComponentProps<"button">) {
  return (
    <button
      {...props}
      className="inline-flex items-center justify-center rounded-lg bg-zinc-900 px-5 py-2.5 text-sm font-medium text-zinc-50 transition-all duration-200 hover:bg-zinc-800 active:scale-[0.98] focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-zinc-950 focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 dark:bg-zinc-50 dark:text-zinc-950 dark:hover:bg-zinc-200 dark:focus-visible:ring-zinc-300 dark:focus-visible:ring-offset-zinc-950"
    >
      {children}
    </button>
  );
}

// Tier 2: Secondary Action Button (Subtle border, light fill, perfect for supporting actions)
export function SecondaryButton({ children, ...props }: React.ComponentProps<"button">) {
  return (
    <button
      {...props}
      className="inline-flex items-center justify-center rounded-lg border border-zinc-200 bg-white px-5 py-2.5 text-sm font-medium text-zinc-700 transition-all duration-200 hover:bg-zinc-50 hover:text-zinc-900 active:scale-[0.98] focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-zinc-950 focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 dark:border-zinc-800 dark:bg-zinc-900 dark:text-zinc-300 dark:hover:bg-zinc-800/80 dark:hover:text-zinc-50 dark:focus-visible:ring-zinc-300 dark:focus-visible:ring-offset-zinc-950"
    >
      {children}
    </button>
  );
}

// Tier 3: Tertiary Action Button (Borderless text, minimal clutter, excellent for Cancel/Back actions)
export function TertiaryButton({ children, ...props }: React.ComponentProps<"button">) {
  return (
    <button
      {...props}
      className="inline-flex items-center justify-center rounded-lg px-4 py-2.5 text-sm font-medium text-zinc-500 transition-all duration-200 hover:text-zinc-900 active:scale-[0.98] focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-zinc-950 focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 dark:text-zinc-400 dark:hover:text-zinc-50 dark:focus-visible:ring-zinc-300 dark:focus-visible:ring-offset-zinc-950"
    >
      {children}
    </button>
  );
}
```

### 5.B Ambient Tinted Shadows
Avoid dark, muddy, high-opacity black shadows. Instead, use soft, multi-layered, diffused shadows containing a microscopic tint of the background color to emulate natural light scattering:

*   **Extra-Soft Component Shadow:**
    `shadow-[0_8px_30px_rgba(0,0,0,0.015),0_1px_2px_rgba(0,0,0,0.01)]`
*   **Elevated Floating Surface (Cards/Grids):**
    `shadow-[0_20px_50px_rgba(0,0,0,0.03),0_1px_3px_rgba(0,0,0,0.02)]`
*   **Highly Elevated Overlays (Dropdowns/Modals):**
    `shadow-[0_32px_64px_-16px_rgba(0,0,0,0.08),0_1px_4px_rgba(0,0,0,0.02)]`
*   **Dark Mode Highlight Ring (Instead of Shadow):**
    Because shadows are invisible on pure dark backgrounds, rely on highly detailed inner highlights and low-opacity borders:
    `border border-zinc-800/80 shadow-[inset_0_1px_1px_rgba(255,255,255,0.03)]`

### 5.C Overlay Architecture (Modals & Tooltips)

Modals demand full user attention and require physical backdrop distortion. Tooltips require hovering safety zones and entry delay filters:

```tsx
"use client";
import { motion, AnimatePresence } from "motion/react";

// Modal Overlay: Restrained scale animation with a high-blur backdrop mask
export function ModalOverlay({ isOpen, onClose, children }: { isOpen: boolean; onClose: () => void; children: React.ReactNode }) {
  return (
    <AnimatePresence>
      {isOpen && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4">
          {/* Backdrop Mask */}
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            onClick={onClose}
            className="fixed inset-0 bg-black/40 backdrop-blur-sm"
          />

          {/* Elevated Modal Content (Note the Level 2 Dark Mode Elevation bg-zinc-850) */}
          <motion.div
            initial={{ opacity: 0, scale: 0.96, y: 8 }}
            animate={{ opacity: 1, scale: 1, y: 0 }}
            exit={{ opacity: 0, scale: 0.96, y: 8 }}
            transition={{ type: "spring", duration: 0.4, bounce: 0 }}
            className="relative z-10 w-full max-w-md overflow-hidden rounded-xl border border-zinc-200/80 bg-white p-6 shadow-[0_32px_64px_-16px_rgba(0,0,0,0.08)] dark:border-zinc-800/80 dark:bg-zinc-900"
          >
            {children}
          </motion.div>
        </div>
      )}
    </AnimatePresence>
  );
}

// Tooltip Overlay: Lightweight text hover with spring transition
export function Tooltip({ text, children }: { text: string; children: React.ReactNode }) {
  return (
    <div className="group relative inline-block">
      {children}
      <div className="pointer-events-none absolute bottom-full left-1/2 mb-2 w-max max-w-xs -translate-x-1/2 scale-95 opacity-0 transition-all duration-200 ease-[cubic-bezier(0.16,1,0.3,1)] group-hover:translate-y-0 group-hover:scale-100 group-hover:opacity-100">
        <div className="rounded bg-zinc-950 px-2.5 py-1.5 text-xs font-medium text-zinc-50 shadow-md dark:bg-zinc-50 dark:text-zinc-950">
          {text}
        </div>
      </div>
    </div>
  );
}
```
