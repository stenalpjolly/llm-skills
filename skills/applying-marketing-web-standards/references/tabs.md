# Tabs Guidelines

This reference defines the visual specs, active border states, content panel transitions, and accessibility keyboard navigation rules for Tabs on Google-branded marketing websites.

---

## 1. Visual & Typography Standards

Tabs organize content into multiple views under corresponding panel headers, allowing users to switch views without reloading the page.

*   **Header Height**: Typically `48px` to `56px`.
*   **Active Tab**: Border bottom `2px solid #1A73E8` (Google Blue), text `#1A73E8`, and font weight `500` (`Roboto Medium`).
*   **Inactive Tab**: Text `#5F6368` (Gray 700), border bottom `2px solid transparent`.
*   **Hover state**: Inactive tabs highlight background slightly to `#F8F9FA` or border bottom turns light gray `#DADCE0`.
*   **Casing**: **Sentence Case** is mandatory.

---

## 2. HTML and CSS Structure

```html
<div class="g-tabs">
  <!-- Tabs list header -->
  <div class="g-tablist" role="tablist" aria-label="Product features">
    <button class="g-tab active" role="tab" aria-selected="true" aria-controls="panel-features-1" id="tab-features-1">
      Performance
    </button>
    <button class="g-tab" role="tab" aria-selected="false" aria-controls="panel-features-2" id="tab-features-2" tabindex="-1">
      Camera specs
    </button>
    <button class="g-tab" role="tab" aria-selected="false" aria-controls="panel-features-3" id="tab-features-3" tabindex="-1">
      Battery life
    </button>
  </div>

  <!-- Tab Panel 1 -->
  <div class="g-tabpanel" id="panel-features-1" role="tabpanel" aria-labelledby="tab-features-1">
    <h3>Pro-level performance</h3>
    <p>Discover the fast Tensor G3 chip optimized with Google AI.</p>
  </div>

  <!-- Tab Panel 2 (Hidden) -->
  <div class="g-tabpanel" id="panel-features-2" role="tabpanel" aria-labelledby="tab-features-2" hidden>
    <h3>Pixel camera capabilities</h3>
    <p>Zoom into details with our advanced triple-camera system.</p>
  </div>

  <!-- Tab Panel 3 (Hidden) -->
  <div class="g-tabpanel" id="panel-features-3" role="tabpanel" aria-labelledby="tab-features-3" hidden>
    <h3>All-day battery efficiency</h3>
    <p>Enjoy up to 24 hours of standard battery life with smart charging.</p>
  </div>
</div>
```

```css
.g-tabs {
  width: 100%;
  font-family: 'Roboto', Arial, sans-serif;
}
.g-tablist {
  display: flex;
  border-bottom: 1px solid #DADCE0;
  gap: 16px;
}
.g-tab {
  background: none;
  border: none;
  border-bottom: 2px solid transparent;
  padding: 16px 8px;
  font-size: 14px;
  font-weight: 500;
  color: #5F6368;
  cursor: pointer;
  transition: all 0.15s ease-in-out;
}
.g-tab:hover {
  color: #202124;
}
.g-tab.active {
  color: #1A73E8;
  border-bottom-color: #1A73E8;
}
.g-tab:focus-visible {
  outline: 2px solid #4285F4;
  outline-offset: -2px;
}

/* Panel transitions */
.g-tabpanel {
  padding: 24px 0;
  display: block;
}
.g-tabpanel[hidden] {
  display: none;
}
.g-tabpanel h3 {
  font-family: 'Google Sans', Arial, sans-serif;
  font-size: 20px;
  font-weight: 500;
  color: #202124;
  margin-top: 0;
}
```

---

## 3. Accessibility & Arrow Key Navigation (WAI-ARIA)

Tabs require native keyboard management to support assistive technologies correctly:

*   **Keyboard Arrow Navigation**:
    *   `Tab` enters the tab headers, focusing on the currently selected tab.
    *   `ArrowRight` focuses on the next tab header, immediately updating the active selection.
    *   `ArrowLeft` focuses on the previous tab header, updating the selection.
    *   `Tab` exits the headers, moving keyboard focus directly into the visible `tabpanel` content.
*   **WAI-ARIA Attributes**:
    *   Header bar wrapper must have `role="tablist"`.
    *   Individual triggers must have `role="tab"`.
    *   Active header must have `aria-selected="true"`, with inactive headers carrying `aria-selected="false"` and `tabindex="-1"`.
    *   Active headers must map `aria-controls` referencing their respective tabpanel `id`.
    *   Individual panel container divs must have `role="tabpanel"` and `aria-labelledby` referencing their matching button header `id`.
    *   Set the `hidden` attribute on inactive panel divs to hide content from keyboard tab orders.
