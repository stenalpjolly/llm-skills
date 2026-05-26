# Grid, Breakpoints, and Layout Guidelines

This reference defines the spatial rules, grid configuration, and responsive breakpoints for Google-branded marketing interfaces. 

---

## 1. The 8dp Grid System

Google marketing websites layout and spacing system is built on an **8dp (8px) grid**. All dimensions, layout positions, paddings, margins, and line heights of major block elements must be integers divisible by 8.

### 1.1 Micro-Spacing
*   **4px Spacing**: Permitted *only* for tight micro-alignments, such as the gap between an icon and its text label, or tight nested elements within a chip or tag.
*   **Usage Rule**: Always favor `8px`, `16px`, `24px`, `32px`, `40px`, `48px`, `56px`, `64px`, `80px`, and `96px` for layout padding and margins.

---

## 2. Responsive Breakpoints

The fluid grid automatically switches column configurations, margins, and gutter spacing to provide optimal readability on all screen sizes:

| Device | Screen Width Range | Columns | Page Margin | Gutter Width | Max Content Width |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **Mobile** | Under `600px` | 4 | `16px` | `16px` | Fluid (100%) |
| **Tablet** | `600px` to `1023px` | 8 | `24px` | `24px` | Fluid (100%) |
| **Desktop** | `1024px` to `1439px` | 12 | `24px` or `48px` | `24px` | `1280px` (Centered) |
| **Large Desktop**| `1440px` and up | 12 | Fluid | `24px` or `32px` | `1280px` or `1440px` |

---

## 3. Structural Layout Best Practices

### 3.1 Content Alignment and Max Width
*   **Containment**: Content must never stretch infinitely on wide screens. Center the main content area and apply a `max-width` limit of `1280px` (recommended) or `1440px` (maximum).
*   **CSS Example**:
    ```css
    .g-container {
      width: 100%;
      max-width: 1280px;
      margin-left: auto;
      margin-right: auto;
      padding-left: 24px;
      padding-right: 24px;
    }
    @media (max-width: 599px) {
      .g-container {
        padding-left: 16px;
        padding-right: 16px;
      }
    }
    ```

### 3.2 HTML5 Semantic Landmarks
All marketing pages must use standard semantic HTML5 elements to structure the page layout, enabling screen reader users to navigate the layout efficiently:
*   `<header role="banner">`: Wrap the main site header and navigation.
*   `<nav role="navigation">`: Wrap primary and footer navigation link blocks.
*   `<main role="main">`: Wrap the core page content. Only one `<main>` is allowed per page.
*   `<section>`: Group thematic content, always starting with a heading (`<h2>`–`<h6>`).
*   `<aside role="complementary">`: Use for sidebars or secondary supporting content blocks.
*   `<footer role="contentinfo">`: Wrap the site footer, site map, and legal links.

### 3.3 Keyboard Skip Navigation
To assist keyboard-only and screen reader users, a visually hidden skip link must be the **very first element** in the HTML structure:
*   **HTML**:
    ```html
    <a href="#main-content" class="g-skip-link">Skip to main content</a>
    ```
*   **CSS**:
    ```css
    .g-skip-link {
      position: absolute;
      top: -100px;
      left: 16px;
      background: #4285F4;
      color: #fff;
      padding: 12px 24px;
      border-radius: 4px;
      z-index: 10000;
      transition: top 0.2s ease;
    }
    .g-skip-link:focus {
      top: 16px;
      outline: 2px solid #202124;
    }
    ```

### 3.4 Screen-Reader Only Utility (.sr-only)
Every Google marketing site must define this standard utility class in its global styles.css to hide descriptive content from sighted users while preserving it for accessibility technology:
```css
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  border: 0;
}
```
