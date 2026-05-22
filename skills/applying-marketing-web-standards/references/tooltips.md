# Tooltips Guidelines

This reference defines the visual specs, bubble positioning, timing thresholds, hover/focus interactions, and accessibility rules for Tooltips on Google-branded marketing websites.

---

## 1. Visual & Structural Standards

Tooltips are small contextual bubble popups that appear upon hover or keyboard focus, providing helpful micro-descriptions or tips about page elements.

*   **Size**: Compact (width limit `200px` to `280px`).
*   **Background**: Solid Dark Gray `#202124` (Gray 900).
*   **Text Color**: White `#FFFFFF`.
*   **Typography**: `Roboto Regular, 12px, line-height 16px`.
*   **Shadow**: Uses Elevation 2 (Subtle floating shadow) to float over surrounding content.
*   **Corner Rounding**: `4px` border-radius.
*   **Bubble Pointer**: Features a small centered triangle arrow (`6px` height) pointing towards the trigger element.

---

## 2. Interactive Triggering Specs

*   **Hover**: Tooltips must trigger instantly (or with a subtle delay of `150ms`) when the mouse hovers over the trigger element. They must dismiss instantly when the mouse leaves.
*   **Keyboard Focus**: Tooltips must trigger automatically as soon as the trigger element receives keyboard focus (`focus` event). Dismisses on focus loss (`blur`).
*   **Escape dismiss**: Pressing the `Escape` key must dismiss tooltips immediately.

---

## 3. HTML and CSS Structure

```html
<div class="g-tooltip-wrapper">
  <!-- Trigger Element (Must be focusable) -->
  <button class="g-tooltip-trigger" aria-describedby="tooltip-desc-storage" id="btn-storage">
    Storage capacities
  </button>
  
  <!-- Tooltip bubble container -->
  <div class="g-tooltip" role="tooltip" id="tooltip-desc-storage" aria-hidden="true">
    This represents total available storage space. Formatted system data occupies approximately 10GB.
    <span class="g-tooltip-arrow"></span>
  </div>
</div>
```

```css
.g-tooltip-wrapper {
  position: relative;
  display: inline-block;
  font-family: 'Roboto', Arial, sans-serif;
}
.g-tooltip-trigger {
  background: none;
  border: none;
  border-bottom: 1px dashed #5F6368;
  color: #202124;
  font-size: 14px;
  font-weight: 500;
  cursor: help;
  padding: 0;
}
.g-tooltip-trigger:focus-visible {
  outline: 2px solid #4285F4;
}

/* Tooltip bubble hidden by default */
.g-tooltip {
  position: absolute;
  bottom: 130%;
  left: 50%;
  transform: translateX(-50%) scale(0.95);
  width: 240px;
  background-color: #202124;
  color: #FFFFFF;
  padding: 8px 12px;
  border-radius: 4px;
  font-size: 12px;
  line-height: 16px;
  box-shadow: 0 2px 6px 2px rgba(60, 64, 67, 0.15);
  pointer-events: none;
  opacity: 0;
  z-index: 1000;
  transition: opacity 0.15s ease, transform 0.15s ease;
}

/* Arrow pointer */
.g-tooltip-arrow {
  position: absolute;
  top: 100%;
  left: 50%;
  transform: translateX(-50%);
  border-width: 6px;
  border-style: solid;
  border-color: #202124 transparent transparent transparent;
}

/* Show Tooltip on Hover or Focus classes */
.g-tooltip-wrapper:hover .g-tooltip,
.g-tooltip-trigger:focus ~ .g-tooltip {
  opacity: 1;
  transform: translateX(-50%) scale(1);
  pointer-events: auto;
}
```

---

## 4. Accessibility Checklist

*   **Keyboard Focusable Trigger**: Ensure tooltips can *only* be triggered from focusable elements (e.g. `<button>`, `<a>`, `<input>`). Never attach tooltips to plain text labels (like `<span>` or `<div>`) that keyboard users cannot access.
*   **Aria Describedby Linking**: The trigger must carry `aria-describedby` referencing the unique `id` of the tooltip container so screen readers read out the tooltip description as soon as the trigger is focused.
*   **Role Tooltip**: Set `role="tooltip"` on the bubble container.
*   **Visibility Control**: Sync `aria-hidden="true"` dynamically on the tooltip container depending on active visibility states to keep screen reader updates accurate.
*   **Hover Persistence**: Users must be able to move their mouse pointer directly over the tooltip box itself without it disappearing immediately, allowing users with zoomed screens to read content.
*   **Responsive Collisions**: Ensure bubble positions adjust dynamically or offset bounds to prevent the tooltip from being clipped at viewport edges.
