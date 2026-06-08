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
