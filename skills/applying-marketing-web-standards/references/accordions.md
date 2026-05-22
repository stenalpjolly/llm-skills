# Accordions Guidelines

This reference defines the visual specs, interactive behaviors, and accessibility standards for Accordions on Google-branded marketing websites.

---

## 1. Visual Specifications

Accordions consist of vertically stacked headers that expand to reveal or collapse nested content panels, conserving vertical space.

| Attribute | Specification | Notes |
| :--- | :--- | :--- |
| **Header Height** | `48px` to `64px` | Aligned with standard vertical margins |
| **Borders** | `1px solid #DADCE0` (Gray 300) | Bottom or surrounding border |
| **Header Typography**| `Google Sans Medium`, `16px` or `18px` | Sentence case is mandatory |
| **Expansion Icon** | Down Chevron icon, `24px` size | Rotates 180deg when expanded |
| **Interactive Transition**| `200ms` slide ease | Smooth opening/closing animations |

---

## 2. Interactive States & Color Palette
*   **Header Default**: Background transparent, text `#202124` (Gray 900), chevron `#5F6368` (Gray 700).
*   **Header Hover**: Background `#F8F9FA` (Gray 50).
*   **Header Focus**: 2px outline focus ring `#4285F4`.
*   **Header Expanded**: Text `#1A73E8` (Google Blue), chevron rotates 180 degrees and turns `#1A73E8`.

---

## 3. HTML and CSS Structure

```html
<div class="g-accordion">
  <!-- Accordion Item 1 -->
  <div class="g-accordion-item">
    <button class="g-accordion-header" aria-expanded="false" aria-controls="panel-1" id="header-1">
      What is included in the Pixel 8 Pro storage options?
      <svg class="g-accordion-chevron" width="24" height="24" viewBox="0 0 24 24"><path d="M7.41 8.59L12 13.17l4.59-4.58L18 10l-6 6-6-6 1.41-1.41z"/></svg>
    </button>
    <div class="g-accordion-panel" id="panel-1" role="region" aria-labelledby="header-1" hidden>
      <div class="g-accordion-content">
        <p>Pixel 8 Pro offers storage options ranging from 128GB up to 1TB, ensuring ample room for photos, videos, and applications.</p>
      </div>
    </div>
  </div>
</div>
```

```css
.g-accordion {
  border-top: 1px solid #DADCE0;
}
.g-accordion-item {
  border-bottom: 1px solid #DADCE0;
}
.g-accordion-header {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 16px 24px;
  background: none;
  border: none;
  cursor: pointer;
  font-family: 'Google Sans', Arial, sans-serif;
  font-size: 16px;
  font-weight: 500;
  text-align: left;
  color: #202124;
  transition: background-color 0.15s, color 0.15s;
}
.g-accordion-header:hover {
  background-color: #F8F9FA;
}
.g-accordion-header:focus-visible {
  outline: 2px solid #4285F4;
  outline-offset: -2px;
}
.g-accordion-chevron {
  fill: #5F6368;
  transition: transform 0.2s cubic-bezier(0, 0, 0.2, 1);
}
.g-accordion-header[aria-expanded="true"] {
  color: #1A73E8;
}
.g-accordion-header[aria-expanded="true"] .g-accordion-chevron {
  transform: rotate(180deg);
  fill: #1A73E8;
}

/* Panel Content transitions */
.g-accordion-panel {
  display: block; /* Overruled by 'hidden' attribute */
  overflow: hidden;
}
.g-accordion-panel[hidden] {
  display: none;
}
.g-accordion-content {
  padding: 0 24px 24px 24px;
  font-family: 'Roboto', Arial, sans-serif;
  font-size: 14px;
  line-height: 20px;
  color: #5F6368;
}
```

---

## 4. Accessibility Checklist

*   **Keyboard Control**:
    *   Focus elements using `Tab`.
    *   Toggle panels open/closed using `Space` or `Enter`.
*   **WAI-ARIA Pattern**:
    *   The expansion toggle must be a native `<button>`.
    *   The button must carry `aria-expanded="true"` when expanded, and `"false"` when collapsed.
    *   The button must carry `aria-controls` referencing the unique `id` of the panel content div.
    *   The panel content div must have `role="region"` and `aria-labelledby` referencing the button header `id`.
*   **Aria Hidden Panel**: When collapsed, apply the HTML `hidden` attribute or `display: none` to panels to prevent focus leakage and screen reader indexing.
