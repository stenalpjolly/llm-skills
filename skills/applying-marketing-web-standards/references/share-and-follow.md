# Share and Follow Guidelines

This reference defines the visual specs, branding rules, social icon parameters, and accessibility regulations for Share and Follow components on Google-branded marketing websites.

---

## 1. Visual & Placement Standards

Share and Follow elements allow users to distribute website links (Share) or visit the product's official social channels (Follow).

*   **Placement**: Often placed at the bottom of blog articles or case studies, or as a small floating column on large screen sizes.
*   **Icons**: Standard social media platforms (LinkedIn, X/Twitter, Facebook, YouTube, Email, Link copy). Icons are sized at `20px` or `24px` within `36px` or `40px` circular button targets.
*   **Design**: Flat circular outline buttons (`1px solid #DADCE0` Gray 300) with solid gray icons (`#5F6368`), highlighting to branding colors or `#1A73E8` (Google Blue) on hover.

---

## 2. Branding Compliance

When linking to third-party social media sites, respect Google's brand guidelines:
*   Never distort, custom-color, or modify trademarked logos of other services (e.g. use standard monochrome or brand-authorized color files).
*   Always structure the block containing these buttons with a clear label in **Sentence Case**: e.g., "Share this article" or "Follow Google Cloud".

---

## 3. HTML and CSS Structure

```html
<div class="g-social-block">
  <span class="g-social-title">Share this article</span>
  
  <div class="g-social-buttons">
    <!-- LinkedIn -->
    <a href="https://www.linkedin.com/sharing/share-offsite/?url=https://example.com" class="g-social-btn" target="_blank" rel="noopener" aria-label="Share on LinkedIn">
      <svg width="20" height="20" viewBox="0 0 24 24"><path d="M19 3a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h14m-.5 15.5v-5.3a3.26 3.26 0 0 0-3.26-3.26c-.85 0-1.84.52-2.32 1.3v-1.11h-2.79v8.37h2.79v-4.93c0-.77.62-1.4 1.39-1.4a1.4 1.4 0 0 1 1.4 1.4v4.93h2.79M6.88 8.56a1.68 1.68 0 0 0 1.68-1.68c0-.93-.75-1.69-1.68-1.69a1.69 1.69 0 0 0-1.69 1.69c0 .93.76 1.68 1.69 1.68m1.39 9.94v-8.37H5.5v8.37h2.77z"/></svg>
    </a>

    <!-- X / Twitter -->
    <a href="https://twitter.com/intent/tweet?url=https://example.com" class="g-social-btn" target="_blank" rel="noopener" aria-label="Share on X">
      <svg width="20" height="20" viewBox="0 0 24 24"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>
    </a>

    <!-- Copy Link Trigger (JS needed to copy) -->
    <button class="g-social-btn" id="btn-copy-link" aria-label="Copy page link">
      <svg width="20" height="20" viewBox="0 0 24 24"><path d="M16 1H4c-1.1 0-2 .9-2 2v14h2V3h12V1zm3 4H8c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h11c1.1 0 2-.9 2-2V7c0-1.1-.9-2-2-2zm0 16H8V7h11v14z"/></svg>
    </button>
  </div>
</div>
```

```css
.g-social-block {
  display: flex;
  flex-direction: column;
  gap: 12px;
  font-family: 'Roboto', Arial, sans-serif;
}
.g-social-title {
  font-size: 14px;
  font-weight: 500;
  color: #202124;
}
.g-social-buttons {
  display: flex;
  gap: 8px;
}
.g-social-btn {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  border: 1px solid #DADCE0;
  background-color: #FFFFFF;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  color: #5F6368;
  fill: currentColor;
  transition: all 0.15s ease-in-out;
}
.g-social-btn:hover {
  background-color: #F8F9FA;
  border-color: #1A73E8;
  color: #1A73E8;
}
.g-social-btn:focus-visible {
  outline: 2px solid #4285F4;
  outline-offset: 2px;
}
```

---

## 4. Accessibility Checklist

*   **Descriptive Aria Labels**: Social links/buttons contain SVG elements and no visible text copy. You must supply descriptive labels like `aria-label="Share on LinkedIn"` or `aria-label="Follow Google Cloud on YouTube"`.
*   **External Anchors (rel)**: To protect memory and security, set `rel="noopener"` or `rel="noreferrer"` on all links opening in new browser tabs (`target="_blank"`).
*   **Copy Clipboard Status**: When triggering clipboard copy scripts via the "Copy Link" button, ensure success notifications are announced immediately using live aria regions (e.g. `role="status"` displaying "Link copied to clipboard").
*   **Tabindex Compatibility**: Icon buttons must be keyboard focusable (`Tab`).
