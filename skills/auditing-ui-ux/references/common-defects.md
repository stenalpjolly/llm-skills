# Common UI Defects & Corrective Patterns Reference

When compiling design audits, map identified issues to these standard corrective patterns to ensure precise, implementation-ready instructions.

## 1. Alignment & Grid Layouts

### 1.1 Misaligned Action Rows (The "Flex-Center" Rule)
*   **What's wrong:** Floating, misaligned buttons, labels, and text in interactive rows.
*   **What it should be:** All horizontal control bars must use CSS Flexbox with strict vertical centering (`align-items: center`) and standardized gaps (e.g., `gap: 16px` on the 8px grid).
*   **Why it matters:** Aligns element center-lines, removing cognitive weight and making the control bar scannable.

### 1.2 Inconsistent Left Margins (The "Unified Left Margin" Rule)
*   **What's wrong:** Section headers, cards, or tables having offset left margins, breaking the vertical alignment line.
*   **What it should be:** Remove custom offsets. Group headers and child components in a parent container with responsive padding (`24px` mobile, `32px` desktop).
*   **Why it matters:** Locks elements into a single vertical grid baseline, creating visual order.

### 1.3 Split Section Elements (The "Header-Action Split" Rule)
*   **What's wrong:** Section headers and top-right actions (Save, Clear, Refresh) are vertically misaligned.
*   **What it should be:** Use a space-between flex layout with vertical centering (`align-items: center`) and Google Sans for headers.
*   **Why it matters:** Symmetrically separates section headers from secondary tools along a single clean line.

## 2. Components & Button Styling

### 2.1 Visually Hidden Native Inputs (The "Hidden Native Input" Rule)
*   **What's wrong:** Duplicate unstyled buttons or default OS interfaces (e.g., native "Choose File" inputs) breaking brand styling.
*   **What it should be:** Use a screen-reader-safe overlay class (`.sr-only`) to hide the input while keeping it keyboard-accessible, and trigger via JS onClick.
*   **Why it matters:** Preserves accessibility for screen readers while displaying a clean, customized branded trigger button.

### 2.2 Lack of Action Hierarchy (The "Button Hierarchy" Rule)
*   **What's wrong:** Too many competing solid primary buttons, or styled buttons lacking semantic meaning (e.g., destructive actions colored as primary).
*   **What it should be:** Enforce a strict 4-tier button hierarchy: Primary (Solid Brand Blue), Secondary (Outlined Gray/Blue), Danger (Outlined Red), and Disabled (Reduced Opacity).
*   **Why it matters:** Visually directs the user to the single primary goal of the page while highlighting the weight of destructive secondary actions.

### 2.3 Bare Icon Targets (The "Interactive Icon" Rule)
*   **What's wrong:** Standalone sort, close, or refresh icons look static, lack hover feedback, or are too small to click easily.
*   **What it should be:** Wrap standalone icons in a circular button container with hover transition (light gray translucent overlay) and a minimum target size of `40px` (`48px` on mobile).
*   **Why it matters:** Meets WCAG touch target dimensions while providing visual feedback for interactive states.

### 2.4 Color Token Fragmentation (The "Single Source of Color" Rule)
*   **What's wrong:** Multiple inconsistent, hardcoded, or mismatched shades of blue across active elements.
*   **What it should be:** Define a single source of color variables inside `:root` (e.g., `--g-blue-interactive`, `--g-text-primary`, `--g-border`) and map all element borders, outlines, and backgrounds to these tokens.
*   **Why it matters:** Eradicates theme fragmentation and ensures colors behave predictably across the site.

## 3. Tables & Form Usability

### 3.1 Oversized Inputs (The "Content-Proportional Width" Rule)
*   **What's wrong:** Short form controls (like 1-3 digit ranking input boxes) are unnecessarily wide, stretching across the page/column.
*   **What it should be:** Limit input width proportional to expected content length (e.g., `max-width: 100px` for ranks or short quantities) and center-align the values.
*   **Why it matters:** Clear visual cues prevent layout bloating and convey expected content structure to users.

### 3.2 Cramped Table Rows (The "Table Breathing Room" Rule)
*   **What's wrong:** Table rows hosting interactive form controls or inputs feel cramped and collide with dividers.
*   **What it should be:** Increase table cell padding (`td`, `th`) to `16px 12px` and use `vertical-align: middle` with dynamic subscript collapsing.
*   **Why it matters:** Gives interactive table states adequate whitespace, improving reading speed and selection accuracy.

### 3.3 Low-Contrast Disabled States (The "Accessible Disabled State" Rule)
*   **What's wrong:** Inactive buttons are colored with low-contrast gray-on-gray, making their labels unreadable or inaccessible.
*   **What it should be:** Keep a visible border outline, reduce button opacity to `0.5`, apply a `not-allowed` cursor, and assign `aria-disabled="true"` with `tabindex="-1"` on non-native button elements.
*   **Why it matters:** Maintains visual legibility for disabled labels while clearly communicating they are currently unclickable.
