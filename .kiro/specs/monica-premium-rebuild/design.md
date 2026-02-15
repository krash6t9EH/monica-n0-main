# Design Document: Monica Premium Rebuild

## Overview

This design specifies the architecture and implementation approach for rebuilding Monica Neural Systems as an ultra-premium 2026 website. The site features a "Liquid Glass Medical-Tech" aesthetic with advanced animations, interactive elements, and cutting-edge web technologies. The design prioritizes visual impact, smooth performance, and accessibility while showcasing Monica's AI companion technology for the senior care market.

The website will be built as a Next.js 15+ application with React Server Components, deployed to Azure infrastructure, and optimized for both performance and visual excellence.

## Architecture

### High-Level Architecture

```
┌─────────────────────────────────────────────────────────┐
│                     Browser Client                       │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  │
│  │   Next.js    │  │    GSAP      │  │  Three.js    │  │
│  │   Pages      │  │  Animations  │  │   Shaders    │  │
│  └──────────────┘  └──────────────┘  └──────────────┘  │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  │
│  │   Framer     │  │    Lenis     │  │ View Trans.  │  │
│  │   Motion     │  │    Scroll    │  │     API      │  │
│  └──────────────┘  └──────────────┘  └──────────────┘  │
└─────────────────────────────────────────────────────────┘
                          │
                          │ HTTPS
                          ▼
┌─────────────────────────────────────────────────────────┐
│              Azure Static Web Apps / App Service         │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  │
│  │   Next.js    │  │    Azure     │  │    Azure     │  │
│  │     SSR      │  │  Functions   │  │    Comms     │  │
│  └──────────────┘  └──────────────┘  └──────────────┘  │
└─────────────────────────────────────────────────────────┘
```

### Technology Stack

**Frontend Framework:**
- Next.js 15+ with App Router and React Server Components
- TypeScript for type safety
- React 19+ for UI components

**Styling:**
- TailwindCSS v4 for utility-first styling
- CSS custom properties for theming
- PostCSS for processing

**Animation Libraries:**
- GSAP 3.12+ with ScrollTrigger plugin for scroll animations
- Framer Motion 11+ for micro-interactions and component animations
- Lenis 1.0+ for smooth scrolling

**3D Graphics:**
- Three.js for WebGL rendering
- Custom GLSL shaders for neural network particle system
- React Three Fiber for React integration

**Page Transitions:**
- View Transitions API (with fallback for unsupported browsers)
- Framer Motion for transition orchestration

**Form Handling:**
- React Hook Form for form state management
- Zod for validation schemas

**Backend:**
- Azure Functions (Node.js runtime) for contact form processing
- Azure Communication Services for email delivery

**Deployment:**
- Azure Static Web Apps (preferred) or Azure App Service
- GitHub Actions for CI/CD

## Components and Interfaces

### Core Layout Components

#### 1. RootLayout Component
```typescript
interface RootLayoutProps {
  children: React.ReactNode;
}

// Provides global layout structure, font loading, and smooth scroll initialization
```

#### 2. SmoothScrollProvider Component
```typescript
interface SmoothScrollProviderProps {
  children: React.ReactNode;
}

// Initializes Lenis smooth scrolling and integrates with GSAP ScrollTrigger
```

#### 3. ViewTransitionProvider Component
```typescript
interface ViewTransitionProviderProps {
  children: React.ReactNode;
}

// Wraps navigation with View Transitions API support
```

### Section Components

#### 4. HeroSection Component
```typescript
interface HeroSectionProps {
  title: string;
  subtitle: string;
  ctaButtons: Array<{
    label: string;
    href: string;
    variant: 'primary' | 'secondary';
  }>;
}

// Full-viewport hero with shader background and animated text
```

#### 5. ShaderBackground Component
```typescript
interface ShaderBackgroundProps {
  mouseInteractive: boolean;
  particleCount: number;
  colorScheme: {
    primary: string;
    accent: string;
  };
}

// Three.js canvas with GLSL shader for neural network animation
```

