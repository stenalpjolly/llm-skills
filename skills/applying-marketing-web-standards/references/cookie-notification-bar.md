# Cookie Notification Bar Guidelines

This reference defines the visual specs, text copies, interaction options, consent loops, and accessibility regulations for the Cookie Notification Bar on Google-branded marketing websites.

---

## 1. Visual & Placement Standards

The Cookie Notification Bar (also called the Cookie Consent Banner) is a high-visibility container anchored to the viewport boundaries.

*   **Placement**: Anchored to the **bottom** of the viewport, overlaying standard content, or as a floating panel centered at the bottom of the screen.
*   **Shadow**: Uses Elevation 3 (Floating Modal shadow) to separate it from the page.
*   **Background**: White (`#FFFFFF`) or Dark Gray (`#202124`).
*   **Borders**: `1px solid #DADCE0` (on light surfaces).
*   **Casing**: **Sentence Case** is mandatory.

---

## 2. Text Copy & Choices

In compliance with global privacy regulations (such as GDPR, CCPA):
*   **Informational text**: Must explain simply what cookies are tracked and link to the Privacy Policy.
*   **CTAs (Standard Duo)**:
    1.  **Accept All (Primary)**: Solid Blue button (`#4285F4`), white text.
    2.  **Reject All (Secondary)**: Outlined Gray button (`#DADCE0`), blue text.
    3.  **Customize Settings (Tertiary)**: Plain blue link text.

---

## 3. HTML and CSS Structure

```html
<section class="g-cookie-bar" role="region" aria-label="Cookie consent banner" id="cookie-banner">
  <div class="g-cookie-inner">
    <div class="g-cookie-text">
      <p>We use cookies to personalize content, analyze our web traffic, and improve your browsing experience. Read our <a href="https://policies.google.com/privacy" target="_blank" class="g-cookie-link">Privacy Policy</a> to learn more.</p>
    </div>
    
    <div class="g-cookie-actions">
      <button class="g-btn g-btn-secondary" id="cookie-reject">Reject all</button>
      <button class="g-btn g-btn-primary" id="cookie-accept">Accept all</button>
    </div>
  </div>
</section>
```

```css
.g-cookie-bar {
  position: fixed;
  bottom: 0;
  left: 0;
  width: 100%;
  background-color: #FFFFFF;
  border-top: 1px solid #DADCE0;
  box-shadow: 0 -4px 16px rgba(60, 64, 67, 0.15);
  padding: 16px 24px;
  box-sizing: border-box;
  font-family: 'Roboto', Arial, sans-serif;
  z-index: 10000;
  transition: transform 0.3s cubic-bezier(0, 0, 0.2, 1);
}
.g-cookie-inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
  max-width: 1280px;
  margin: 0 auto;
  gap: 24px;
}
.g-cookie-text p {
  margin: 0;
  font-size: 14px;
  line-height: 20px;
  color: #5F6368;
}
.g-cookie-link {
  color: #1A73E8;
  text-decoration: underline;
}
.g-cookie-link:hover {
  text-decoration: none;
}
.g-cookie-actions {
  display: flex;
  gap: 12px;
  flex-shrink: 0;
}

@media (max-width: 767px) {
  .g-cookie-inner {
    flex-direction: column;
    align-items: stretch;
    gap: 16px;
  }
  .g-cookie-actions {
    justify-content: flex-end;
  }
}
```

---

## 4. Accessibility Checklist

*   **Priority Index**: Set `z-index` values high enough to prevent other floating overlays from obscuring the banner.
*   **WAI-ARIA Landmark**: Use `<section role="region" aria-label="Cookie consent banner">` to allow screen reader users to find the banner instantly.
*   **Keyboard Focus Focus Loop**:
    *   On load, keep keyboard tab order standard, but place the cookie banner *before* main content in the DOM tree, or intercept `Tab` key presses if a modal consent variant is active.
    *   Pressing `Enter` on "Accept all" or "Reject all" must dismiss the block and immediately return focus to the top of the viewport or the skip-link.
*   **Persistent Dismiss**: Consent state changes must save to storage (e.g. `localStorage`), removing the element from the DOM on subsequent page requests.
