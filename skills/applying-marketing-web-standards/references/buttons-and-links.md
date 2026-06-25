# Buttons and Links Guidelines

This reference defines the visual specs, style hierarchy, interactive states, and accessibility rules for both button actions and hyperlink text on Google-branded marketing websites.

---

## 1. Visual Specifications

Buttons are circular pill-shapes that focus user attention and guide them through core actions, while hyperlinks integrate smoothly within editorial flows.

| Attribute | Specification | Notes |
| :--- | :--- | :--- |
| **Corner Radius** | `24px` or more (fully rounded pill-shape) | Half of height or greater |
| **Height (Button)**| `40px` (Desktop) or `48px` (Mobile/Touch target) | Sizing ensures compliance with touch-target metrics |
| **Horizontal Padding**| `24px` (Standard) or `16px` (Dense/with icons) | Sizing of inner left/right buffers |
| **Typography** | `Roboto Medium`, `14px` or `16px` | Weight matches readability standards |
| **Casing** | **Sentence Case Only** | Always use sentence case (e.g., "Start free trial") |

---

## 2. Button Hierarchy and Colors

Marketing pages must enforce a strict action hierarchy. Never place multiple solid buttons side-by-side.

*   **Primary Button (Solid)**: Background `#4285F4`, text `#FFFFFF`. Hover state: `#1A73E8`, active state: `#1557B0`. Focus: `2px` solid `#4285F4` with `2px` transparent offset.
*   **Secondary Button (Outlined)**: Border `1px solid #DADCE0`, text `#1A73E8`. Hover: background `#F8F9FA` and border `#80868B`. Active: `#F1F3F4`.
*   **Tertiary Button (Text CTA)**: Background transparent, text `#1A73E8`. Hover: `#F8F9FA` with underline. Active: `#E8F0FE`.
*   **Danger Button (Outlined Red)**: Border `1px solid #DADCE0`, text `#EA4335` (Google Red). Hover: background `#FDF2F2` (Light Red), border `#EA4335`. Used for destructive or negative actions (The "Button Hierarchy" Rule).

---

## 3. Links and Inline Hyperlinks

Hyperlinks must be clearly identifiable from regular body copy to ensure rapid visual scanning.

*   **Color**: Use `Google Blue (#1A73E8)` for active hyperlinks.
*   **Hover State**: Links must underline on hover. Text color remains blue or darkens to `#1557B0`.
*   **External Links**: Links opening a new tab must feature a trailing "external-link" arrow icon (`14px`) with `aria-hidden="true"`.

---

## 4. HTML and CSS Implementation

```html
<!-- Submit Form Button -->
<button class="g-btn g-btn-primary">Sign up now</button>

<!-- Navigation Link as Secondary Button -->
<a href="/products" class="g-btn g-btn-secondary">Explore products</a>

<!-- Text Link with arrow icon -->
<a href="/details" class="g-btn-link">
  Learn more
  <svg class="g-link-icon" width="18" height="18" viewBox="0 0 24 24"><path d="M5 13h11.86l-5.43 5.43L12.85 20l8-8-8-8-1.42 1.42L16.86 11H5v2z"/></svg>
</a>
```

```css
.g-btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  height: 40px;
  border-radius: 20px;
  padding: 0 24px;
  box-sizing: border-box;
  font-family: 'Roboto', Arial, sans-serif;
  font-size: 14px;
  font-weight: 500;
  text-decoration: none;
  cursor: pointer;
  border: 1px solid transparent;
  user-select: none;
  white-space: nowrap;
  transition: all 0.15s ease-in-out;
}
.g-btn-primary {
  background-color: #4285F4;
  color: #FFFFFF;
}
.g-btn-primary:hover {
  background-color: #1A73E8;
}
.g-btn-secondary {
  background-color: #FFFFFF;
  border-color: #DADCE0;
  color: #1A73E8;
}
.g-btn-secondary:hover {
  background-color: #F8F9FA;
  border-color: #80868B;
}
.g-btn-danger {
  background-color: #FFFFFF;
  border-color: #DADCE0;
  color: #EA4335;
}
.g-btn-danger:hover {
  background-color: #FDF2F2;
  border-color: #EA4335;
}
.g-btn:disabled,
.g-btn[aria-disabled="true"] {
  opacity: 0.5;
  cursor: not-allowed;
  pointer-events: none; /* Prevents click events on links */
}
.g-btn:focus-visible {
  outline: 2px solid #4285F4;
  outline-offset: 2px;
}

/* Link Style */
.g-btn-link {
  font-family: 'Roboto', Arial, sans-serif;
  font-size: 14px;
  font-weight: 500;
  color: #1A73E8;
  text-decoration: none;
  display: inline-flex;
  align-items: center;
}
.g-btn-link:hover {
  text-decoration: underline;
  color: #1557B0;
}
.g-link-icon {
  margin-left: 4px;
  fill: currentColor;
  transition: transform 0.15s ease;
}
.g-btn-link:hover .g-link-icon {
  transform: translateX(4px);
}

/* Circular Interactive Icon Button (The "Interactive Icon" Rule) */
.g-icon-btn {
  width: 40px; /* Aligns with 8px grid and touch targets */
  height: 40px;
  border-radius: 50%;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border: none;
  background-color: transparent;
  cursor: pointer;
  transition: background-color 0.15s ease-in-out;
}
.g-icon-btn:hover {
  background-color: rgba(32, 33, 36, 0.04); /* Subtle brand gray hover */
}
.g-icon-btn:focus-visible {
  outline: 2px solid #4285F4;
  outline-offset: 2px;
}
```

### 4.2 Screen-Reader-Safe Custom Triggers (The "Hidden Native Input" Rule)
When triggering hidden browser controls (such as `<input type="file">`) from a custom button, do not use `display: none` or `visibility: hidden` directly on inputs that need keyboard access. Instead, use a screen-reader-only utility and trigger via JavaScript.

```html
<div class="g-upload-row">
  <!-- Screen-reader accessible hidden native input -->
  <input type="file" id="g-csv-input" class="sr-only" onchange="console.log(this.files)" />
  <button class="g-btn g-btn-secondary" onclick="document.getElementById('g-csv-input').click()">
    Choose CSV file
  </button>
</div>
```

---

## 5. Accessibility Checklist

*   **Keyboard Control**: Native `<button>` elements must be activated using `Space` or `Enter`. Hyperlink anchors `<a>` must open on `Enter`.
*   **Invisible Labels**: If a button contains an icon alone (like `.g-icon-btn`), an explicit `aria-label` is mandatory (e.g., `aria-label="Refresh list"`).
*   **Tactile Targets**: Vertical spacing/padding should be inflated on touch screen viewports to ensure circular or rectangular targets are at least `40px` tall (desktop) or `48px` tall (mobile).
*   **Disabled Link Elements (The "Accessible Disabled State" Rule)**: Styled anchor links `<a>` used as buttons cannot natively handle `disabled`. You must set `aria-disabled="true"`, apply the `.g-btn:disabled` opacity styling, and assign `tabindex="-1"` so they are completely bypassed by keyboard tab flows.
