# AI Tells & Redesign Protocols (Forbidden Patterns)

This reference document catalogs the visual, structural, and content-level signatures that identify a website as "AI-generated" or "templated" (the **AI Tells**). It also defines the strict protocols to follow when modernizing an existing codebase.

---

## 1. Banned Visual & CSS Patterns
*   **No neon / outer glows:** Avoid automatic glowing buttons, glowing cards, or purple/blue radial light mesh gradients behind text by default. Use 1px inner borders or soft, tinted shadows instead.
*   **No pure black (`#000000`):** Use off-black, zinc-950, or dark charcoal. Pure black destroys depth.
*   **No oversaturated accents:** Saturation for accents must remain under 80% to blend naturally with neutral tones.
*   **No excessive gradient text:** Avoid massive headlines colored with horizontal/diagonal gradients.
*   **No custom mouse cursors:** Banned due to poor performance and negative accessibility impact.

---

## 2. Banned Typography & Content Patterns
*   **No Inter as default:** Avoid defaulting to standard `Inter` or system sans-serifs for premium, high-end briefs. Refer to `SKILL.md` for premium alternatives.
*   **No oversized H1s:** Do not let headlines scream. Control hierarchy through weights, colors, and line-heights rather than raw font size.
*   **No generic serifs:** Standard serif fonts (Times New Roman, Georgia, Garamond) are banned. Use distinctive modern serifs (Recoleta, Cormorant, Editorial New) only when brand-appropriate, and never in product dashboards.
*   **No generic placeholder names:** Avoid "John Doe", "Jane Smith", "Sarah Chan". Use realistic, context-appropriate names.
*   **No generic mock brands:** Avoid "Acme", "Nexus", "SmartFlow", "Cloudly".
*   **No AI copywriting cliches:** Never use *"Elevate", "Seamless", "Unleash", "Next-Gen", "Revolutionize", "Delve", "Tapestry"*. Use direct, active voice.
*   **No fake-perfect numbers:** Avoid `99.99%`, `50%`, `1234567`. Use organic, messy data (`47.2%`, `13.4 lb`, `4.1x`).

---

## 3. Banned Layout & Rhythm Patterns
*   **No 3-column equal feature cards:** The generic "three identical cards in a row" layout is banned. Break the rhythm with a 2-column zig-zag, asymmetric grid, or horizontal scroll snap.
*   **No box-in-box UIs:** Avoid giant rounded section containers wrapping cards that contain more cards. Use negative space, borders (`border-t`), and dividers to establish hierarchy.
*   **No version labels in heroes:** Avoid `v0.6`, `BETA`, or `EARLY ACCESS` as hero eyebrows unless the brief is explicitly about a product launch.
*   **No section-number eyebrows:** Avoid `01 / INDEX`, `002 · Capabilities`. Eyebrows must name the topic, not enumerate.
*   **No decorative status dots:** Avoid placing colored dots before nav links or list items unless they represent active, real-time status.
*   **No scroll cues:** Banned. Do not write "Scroll to explore" or draw animated mouse icons at the viewport bottom.

---

## 4. The Em-Dash Ban (Critical & Non-Negotiable)

**The em-dash (`—`) and en-dash (`–`) are completely banned from all visible copy.** This is the single most common AI stylistic Tell.

*   **Banned in headlines & eyebrows:** Replace with periods, commas, or line breaks.
*   **Banned in body copy:** Restructure the sentence. Divide into two sentences with a period, or use commas, colons, or parentheses.
*   **Banned in quote attributions:** Use a normal hyphen (` - `) or a line break + smaller font weight.
*   **Banned as numeric ranges:** Date and price ranges (`2018-2026`, `$40-80k`) must use a standard hyphen (`-`).

The ONLY permitted dash characters on the page are the regular hyphen (`-`) and the mathematical minus sign. If a single `—` or `–` is found, the output fails pre-flight.

---

## 5. Redesign & Preservation Protocols

When modernizing an existing project, you must classify the task into one of three modes:
1.  **Greenfield:** Full visual build from scratch.
2.  **Redesign - Preserve:** Modernize visuals without breaking the brand. Evolve gradually.
3.  **Redesign - Overhaul:** Apply a brand-new visual language while strictly preserving content and IA.

### 5.A What Never Changes Silently
Do not modify the following without explicit user approval:
*   URL structures, route slugs, or anchor IDs (prevents SEO catastrophic failure).
*   Primary navigation labels and layouts.
*   Form field names, structures, or order (prevents breaking autocomplete and analytics).
*   Original brand logos, wordmarks, or legal copy.
*   Downstream tracking IDs and analytics event hooks.

### 5.B Modernization Levers (Priority Order)
Apply upgrades in this sequence. Stop as soon as the design goals are met:
1.  **Typography refresh:** Biggest visual lift with zero functional risk.
2.  **Spacing & rhythm:** Increase section padding and correct vertical rhythm. Un-cramp elements.
3.  **Color recalibration:** Desaturate, unify neutral grays (no mixing warm and cool grays), lock the brand accent.
4.  **Motion layer:** Add subtle micro-interactions to buttons, cards, and nav items.
5.  **Hero & key-section recomposition:** Restructure above-the-fold using asymmetric layouts.
6.  **Full block replacement:** Only when the existing block is completely unsalvageable.
