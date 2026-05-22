# Ambient Videos Guidelines

This reference defines the visual requirements, playback restrictions, performance guidelines, and accessibility regulations for Ambient Videos on Google-branded marketing websites.

---

## 1. Visual & Playback Standards

Ambient videos are looping, auto-playing background clips (such as abstracts, scrolling phone screens, or contextual lifestyle loops) used to enrich the visual narrative without distracting from primary copy.

*   **Audio Restriction**: Must be **completely silent** (possessing no audio tracks or explicitly muted in HTML).
*   **Looping**: Continuously loop playback seamlessly.
*   **Playsinline**: Play natively in-place within the page flow on mobile rather than launching full-screen players.
*   **Controls**: Standard video control tracks (playbar, volume) must be hidden from view.
*   **Interaction**: Text or primary CTAs must never be placed directly over complex, high-contrast moving video backgrounds without high-contrast translucent dark or light overlays to maintain readability.

---

## 2. Performance & Delivery Specs

To avoid delaying the page's First Contentful Paint (FCP) or degrading Core Web Vitals:
*   **Resolution**: Cap ambient videos to standard Web HD/SD resolutions (e.g. `1080p` max, ideally `720p`).
*   **Size**: Limit video files to under **5MB** (ideally under 2MB).
*   **Format**: Serve modern formats like WebM or MP4 (H.264) using responsive sources.
*   **Poster Image**: Include a static high-quality fallback `poster` image to display while the video loads or when auto-play is blocked.
*   **Preloading**: Set `preload="none"` or `preload="metadata"` so videos do not block the page load waterfall.

---

## 3. HTML and CSS Implementation

```html
<div class="g-ambient-video-container">
  <!-- Muted playsinline loops with poster fallback -->
  <video class="g-ambient-video" autoplay loop muted playsinline poster="lifestyle-poster.jpg" id="bg-video">
    <source src="lifestyle-loop.webm" type="video/webm">
    <source src="lifestyle-loop.mp4" type="video/mp4">
  </video>
  
  <!-- Play/Pause Control (Mandatory for Accessibility) -->
  <button class="g-video-toggle" aria-label="Pause background video" aria-controls="bg-video">
    <svg class="icon-pause" width="18" height="18" viewBox="0 0 24 24"><path d="M6 19h4V5H6v14zm8-14v14h4V5h-4z"/></svg>
  </button>
</div>
```

```css
.g-ambient-video-container {
  position: relative;
  width: 100%;
  height: 400px;
  overflow: hidden;
  background-color: #F8F9FA;
}
.g-ambient-video {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

/* Play/Pause Control overlap */
.g-video-toggle {
  position: absolute;
  bottom: 16px;
  right: 16px;
  width: 36px;
  height: 36px;
  border-radius: 50%;
  background: rgba(32, 33, 36, 0.6);
  border: none;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #FFFFFF;
  transition: background-color 0.15s;
  z-index: 10;
}
.g-video-toggle:hover {
  background: rgba(32, 33, 36, 0.8);
}
.g-video-toggle:focus-visible {
  outline: 2px solid #4285F4;
}

/* Pause/Play svg transitions */
.g-video-toggle.paused .icon-pause {
  display: none;
}
```

---

## 4. Accessibility & Motion Regulations

Auto-playing animations and videos can trigger vestibular disorders and disrupt users with cognitive disabilities.
*   **Reduced Motion**: If OS-level motion reduction is active (`@media (prefers-reduced-motion: reduce)`), the video **must stop playing automatically** on page load, or the video element must be completely swapped with a static poster image.
*   **Mandatory Manual Controls**: Always provide a visible Play/Pause toggle overlay. Never hide this switch, as keyboard users must be able to stop screen movement.
*   **Keyboard Support**: Ensure the Play/Pause trigger is fully focusable using `Tab` and triggers using `Enter` or `Space`.
*   **Aria Labels**: Toggle buttons must carry `aria-label="Pause background video"` when playing, and dynamically switch to `"Play background video"` when paused.
