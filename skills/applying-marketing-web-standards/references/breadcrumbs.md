# Breadcrumbs Guidelines

This reference defines the visual requirements, divider specifications, active styles, and accessibility regulations for Breadcrumbs on Google-branded marketing websites.

---

## 1. Visual & Structural Standards

Breadcrumbs represent a horizontal trail of nested page links showing the user's current location within the site's folder hierarchy.

*   **Location**: Positioned at the top of the content page area, directly below the site header but above the main `<h1>` title.
*   **Separators**: Separate page items using a subtle right chevron icon (`12px` height) or a forward slash (`/`). Separators must be unclickable and ignored by screen readers.
*   **Active Item**: The final breadcrumb represents the active page. It must be unclickable, styled in bold or dark gray text (`#202124`), and have no hover highlights.
*   **Typography**: `Roboto Regular, 14px, #5F6368` (Gray 700).
*   **Casing**: **Sentence Case** is mandatory.

---

## 2. HTML and CSS Structure

```html
<nav role="navigation" aria-label="Breadcrumb" class="g-breadcrumbs">
  <ol class="g-breadcrumb-list">
    <!-- Level 1 -->
    <li class="g-breadcrumb-item">
      <a href="/" class="g-breadcrumb-link">Home</a>
    </li>
    
    <!-- Separator -->
    <li class="g-breadcrumb-separator" aria-hidden="true">
      <svg width="12" height="12" viewBox="0 0 24 24"><path d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"/></svg>
    </li>

    <!-- Level 2 -->
    <li class="g-breadcrumb-item">
      <a href="/products" class="g-breadcrumb-link">Products</a>
    </li>

    <!-- Separator -->
    <li class="g-breadcrumb-separator" aria-hidden="true">
      <svg width="12" height="12" viewBox="0 0 24 24"><path d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"/></svg>
    </li>

    <!-- Level 3 (Active page - non-clickable) -->
    <li class="g-breadcrumb-item active" aria-current="page">
      Pixel 8 Pro
    </li>
  </ol>
</nav>
```

```css
.g-breadcrumbs {
  padding: 16px 0;
  font-family: 'Roboto', Arial, sans-serif;
}
.g-breadcrumb-list {
  display: flex;
  align-items: center;
  list-style: none;
  padding: 0;
  margin: 0;
  flex-wrap: wrap;
}
.g-breadcrumb-item {
  font-size: 14px;
  line-height: 20px;
  color: #5F6368;
}
.g-breadcrumb-link {
  color: #5F6368;
  text-decoration: none;
  transition: color 0.15s;
}
.g-breadcrumb-link:hover {
  color: #4285F4;
  text-decoration: underline;
}

/* Separator styling */
.g-breadcrumb-separator {
  display: flex;
  align-items: center;
  padding: 0 8px;
  color: #80868B;
  fill: currentColor;
}

/* Active current item styling */
.g-breadcrumb-item.active {
  color: #202124;
  font-weight: 500;
  cursor: default;
}
```

---

## 3. Accessibility Checklist

*   **Semantic Container**: Wrap the breadcrumb trail inside `<nav aria-label="Breadcrumb">`.
*   **Ordered List**: Markup list items using a semantic `<ol>` structure so screen readers can announce the absolute depth (e.g. "List item 3 of 5").
*   **Active Item Marking**: Set `aria-current="page"` on the list item containing the current/final page label.
*   **Hide Separators**: Hide decorative divider icons from screen readers using `aria-hidden="true"` to prevent unhelpful readouts (e.g. "greater than symbol" or "slash").
