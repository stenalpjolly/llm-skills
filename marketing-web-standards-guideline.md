# Google Marketing Web Standards (MWS) Design & Development Guideline

This document defines the core design, accessibility, performance, and legal compliance standards for building and maintaining Google-branded marketing websites. Adhering to these guidelines ensures a consistent, accessible, high-performance, and secure user experience across all Google web properties.

---

## 1. Core Principles
*   **Helpful & Human**: Web experiences should feel helpful, honest, beautiful, and thoughtful. Avoid complicated jargon, intrusive overlays, or dark patterns.
*   **Simple & Focused**: Design with clarity. Minimize visual noise to help users achieve their goals quickly.
*   **Accessible by Default**: Design and develop with accessibility as a baseline, not an afterthought. Every user should have an equivalent experience.
*   **Performance-First**: Fast loading speeds and smooth interactions are essential to keeping users engaged and improving SEO rankings.

---

## 2. Layout, Grid, & Responsive Breakpoints

### 2.1 The 8dp Grid System
All layouts, components, margins, and padding must align to an **8px grid** (increments of 8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 96px, etc.).
*   **Micro-spacing**: 4px is allowed only for very tight, precise alignments (e.g., spacing between an icon and text or small labels).
*   **Component Heights**: Form inputs, buttons, and headers must have heights that are multiples of 8px.

### 2.2 Responsive Grid & Breakpoints
The standard layout employs a fluid grid system that adjusts columns, margins, and gutters based on screen width:

| Device Category | Breakpoint Range | Columns | Page Margin | Gutter Width | Max Content Width |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **Mobile** | Under `600px` | 4 | `16px` | `16px` | Fluid (100%) |
| **Tablet** | `600px` to `1023px` | 8 | `24px` | `24px` | Fluid (100%) |
| **Desktop** | `1024px` to `1439px` | 12 | `24px` or `48px` | `24px` | `1280px` (Centered) |
| **Large Desktop**| `1440px` and up | 12 | Fluid | `24px` or `32px` | `1280px` or `1440px` |

---

## 3. Typography & Typescale

### 3.1 Font Families
Google marketing sites must strictly use the following designated typefaces. Custom or third-party web fonts are prohibited unless explicitly approved by the Brand team.

*   **Google Sans (Headline Font)**: Used exclusively for display text, headings (`H1` to `H6`), large marketing copy, and prominent callouts. It is optimized for high-readability at large sizes. *Do not use Google Sans for body copy.*
*   **Roboto (Body/UI Font)**: The workhorse font for all body text, bullet lists, forms, helper text, dense UI components, table content, and small-to-medium button labels.
*   **Fallback Fonts**: For environments or initial load states before web fonts are fully rendered, use system-default sans-serif fallbacks:
    ```css
    font-family: 'Google Sans', Arial, sans-serif;
    font-family: 'Roboto', Arial, sans-serif;
    ```

### 3.2 Typescale Hierarchy (Desktop-Optimized)

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

### 3.3 Text capitalization Rules
*   **Sentence Case**: Sentence case must be used for all headers, subheads, UI labels, and CTAs (e.g., "Get started", "Learn more", "Create your account").
*   **Title Case**: Avoid Title Case across the site unless citing a formal publication, product name, or legal entity.
*   **All Caps**: Strictly prohibited for headings or body paragraphs. It may only be used for short, 1-word uppercase tags (e.g., "NEW", "BETA") with a minimum letter-spacing of `0.5px` or `1px`.

---

## 4. Brand Color Palette & Contrast Requirements

### 4.1 Core Google Brand Colors
Google's primary brand identity relies on the four primary brand colors:

| Color | Hex Code | RGB | Key Applications |
| :--- | :--- | :---: | :--- |
| **Google Blue** | `#4285F4` | `66, 133, 244` | Primary brand presence, primary CTAs, links, active states |
| **Google Red** | `#EA4335` | `234, 67, 53` | Accent highlights, error states, system alerts |
| **Google Yellow**| `#FBBC05` | `251, 188, 5` | Accent highlights, warning/attention alerts |
| **Google Green** | `#34A853` | `52, 168, 83` | Accent highlights, success states, green-lit status |

### 4.2 Light Palette & Neutral Grays
Light backgrounds represent Google's signature "clean white space" aesthetic:

*   **Surface Base (White)**: `#FFFFFF`
*   **Surface Alt (Gray 50)**: `#F8F9FA` — Used for light-gray section strips or card backgrounds.
*   **Surface Alt 2 (Gray 100)**: `#F1F3F4` — Used for disabled fields or secondary section cards.
*   **Primary Text (Gray 900)**: `#202124` — Base color for headings and core readable paragraphs.
*   **Secondary Text (Gray 700)**: `#5F6368` — Used for supporting descriptions, subtitles, and captions.
*   **Helper / Disabled Text (Gray 600)**: `#80868B` — Used for helper instructions, placeholder text, and muted labels.
*   **Borders & Dividers (Gray 300)**: `#DADCE0` — Used for card outlines, button borders, and dividing lines.

