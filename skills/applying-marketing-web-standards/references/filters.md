# Filters Guidelines

This reference defines the visual specs, interactive states, and accessibility standards for Filters and Chips on Google-branded marketing websites.

---

## 1. Interaction and Visual Standards

Filters allow users to narrow down products, case studies, or search results by toggling specific attributes. They primarily use **Chips** as the standard UI selector.

| Attribute | Specification | Notes |
| :--- | :--- | :--- |
| **Height (Chips)** | `32px` (Standard) or `28px` (Dense layout) | Includes vertical padding |
| **Corner Radius** | `16px` or `14px` (fully rounded pill-shape) | Half of the vertical height |
| **Horizontal Padding**| `12px` (without icon) or `8px` (with leading icon) | Buffer to the boundary margins |
| **Typography** | `Roboto Medium`, `14px` | Sentence case is mandatory |

---

## 2. Chip Filtering Styles

*   **Filter Chips (Multi-Select)**: Used to toggle filters. Multiple filters in a group can be active.
    *   **Unselected State**: Border `1px solid #DADCE0` (Gray 300), background `#FFFFFF`, text `#3C4043` (Gray 800).
    *   **Selected State**: Border `1px solid #1A73E8` (Blue 700), background `#E8F0FE` (Blue 50), text `#1A73E8` (Blue 700), with a leading checkmark icon (`18px`).
*   **Choice Chips (Single-Select)**: Used to select one option from a mutually exclusive list (e.g. sorting direction).
*   **Input Chips (Removable)**: Displayed above results as selected filter tags, allowing rapid deletion using a trailing close ("x") icon.

---

## 3. HTML and CSS Structure

```html
<!-- Multi-Select Filter Chip -->
<button class="g-chip g-chip-filter" aria-pressed="true">
  <svg class="g-chip-icon check" width="18" height="18" viewBox="0 0 24 24"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/></svg>
  <span class="g-chip-text">Pixel phones</span>
</button>

<!-- Removable Active Filter Tag -->
<div class="g-chip g-chip-tag" id="filter-tag-pixel">
  <span class="g-chip-text">Pixel 8 Pro</span>
  <button class="g-chip-close-btn" aria-label="Remove filter: Pixel 8 Pro" aria-controls="filter-tag-pixel">
    <svg width="18" height="18" viewBox="0 0 24 24"><path d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z"/></svg>
  </button>
</div>
```

```css
.g-chip {
  display: inline-flex;
  align-items: center;
  height: 32px;
  border-radius: 16px;
  padding: 0 12px;
  box-sizing: border-box;
  font-family: 'Roboto', Arial, sans-serif;
  font-size: 14px;
  font-weight: 500;
  color: #3C4043;
  background-color: #FFFFFF;
  border: 1px solid #DADCE0;
  cursor: pointer;
  transition: all 0.15s cubic-bezier(0.4, 0, 0.2, 1);
}
.g-chip:hover {
  background-color: #F8F9FA;
  border-color: #80868B;
}
.g-chip:focus-visible {
  outline: 2px solid #4285F4;
  outline-offset: 2px;
}
.g-chip-icon {
  margin-right: 6px;
  fill: currentColor;
}

/* Selected Filter Chip styling */
.g-chip-filter[aria-pressed="true"] {
  background-color: #E8F0FE;
  border-color: #1A73E8;
  color: #1A73E8;
  padding-left: 8px;
}
.g-chip-close-btn {
  background: none;
  border: none;
  cursor: pointer;
  padding: 0;
  margin-left: 6px;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 18px;
  height: 18px;
  border-radius: 50%;
  color: #5F6368;
}
.g-chip-close-btn:hover {
  background-color: rgba(60, 64, 67, 0.12);
  color: #202124;
}
```

---

## 4. Accessibility Checklist

*   **Aria Pressed**: Toggling filter chips must dynamically toggle `aria-pressed="true|false"` to announce active status.
*   **Aria Labels**: Trailing close buttons must feature descriptive labels linking them to their corresponding element (e.g. `aria-label="Remove filter: Pixel 8 Pro"`).
*   **Screen Reader Announcements**: When toggling filters, active results updates must be announced using a live region (e.g., `<div role="status" aria-live="polite">Showing 12 results</div>`).
*   **Keyboard Support**: Ensure chips support standard focus indexing (`Tab`) and selection triggers via `Space` or `Enter`.
