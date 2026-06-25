# Tables Guidelines

This reference defines the visual specs, column alignment, border options, and accessibility regulations for Tables on Google-branded marketing websites.

---

## 1. Visual & Typography Standards

Tables present structured comparative datasets (such as product specs, plans, storage limits, or price tiers) in neat row and column grids.

*   **Row Height**: Vertical cell padding should be at least `12px` to `16px` to maintain a spacious, readable layout.
*   **Breathing Room around Forms (The "Table Breathing Room" Rule)**: When table rows host form fields, select menus, or inline actions, increase cell padding to a minimum of `16px 12px` and use `vertical-align: middle` to prevent cramped elements, ensuring sufficient room for interactive form controls.
*   **Dividers**: Standard horizontal rows are divided by `1px solid #DADCE0` (Gray 300) borders.
*   **Header Row (thead)**: Styled in bold `Roboto Medium, 14px, #202124`. The header row background is often a flat light gray surface `#F8F9FA` (Gray 50).
*   **Cell Typography**: `Roboto Regular, 14px, #5F6368` (Gray 700).

---

## 2. Text Alignment Principles

*   **Left-Align**: Text descriptions, emails, names, or alphanumeric columns.
*   **Right-Align**: Numeric quantities, prices, currency figures, and percentages.
*   **Center-Align**: Icon ticks, status checkmarks, or short centered binary attributes.
*   **Header Alignment**: Header column titles must align symmetrically with their matching column data (e.g. if the data is right-aligned, the column header must be right-aligned).

---

## 3. HTML and CSS Structure

```html
<div class="g-table-container">
  <table class="g-table">
    <caption>Google Cloud storage pricing comparison</caption>
    <thead>
      <tr>
        <th scope="col">Storage class</th>
        <th scope="col">Minimum duration</th>
        <th scope="col" class="text-right">Price per GB / month</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <th scope="row">Standard storage</th>
        <td>None</td>
        <td class="text-right">$0.020</td>
      </tr>
      <tr>
        <th scope="row">Nearline storage</th>
        <td>30 days</td>
        <td class="text-right">$0.010</td>
      </tr>
      <tr>
        <th scope="row">Coldline storage</th>
        <td>90 days</td>
        <td class="text-right">$0.004</td>
      </tr>
    </tbody>
  </table>
</div>
```

```css
.g-table-container {
  width: 100%;
  overflow-x: auto; /* Enables horizontal scroll on mobile viewports */
  border: 1px solid #DADCE0;
  border-radius: 8px;
}
.g-table {
  width: 100%;
  border-collapse: collapse;
  font-family: 'Roboto', Arial, sans-serif;
  font-size: 14px;
  text-align: left;
}
.g-table caption {
  font-size: 0; /* Visually hidden table title; visible only to screen readers */
}
.g-table th, .g-table td {
  padding: 16px;
  border-bottom: 1px solid #DADCE0;
  color: #5F6368;
}
.g-table thead th {
  background-color: #F8F9FA;
  font-weight: 500;
  color: #202124;
}
.g-table tbody th {
  font-weight: 500;
  color: #202124;
}

/* Row Hover styling */
.g-table tbody tr:hover {
  background-color: #F8F9FA;
}

/* Alignment utilities */
.text-right {
  text-align: right !important;
}
```

---

## 4. Accessibility Checklist

*   **Semantic Elements**: Always construct tables using native HTML tags (`<table>`, `<thead>`, `<tbody>`, `<tr>`, `<th>`, `<td>`). Avoid CSS grid/flex structures pretending to be tables.
*   **Keyboard Navigation & Column Scopes**: Custom data tables often omit structural column and row scopes, which breaks keyboard navigation context. You must explicitly enforce:
    *   `scope="col"` on all header headers (`<th>`).
    *   `scope="row"` on row header titles to announce row contexts to screen readers.
    *   `tabindex="0"` on all scrollable table wrappers to allow keyboard focus.
*   **Responsive Scrolling**: Wrap large tables in an `<div class="g-table-container">` with `overflow-x: auto` so the mobile viewport does not clip text.
*   **Table Captions**: Include a `<caption>` element describing the dataset's purpose for assistive tech.
