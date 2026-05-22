# Overlays Guidelines

This reference defines the visual specs, modal dialog popups, background backdrops, shadow values, and accessibility keyboard trapping rules for Overlays on Google-branded marketing websites.

---

## 1. Visual & Structural Standards

Overlays (such as Modal Dialogs, Lightboxes, Popovers, and Slide drawers) are high-priority containers that sit on top of the primary page content.

*   **Sizing**: Fluid max-width sizes: Small (`400px`), Medium (`640px`), or Large (`960px`), centered vertically and horizontally in the viewport.
*   **Shadow**: Enforces Elevation 3 (Floating Modal shadow) depth.
*   **Backdrop**: Transparent dark overlay (`rgba(32, 33, 36, 0.6)`) that dims background content.
*   **Corner Rounding**: `8px` or `16px` border-radius.
*   **Header**: Standard header containing a title and a top-right Close button ("x") styled as a circular focus button.

---

## 2. HTML and CSS Structure

```html
<div class="g-overlay-backdrop" id="overlay-demo" aria-hidden="true" tabindex="-1">
  <!-- Modal dialogue container -->
  <div class="g-overlay-modal" role="dialog" aria-modal="true" aria-labelledby="modal-title" id="modal-container">
    <div class="g-overlay-header">
      <h2 id="modal-title" class="g-overlay-title">Join our monthly newsletter</h2>
      <button class="g-overlay-close" aria-label="Close dialog" aria-controls="overlay-demo">
        <svg width="24" height="24" viewBox="0 0 24 24"><path d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z"/></svg>
      </button>
    </div>
    
    <div class="g-overlay-body">
      <p>Stay up to date with the latest product specs, feature updates, and developer guides from Google.</p>
    </div>
    
    <div class="g-overlay-footer">
      <button class="g-btn g-btn-secondary" id="btn-cancel">Cancel</button>
      <button class="g-btn g-btn-primary" id="btn-submit">Subscribe</button>
    </div>
  </div>
</div>
```

```css
.g-overlay-backdrop {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(32, 33, 36, 0.6);
  display: none; /* Block on show classes */
  align-items: center;
  justify-content: center;
  z-index: 2000;
  padding: 24px;
  box-sizing: border-box;
}
.g-overlay-backdrop.show {
  display: flex;
}
.g-overlay-modal {
  background-color: #FFFFFF;
  border-radius: 8px;
  width: 100%;
  max-width: 560px;
  box-shadow: 0 4px 16px 0 rgba(60, 64, 67, 0.15), 0 1px 4px 0 rgba(60, 64, 67, 0.3);
  display: flex;
  flex-direction: column;
  overflow: hidden;
  font-family: 'Roboto', Arial, sans-serif;
  animation: modalScaleUp 0.25s cubic-bezier(0, 0, 0.2, 1);
}

@keyframes modalScaleUp {
  from { transform: scale(0.95); opacity: 0; }
  to { transform: scale(1); opacity: 1; }
}

.g-overlay-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 24px 24px 16px 24px;
}
.g-overlay-title {
  margin: 0;
  font-family: 'Google Sans', Arial, sans-serif;
  font-size: 20px;
  font-weight: 500;
  color: #202124;
}
.g-overlay-close {
  background: none;
  border: none;
  cursor: pointer;
  width: 36px;
  height: 36px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #5F6368;
}
.g-overlay-close:hover {
  background-color: rgba(32, 33, 36, 0.08);
}
.g-overlay-close:focus-visible {
  outline: 2px solid #4285F4;
}
.g-overlay-body {
  padding: 0 24px 24px 24px;
  font-size: 14px;
  line-height: 20px;
  color: #5F6368;
}
.g-overlay-footer {
  display: flex;
  justify-content: flex-end;
  gap: 12px;
  padding: 16px 24px 24px 24px;
  background-color: #F8F9FA;
  border-top: 1px solid #DADCE0;
}
```

---

## 3. Accessibility & Keyboard Trapping (Mandatory)

Overlays introduce critical compliance hazards if focus is not strictly managed.

*   **Keyboard Focus Trap**:
    *   When the modal triggers, capture the active element (`document.activeElement`) to return focus on close.
    *   Set focus to the Close button, or the first active element in the modal immediately.
    *   Trap the `Tab` focus ordering strictly inside the modal container. Pressing `Tab` on the last focusable element in the modal must cycle back to the Close button (and vice versa on `Shift+Tab`).
*   **Dismiss on Escape**: Listen for keyup events and close the overlay immediately when the user presses `Escape`.
*   **WAI-ARIA Pattern attributes**:
    *   The container must have `role="dialog"` and `aria-modal="true"`.
    *   Use `aria-labelledby` referencing the modal title heading `id` and `aria-describedby` referencing body text.
    *   Hide page elements outside the modal from screen readers using `aria-hidden="true"` on parent content wrappers while active.