#### 6. ProblemSection Component
```typescript
interface ProblemSectionProps {
  statistics: Array<{
    value: string;
    label: string;
    animationDelay: number;
  }>;
}

// Scroll-triggered section with animated statistics
```

#### 7. SolutionGrid Component
```typescript
interface SolutionGridProps {
  features: Array<{
    icon: React.ReactNode;
    title: string;
    description: string;
  }>;
}

// Grid of liquid glass feature cards with stagger animation
```

#### 8. LiquidGlassCard Component
```typescript
interface LiquidGlassCardProps {
  children: React.ReactNode;
  hoverable?: boolean;
  className?: string;
}

// Reusable card with frosted glass effect and hover animations
```

#### 9. WellnessSimulator Component
```typescript
interface WellnessSimulatorProps {
  minHours: number;
  maxHours: number;
  defaultHours: number;
}

interface WellnessMetrics {
  happinessIndex: number;
  medicationErrorRisk: number;
  clinicalCareNeed: number;
}

// Interactive slider with real-time gauge updates
```

#### 10. CircularGauge Component
```typescript
interface CircularGaugeProps {
  value: number; // 0-100
  label: string;
  color: string;
  direction: 'increase' | 'decrease'; // Visual indicator of good/bad
}

// Animated circular progress gauge
```

#### 11. TechnologyDiagram Component
```typescript
interface TechnologyNode {
  id: string;
  label: string;
  position: { x: number; y: number };
}

interface TechnologyConnection {
  from: string;
  to: string;
}

interface TechnologyDiagramProps {
  nodes: TechnologyNode[];
  connections: TechnologyConnection[];
}

// Animated architecture diagram with pulsing nodes and connecting lines
```

#### 12. DataSovereigntySection Component
```typescript
interface DataSovereigntyProps {
  badges: Array<{
    name: string;
    icon: React.ReactNode;
  }>;
}

// Trust and compliance messaging with animated badges
```

#### 13. MarketSection Component
```typescript
interface MarketSectionProps {
  marketSize: string;
  growthData: Array<{
    year: number;
    value: number;
  }>;
  keyStats: Array<{
    label: string;
    value: string;
  }>;
}

// Market opportunity visualization with animated chart
```

#### 14. ContactForm Component
```typescript
interface ContactFormData {
  name: string;
  email: string;
  company: string;
  message: string;
}

interface ContactFormProps {
  onSubmit: (data: ContactFormData) => Promise<void>;
}

// Liquid glass styled form with validation and success animation
```

#### 15. AnimatedCounter Component
```typescript
interface AnimatedCounterProps {
  target: number;
  suffix?: string;
  prefix?: string;
  duration?: number;
  triggerOnScroll?: boolean;
}

// Number that animates from 0 to target value
```

#### 16. ScrollIndicator Component
```typescript
interface ScrollIndicatorProps {
  variant: 'pulse' | 'bounce';
}

// Animated scroll prompt at bottom of hero
```

### Utility Components

#### 17. CTAButton Component
```typescript
interface CTAButtonProps {
  children: React.ReactNode;
  href?: string;
  onClick?: () => void;
  variant: 'primary' | 'secondary';
  size?: 'sm' | 'md' | 'lg';
}

// Liquid glass button with tactile hover effects
```

#### 18. TrustBadge Component
```typescript
interface TrustBadgeProps {
  name: string;
  icon: React.ReactNode;
  animationDelay?: number;
}

// Compliance badge with scroll-triggered animation
```

## Data Models

### Contact Form Submission

```typescript
interface ContactFormSubmission {
  name: string;
  email: string;
  company: string;
  message: string;
  timestamp: Date;
  source: 'contact_form' | 'demo_request';
}

// Validation rules:
// - name: required, 2-100 characters
// - email: required, valid email format
// - company: optional, max 100 characters
// - message: required, 10-1000 characters
```

