# Enterprise Design Systems & Real-World Implementations

This reference guide maps specific brand briefs and project requirements to **official design systems**. It also provides installation commands, canonical documentation links, and custom visual approximations.

---

## 1. Enterprise Design System Map

If a project brief aligns with one of the profiles below, you must install and use the **official** package. Do not reinvent their CSS by hand or mix systems.

| Brand Brief / Context | Recommended System | Installation Packages |
| :--- | :--- | :--- |
| **Microsoft / Enterprise SaaS** | Fluent UI (v9) | `@fluentui/react-components` |
| **Google-ish / Material 3 Product** | Material Web (M3) | `@material/web` |
| **IBM / Enterprise Analytics B2B** | IBM Carbon | `@carbon/react` + `@carbon/styles` |
| **Shopify Admin / E-commerce App** | Shopify Polaris | `polaris.js` or `@shopify/polaris` |
| **Atlassian / Jira-style Devtool** | Atlassian Design System | `@atlaskit/tokens` + `@atlaskit/button` etc. |
| **GitHub-style Developer Marketing** | Primer Brand | `@primer/react-brand` |
| **UK Government / Public Sector** | GOV.UK Frontend | `govuk-frontend` |
| **US Government / Trust-Critical** | USWDS | `uswds` |
| **Modern High-Accessibility React Shell** | Radix Themes | `@radix-ui/themes` |
| **Modern Tailwind SaaS** | shadcn/ui | `npx shadcn@latest init` |
| **Fast Local Business / Legacy MVP** | Bootstrap 5.3 | `bootstrap` |

---

## 2. Aesthetic Styles vs. Official Systems

For these visual styles, **there is no single official package**. You must build them using native CSS and Tailwind utility classes. Avoid claiming these are official systems in code comments:

*   **Glassmorphism (Frosted Glass):** Built using `backdrop-filter: blur()`, layered transparent borders, and highlight overlays. Provide solid fallbacks for `prefers-reduced-transparency`.
*   **Bento (Apple Grid):** Built using CSS Grid with mixed cell sizes and gapless rhythm.
*   **Industrial Brutalism:** Monospace fonts, sharp 90-degree corners, raw black borders, and micro-telemetry symbols.
*   **Apple Liquid Glass:** *Apple does not issue a web package for this.* It is an approximation built via CSS. (See Section 4 for the canonical web approximation skeleton).

---

## 3. Package Installation Registry

```bash
# Material Web Components
npm install @material/web

# Fluent UI React (v9)
npm install @fluentui/react-components

# IBM Carbon React
npm install @carbon/react @carbon/styles

# Radix Themes (Highly Accessible Primitives)
npm install @radix-ui/themes

# shadcn/ui Initialization
npx shadcn@latest init
npx shadcn@latest add button card badge separator input

# Primer Brand (GitHub-Style Marketing)
npm install @primer/react-brand

# GOV.UK Frontend
npm install govuk-frontend
```

---

## 4. Apple Liquid Glass: High-Fidelity Web Approximation

Use this custom CSS skeleton to approximate Apple's platform-level Liquid Glass material. It features layered border refractions, radial highlights, dark mode compatibility, and a `prefers-reduced-transparency` fallback:

```css
.liquid-glass-web-approx {
  position: relative;
  isolation: isolate;
  overflow: hidden;
  border-radius: 999px;
  border: 1px solid rgba(255, 255, 255, 0.32);
  background:
    linear-gradient(135deg, rgba(255, 255, 255, 0.30), rgba(255, 255, 255, 0.08)),
    rgba(255, 255, 255, 0.12);
  backdrop-filter: blur(24px) saturate(180%) contrast(1.05);
  -webkit-backdrop-filter: blur(24px) saturate(180%) contrast(1.05);
  box-shadow:
    inset 0 1px 0 rgba(255, 255, 255, 0.48),
    inset 0 -1px 0 rgba(255, 255, 255, 0.12),
    0 18px 60px rgba(0, 0, 0, 0.18);
}

.liquid-glass-web-approx::before {
  content: "";
  position: absolute;
  inset: 0;
  z-index: -1;
  border-radius: inherit;
  background:
    radial-gradient(circle at 20% 0%, rgba(255, 255, 255, 0.55), transparent 34%),
    linear-gradient(90deg, rgba(255, 255, 255, 0.18), transparent 42%, rgba(255, 255, 255, 0.14));
  pointer-events: none;
}

.liquid-glass-web-approx::after {
  content: "";
  position: absolute;
  inset: 1px;
  border-radius: inherit;
  border: 1px solid rgba(255, 255, 255, 0.14);
  pointer-events: none;
}

/* Dark Mode Calibration */
@media (prefers-color-scheme: dark) {
  .liquid-glass-web-approx {
    border-color: rgba(255, 255, 255, 0.18);
    background:
      linear-gradient(135deg, rgba(255, 255, 255, 0.16), rgba(255, 255, 255, 0.04)),
      rgba(15, 23, 42, 0.42);
    box-shadow:
      inset 0 1px 0 rgba(255, 255, 255, 0.22),
      0 18px 60px rgba(0, 0, 0, 0.42);
  }
}

/* Accessibility Fallback */
@media (prefers-reduced-transparency: reduce) {
  .liquid-glass-web-approx {
    background: #ffffff;
    backdrop-filter: none;
    -webkit-backdrop-filter: none;
    border-color: #eaeaea;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
  }
  @media (prefers-color-scheme: dark) {
    .liquid-glass-web-approx {
      background: #18181b;
      border-color: #27272a;
    }
  }
}
```
Ensure that container contrast remains high enough for readability even when transparency or blurs are disabled by system preferences.
