# Carousels Guidelines

This reference defines the design requirements, interactive standards, transition parameters, and accessibility rules for carousels and slideshow components on Google-branded marketing websites.

---

## 1. Interaction and Visual Standards

Carousels house multiple horizontal slides within a single region, allowing users to scroll or swipe through them systematically.

| Component | Standard Design Specification | Notes |
| :--- | :--- | :--- |
| **Navigation Arrows**| Circular buttons, minimum `40px` diameter | Placed on left/right outer boundaries of the slide track |
| **Arrow Icons** | Chevron-left and Chevron-right | Sized at `24px` centered within circular targets |
| **Indicators** | Circle dots, `8px` diameter | Placed at the bottom center; spacing between dots is `8px` |
| **Dot Active State**| Solid `Google Blue (#4285F4)` | Inactive dots are in `Gray 300 (#DADCE0)` |
| **Transition Speed**| `300ms` to `500ms` duration | Smooth linear-out-slow-in (`cubic-bezier(0, 0, 0.2, 1)`) curves |

---

## 2. Auto-Play and Animation Guidelines

Auto-playing carousels present severe accessibility issues if implemented poorly. Google MWS enforces strict rules on auto-play mechanisms:

1.  **Mandatory Play/Pause Control**: If a carousel auto-scrolls, a highly visible, keyboard-accessible Play/Pause toggle button must be provided.
2.  **Auto-Scroll Time Limits**: Slides must remain active for a minimum of **5 to 7 seconds** before advancing automatically.
3.  **Interaction Interruption**: Auto-play must stop immediately under the following circumstances:
    *   The user hovers their mouse over any part of the carousel.
    *   The user keyboard-focuses on any link, button, or input within the active slide.
    *   The user manually triggers any navigation button (arrows, dots).
4.  **Reduced Motion Compliance**: If the user has enabled OS-level reduced motion (`@media (prefers-reduced-motion: reduce)`), auto-play must be completely disabled, and transitions must use instant opacity cuts rather than slide animations.

---

## 3. Accessible Implementation Structure

To make carousels accessible, use standard WAI-ARIA carousel structures.

### 3.1 HTML Layout
```html
<section class="g-carousel" aria-roledescription="carousel" aria-label="Featured case studies">
  <!-- Visually hidden notice for screen reader users -->
  <div class="g-sr-only" aria-live="polite">Showing slide 1 of 3</div>

  <!-- Main Slide region wrapper -->
  <div class="g-carousel-viewport">
    <div class="g-carousel-track">
      <!-- Slide 1 -->
      <div class="g-carousel-slide" role="group" aria-roledescription="slide" aria-label="1 of 3" id="slide-1">
        <div class="g-slide-content">
          <h3>Google Pixel 8 Pro</h3>
          <p>Meet the pro-level camera and helpful AI tools that make life easier.</p>
          <a href="#" class="g-btn-primary">Learn more</a>
        </div>
      </div>

      <!-- Slide 2 (Inactive/Hidden) -->
      <div class="g-carousel-slide" role="group" aria-roledescription="slide" aria-label="2 of 3" id="slide-2" aria-hidden="true">
        <div class="g-slide-content">
          <h3>Google Pixel Watch 2</h3>
          <p>Help by Google. Health by Fitbit. Made for you.</p>
          <a href="#" class="g-btn-primary" tabindex="-1">Learn more</a>
        </div>
      </div>

      <!-- Slide 3 (Inactive/Hidden) -->
      <div class="g-carousel-slide" role="group" aria-roledescription="slide" aria-label="3 of 3" id="slide-3" aria-hidden="true">
        <div class="g-slide-content">
          <h3>Pixel Tablet</h3>
          <p>The tablet that only Google could make, now with a Speaker Dock.</p>
          <a href="#" class="g-btn-primary" tabindex="-1">Learn more</a>
        </div>
      </div>
    </div>
  </div>

  <!-- Navigation Controls -->
  <div class="g-carousel-controls">
    <button class="g-carousel-btn prev" aria-label="Previous slide" aria-controls="slide-track">
      <svg width="24" height="24" viewBox="0 0 24 24"><path d="M15.41 7.41L14 6l-6 6 6 6 1.41-1.41L10.83 12z"/></svg>
    </button>
    
    <div class="g-carousel-indicators" role="tablist" aria-label="Slides">
      <button class="g-carousel-dot active" role="tab" aria-selected="true" aria-controls="slide-1" aria-label="Slide 1"></button>
      <button class="g-carousel-dot" role="tab" aria-selected="false" aria-controls="slide-2" aria-label="Slide 2" tabindex="-1"></button>
      <button class="g-carousel-dot" role="tab" aria-selected="false" aria-controls="slide-3" aria-label="Slide 3" tabindex="-1"></button>
    </div>

    <button class="g-carousel-btn next" aria-label="Next slide" aria-controls="slide-track">
      <svg width="24" height="24" viewBox="0 0 24 24"><path d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"/></svg>
    </button>
  </div>
</section>
```

### 3.2 CSS Rules
```css
.g-carousel {
  position: relative;
  width: 100%;
  overflow: hidden;
  font-family: 'Roboto', Arial, sans-serif;
}
.g-sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  border: 0;
}
.g-carousel-viewport {
  width: 100%;
  overflow: hidden;
}
.g-carousel-track {
  display: flex;
  transition: transform 0.4s cubic-bezier(0, 0, 0.2, 1);
}
.g-carousel-slide {
  min-width: 100%;
  box-sizing: border-box;
}
.g-carousel-slide[aria-hidden="true"] {
  visibility: hidden;
}
.g-carousel-controls {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-top: 16px;
  gap: 16px;
}
.g-carousel-btn {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  border: 1px solid #DADCE0;
  background-color: #FFFFFF;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: background-color 0.15s, border-color 0.15s;
}
.g-carousel-btn:hover {
  background-color: #F8F9FA;
  border-color: #80868B;
}
.g-carousel-btn:focus-visible {
  outline: 2px solid #4285F4;
  outline-offset: 2px;
}
.g-carousel-indicators {
  display: flex;
  gap: 8px;
}
.g-carousel-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  border: none;
  background-color: #DADCE0;
  cursor: pointer;
  padding: 0;
  transition: background-color 0.15s;
}
.g-carousel-dot.active {
  background-color: #4285F4;
}
.g-carousel-dot:focus-visible {
  outline: 2px solid #4285F4;
  outline-offset: 2px;
}
```

---

## 4. Accessibility Checklist

*   **Slide Visibility**: Ensure offscreen/inactive slides are strictly given `aria-hidden="true"` and `visibility: hidden` (or `display: none`) to prevent focus leakage.
*   **Disabled Focus**: Inactive slides must have all clickable child items (links, buttons) set to `tabindex="-1"` so users cannot tab into invisible components.
*   **Keyboard Navigation Support**:
    *   Pressing `ArrowRight` focuses and activates the next indicator dot/slide.
    *   Pressing `ArrowLeft` focuses and activates the previous indicator dot/slide.
*   **Descriptive Labels**: Standard arrow selectors must have `aria-label="Next slide"` and `aria-label="Previous slide"`, avoiding generic words like "Forward" or "Back".