### Wellness Simulation Data

```typescript
interface WellnessSimulationInput {
  hoursPerDay: number; // 0-24
}

interface WellnessSimulationOutput {
  happinessIndex: number; // 0-100
  medicationErrorRisk: number; // 0-100
  clinicalCareNeed: number; // 0-100
}

// Calculation formulas:
// happinessIndex = min(100, 40 + (hoursPerDay * 8))
// medicationErrorRisk = max(0, 80 - (hoursPerDay * 10))
// clinicalCareNeed = max(0, 70 - (hoursPerDay * 9))
```

### Technology Architecture Data

```typescript
interface TechnologyArchitecture {
  nodes: Array<{
    id: string;
    label: string;
    category: 'azure' | 'monica' | 'storage' | 'capability';
    position: { x: number; y: number };
  }>;
  connections: Array<{
    from: string;
    to: string;
    label?: string;
  }>;
}

// Static data structure for the technology diagram
```

### Market Data

```typescript
interface MarketData {
  totalMarketSize: number; // in trillions
  growthRate: number; // percentage
  timeline: Array<{
    year: number;
    marketSize: number;
  }>;
  keyMetrics: Array<{
    label: string;
    value: string;
    trend: 'up' | 'down' | 'stable';
  }>;
}
```

## Correctness Properties

*A property is a characteristic or behavior that should hold true across all valid executions of a system—essentially, a formal statement about what the system should do. Properties serve as the bridge between human-readable specifications and machine-verifiable correctness guarantees.*


### Property Reflection

After analyzing all acceptance criteria, I've identified the following consolidations:

**Redundancy Analysis:**
- Properties 5.3, 5.4, 5.5 (individual gauge behaviors) can be combined into one comprehensive property about wellness calculation correctness
- Properties 1.1, 1.2 (glass effects and hover feedback) are both about consistent liquid glass styling and can be combined
- Properties 3.1, 4.2, 6.3, 7.5, 8.4 (various scroll-triggered animations) share the same underlying mechanism and can be validated by one property about ScrollTrigger integration
- Properties 6.4, 6.5 (node pulsing and connection animations) are both about diagram animation and can be combined
- Properties 11.2, 11.3, 11.4 (various animation library usage) are implementation details that can be verified together
- Properties 12.4, 12.5 (keyboard navigation and ARIA labels) are both accessibility concerns that can be combined

**Properties to Keep as Separate:**
- Color system validation (1.3) - unique validation of design tokens
- Font usage (1.4) - unique typography validation
- Mouse interactivity (2.3) - specific shader behavior
- Navigation transitions (2.8) - specific View Transitions API usage
- Form validation (9.5) - comprehensive input validation across all fields
- Form submission (9.3, 9.4) - API integration and success handling
- Content exclusion (6.2) - specific negative test for NVIDIA references
- Wellness simulator reactivity (5.2) - real-time gauge updates
- Card structure (4.5) - component composition validation

### Correctness Properties

**Property 1: Liquid Glass Consistency**
*For any* interactive component (card, button, form input), the rendered output should include frosted glass styling (backdrop-blur CSS) and hover interactions should trigger lift transforms and shadow changes.
**Validates: Requirements 1.1, 1.2**

**Property 2: Color System Compliance**
*For any* color value used in the application's styles, that color should match one of the specified design tokens: #0a1628 (navy), #3b82f6 (blue), #7c3aed (purple), or rgba(255,255,255,0.05) (glass), or be derived from these base colors.
**Validates: Requirements 1.3**

**Property 3: Typography Consistency**
*For any* heading element (h1-h6), the computed font-family should be "Cal Sans", and for any body text element (p, span, div with text), the computed font-family should be "Inter".
**Validates: Requirements 1.4**

