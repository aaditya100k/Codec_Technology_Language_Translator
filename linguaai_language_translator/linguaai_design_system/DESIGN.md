---
name: LinguaAI Design System
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#3a3939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#201f1f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353534'
  on-surface: '#e5e2e1'
  on-surface-variant: '#cfc2d6'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#988d9f'
  outline-variant: '#4d4354'
  surface-tint: '#ddb7ff'
  primary: '#ddb7ff'
  on-primary: '#490080'
  primary-container: '#b76dff'
  on-primary-container: '#400071'
  inverse-primary: '#842bd2'
  secondary: '#adc6ff'
  on-secondary: '#002e6a'
  secondary-container: '#0566d9'
  on-secondary-container: '#e6ecff'
  tertiary: '#ffb0cd'
  on-tertiary: '#640039'
  tertiary-container: '#f751a1'
  on-tertiary-container: '#570032'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#f0dbff'
  primary-fixed-dim: '#ddb7ff'
  on-primary-fixed: '#2c0051'
  on-primary-fixed-variant: '#6900b3'
  secondary-fixed: '#d8e2ff'
  secondary-fixed-dim: '#adc6ff'
  on-secondary-fixed: '#001a42'
  on-secondary-fixed-variant: '#004395'
  tertiary-fixed: '#ffd9e4'
  tertiary-fixed-dim: '#ffb0cd'
  on-tertiary-fixed: '#3e0022'
  on-tertiary-fixed-variant: '#8c0053'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353534'
typography:
  display-lg:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  display-lg-mobile:
    fontFamily: Inter
    fontSize: 36px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
    letterSpacing: -0.01em
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-sm:
    fontFamily: Geist
    fontSize: 13px
    fontWeight: '500'
    lineHeight: '1'
    letterSpacing: 0.05em
  mono-code:
    fontFamily: Geist
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 4px
  container-max: 1280px
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: 48px
  stack-xs: 8px
  stack-md: 24px
  stack-xl: 64px
---

## Brand & Style
The design system embodies a futuristic, high-fidelity aesthetic tailored for a cutting-edge AI translation platform. The brand personality is visionary, intelligent, and fluid, aiming to evoke a sense of "magic" through instant, seamless communication.

The visual style is a sophisticated blend of **Glassmorphism** and **Modern Corporate**, utilizing deep obsidian backgrounds to provide a canvas for vibrant, glowing accents. The UI features floating elements, translucent layers with backdrop blurs, and soft, spectral gradients that mimic the movement of data and thought. Every interaction should feel polished and atmospheric, prioritizing high-fidelity transitions that reinforce the "intelligent" nature of the product.

## Colors
This design system utilizes a high-contrast dark palette to emphasize its futuristic narrative.
- **Deep Obsidian (#0a0a0a):** The foundational background color, providing infinite depth.
- **Vibrant Purple (#a855f7):** The primary brand color, used for core actions and active states.
- **Electric Blue (#3b82f6):** The secondary color, used for supportive data visualization and alternate actions.
- **Hot Pink (#ec4899):** The tertiary accent, primarily used in gradients to create a sense of energy and heat.

**Gradients:**
Use a "Neural Flow" gradient for primary buttons and focus states: `linear-gradient(135deg, #a855f7 0%, #3b82f6 50%, #ec4899 100%)`.

## Typography
The typography is systematic and utilitarian, utilizing **Inter** for its exceptional legibility in digital interfaces. For technical or meta-information (like language codes or AI confidence scores), **Geist** is employed to provide a precise, developer-friendly feel.

Headlines should use tighter letter-spacing to feel more "locked-in" and architectural. Body text maintains a generous line-height to ensure readability against dark backgrounds, where eye strain is more prevalent. Use a subtle text-shadow on large display type to ensure it "pops" against glass surfaces.

## Layout & Spacing
The layout follows a **Fluid Grid** philosophy with a focus on "floating" content blocks.
- **Desktop:** 12-column grid with a 1280px max-width. Use generous vertical "stack" spacing (64px+) between major sections to emphasize the airy, futuristic feel.
- **Tablet:** 8-column grid with 24px margins.
- **Mobile:** 4-column grid with 16px margins.

Spacing is based on a 4px scale, but core layout components should favor larger increments (16, 24, 32, 48) to prevent visual clutter. Glass cards should have internal padding of at least 24px to feel premium.

## Elevation & Depth
Depth is created through **Glassmorphism** and **Luminous Shadows** rather than traditional grey drop shadows.

1.  **Base Layer:** Solid `#0a0a0a`.
2.  **Floating Surface (Glass):** `rgba(255, 255, 255, 0.03)` with a `backdrop-filter: blur(12px)`.
3.  **Borders:** Use a 1px solid border `rgba(255, 255, 255, 0.08)` to define edges without adding weight.
4.  **Luminous Glow:** For active or high-priority elements, apply an outer glow using the primary purple: `box-shadow: 0 0 20px rgba(168, 85, 247, 0.15)`.
5.  **Interactive Depth:** On hover, glass surfaces should increase their backdrop-blur and brightness slightly (to `0.06` opacity) to simulate the element lifting toward the user.

## Shapes
The design system uses a **Rounded** shape language to feel approachable and organic.
- **Standard Cards/Containers:** 16px (`rounded-lg`) corner radius.
- **Buttons and Inputs:** 8px (`rounded-md`) for a precise, functional look.
- **Small Accents (Chips/Badges):** Fully pill-shaped to contrast against the structured layout.

## Components
- **Glass Cards:** The primary container. Must have a 1px top-weighted border to catch light, simulating a glass edge.
- **Action Buttons:**
    - *Primary:* "Neural Flow" gradient background with white text.
    - *Secondary:* Ghost style with the 1px glass border and a subtle purple glow on hover.
- **Input Fields:** Darker than the background (`#000000`), with the 1px glass border. On focus, the border transitions to a Blue-to-Purple gradient.
- **Language Chips:** Small, pill-shaped elements with a subtle `rgba(255, 255, 255, 0.05)` fill and Geist typography for the language code (e.g., EN, JP).
- **Floating Translation Toggle:** A central, elevated component using a high-blur glass effect to swap source/target languages, featuring a rotating animation on click.
- **Glow Indicators:** Used next to "AI Active" or "Live Sync" labels—a pulsing `primary_color` dot with a 10px blur radius.