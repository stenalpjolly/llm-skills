# Jump Links Guidelines

This reference defines the visual requirements, smooth scroll interactions, highlight updates, and accessibility regulations for Jump Links on Google-branded marketing websites.

---

## 1. Visual & Placement Standards

Jump Links (also called Anchor Menus or Table of Contents) are sticky horizontal or vertical bars of local anchor links that jump the user directly to specific headings of a long-form page.

*   **Location**: Either as a sticky left sidebar vertical menu (on desktop) or as a sticky sub-header horizontal strip (directly below the primary site header).
*   **Typography**: `Roboto Medium, 14px, #5F6368` (Gray 700). Active section has bold `Google Blue (#1A73E8)` text with a left/bottom blue accent border (`2px`).
*   **Casing**: **Sentence Case** is mandatory.

---

## 2. Interactive Behavior & Scroll Specs

*   **Smooth Scrolling**: Scroll to the anchor target heading smoothly when clicked.
*   **Active Indicator Highlight**: As the user scrolls through the page, the jump-link corresponding to the visible section must automatically highlight.
*   **Offset**: The scroll target position must offset the header's height (typically `64px` or `80px`) using CSS `scroll-margin-top` to prevent the sticky header from blocking target headings.

---

## 3. HTML and CSS Structure

```html
<nav class="g-jump-links" aria-label="Page Sections">
  <ul class="g-jump-list">
    <li><a href="#section-specs" class="g-jump-link active">Specifications</a></li>
    <li><a href="#section-design" class="g-jump-link">Design features</a></li>
    <li><a href="#section-pricing" class="g-jump-link">Pricing plans</a></li>
  </ul>
</nav>

<!-- Page targets with offset -->
<section id="section-specs" class="g-page-section">
  <h2 tabindex="-1">Specifications</h2>
  <p>Detailed overview of product specifications...</p>
</section>
```

```css
.g-jump-links {
  position: sticky;
  top: 64px; /* Directly below sticky header */
  background-color: #FFFFFF;
  border-bottom: 1px solid #DADCE0;
  z-index: 90;
  font-family: 'Roboto', Arial, sans-serif;
}
.g-jump-list {
  display: flex;
  list-style: none;
  padding: 0;
  margin: 0;
  max-width: 1280px;
  margin: 0 auto;
  gap: 24px;
}
.g-jump-link {
  display: block;
  padding: 16px 0;
  font-size: 14px;
  font-weight: 500;
  color: #5F6368;
  text-decoration: none;
  border-bottom: 2px solid transparent;
  transition: all 0.15s ease;
}
.g-jump-link:hover {
  color: #202124;
}
.g-jump-link.active {
  color: #1A73E8;
  border-bottom-color: #1A73E8;
}

/* Offset Target Scroll-Margin-Top (Mandatory) */
.g-page-section h2 {
  scroll-margin-top: 130px; /* offset sticky header height + jump links bar height */
}
```

---

## 4. Accessibility Checklist

*   **Shift Keyboard Focus**: A common accessibility bug is jumping visual viewports without shifting the browser's keyboard focus.
    *   Set `tabindex="-1"` on target heading elements.
    *   Using JavaScript, move focus onto the target heading element (`heading.focus()`) upon clicking a jump link.
*   **Aria Navigation Landmark**: Wrap the jump link list inside `<nav aria-label="Page Sections">`.
*   **Skip Option Compatibility**: Ensure the Jump Links bar resides directly after the Skip to main content link in the focus ordering.
*   **Reduced Motion**: Respect system motion cuts by turning off smooth scrolling behavior (`html { scroll-behavior: smooth; }`) inside `@media (prefers-reduced-motion: reduce)`.
