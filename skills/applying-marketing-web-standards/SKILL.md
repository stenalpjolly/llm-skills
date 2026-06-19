---
name: applying-marketing-web-standards
description: >-
  Provides guidelines, visual specs, and accessibility rules for Google-branded marketing websites.
  Use when building or modifying web pages, landing pages, or components (such as buttons, forms, carousels, or chips)
  to ensure they conform to Google's layout, design, accessibility, and legal standards.
  Don't use for mobile native app development, generic backend service design, or premium creative visual styling (micro-animations, artistic designs)—use `designing-tasteful-frontends` for that.
---

# Applying Marketing Web Standards

Google Marketing Web Standards (MWS) ensure that all marketing sites, product landing pages, and microsites deliver a consistent, highly accessible, and performance-optimized experience representing Google's brand identity.

This skill provides step-by-step instructions and technical specs for applying these standards using precise component guidelines.

---

## 1. Core Principles & Workflow

When designing or implementing a Google marketing page or component, adhere to these fundamental principles:

*   **Helpful & Human**: Web experiences should feel helpful, honest, beautiful, and thoughtful. Avoid complicated jargon, intrusive overlays, or dark patterns.
*   **Simple & Focused**: Design with clarity. Minimize visual noise to help users achieve their goals quickly.
*   **Accessible by Default**: Design and develop with accessibility as a baseline, not an afterthought. Every user should have an equivalent experience.
*   **Performance-First**: Fast loading speeds and smooth interactions are essential to keeping users engaged and improving SEO rankings.

### 1.1 Development Workflow
1.  **Reference Component Specs**: Inspect the individual component references in the `references/` directory before writing code.
2.  **Verify Accessibility (a11y)**: Every component must meet WCAG 2.1 Level AA criteria, including keyboard focus management and screen reader support.
3.  **Adhere to Spacing Grid**: Align all layouts and dimensions to an 8px grid.
4.  **Enforce Typography and Case**: Use Google Sans for headings and Roboto for body text. All labels and CTA text must use sentence case.

---

## 2. Standard Components Library

Detailed specifications, HTML structures, and CSS styles for each of the 18 standardized page components are hosted in dedicated reference files:

### Fundamentals
*   **[Grid, Breakpoints, and Layout](references/layout.md)**: Rules for the 8px grid system, standard responsive screen breakpoints, margins, and HTML5 landmark regions.

### Standard Page Components
1.  **[Accordions](references/accordions.md)**: Expandable vertical item lists using standard WAI-ARIA states.
2.  **[Ambient Videos](references/ambient-videos.md)**: Silent, auto-playing background video loops, preloading, and prefers-reduced-motion accessibility rules.
3.  **[Banners](references/banners.md)**: Top horizontal notice strips with semantic color archetypes (Info, Success, Warning, Error) and dismiss actions.
4.  **[Breadcrumbs](references/breadcrumbs.md)**: Horizontal folder location trails with proper separators and active item tags.
5.  **[Buttons and Links](references/buttons-and-links.md)**: Rounded pill buttons, primary/secondary/tertiary hierarchies, and external hyperlink arrow indicators.
6.  **[Cards](references/cards.md)**: Content cards, borders, custom box shadow elevations (1-3), card lift animations, and full-card relative overlays.
7.  **[Carousels](references/carousels.md)**: Interactive slide carousels, dot indicators, auto-play interrupts, and keyboard slide triggers.
8.  **[Cookie Notification Bar](references/cookie-notification-bar.md)**: Fixed bottom cookie consent drawer with accept/reject CTAs and persistent storage consent.
9.  **[Filters](references/filters.md)**: Search filters, multi-select chips, active selection labels, and live region result announcements.
10. **[Forms](references/forms.md)**: Material Outlined text fields, checkboxes, radio buttons, helper text, and validation alert errors.
11. **[Header](references/header.md)**: Fixed top site header, utility actions, responsive search triggers, and sliding mobile menus.
12. **[Jump Links](references/jump-links.md)**: Local anchor links sidebar with smooth scrolling, active highlights, and keyboard focus shifting.
13. **[Overlays](references/overlays.md)**: Dialog popups, background backdrops, close buttons, escape dismissal, and focus trapping.
14. **[Share and Follow](references/share-and-follow.md)**: Monochrome social media sharing links and copy-to-clipboard state management.
15. **[Tables](references/tables.md)**: Row cell heights, left/right data alignments, responsive overflow, and th/scope column properties.
16. **[Tabs](references/tabs.md)**: Horizontal tab headers, active blue borders, hidden panel panels, and keyboard arrow key traversal.
17. **[Tooltips](references/tooltips.md)**: Bubble context tip overlays, pointer arrows, trigger thresholds, and focus-visible triggers.
18. **[Video Players](references/video-players.md)**: Inline player skins, play overlay buttons, custom timelines, and VTT subtitles/captions.

