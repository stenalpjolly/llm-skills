# Agent-Ready UI Architecture: Semantic Engineering for Autonomous Systems

This reference guide establishes strict guidelines for designing web interfaces that are highly navigable, parsable, and controllable by both humans and autonomous AI agents (such as LLMs executing browser-use actions or scrapers extracting structured data).

---

## 1. Core Philosophy of Agent-Ready Design

As we transition from UIs built purely for human screens to interfaces navigated by software agents:
*   **The UI is the API:** For an AI agent, the rendered HTML and accessibility tree are its direct interfaces.
*   **Aesthetic != Fragile:** Premium visual design must never come at the cost of broken HTML structure or missing labels.
*   **Deterministic Anchoring:** Agents rely on stable DOM keys and interactive states to execute tasks reliably.

---

## 2. The Semantic Landmark and Tree Standards

Ensure that your page structure builds a clean, readable layout tree.

*   **Landmark Dominance:** Wrap page content in semantic wrappers instead of generic nested `<div>` groups:
    *   `<header>` for site banners and primary navigation.
    *   `<nav>` for link lists and menu systems.
    *   `<main>` for primary page content (only one per page).
    *   `<section>` for logically grouped content, always paired with a heading.
    *   `<footer>` for utility links and copyright rows.
*   **Sequential Heading Hierarchy:** Heading levels must proceed sequentially without gaps:
    *   `<h1>` (Only one per page, in the Hero).
    *   `<h2>` (Main section headings).
    *   `<h3>` (Card headers or subsection details).
    *   Never skip from `<h1>` to `<h4>` merely to inherit a specific visual size. Override typography sizes using Tailwind utility classes (`text-xl`, `font-bold`), preserving the correct semantic tag.

---

## 3. Interactive Semantic Elements & Controls

An agent must be able to instantly identify what elements are clickable.

*   **Buttons vs. Links:**
    *   Use `<button>` for in-page actions, forms, modal toggles, and state changes.
    *   Use `<a>` with a valid `href` for navigation between pages or anchors.
    *   *Banned:* Adding `onClick` listeners to generic elements (`<div>`, `<span>`, `<img>`) to make them behave like buttons. If required, you must add `role="button"` and `tabIndex={0}` to make them keyboard-navigable and machine-parsable.
*   **Stable Attribute Anchors (`data-agent`):**
    Because modern utility-first CSS frameworks generate long, dynamic class strings (e.g., `flex items-center justify-center rounded-lg bg-zinc-900 px-5 py-2.5`), automated agents cannot target them reliably.
    *   Add clean, semantic `data-` attributes to primary interactive elements:
        ```html
        <button data-agent="hero-cta-primary" class="...">
          Get Started
        </button>
        ```

---

## 4. The 100% Label Completeness Standard

Never render visual elements without machine-readable alternative descriptions.

*   **Icon-Only Controls:**
    Buttons containing only an icon (e.g., a magnifying glass or a shopping bag) are invisible to screen readers and AI vision systems. You must add an `aria-label` or a visually hidden screen-reader label:
    ```html
    <button aria-label="Search site" class="...">
      <SearchIcon />
    </button>
    ```
    Alternatively, wrap the label in a screen-reader-only utility:
    ```html
    <button class="...">
      <SearchIcon />
      <span class="sr-only">Search site</span>
    </button>
    ```
*   **Descriptive Image Alt Text:**
    All photographic assets must feature meaningful, context-aware `alt` descriptions instead of generic placeholder names:
    *   *Bad:* `alt="image"` or `alt="banner"`
    *   *Good:* `alt="Interactive dashboard preview displaying financial revenue charts and monthly growth metrics"`

---

## 5. Forms, Inputs, and Autocomplete

AI agents frequently automate form filling (such as checkouts, sign-ups, and searches).

*   **Explicit Label Pairing:**
    Every `<input>`, `<textarea>`, and `<select>` must be explicitly linked to a `<label>` using the `htmlFor` (or `for` in pure HTML) attribute:
    ```html
    <div class="flex flex-col gap-2">
      <label htmlFor="email-address" class="text-sm font-medium">Email Address</label>
      <input id="email-address" type="email" autocomplete="email" class="..." />
    </div>
    ```
*   **Deterministic Autocomplete Hinting:**
    Always declare explicit `autocomplete` attributes on inputs (e.g., `autocomplete="email"`, `autocomplete="given-name"`, `autocomplete="current-password"`) to allow autofill agents to function instantly.

---

## 6. Overlay Isolation (Modals & Dropdowns)

When overlays are active, agents must be prevented from accidentally triggering background links.

*   **Aria-Hidden & Focus Traps:**
    *   When a modal is active, apply `aria-hidden="true"` to the background container to hide it from the accessibility tree.
    *   Ensure focus is trapped inside the active overlay, preventing the user or an agent from tabbing out into hidden page layers.
*   **Visual Contrast & ARIA States:**
    *   Use `aria-expanded="true | false"` on dropdown triggers to signal menu state.
    *   Use `aria-haspopup="listbox"` to explicitly define overlay capabilities.
