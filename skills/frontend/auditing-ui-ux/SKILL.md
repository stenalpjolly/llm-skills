---
name: auditing-ui-ux
description: >-
  Performs a comprehensive UI/UX design audit on application screens or components. 
  Use when a user asks to review design, audit UI/UX, improve visual hierarchy, or polish an interface. 
  Don't use for code reviews, performance audits, or backend architecture reviews.
---

# UI/UX Auditing Workflow

Follow these steps exactly when conducting a design audit.

## Step 1: Full Audit
Review every screen against these dimensions. Miss nothing.

- **Visual Hierarchy:** Does the eye land where it should? Primary action unmissable? Screen readable in 2 seconds?
- **Spacing & Rhythm:** Consistent, intentional whitespace? Vertical rhythm harmonious?
- **Typography:** Clear size hierarchy? Too many weights competing? Calm or chaotic?
- **Color:** Restraint and purpose? Guiding attention or scattering it? Accessible contrast?
- **Alignment & Grid:** Consistent grid? Anything off by 1–2px? Every element locked in?
- **Components:** Identical styling across screens? Interactive elements obvious? All states covered (hover, focus, disabled)?
- **Iconography:** Consistent style, weight, size? One cohesive set or mixed libraries?
- **Motion:** Natural and purposeful transitions? Any gratuitous animation? Feasible in current stack?
- **Empty States:** Every screen with no data — intentional or broken? User guided to first action?
- **Loading States:** Consistent skeletons/spinners? App feels alive while waiting?
- **Error States:** Styled consistently? Helpful and clear, not hostile and technical?
- **Dark Mode:** If supported — actually designed or just inverted? Tokens/shadows/contrast hold up?
- **Density:** Can anything be removed? Redundant elements? Every element earning its place?
- **Responsiveness:** Works at every viewport? Touch targets sized for thumbs? Fluid adaptation, not just breakpoints?
- **Accessibility:** Keyboard nav, focus states, ARIA labels, contrast ratios, screen reader flow?

## Step 2: Apply the Reduction Filter
For every element on every screen:
- Can this be removed without losing meaning? → Remove it.
- Would a user need to be told this exists? → Redesign until obvious.
- Does this feel inevitable? → If not, it's not done.
- Is visual weight proportional to functional importance? → If not, fix hierarchy.

## Step 3: Compile the Plan
Read `references/audit-template.md` for the exact output format. Organize findings into three phases:
- **Phase 1 — Critical:** Hierarchy, usability, responsiveness, consistency issues that actively hurt UX
- **Phase 2 — Refinement:** Spacing, typography, color, alignment, iconography that elevate the experience
- **Phase 3 — Polish:** Micro-interactions, transitions, empty/loading/error states, dark mode, subtle details

Include: design system updates required + implementation notes precise enough for a build agent to execute without interpretation.

Review `references/design-principles.md` to ensure all recommendations strictly adhere to core UI/UX principles. Refer to `references/common-defects.md` for standard UI defects and their corresponding corrective patterns.

## Step 4: Wait for Approval
Present the plan. **Do not implement anything.**
- User may reorder, cut, or modify any recommendation.
- Execute only what's approved, surgically.
- After each phase: present results for review before moving to the next.
- If the result doesn't feel right, say so. Propose refinement before proceeding.
