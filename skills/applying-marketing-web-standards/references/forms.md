# Forms Guidelines

This reference defines the visual specs, input elements, checkboxes, radio buttons, helper text, and validation rules for Forms on Google-branded marketing websites.

---

## 1. Text Inputs (Material Outlined)

Google marketing websites primarily use the **Material Outlined** text field style, characterized by a clean container outline.

| Attribute | Specification | Notes |
| :--- | :--- | :--- |
| **Height** | `48px` (Standard) or `56px` (Dense layout) | Total height of the input container box |
| **Corner Radius** | `4px` | Standard corner rounding |
| **Border Width** | `1px` (Default) or `2px` (Focused/Active) | Visual outline thickness |
| **Internal Padding**| `16px` left/right, vertical centered | Spacing inside the input box |

### 1.1 Input Color States
*   **Default Empty**: Border `#DADCE0` (Gray 300), Label `#5F6368` (Gray 700).
*   **Hover**: Border `#80868B` (Gray 600).
*   **Focus / Active**: `2px` outline `#4285F4` (Google Blue).
*   **Error**: `2px` outline `#EA4335` (Google Red), Label `#EA4335`.

### 1.2 Dense Layouts and Subscript Collapsing
When form elements are placed inside dense containers (like table cells) where helper text/validation error spacing is not needed, you must collapse the empty reserved subscript wrapper space to prevent vertical alignment shifts:
1. Set `subscriptSizing="dynamic"` on `<mat-form-field>`.
2. Hide the wrapper and center the text container using CSS:
   ```css
   .g-field-dense ::ng-deep .mat-mdc-form-field-subscript-wrapper {
     display: none !important;
   }
   .g-field-dense ::ng-deep .mat-mdc-form-field-infix {
     padding: 8px 0px !important;
     min-height: 40px !important;
   }
   ```

### 1.3 Clean Outlined Number Inputs
For numeric inputs, browser-native spinner buttons must be hidden to maintain a clean, modern appearance. The input text should be centered:
```css
.g-input-number ::ng-deep input {
  text-align: center !important;
}
.g-input-number ::ng-deep input::-webkit-outer-spin-button,
.g-input-number ::ng-deep input::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
}
.g-input-number ::ng-deep input[type=number] {
  -moz-appearance: textfield;
}
```

### 1.4 Content-Proportional Width (The "Content-Proportional Width" Rule)
Input fields should visually match the maximum expected length of the data being inputted to avoid layout bloating and clarify the interface.
*   **Ranking/Quantities**: For short numbers (e.g., final ranks or quantities 1-99), strictly constrain the input field's width.
*   **Implementation**:
    ```css
    .g-input-dense-number {
      max-width: 100px; /* Perfectly sized for a 1-3 digit rank/score */
      text-align: center;
      height: 40px; /* Dense 8px-grid component height */
    }
    ```

---

## 2. Checkboxes

Checkboxes are square selectors used when users can select one or more options from a set of choices.

*   **Size**: `18px` width x `18px` height.
*   **Corner Radius**: `2px` or `3px`.
*   **Colors**: Border `#80868B` unchecked, solid `#4285F4` background with a white checkmark when checked.
*   **Spacing to Label**: `12px` or `16px` gap.

---

## 3. Radio Buttons

Radio buttons are circular selectors used when a user must select exactly one option from a mutually exclusive list.

*   **Size**: `20px` diameter outer ring.
*   **Inner Dot**: `10px` diameter inner selected dot.
*   **Colors**: Outer ring `#80868B` unchecked, outer ring `#4285F4` and inner dot `#4285F4` when checked.

---

## 4. Helper Text & Validation Errors

Supporting texts must be positioned directly underneath the respective input container to guide users.

*   **Typography**: `Roboto Regular, 12px, line-height 16px`.
*   **Helper Color**: `#80868B` (Gray 600).
*   **Error Color**: `#EA4335` (Google Red).
*   **Accessibility**: Link the helper or error text elements to the input using `aria-describedby` referencing the helper element's `id`.

---

## 5. HTML and CSS Implementation

```html
<form class="g-form">
  <!-- Text Input Block -->
  <div class="g-field-wrapper">
    <div class="g-input-container">
      <input type="email" id="user-email" class="g-input-field" placeholder=" " required aria-describedby="email-helper">
      <label for="user-email" class="g-input-label">Email address</label>
    </div>
    <span id="email-helper" class="g-helper-text">Enter your primary work email address</span>
  </div>

  <!-- Checkbox Block -->
  <label class="g-checkbox-container">
    <input type="checkbox" class="g-checkbox-input">
    <span class="g-checkbox-visual"></span>
    <span class="g-checkbox-label">Receive monthly Google Cloud updates</span>
  </label>
</form>
```

```css
.g-field-wrapper {
  display: flex;
  flex-direction: column;
  margin-bottom: 24px;
}
.g-input-container {
  position: relative;
  width: 100%;
  height: 48px;
}
.g-input-field {
  width: 100%;
  height: 100%;
  padding: 12px 16px;
  border: 1px solid #DADCE0;
  border-radius: 4px;
  background-color: #FFFFFF;
  color: #202124;
  font-size: 16px;
  transition: all 0.15s ease-in-out;
}
.g-input-field:focus {
  border: 2px solid #4285F4;
  outline: none;
}
.g-input-label {
  position: absolute;
  left: 16px;
  top: 50%;
  transform: translateY(-50%);
  background-color: #FFFFFF;
  padding: 0 4px;
  color: #5F6368;
  font-size: 16px;
  pointer-events: none;
  transition: all 0.15s cubic-bezier(0.4, 0, 0.2, 1);
}
.g-input-field:focus ~ .g-input-label,
.g-input-field:not(:placeholder-shown) ~ .g-input-label {
  transform: translateY(-28px) scale(0.75);
  color: #4285F4;
}
.g-helper-text {
  font-size: 12px;
  line-height: 16px;
  color: #80868B;
  margin-top: 6px;
  padding-left: 16px;
}

/* Custom Checkbox visual */
.g-checkbox-container {
  display: inline-flex;
  align-items: center;
  cursor: pointer;
  margin-bottom: 16px;
}
.g-checkbox-input {
  position: absolute;
  opacity: 0;
  width: 0;
  height: 0;
}
.g-checkbox-visual {
  width: 18px;
  height: 18px;
  border: 2px solid #80868B;
  border-radius: 2px;
  margin-right: 12px;
  position: relative;
  transition: all 0.15s ease-in-out;
}
.g-checkbox-input:checked ~ .g-checkbox-visual {
  background-color: #4285F4;
  border-color: #4285F4;
}
.g-checkbox-visual::after {
  content: "";
  position: absolute;
  display: none;
  left: 5px;
  top: 1px;
  width: 4px;
  height: 8px;
  border: solid #ffffff;
  border-width: 0 2px 2px 0;
  transform: rotate(45deg);
}
.g-checkbox-input:checked ~ .g-checkbox-visual::after {
  display: block;
}
```

---

## 6. Accessibility Checklist

*   **Explicit Label Connections**: Ensure every input is explicitly bound to a `<label>` using matched `id` and `for` properties.
*   **Error States**: Dynamically append `aria-invalid="true"` to input elements upon validation failures. Set `role="alert"` or `aria-live="polite"` on error message divs to announce errors.
*   **Keyboard Support**: Form components must support `Tab` indexing, and checkbox/radio components must toggle or change via `Space` and `Arrow Keys`.