### 4.3 Contrast & Accessibility (a11y) Rules
All text color pairings must satisfy **WCAG 2.1 Level AA** contrast standards:
*   **Regular text (<18pt or <24px normal weight)**: Must have a contrast ratio of at least **4.5:1** against the background.
*   **Large text (>=18pt or >=24px)**: Must have a contrast ratio of at least **3.0:1** against the background.
*   **UI Components & Icons**: Focus borders, input borders, and active icons must have a contrast ratio of at least **3.0:1** against surrounding backgrounds.

---

## 5. Branding & Logo Usage

### 5.1 Google Wordmark & Product Logos
*   **Header Logo**: Place the standard full-color Google wordmark or the official product lockup at the **top-left** of the primary navigation bar.
*   **Footer Logo**: Place the standard full-color Google wordmark at the **bottom-right** of the footer.
*   **Color Lock**: On light/white backgrounds, always use the standard multi-color logo. On dark or saturated solid color backgrounds, use the monochromatic **white-out** version.
*   **Aspect Ratio**: The logo must never be warped, squished, stretched, or recolored under any circumstances.

### 5.2 Clear Space & Size Constraints
*   **Clear Space**: Standard clear space must surround the logo on all sides, equal to at least **50% of the height of the capital "G"** in the wordmark.
*   **Minimum Dimensions**:
    *   Desktop: Logo height must be at least `24px`.
    *   Mobile: Logo height must be at least `20px`.

---

## 6. Core UI Component Guidelines

### 6.1 Header & Navigation Bar
*   **Dimensions**: Height of the primary header must be `64px` on mobile/tablet and `64px` to `80px` on desktop.
*   **Position**: Stickily or fixed at the top of the viewport (`position: sticky; top: 0; z-index: 1000;`) with a subtle bottom shadow or border (`1px solid #DADCE0`) on scroll.
*   **Desktop Layout**: Left-aligned Google Logo, followed by left-aligned/centered navigation links (up to 5 links max), followed by right-aligned Utility Actions (Search, Sign In, and a primary CTA button).
*   **Mobile Layout**: Left-aligned Google Logo, right-aligned hamburger menu trigger, and a primary CTA button if space allows. Hamburger menu must open a clean full-screen or side slide drawer.

### 6.2 Footer
Every marketing web page must feature a standardized footer matching GWS requirements:
*   **Top Footer Tier**: Primary sitemap links arranged in multi-column vertical lists (e.g., About, Products, Careers, Support).
*   **Bottom Footer Tier**:
    *   Left-aligned links: Privacy Policy, Terms of Service, About Google, Google Products.
    *   Language/Locale Selector dropdown (with globe icon).
    *   Right-aligned: Google Wordmark and "© [Current Year] Google".
*   **Style**: Dark text (`#5F6368`) on gray surface (`#F8F9FA` or `#F1F3F4`).

### 6.3 Buttons & Calls to Action (CTAs)
Google marketing websites employ pill-shaped or rounded-corner CTAs to direct user actions.

*   **Pill Button (Recommended)**: Fully rounded edges (`border-radius: 24px;` or higher, depending on button height).
*   **Standard Button**: Alternatively, a rounded rectangle with `border-radius: 4px;` is allowed for specific enterprise product alignments.
*   **Button Hierarchy**:
    1.  **Primary Button (Solid)**: Background `Google Blue (#4285F4)` with white text. Hover state: darken background to `#1A73E8`. Focus state: outline ring of `2px` around the button with a `2px` white spacer.
    2.  **Secondary Button (Outlined)**: Outlined border `1px solid #DADCE0` (Gray 300) with blue text `#4285F4`. Hover state: background transitions to `#F8F9FA`.
    3.  **Tertiary Button (Text/Link)**: Plain text `#4285F4` with no border or background. Hover state: underline text.
*   **Case Rule**: All button text must be in **sentence case** (e.g., "Start free trial", "Learn more").

### 6.4 Cards & Containers
*   **Rounding**: Cards must have rounded corners with a `border-radius` of either `8px` or `16px`. Choose one and apply consistently.
*   **Borders vs. Shadows**: Use flat, outlined borders (`1px solid #DADCE0`) on a clean white background. For layered layouts, a light, soft shadow (elevation 1 in Material Design) is permitted:
    ```css
    box-shadow: 0 1px 2px 0 rgba(60,64,67,0.3), 0 1px 3px 1px rgba(60,64,67,0.15);
    ```
*   **Hover States**: Elevate the card slightly on hover by scaling (`transform: translateY(-2px);`) or increasing shadow depth.

### 6.5 Forms & Text Inputs
*   **Input Box Style**: Outlined borders with `border-radius: 4px;` and minimum height of `48px`.
*   **Interactive States**:
    *   Default border: `1px solid #DADCE0`
    *   Hover border: `1px solid #80868B`
    *   Focus border: `2px solid #4285F4`
*   **Placeholders**: Placeholders must be in `Gray 600 (#80868B)` and must disappear when the user starts typing.
*   **Focus Ring**: Under no circumstances should the default outline be hidden using `outline: none;` without providing a custom CSS focus indicator (minimum `2px` solid `#4285F4` with high contrast).

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
