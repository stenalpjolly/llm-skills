# Header & Navigation Guidelines

This reference defines the structural layouts, visual guidelines, interactive menus, search elements, and accessibility rules for site Headers on Google-branded marketing websites.

---

## 1. Visual Specifications

The Header anchors the site's brand and establishes primary paths to core sections, pricing, and login pathways.

| Attribute | Specification | Notes |
| :--- | :--- | :--- |
| **Height** | `64px` (Mobile) or `64px` to `80px` (Desktop) | Symmetrical vertical grid alignment |
| **Positioning** | `position: sticky; top: 0; z-index: 1000;` | Floats atop screen during scrolling |
| **Background Surface** | `#FFFFFF` (Surface Base) | Clean brand background |
| **Bottom Border** | `1px solid #DADCE0` (Gray 300) | Visual separator differentiating header from page on scroll |
| **Max Nav Links** | `5` links maximum | Prevents horizontal density overload |
| **Typography** | `Roboto Medium`, `14px`, `#5F6368` (Gray 700) | Sentence case is mandatory |

---

## 2. Desktop Blueprint & Interactive Elements

*   **Logo (Left)**: Symmetrical clear space surrounding the official Google Wordmark or Product Lockup.
*   **Navigation Links (Center/Left)**: Highlighting active page with `Google Blue (#4285F4)` or a discrete `2px` blue underline.
*   **Utility Actions (Right)**:
    *   **Search**: Interactive search trigger button.
    *   **Sign In**: Clean link text leading to the Google login page.
    *   **Primary CTA**: Rounded pill-shaped button ("Get started").

---

## 3. Mobile Navigation Drawer

On smaller screen sizes (under `1024px`), navigation items must collapse into a right-aligned Hamburger menu button.

### 3.1 Drawer Transition
*   Clicking the hamburger menu button triggers a sliding panel from the right edge.
*   The transition duration must be `300ms` using standard linear-out-slow-in (`cubic-bezier(0, 0, 0.2, 1)`) easing.
*   Includes a prominent close ("x") button in the top right of the drawer panel.

### 3.2 HTML and CSS Structure
```html
<header role="banner" class="g-header">
  <div class="g-header-inner">
    <!-- Brand Logo -->
    <a href="/" class="g-logo-link" aria-label="Google Cloud Home">
      <svg class="g-logo" width="74" height="24" viewBox="0 0 74 24"><!-- SVG content --></svg>
    </a>

    <!-- Desktop Menu -->
    <nav role="navigation" aria-label="Primary" class="g-desktop-nav">
      <ul class="g-nav-list">
        <li><a href="/features" aria-current="page" class="g-nav-link active">Features</a></li>
        <li><a href="/solutions" class="g-nav-link">Solutions</a></li>
        <li><a href="/pricing" class="g-nav-link">Pricing</a></li>
      </ul>
    </nav>

    <!-- Right Controls -->
    <div class="g-header-actions">
      <button class="g-search-btn" aria-label="Search site">
        <svg width="24" height="24" viewBox="0 0 24 24"><path d="M15.5 14h-.79l-.28-.27C15.41 12.59 16 11.11 16 9.5 16 5.91 13.09 3 9.5 3S3 5.91 3 9.5 5.91 16 9.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z"/></svg>
      </button>
      <a href="/login" class="g-login-link">Sign in</a>
      <a href="/start" class="g-btn g-btn-primary">Get started</a>
      
      <!-- Hamburger Toggle -->
      <button class="g-hamburger" aria-expanded="false" aria-controls="mobile-nav-drawer" aria-label="Open navigation menu">
        <svg width="24" height="24" viewBox="0 0 24 24"><path d="M3 18h18v-2H3v2zm0-5h18v-2H3v2zm0-7v2h18V6H3z"/></svg>
      </button>
    </div>
  </div>
</header>
```

```css
.g-header {
  position: sticky;
  top: 0;
  z-index: 1000;
  background-color: #FFFFFF;
  border-bottom: 1px solid #DADCE0;
  height: 64px;
  font-family: 'Roboto', Arial, sans-serif;
}
.g-header-inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 100%;
  max-width: 1280px;
  margin: 0 auto;
  padding: 0 24px;
}
.g-desktop-nav {
  display: flex;
  margin-left: 32px;
}
.g-nav-list {
  display: flex;
  list-style: none;
  padding: 0;
  margin: 0;
  gap: 24px;
}
.g-nav-link {
  color: #5F6368;
  text-decoration: none;
  font-size: 14px;
  font-weight: 500;
}
.g-nav-link:hover, .g-nav-link.active {
  color: #4285F4;
}
.g-hamburger {
  display: none;
  background: none;
  border: none;
  cursor: pointer;
}

@media (max-width: 1023px) {
  .g-desktop-nav, .g-login-link, .g-header-actions .g-btn {
    display: none;
  }
  .g-hamburger {
    display: block;
  }
}
```

---

## 4. Accessibility Checklist

*   **Aria Expanded State**: The hamburger button must toggle `aria-expanded="true"` when the menu drawer is open, and `aria-expanded="false"` when closed.
*   **Focus Trap**: Standard keyboard navigation (`Tab`) must remain locked inside the mobile navigation drawer when open. Focus must return to the Hamburger button on drawer close.
*   **Aria Current**: Apply `aria-current="page"` to the link representing the active web page inside navigation lists.