---

## 3. Layout, Grid, & Responsive Breakpoints

### 3.1 The 8dp Grid System
All layouts, components, margins, and padding must align to an **8px grid** (increments of 8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 96px, etc.).
*   **Micro-spacing**: 4px is allowed only for very tight, precise alignments (e.g., spacing between an icon and text or small labels).
*   **Component Heights**: Form inputs, buttons, and headers must have heights that are multiples of 8px.

### 3.2 Responsive Grid & Breakpoints
The standard layout employs a fluid grid system that adjusts columns, margins, and gutters based on screen width:

| Device Category | Breakpoint Range | Columns | Page Margin | Gutter Width | Max Content Width |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **Mobile** | Under `600px` | 4 | `16px` | `16px` | Fluid (100%) |
| **Tablet** | `600px` to `1023px` | 8 | `24px` | `24px` | Fluid (100%) |
| **Desktop** | `1024px` to `1439px` | 12 | `24px` or `48px` | `24px` | `1280px` (Centered) |
| **Large Desktop**| `1440px` and up | 12 | Fluid | `24px` or `32px` | `1280px` or `1440px` |

---

## 4. Typography & Typescale

### 4.1 Font Families
Google marketing sites must strictly use the following designated typefaces. Custom or third-party web fonts are prohibited unless explicitly approved by the Brand team.

*   **Google Sans (Headline Font)**: Used exclusively for display text, headings (`H1` to `H6`), large marketing copy, and prominent callouts. It is optimized for high-readability at large sizes. *Do not use Google Sans for body copy.*
*   **Roboto (Body/UI Font)**: The workhorse font for all body text, bullet lists, forms, helper text, dense UI components, table content, and small-to-medium button labels.
*   **Fallback Fonts**: For environments or initial load states before web fonts are fully rendered, use system-default sans-serif fallbacks:
    ```css
    font-family: 'Google Sans', Arial, sans-serif;
    font-family: 'Roboto', Arial, sans-serif;
    ```

### 4.2 Typescale Hierarchy (Desktop-Optimized)

| Role | Font Family | Weight | Size | Line Height | Case / Usage |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **Display 2** | Google Sans | Bold / Medium | `96px` | `104px` | Hero headings (marketing-heavy pages) |
| **Display 1** | Google Sans | Medium | `64px` | `72px` | Standard Hero headers |
| **Headline 1**| Google Sans | Medium | `44px` | `52px` | Primary section headings (`<h1>`) |
| **Headline 2**| Google Sans | Medium | `32px` | `40px` | Secondary section headings (`<h2>`) |
| **Headline 3**| Google Sans | Regular | `24px` | `32px` | Subsection titles (`<h3>`) |
| **Headline 4**| Google Sans | Regular | `20px` | `28px` | Small subsection headers (`<h4>`) |
| **Body 1** | Roboto | Regular | `16px` | `24px` | Primary paragraph text and body lists |
| **Body 2** | Roboto | Regular | `14px` | `20px` | Secondary text, forms, table metadata |
| **Caption** | Roboto | Regular | `12px` | `16px` | Footnotes, legal disclaimers, micro-labels |

### 4.3 Text Capitalization Rules
*   **Sentence Case**: Sentence case must be used for all headers, subheads, UI labels, and CTAs (e.g., "Get started", "Learn more", "Create your account").
*   **Title Case**: Avoid Title Case across the site unless citing a formal publication, product name, or legal entity.
*   **All Caps**: Strictly prohibited for headings or body paragraphs. It may only be used for short, 1-word uppercase tags (e.g., "NEW", "BETA") with a minimum letter-spacing of `0.5px` or `1px`.

---

## 5. Brand Color Palette & Contrast Requirements

### 5.1 Core Google Brand Colors
Google's primary brand identity relies on the four primary brand colors:

| Color | Hex Code | RGB | Key Applications |
| :--- | :--- | :---: | :--- |
| **Google Blue** | `#4285F4` | `66, 133, 244` | Primary brand presence, primary CTAs, links, active states |
| **Google Red** | `#EA4335` | `234, 67, 53` | Accent highlights, error states, system alerts |
| **Google Yellow**| `#FBBC05` | `251, 188, 5` | Accent highlights, warning/attention alerts |
| **Google Green** | `#34A853` | `52, 168, 83` | Accent highlights, success states, green-lit status |

### 5.2 Light Palette & Neutral Grays
Light backgrounds represent Google's signature "clean white space" aesthetic:

*   **Surface Base (White)**: `#FFFFFF`
*   **Surface Alt (Gray 50)**: `#F8F9FA` — Used for light-gray section strips or card backgrounds.
*   **Surface Alt 2 (Gray 100)**: `#F1F3F4` — Used for disabled fields or secondary section cards.
*   **Primary Text (Gray 900)**: `#202124` — Base color for headings and core readable paragraphs.
*   **Secondary Text (Gray 700)**: `#5F6368` — Used for supporting descriptions, subtitles, and captions.
*   **Helper / Disabled Text (Gray 600)**: `#80868B` — Used for helper instructions, placeholder text, and muted labels.
*   **Borders & Dividers (Gray 300)**: `#DADCE0` — Used for card outlines, button borders, and dividing lines.