**Property 4: Shader Mouse Reactivity**
*For any* mouse movement event over the hero section, the shader uniforms (mouse position) should update to reflect the new mouse coordinates within a single frame.
**Validates: Requirements 2.3**

**Property 5: View Transitions on Navigation**
*For any* navigation action triggered by CTA buttons or links, the View Transitions API should be invoked (or fallback animation should trigger if unsupported).
**Validates: Requirements 2.8**

**Property 6: Scroll-Triggered Animation Activation**
*For any* section with scroll-triggered animations (Problem, Solution, Technology, Data Sovereignty, Market), when that section enters the viewport, GSAP ScrollTrigger should activate the associated animations.
**Validates: Requirements 3.1, 4.2, 6.3, 7.5, 8.4**

**Property 7: Parallax Transform Application**
*For any* section with parallax effects (Problem, Data Sovereignty), scrolling should apply CSS transforms to background elements proportional to scroll distance.
**Validates: Requirements 3.5, 7.6**

**Property 8: Card Hover Interactions**
*For any* Liquid_Glass_Card component, hovering should trigger a lift transform (translateY negative value) and increase box-shadow intensity.
**Validates: Requirements 4.4**

**Property 9: Card Structure Completeness**
*For any* feature card in the Solution grid, the rendered output should contain three child elements: an icon, a title, and a description.
**Validates: Requirements 4.5**

**Property 10: Wellness Simulator Reactivity**
*For any* slider value change in the Wellness Simulator, all three gauges (Happiness Index, Medication Error Risk, Clinical Care Need) should update their displayed values within 100ms.
**Validates: Requirements 5.2**

**Property 11: Wellness Calculation Correctness**
*For any* slider value H (hours per day, 0-24):
- Happiness Index = min(100, 40 + (H × 8))
- Medication Error Risk = max(0, 80 - (H × 10))
- Clinical Care Need = max(0, 70 - (H × 9))

All three calculations should produce values in the range [0, 100].
**Validates: Requirements 5.3, 5.4, 5.5**

**Property 12: GSAP Animation Usage**
*For any* animated gauge fill in the Wellness Simulator, the animation should be implemented using GSAP tweens (verifiable by checking for GSAP timeline or tween instances).
**Validates: Requirements 5.7**

**Property 13: Content Exclusion**
*For any* text content rendered in the Technology Diagram section, the string "NVIDIA" should not appear.
**Validates: Requirements 6.2**

**Property 14: Diagram Animation Completeness**
*For any* node in the Technology Diagram, the node should have a continuous pulse animation (scale or opacity oscillation), and for any connection between nodes, an animated line (SVG path with stroke-dashoffset animation or similar) should be rendered.
**Validates: Requirements 6.4, 6.5**

**Property 15: Form Submission Integration**
*For any* valid Contact Form submission, an HTTP POST request should be sent to the Azure Functions endpoint with the form data as JSON payload.
**Validates: Requirements 9.3**

**Property 16: Form Success State**
*For any* successful form submission (HTTP 200 response), the form should transition to a success state with animated confirmation message within 500ms.
**Validates: Requirements 9.4**

**Property 17: Form Validation Feedback**
*For any* invalid form input (empty required field, invalid email format, message too short), the form should display field-specific error messages with animation.
**Validates: Requirements 9.5**

**Property 18: Animation Library Integration**
*For any* page load, the application should initialize Lenis for smooth scrolling, GSAP ScrollTrigger for scroll animations, and Framer Motion for component animations (verifiable by checking for library instances in window/global scope).
**Validates: Requirements 11.1, 11.2, 11.3, 11.4**

**Property 19: Keyboard Accessibility**
*For any* interactive element (button, link, form input), the element should be reachable via Tab key navigation and should have visible focus indicators.
**Validates: Requirements 12.4**

**Property 20: ARIA Label Presence**
*For any* interactive element without visible text labels (icon buttons, form inputs), the element should have an aria-label or aria-labelledby attribute.
**Validates: Requirements 12.5**

