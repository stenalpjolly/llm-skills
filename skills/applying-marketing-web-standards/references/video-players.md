# Video Players Guidelines

This reference defines the visual requirements, customized player control setups, caption requirements, and accessibility keyboard controls for Video Players on Google-branded marketing websites.

---

## 1. Visual & Playback Standards

Video players display rich product trailers, product demo screens, or keynote sessions directly inline or inside overlay modal blocks.

*   **Aspect Ratio**: Standard video containers must maintain a fluid widescreen responsive aspect ratio of `16:9` (or `2:1` on specialized visual displays).
*   **Default State**: Display a clear, high-contrast poster placeholder image containing a centered solid white circular play button (`64px` diameter) with a centered triangle play icon.
*   **Colors**: Custom skins or visual progress bars should align with the core brand palette (e.g. progress bar active highlight is in `Google Blue #4285F4`).
*   **Casing**: **Sentence Case** is mandatory for all menus and subtitles.

---

## 2. Captions and Subtitles (Mandatory)

In accordance with global standard web policies and Google brand commitments:
*   All marketing video assets must feature **synchronized closed captions** (using WebVTT formats or YouTube's standard caption tracks).
*   Captions must load automatically or be instantly toggled using a highly visible "CC" button inside the player controller panel.
*   Text sizes of captions must scale dynamically to remain legible on smaller mobile screens.

---

## 3. HTML and CSS Structure

```html
<div class="g-video-player" id="player-container">
  <!-- 16:9 responsive video frame -->
  <div class="g-video-wrapper">
    <video class="g-video-element" id="demo-video" poster="pixel-video-poster.jpg" preload="metadata">
      <source src="pixel-video.mp4" type="video/mp4">
      <!-- Closed caption track -->
      <track label="English" kind="subtitles" srclang="en" src="pixel-captions-en.vtt" default>
      Your browser does not support the video tag.
    </video>
    
    <!-- Big Play Overlay button -->
    <button class="g-video-overlay-play" aria-label="Play video" aria-controls="demo-video" id="btn-overlay-play">
      <svg width="32" height="32" viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg>
    </button>
  </div>

  <!-- Custom Player Control Panel -->
  <div class="g-player-controls">
    <button class="g-player-btn" aria-label="Play" id="btn-play-pause">
      <svg width="24" height="24" viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg>
    </button>
    
    <div class="g-player-progress-container" role="slider" aria-label="Time elapsed" aria-valuemin="0" aria-valuemax="100" aria-valuenow="0">
      <div class="g-player-progress-bar">
        <div class="g-player-progress-active" style="width: 0%"></div>
      </div>
    </div>
    
    <button class="g-player-btn" aria-label="Toggle mute" id="btn-mute">
      <svg width="24" height="24" viewBox="0 0 24 24"><path d="M3 9v6h4l5 5V4L7 9H3zm13.5 3c0-1.77-1.02-3.29-2.5-4.03v8.05c1.48-.73 2.5-2.25 2.5-4.02z"/></svg>
    </button>
    
    <button class="g-player-btn" aria-label="Toggle captions" id="btn-cc">CC</button>
  </div>
</div>
```

```css
.g-video-player {
  width: 100%;
  max-width: 800px;
  background-color: #000000;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 1px 3px rgba(0,0,0,0.3);
  font-family: 'Roboto', Arial, sans-serif;
}
.g-video-wrapper {
  position: relative;
  width: 100%;
  padding-top: 56.25%; /* 16:9 Aspect Ratio */
}
.g-video-element {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
}

/* Centered big play button overlay */
.g-video-overlay-play {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 64px;
  height: 64px;
  border-radius: 50%;
  background-color: #FFFFFF;
  border: none;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 2px 10px rgba(0,0,0,0.3);
  transition: transform 0.15s ease-in-out;
  color: #202124;
}
.g-video-overlay-play:hover {
  transform: translate(-50%, -50%) scale(1.1);
}
.g-video-overlay-play svg {
  fill: currentColor;
  margin-left: 4px; /* Center the visual offset of play triangle */
}

/* Control bar styling */
.g-player-controls {
  display: flex;
  align-items: center;
  background-color: #202124;
  padding: 8px 16px;
  gap: 16px;
}
.g-player-btn {
  background: none;
  border: none;
  cursor: pointer;
  color: #FFFFFF;
  font-size: 14px;
  font-weight: 700;
  display: flex;
  align-items: center;
}
.g-player-btn svg {
  fill: currentColor;
}
.g-player-progress-container {
  flex-grow: 1;
  height: 8px;
  background-color: #5F6368;
  border-radius: 4px;
  position: relative;
  cursor: pointer;
}
.g-player-progress-bar {
  width: 100%;
  height: 100%;
  position: relative;
}
.g-player-progress-active {
  position: absolute;
  top: 0;
  left: 0;
  height: 100%;
  background-color: #4285F4; /* Google Blue progress */
  border-radius: 4px;
}
```

---

## 4. Accessibility Checklist

*   **Keyboard Controls**: Keyboard users must be able to operate player actions fully:
    *   `Space` or `Enter` must toggle play/pause when focused on the player window.
    *   `ArrowUp` / `ArrowDown` keys adjust volume settings.
    *   `ArrowRight` / `ArrowLeft` seek forward and backward through the timeline.
    *   `Tab` navigates through buttons (Play, Mute, CC) in order.
*   **Synchronized Captions**: Do not launch marketing videos without valid `<track>` tags referencing compliant closed caption files.
*   **State Announcements**: Toggle controls (like Mute and Play) must carry dynamic `aria-label` updates on state change (e.g. toggle `aria-label="Unmute"` when muted, and `aria-label="Mute"` when sound is active).
*   **Auto-play block**: Never auto-play video players with audio. Instant audio on load is a critical failure that violates accessibility standards.
*   **Transcript Links**: Include a text-transcript download link near the player container to assist users with hearing and cognitive impairments.
