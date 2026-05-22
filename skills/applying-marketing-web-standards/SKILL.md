---
name: applying-marketing-web-standards
description: >-
  Provides guidelines, visual specs, and accessibility rules for Google-branded marketing websites.
  Use when building or modifying web pages, landing pages, or components (such as buttons, forms, carousels, or chips)
  to ensure they conform to Google's layout, design, accessibility, and legal standards.
  Don't use for mobile native app development or generic backend service design.
---

# Applying Marketing Web Standards

Google Marketing Web Standards (MWS) ensure that all marketing sites, product landing pages, and microsites deliver a consistent, highly accessible, and performance-optimized experience representing Google's brand identity.

This skill provides step-by-step instructions and technical specs for applying these standards using precise component guidelines.

## 1. Core Principles & Workflow

When designing or implementing a Google marketing page or component, follow this workflow:
1.  **Reference Component Specs**: Inspect the individual component references in the `references/` directory before writing code.
2.  **Verify Accessibility (a11y)**: Every component must meet WCAG 2.1 Level AA criteria, including keyboard focus management and screen reader support.
3.  **Adhere to Spacing Grid**: Align all layouts and dimensions to an 8px grid.
4.  **Enforce Typography and Case**: Use Google Sans for headings and Roboto for body text. All labels and CTA text must use sentence case.

---

## 2. Standard Components Library

Detailed specifications, HTML structures, and CSS styles for each of the 18 standardized page components, along with fundamental layouts, are hosted in dedicated reference files:

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

## 3. Global Styling Guidelines

### 3.1 Core Brand Colors
All components must only use colors from Google's official brand palette:
*   **Google Blue**: `#4285F4` (Primary focus, active buttons, links)
*   **Google Red**: `#EA4335` (Accent highlights, error validation states)
*   **Google Yellow**: `#FBBC05` (Accent highlights, warnings)
*   **Google Green**: `#34A853` (Success indicators, positive notifications)
*   **Neutral Text**: `#202124` (Primary copy), `#5F6368` (Secondary supporting copy)
*   **Neutral Borders**: `#DADCE0` (Default borders)

### 3.2 Typography Rules
*   **Headlines & Display**: Use `'Google Sans', Arial, sans-serif` in Bold/Medium.
*   **Body, Form Labels, Dense UI**: Use `'Roboto', Arial, sans-serif` in Regular/Medium.
*   **Sentence Case Rule**: Never use Title Case or Uppercase for headings, menus, buttons, or checkboxes. All texts must be in sentence case (e.g., "Receive newsletter updates", "Select all").