## Error Handling

### Client-Side Error Handling

**Form Validation Errors:**
- Display inline error messages for invalid inputs
- Prevent form submission until all validation passes
- Use Zod schemas for type-safe validation
- Provide clear, actionable error messages

**Animation Errors:**
- Gracefully degrade if GSAP or Framer Motion fail to load
- Provide CSS fallback animations for critical UI elements
- Log animation errors to console in development mode

**Shader Rendering Errors:**
- Detect WebGL support on page load
- Fall back to static gradient background if WebGL unavailable
- Display user-friendly message if Three.js fails to initialize

**View Transitions API Fallback:**
- Detect browser support for View Transitions API
- Fall back to Framer Motion page transitions if unsupported
- Ensure navigation works even without transitions

### Server-Side Error Handling

**Form Submission Errors:**
- Handle network failures with retry logic (max 3 attempts)
- Display user-friendly error messages for server errors
- Log detailed error information for debugging
- Validate input on server-side even if client validation passes

**Azure Functions Error Handling:**
- Return appropriate HTTP status codes (400 for validation, 500 for server errors)
- Include error messages in response body
- Log errors to Azure Application Insights
- Implement rate limiting to prevent abuse

**Email Delivery Errors:**
- Queue failed email sends for retry
- Log delivery failures to monitoring system
- Provide fallback contact method if email fails
- Return success to user even if email queuing succeeds (don't block on delivery)

### Performance Error Handling

**Large Asset Loading:**
- Implement lazy loading for images and heavy components
- Show loading skeletons while content loads
- Provide fallback content if assets fail to load
- Optimize images with Next.js Image component

**Animation Performance:**
- Monitor frame rate and disable heavy animations if FPS drops below 30
- Use will-change CSS property sparingly
- Implement intersection observers to only animate visible elements
- Provide reduced motion mode for users with motion sensitivity

## Testing Strategy

### Dual Testing Approach

This project requires both unit tests and property-based tests for comprehensive coverage:

**Unit Tests** focus on:
- Specific examples of component rendering
- Edge cases in form validation
- Integration between animation libraries
- Error conditions and fallback behavior
- Specific content requirements (e.g., "footer contains copyright text")

**Property-Based Tests** focus on:
- Universal properties that hold for all inputs
- Calculation correctness (wellness simulator formulas)
- Consistent styling across all components
- Animation behavior across all scroll positions
- Form validation across all possible invalid inputs

Together, these approaches provide comprehensive coverage: unit tests catch concrete bugs in specific scenarios, while property tests verify general correctness across the entire input space.

### Property-Based Testing Configuration

**Library Selection:**
- Use **fast-check** for TypeScript/JavaScript property-based testing
- Fast-check integrates well with Jest/Vitest and provides excellent TypeScript support

**Test Configuration:**
- Each property test MUST run minimum 100 iterations
- Use deterministic seeds for reproducible test runs
- Configure timeouts appropriately for animation tests (may need longer timeouts)

**Test Tagging:**
Each property-based test must include a comment tag referencing the design document:

```typescript
// Feature: monica-premium-rebuild, Property 11: Wellness Calculation Correctness
test('wellness calculations produce valid ranges for all inputs', () => {
  fc.assert(
    fc.property(fc.integer({ min: 0, max: 24 }), (hours) => {
      const metrics = calculateWellnessMetrics(hours);
      expect(metrics.happinessIndex).toBeGreaterThanOrEqual(0);
      expect(metrics.happinessIndex).toBeLessThanOrEqual(100);
      // ... more assertions
    }),
    { numRuns: 100 }
  );
});
```

### Unit Testing Strategy

**Component Testing:**
- Test each section component renders without errors
- Test specific content requirements (hero text, feature titles, etc.)
- Test component props and variants
- Use React Testing Library for component tests

**Integration Testing:**
- Test form submission flow end-to-end
- Test scroll animation triggers with mocked scroll events
- Test navigation with View Transitions API
- Test Azure Functions locally with emulator

**Visual Regression Testing:**
- Use Playwright or Chromatic for visual regression tests
- Capture screenshots of each section in different viewport sizes
- Test hover states and animations
- Verify liquid glass effects render correctly

**Accessibility Testing:**
- Run axe-core automated accessibility tests
- Test keyboard navigation manually
- Verify ARIA labels with screen reader testing
- Test with reduced motion preferences

**Performance Testing:**
- Run Lighthouse CI in GitHub Actions
- Set performance budget: LCP < 2.5s, FID < 100ms, CLS < 0.1
- Test on throttled network and CPU
- Monitor bundle size with size-limit

### Testing Tools

- **Test Runner:** Vitest (fast, Vite-native)
- **Component Testing:** React Testing Library
- **Property Testing:** fast-check
- **E2E Testing:** Playwright
- **Visual Testing:** Playwright screenshots
- **Accessibility:** axe-core, pa11y
- **Performance:** Lighthouse CI

### Test Coverage Goals

- Unit test coverage: 80%+ for business logic
- Property test coverage: All calculation functions and validation logic
- E2E test coverage: All critical user paths (form submission, navigation)
- Accessibility: 100% of interactive elements tested

## Implementation Notes

### Animation Performance Optimization

1. **Use CSS transforms and opacity** for animations (GPU-accelerated)
2. **Implement intersection observers** to only animate visible elements
3. **Use will-change sparingly** and remove after animation completes
4. **Batch DOM reads and writes** to avoid layout thrashing
5. **Use requestAnimationFrame** for custom animations

### Liquid Glass Effect Implementation

The liquid glass effect requires careful layering:

```css
.liquid-glass {
  background: rgba(255, 255, 255, 0.05);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
}
```

### GLSL Shader Considerations

- Keep particle count reasonable (< 1000) for mobile performance
- Use instanced rendering for particles
- Implement LOD (Level of Detail) based on device capabilities
- Provide static fallback for low-end devices

### Accessibility Considerations

- Provide `prefers-reduced-motion` media query support
- Ensure all animations can be disabled
- Maintain 4.5:1 contrast ratio for text
- Provide keyboard shortcuts for navigation
- Test with screen readers (NVDA, JAWS, VoiceOver)

### Azure Deployment Considerations

**Static Web Apps vs App Service:**
- Use Static Web Apps if all pages can be pre-rendered or client-rendered
- Use App Service if server-side rendering is required for dynamic content
- Static Web Apps is more cost-effective for mostly static sites

**Environment Variables:**
- Store Azure Functions connection strings in Azure Key Vault
- Use different environments for dev/staging/production
- Never commit secrets to repository

**CI/CD Pipeline:**
- Use GitHub Actions for automated deployment
- Run tests before deployment
- Implement preview deployments for pull requests
- Use Azure CDN for global content delivery

### Content Migration

Preserve existing content by:
1. Moving `pitch/` and `info/` folders to `public/` directory
2. Creating routes for existing content (`/pitch`, `/info`)
3. Keeping `monica.agent.md` and `foundry_mcp.py` in project root
4. Updating any internal links to new structure

### Font Loading Strategy

Use Next.js font optimization:
```typescript
import { Inter } from 'next/font/google';
import localFont from 'next/font/local';

const inter = Inter({ subsets: ['latin'], variable: '--font-inter' });
const calSans = localFont({
  src: './fonts/CalSans-SemiBold.woff2',
  variable: '--font-cal-sans',
});
```

### Responsive Design Breakpoints

```typescript
const breakpoints = {
  sm: '640px',   // Mobile landscape
  md: '768px',   // Tablet
  lg: '1024px',  // Desktop
  xl: '1280px',  // Large desktop
  '2xl': '1536px', // Extra large
};
```

Optimize animations and shader complexity for mobile devices.
