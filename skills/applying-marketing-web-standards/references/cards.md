# Cards Guidelines

This reference defines the visual specs, surface backgrounds, shadow values, corner rounding, hover interactions, and accessibility requirements for Card components on Google-branded marketing websites.

---

## 1. Visual Specifications

Cards group related content, media, description text, and actions together, establishing structured visual regions.

| Attribute | Specification | Notes |
| :--- | :--- | :--- |
| **Corner Radius** | `8px` (Standard Card) or `16px` (Feature/Hero Card) | Select one and apply consistently across the site |
| **Border Outline** | `1px solid #DADCE0` (Gray 300) | Recommended default border layout |
| **Background Surface** | `#FFFFFF` (Surface Base) or `#F8F9FA` (Gray 50) | Ensures clean high contrast for text copy |
| **Internal Padding**| `24px` on mobile, `32px` on desktop | Symmetrical vertical and horizontal padding |

---

## 2. Shadows and Elevations

When shadows are used to denote layered visual depth, Google MWS requires subtle, soft blur values rather than dark, harsh shadows.

### 2.1 Standard Elevation Levels
*   **Flat (Default Brand Preference)**: No shadow, border `1px solid #DADCE0` (Gray 300).
*   **Elevation 1 (Subtle Card/Interactive)**: Used for standard product cards.
    ```css
    box-shadow: 0 1px 2px 0 rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);
    ```
*   **Elevation 2 (Floating/Hovered Card)**: Used for cards on hover state.
    ```css
    box-shadow: 0 2px 6px 2px rgba(60, 64, 67, 0.15), 0 1px 2px 0 rgba(60, 64, 67, 0.3);
    ```

---

## 3. Card Interactivity & Hover Transitions

Interactive cards acting as links must provide smooth and distinct hover transitions.

### 3.1 CSS Interaction Specs
*   **Translation**: Shift card up by `4px` on hover.
*   **Shadow Transition**: Transition the box shadow from Elevation 1 (or flat border) to Elevation 2.
*   **Transition Duration**: `200ms` using standard linear-out-slow-in (`cubic-bezier(0, 0, 0.2, 1)`) ease curves.

### 3.2 Code Implementation (Full-Card Click Overlay)
```html
<article class="g-card g-card-interactive">
  <div class="g-card-media">
    <img src="pixel-phone.webp" alt="Google Pixel 8 phone" loading="lazy">
  </div>
  <div class="g-card-content">
    <h3 class="g-card-title">
      <a href="#" class="g-card-link">Pixel 8 hardware specs</a>
    </h3>
    <p class="g-card-description">Discover the hardware specs, cameras, battery, and AI tools of our latest smartphone.</p>
    <span class="g-card-cta" aria-hidden="true">Read specs <svg width="18" height="18" viewBox="0 0 24 24"><path d="M5 13h11.86l-5.43 5.43L12.85 20l8-8-8-8-1.42 1.42L16.86 11H5v2z"/></svg></span>
  </div>
</article>
```

```css
.g-card {
  display: flex;
  flex-direction: column;
  border-radius: 8px;
  background-color: #FFFFFF;
  border: 1px solid #DADCE0;
  overflow: hidden;
  box-sizing: border-box;
  font-family: 'Roboto', Arial, sans-serif;
  transition: transform 0.2s cubic-bezier(0, 0, 0.2, 1), 
              box-shadow 0.2s cubic-bezier(0, 0, 0.2, 1), 
              border-color 0.2s cubic-bezier(0, 0, 0.2, 1);
}
.g-card-media img {
  width: 100%;
  height: 200px;
  object-fit: cover;
  display: block;
}
.g-card-content {
  padding: 24px;
  display: flex;
  flex-direction: column;
  flex-grow: 1;
}
.g-card-title {
  margin: 0 0 8px 0;
  font-family: 'Google Sans', Arial, sans-serif;
  font-size: 20px;
  font-weight: 500;
  line-height: 28px;
}
.g-card-title a {
  color: #202124;
  text-decoration: none;
}
/* Expands anchor click area to the entire card layout */
.g-card-title a::after {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 1;
}
.g-card-description {
  margin: 0 0 16px 0;
  font-size: 14px;
  line-height: 20px;
  color: #5F6368;
}
.g-card-cta {
  font-size: 14px;
  font-weight: 500;
  color: #4285F4;
  display: inline-flex;
  align-items: center;
  gap: 4px;
}
.g-card-interactive {
  position: relative;
  cursor: pointer;
}
.g-card-interactive:hover {
  transform: translateY(-4px);
  border-color: transparent;
  box-shadow: 0 2px 6px 2px rgba(60, 64, 67, 0.15), 0 1px 2px 0 rgba(60, 64, 67, 0.3);
}
.g-card-interactive:focus-within {
  outline: 2px solid #4285F4;
  outline-offset: 2px;
}
```

---

## 4. Accessibility Checklist

*   **HTML5 Semantic Elements**: Wrap standalone card instances inside `<article>` tags to help screen reader cataloging.
*   **Avoid Nested Link Traps**: Do not embed multiple independent click targets inside the card if using the full-card click overlay hack, as it breaks HTML validation and keyboard focus flow.
*   **Reduced Motion**: On users requesting reduced motion, disable the `transform: translateY(-4px)` lift translation.
*   **Focus Ring**: Ensure focus indicators encapsulate the entire card boundary when nested tab elements receive focus.