### 5.3 Contrast & Accessibility (a11y) Rules
All text color pairings must satisfy **WCAG 2.1 Level AA** contrast standards:
*   **Regular text (<18pt or <24px normal weight)**: Must have a contrast ratio of at least **4.5:1** against the background.
*   **Large text (>=18pt or >=24px)**: Must have a contrast ratio of at least **3.0:1** against the background.
*   **UI Components & Icons**: Focus borders, input borders, and active icons must have a contrast ratio of at least **3.0:1** against surrounding backgrounds.

---

## 6. Branding & Logo Usage

### 6.1 Google Wordmark & Product Logos
*   **Header Logo**: Place the standard full-color Google wordmark or the official product lockup at the **top-left** of the primary navigation bar.
*   **Footer Logo**: Place the standard full-color Google wordmark at the **bottom-right** of the footer.
*   **Color Lock**: On light/white backgrounds, always use the standard multi-color logo. On dark or saturated solid color backgrounds, use the monochromatic **white-out** version.
*   **Aspect Ratio**: The logo must never be warped, squished, stretched, or recolored under any circumstances.

### 6.2 Clear Space & Size Constraints
*   **Clear Space**: Standard clear space must surround the logo on all sides, equal to at least **50% of the height of the capital "G"** in the wordmark.
*   **Minimum Dimensions**:
    *   Desktop: Logo height must be at least `24px`.
    *   Mobile: Logo height must be at least `20px`.

---

## 7. Accessibility (a11y) Requirements

Google marketing pages must target **WCAG 2.1 Level AA** compliance.

*   **Keyboard Navigation**: All interactive elements (links, buttons, forms, dropdowns, hamburger menu) must be focusable and fully operable using the keyboard alone (using `Tab`, `Enter`, `Space`, and `Arrow Keys`).
*   **Focus Management**: Focus must never be trapped in visual elements. For modals or drop-down drawers, trap keyboard focus *inside* the component while active and restore focus to the trigger on close.
*   **Alt Text for Images**: All decorative images must have an empty `alt=""` tag. All informative images must have descriptive, contextual alt attributes.
*   **Aria Roles & Attributes**: Use native HTML5 elements where possible. If custom elements are created, map appropriate ARIA attributes (e.g., `aria-expanded="false"`, `aria-haspopup="true"`, `role="dialog"`).
*   **Skip Navigation Link**: Include a visually hidden "Skip to main content" link as the very first keyboard-focusable item in the document (`href="#main-content"`).
*   **Document Language**: Ensure the `<html>` tag contains a valid `lang` attribute corresponding to the target locale (e.g., `<html lang="en">`).

---

## 8. Performance & Core Web Vitals

High-speed loading times are a core pillar of Google's search positioning and marketing efficiency. Websites must target a green Lighthouse score (**>= 90**) across all categories.

### 8.1 Core Web Vitals (Threshold Targets)
*   **Largest Contentful Paint (LCP)**: `< 2.5s` (measures loading performance).
*   **Interaction to Next Paint (INP)**: `< 200ms` (measures interface responsiveness).
*   **Cumulative Layout Shift (CLS)**: `< 0.1` (measures visual stability).

### 8.2 Optimization Directives
*   **Image Compression**: Compress all imagery. Serve modern formats (e.g., `WebP`, `AVIF`) with explicit `width` and `height` dimensions to prevent CLS.
*   **Lazy Loading**: Use native lazy loading for off-screen images (`loading="lazy"`) and deferred loading for non-critical JavaScript.
*   **CSS & JS Delivery**: Inline critical CSS. Minify and bundle assets. Avoid large external libraries unless essential.
*   **Font Preloading**: Preload the critical 'Google Sans' and 'Roboto' web fonts to prevent FOIT (Flash of Invisible Text) or FOUT (Flash of Unstyled Text):
    ```html
    <link rel="preload" href="/fonts/google-sans-bold.woff2" as="font" type="font/woff2" crossorigin>
    ```

---

## 9. Legal, Tracking, & Cookie Consent

*   **Cookie Consent**: A standard, compliant cookie banner must be visible to users in jurisdictions that require it (e.g., GDPR in the EU, CCPA in California) before any tracking or marketing cookies are written.
*   **Analytics Tracking**: All Google Analytics, Tag Manager, or tracking pixels must be initialized through the standard tag container *only after* receiving user cookie consent.
*   **Privacy & Terms Visibility**: Privacy Policy and Terms of Service links must be clearly accessible and legible inside the standard site footer.
