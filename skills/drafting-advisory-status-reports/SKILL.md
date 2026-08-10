---
name: drafting-advisory-status-reports
description: Generates executive Google Cloud Advisory Weekly Status Report HTML documents with base64 logo embedding and A4 print-deterministic CSS.
disable-model-invocation: true
---

# Drafting Advisory Status Reports

This skill enforces a predictable, **brand-locked** workflow for generating Google Cloud Advisory Weekly Status Report (WSR) HTML documents. It eliminates external asset dependencies, adapts page orientation to workspace conventions, and guarantees clean A4 pagination.

## Leading Words & Principles
- **zero-external-asset**: All logos and images must be embedded as base64 data URIs. No report may rely on external image URLs or relative disk paths for rendering.
- **orientation-adaptive**: Inspect existing WSR files in the workspace to determine A4 portrait vs. landscape conventions before drafting.
- **print-deterministic**: Enforce CSS page-break rules so multi-page reports split cleanly across A4 sheets without clipping cards, headers, or table rows.
- **brand-locked**: Maintain strict Google Cloud visual hierarchy (`Roboto`/`Roboto Mono` typography, gradient headers, and curated color-accented cards).

## In-Skill Steps

### 1. Reconnaissance & Orientation Selection (*orientation-adaptive*)
1. Scan the workspace for existing WSR HTML files or templates to determine established `@page` size conventions.
2. If an existing report uses `A4 portrait` or `A4 landscape`, adopt that orientation automatically.
3. If no convention exists or files conflict, ask the user: *"Would you like this Weekly Status Report in A4 portrait or A4 landscape?"*
4. **Completion criterion**: Page orientation is explicitly set to `A4 portrait` (1-column vertical card stack) or `A4 landscape` (2/3-column card grid).

### 2. Brand Asset Harvesting (*zero-external-asset*)
1. Locate the customer logo image in the workspace (e.g., within `logos/` or project root).
2. Execute a local script/command to encode the image file into a `data:image/png;base64,...` data URI string.
3. If no customer logo image is found in the workspace, configure the header to display a styled text-only customer brand badge with an appropriate FontAwesome icon.
4. **Completion criterion**: Customer logo is available as a valid base64 string or explicitly fallback-styled.

### 3. Template Loading & Content Structuring (*brand-locked*)
1. Load the corresponding reference template via progressive disclosure:
   - For portrait: read `templates/wsr_portrait.html`
   - For landscape: read `templates/wsr_landscape.html`
2. Populate the required report sections:
   - **Header**: Google Cloud SVG logo, vertical divider, and base64 customer logo (or text badge), plus active Status Badge (`Week X Status Report`).
   - **Title & Meta Bar**: Document title with gradient accent, Date, Period, and Focus area.
   - **Accomplishments This Week**: Green-accented `.card` (`#34A853`) with checkmark items.
   - **Plan For Next Week**: Blue-accented `.card` (`#4285F4`) with forward-arrow items.
   - **Open Action Items**: Amber-accented `.card` (`#FBBC05`) with a structured `.action-table` and team owner badges (`[Customer Team]`, `[Google Team]`).
3. **Completion criterion**: All mandatory sections are populated using the design tokens from the selected template.

### 4. Pagination & Print Validation (*print-deterministic*)
1. Verify that all `.card` and `.action-table` elements include `page-break-inside: avoid;`.
2. For reports exceeding a single page, insert `<div class="page-break"></div>` between major sections where needed so that content never splits awkwardly across page boundaries.
3. Verify that print stylesheet overrides (`@media print`) remove box shadows, backgrounds, and margins appropriately.
4. **Completion criterion**: Zero external image URLs remain in the HTML, and CSS pagination rules are verified.
