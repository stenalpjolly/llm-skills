# Banners Guidelines

This reference defines the visual requirements, color setups, placements, close behaviors, and accessibility regulations for Banners on Google-branded marketing websites.

---

## 1. Visual & Placement Standards

Banners are informational notice strips anchored at the top of a page (or inside section columns) used to broadcast system updates, product releases, or promotional offers.

*   **Placement**: Standard banners are positioned directly above or integrated within the main website header. They can either remain sticky or scroll with the page.
*   **Height**: Compact vertical profile (typically `40px` to `56px` tall).
*   **Typography**: `Roboto Regular, 14px, line-height 20px`. Links inside banners are underlined and bolded.
*   **Casing**: **Sentence Case** is mandatory.

---

## 2. Banner Color Archetypes

Banners utilize standard semantic colors representing the priority of the announcement:

| Archetype | Background | Text Color | Icon | Usage |
| :--- | :--- | :--- | :--- | :--- |
| **Info / Promo** | `#E8F0FE` (Blue 50) | `#1A73E8` (Blue 700) | Info circle | Promotional alerts, tips |
| **Success** | `#E6F4EA` (Green 50) | `#137333` (Green 800) | Check circle | Completed setup confirmations |
| **Warning** | `#FEF7E0` (Yellow 50)| `#B06000` (Yellow 900)| Alert triangle | Subscription renewals, maintenance alerts |
| **Error** | `#FCE8E6` (Red 50) | `#C5221F` (Red 800) | Block circle | Payment failures, system outages |

---

## 3. HTML and CSS Structure

```html
<div class="g-banner g-banner-info" role="status" id="promo-banner">
  <div class="g-banner-inner">
    <!-- Informational icon -->
    <svg class="g-banner-icon" width="20" height="20" viewBox="0 0 24 24" aria-hidden="true">
      <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-6h2v6zm0-8h-2V7h2v2z"/>
    </svg>
    
    <div class="g-banner-content">
      <span>Get $300 in free credits when you sign up for Google Cloud. <a href="/signup" class="g-banner-link">Claim offer</a></span>
    </div>
    
    <!-- Close Button -->
    <button class="g-banner-close" aria-label="Dismiss banner" aria-controls="promo-banner">
      <svg width="18" height="18" viewBox="0 0 24 24"><path d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z"/></svg>
    </button>
  </div>
</div>
```

```css
.g-banner {
  width: 100%;
  padding: 12px 24px;
  box-sizing: border-box;
  font-family: 'Roboto', Arial, sans-serif;
  transition: opacity 0.2s ease, transform 0.2s ease;
}
.g-banner-inner {
  display: flex;
  align-items: center;
  max-width: 1280px;
  margin: 0 auto;
}
.g-banner-info {
  background-color: #E8F0FE;
  color: #1A73E8;
  border-bottom: 1px solid #ADCCF9;
}
.g-banner-icon {
  margin-right: 12px;
  fill: currentColor;
  flex-shrink: 0;
}
.g-banner-content {
  flex-grow: 1;
  font-size: 14px;
  line-height: 20px;
}
.g-banner-link {
  color: inherit;
  font-weight: 500;
  text-decoration: underline;
  margin-left: 4px;
}
.g-banner-link:hover {
  text-decoration: none;
}
.g-banner-close {
  background: none;
  border: none;
  cursor: pointer;
  padding: 4px;
  color: inherit;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: background-color 0.15s;
}
.g-banner-close:hover {
  background-color: rgba(26, 115, 232, 0.12);
}
.g-banner-close:focus-visible {
  outline: 2px solid #4285F4;
}
```

---

## 4. Accessibility Checklist

*   **Landmark & Roles**:
    *   For standard promos or logs, use `role="status"` (which has an implicit `aria-live="polite"`).
    *   For critical alerts or errors, use `role="alert"` (with implicit `aria-live="assertive"`) so the screen reader interrupts immediately.
*   **Labels**: Close buttons must have an explicit `aria-label="Dismiss banner"`.
*   **Aria Controls**: Set `aria-controls` on the close button referencing the unique `id` of the parent banner container.
*   **Keyboard Support**: Keyboard users must be able to navigate to any links and close buttons within the banner using the standard `Tab` order.
