# Implementation Plan: Monica Premium Rebuild

## Overview

This implementation plan breaks down the Monica Premium Rebuild into discrete, incremental coding tasks. The approach follows a bottom-up strategy: establish the foundation (Next.js setup, design system), build reusable components (liquid glass cards, animations), then compose sections, and finally integrate everything. Each task builds on previous work, with testing integrated throughout to catch issues early.

## Tasks

- [ ] 1. Initialize Next.js 15 project with TypeScript and core dependencies
  - Create new Next.js 15+ project with App Router and TypeScript
  - Install and configure TailwindCSS v4
  - Install animation libraries: GSAP (with ScrollTrigger), Framer Motion, Lenis
  - Install Three.js and React Three Fiber for shader background
  - Install form libraries: React Hook Form, Zod
  - Install testing libraries: Vitest, React Testing Library, fast-check, Playwright
  - Configure TypeScript with strict mode
  - Set up ESLint and Prettier
  - _Requirements: 13.1, 13.2, 13.3, 13.4, 13.5, 13.6, 13.7, 13.8_

- [ ] 2. Set up design system and global styles
  - [ ] 2.1 Create design tokens file with color system and typography
    - Define CSS custom properties for colors: navy (#0a1628), blue (#3b82f6), purple (#7c3aed), glass (rgba(255,255,255,0.05))
    - Configure Cal Sans font (local) and Inter font (Google Fonts) with Next.js font optimization
    - Create Tailwind theme extension with design tokens
    - _Requirements: 1.3, 1.4_
  
  - [ ]* 2.2 Write property test for color system compliance
    - **Property 2: Color System Compliance**
    - **Validates: Requirements 1.3**
  
  - [ ]* 2.3 Write property test for typography consistency
    - **Property 3: Typography Consistency**
    - **Validates: Requirements 1.4**

- [ ] 3. Create core layout and providers
  - [ ] 3.1 Implement RootLayout with font loading and metadata
    - Create app/layout.tsx with Cal Sans and Inter fonts
    - Add viewport meta tags and SEO metadata
    - _Requirements: 1.4, 13.1_
  
  - [ ] 3.2 Implement SmoothScrollProvider with Lenis
    - Create component that initializes Lenis on mount
    - Integrate Lenis with GSAP ScrollTrigger
    - Handle cleanup on unmount
    - _Requirements: 11.1, 11.3_
  
  - [ ] 3.3 Implement ViewTransitionProvider for page navigation
    - Create wrapper component for View Transitions API
    - Implement fallback for unsupported browsers using Framer Motion
    - _Requirements: 11.2_
  
  - [ ]* 3.4 Write property test for animation library integration
    - **Property 18: Animation Library Integration**
    - **Validates: Requirements 11.1, 11.2, 11.3, 11.4**

- [ ] 4. Build liquid glass component system
  - [ ] 4.1 Create LiquidGlassCard component
    - Implement frosted glass effect with backdrop-blur
    - Add hover animations (lift transform, shadow, glow)
    - Make component flexible with className prop
    - _Requirements: 1.1, 1.2_
  
  - [ ] 4.2 Create CTAButton component with variants
    - Implement primary and secondary variants with liquid glass styling
    - Add tactile hover effects (scale, shadow)
    - Support both link and button modes
    - _Requirements: 1.1, 1.2_
  
  - [ ]* 4.3 Write property test for liquid glass consistency
    - **Property 1: Liquid Glass Consistency**
    - **Validates: Requirements 1.1, 1.2**
  
  - [ ]* 4.4 Write property test for card hover interactions
    - **Property 8: Card Hover Interactions**
    - **Validates: Requirements 4.4**
  
  - [ ]* 4.5 Write unit tests for LiquidGlassCard and CTAButton
    - Test component rendering with different props
    - Test hover state changes
    - Test accessibility attributes

- [ ] 5. Checkpoint - Verify design system and core components
  - Ensure all tests pass, ask the user if questions arise.

- [ ] 6. Implement Hero section with shader background
  - [ ] 6.1 Create ShaderBackground component with Three.js
    - Set up Three.js scene, camera, and renderer with React Three Fiber
    - Write GLSL vertex and fragment shaders for neural network particles
    - Implement mouse position tracking and uniform updates
    - Add particle instancing for performance
    - Implement fallback gradient for devices without WebGL
    - _Requirements: 2.2, 2.3, 13.7_
  
  - [ ] 6.2 Create HeroSection component
    - Implement full-viewport layout
    - Add ShaderBackground as background layer
    - Implement text animations (heading slide-in, subtitle fade-in with delay) using Framer Motion
    - Add two CTAButton components: "Investor Pitch Deck" and "Request a Demo"
    - Create ScrollIndicator component with pulse animation
    - _Requirements: 2.1, 2.4, 2.5, 2.6, 2.7_
  
  - [ ]* 6.3 Write property test for shader mouse reactivity
    - **Property 4: Shader Mouse Reactivity**
    - **Validates: Requirements 2.3**
  
  - [ ]* 6.4 Write property test for View Transitions on navigation
    - **Property 5: View Transitions on Navigation**
    - **Validates: Requirements 2.8**
  
  - [ ]* 6.5 Write unit tests for HeroSection
    - Test hero section renders with correct content
    - Test CTA buttons are present with correct labels
    - Test scroll indicator is visible
    - Test WebGL fallback when not supported

- [ ] 7. Implement AnimatedCounter component
  - [ ] 7.1 Create AnimatedCounter with GSAP
    - Implement counter that animates from 0 to target value
    - Support prefix, suffix, and custom duration
    - Add scroll trigger option to start animation on viewport entry
    - Use GSAP for smooth number interpolation
    - _Requirements: 3.2, 3.3, 8.1_
  
  - [ ]* 7.2 Write unit tests for AnimatedCounter
    - Test counter animates to target value
    - Test prefix and suffix rendering
    - Test scroll trigger activation

- [ ] 8. Implement Problem section
  - [ ] 8.1 Create ProblemSection component
    - Implement layout with two AnimatedCounter components
    - Add statistics: "42% of seniors experience dangerous loneliness" and "30,000+ medication error deaths annually"
    - Implement sequential animation with delays using GSAP timeline
    - Add subtle parallax effect to background
    - Use ScrollTrigger to activate animations on scroll
    - _Requirements: 3.1, 3.2, 3.3, 3.4, 3.5_
  
  - [ ]* 8.2 Write property test for scroll-triggered animations
    - **Property 6: Scroll-Triggered Animation Activation**
    - **Validates: Requirements 3.1, 4.2, 6.3, 7.5, 8.4**
  
  - [ ]* 8.3 Write property test for parallax transforms
    - **Property 7: Parallax Transform Application**
    - **Validates: Requirements 3.5, 7.6**

- [ ] 9. Implement Solution section with feature grid
  - [ ] 9.1 Create SolutionGrid component
    - Define 6 features: Persistent Memory, Medication Management, Emotional Companionship, Family Dashboard, Offline Capable (WebNN), Clinical Integration (HIPAA)
    - Create icon components for each feature
    - Implement grid layout with LiquidGlassCard components
    - Add stagger animation on scroll using GSAP and ScrollTrigger
    - _Requirements: 4.1, 4.2, 4.3, 4.5_
  
  - [ ]* 9.2 Write property test for card structure completeness
    - **Property 9: Card Structure Completeness**
    - **Validates: Requirements 4.5**
  
  - [ ]* 9.3 Write unit tests for SolutionGrid
    - Test exactly 6 cards are rendered
    - Test each card contains icon, title, and description
    - Test all feature titles are present

- [ ] 10. Checkpoint - Verify hero, problem, and solution sections
  - Ensure all tests pass, ask the user if questions arise.

- [ ] 11. Implement Wellness Simulator
  - [ ] 11.1 Create wellness calculation functions
    - Implement calculateWellnessMetrics function with formulas:
      - happinessIndex = min(100, 40 + (hours × 8))
      - medicationErrorRisk = max(0, 80 - (hours × 10))
      - clinicalCareNeed = max(0, 70 - (hours × 9))
    - Add TypeScript types for input/output
    - _Requirements: 5.3, 5.4, 5.5_
  
  - [ ]* 11.2 Write property test for wellness calculation correctness
    - **Property 11: Wellness Calculation Correctness**
    - **Validates: Requirements 5.3, 5.4, 5.5**
  
  - [ ] 11.3 Create CircularGauge component
    - Implement circular progress visualization with SVG
    - Add GSAP animation for fill transitions
    - Support direction indicator (increase/decrease is good)
    - Add color prop for customization
    - _Requirements: 5.7_
  
  - [ ]* 11.4 Write property test for GSAP animation usage
    - **Property 12: GSAP Animation Usage**
    - **Validates: Requirements 5.7**
  
  - [ ] 11.5 Create WellnessSimulator component
    - Implement slider input for hours (0-24)
    - Display three CircularGauge components
    - Connect slider to calculation function
    - Update gauges in real-time on slider change
    - Wrap in LiquidGlassCard
    - _Requirements: 5.1, 5.2, 5.6_
  
  - [ ]* 11.6 Write property test for wellness simulator reactivity
    - **Property 10: Wellness Simulator Reactivity**
    - **Validates: Requirements 5.2**
  
  - [ ]* 11.7 Write unit tests for WellnessSimulator
    - Test slider renders with correct range
    - Test all three gauges are present
    - Test initial values are correct

- [ ] 12. Implement Technology Diagram section
  - [ ] 12.1 Create technology architecture data structure
    - Define nodes: Azure AI Foundry, Monica Brain, Azure Voice Live, Monica Speaks, WebNN, Offline Mode, Cosmos DB, Memory Storage
    - Define connections between nodes
    - Ensure no NVIDIA references
    - _Requirements: 6.1, 6.2_
  
  - [ ] 12.2 Create TechnologyDiagram component
    - Implement SVG-based node and connection rendering
    - Add pulsing animations to nodes using CSS or GSAP
    - Implement animated connection lines (stroke-dashoffset animation)
    - Add scroll-triggered build animation using ScrollTrigger
    - Animate nodes and connections progressively
    - _Requirements: 6.3, 6.4, 6.5_
  
  - [ ]* 12.3 Write property test for content exclusion
    - **Property 13: Content Exclusion**
    - **Validates: Requirements 6.2**
  
  - [ ]* 12.4 Write property test for diagram animation completeness
    - **Property 14: Diagram Animation Completeness**
    - **Validates: Requirements 6.4, 6.5**
  
  - [ ]* 12.5 Write unit tests for TechnologyDiagram
    - Test all nodes are rendered
    - Test connections are drawn between correct nodes
    - Test no NVIDIA text appears

- [ ] 13. Implement Data Sovereignty section
  - [ ] 13.1 Create TrustBadge component
    - Implement badge with icon and label
    - Add scroll-triggered fade-in animation
    - Support animation delay prop for stagger effect
    - _Requirements: 7.5_
  
  - [ ] 13.2 Create DataSovereigntySection component
    - Add Canadian flag visual accent
    - Display shield icon in LiquidGlassCard
    - Add "Your data never leaves Canada" message
    - Display TrustBadge components for HIPAA, SOC2, PIPEDA
    - Implement stagger animation for badges
    - Add subtle parallax to background
    - _Requirements: 7.1, 7.2, 7.3, 7.4, 7.5, 7.6_
  
  - [ ]* 13.3 Write unit tests for DataSovereigntySection
    - Test Canadian flag is displayed
    - Test shield icon is present
    - Test data sovereignty message is displayed
    - Test all three trust badges are rendered

- [ ] 14. Implement Market section
  - [ ] 14.1 Create MarketSection component
    - Add AnimatedCounter for "$3T" market size
    - Create growth chart visualization with SVG
    - Implement GSAP draw animation for chart path
    - Display key statistics in LiquidGlassCard components
    - Use ScrollTrigger to activate all animations
    - _Requirements: 8.1, 8.2, 8.3, 8.4_
  
  - [ ]* 14.2 Write unit tests for MarketSection
    - Test market size counter is displayed
    - Test growth chart is rendered
    - Test statistics cards are present

- [ ] 15. Checkpoint - Verify all content sections
  - Ensure all tests pass, ask the user if questions arise.

- [ ] 16. Implement Contact Form with Azure Functions backend
  - [ ] 16.1 Create form validation schema with Zod
    - Define schema for name (required, 2-100 chars), email (required, valid format), company (optional, max 100 chars), message (required, 10-1000 chars)
    - Export TypeScript types from schema
    - _Requirements: 9.1_
  
  - [ ] 16.2 Create ContactForm component
    - Implement form with React Hook Form
    - Style inputs with liquid glass aesthetic
    - Add real-time validation with error messages
    - Implement animated validation feedback
    - Add loading state during submission
    - Implement animated success state
    - _Requirements: 9.1, 9.2, 9.4, 9.5_
  
  - [ ]* 16.3 Write property test for form validation feedback
    - **Property 17: Form Validation Feedback**
    - **Validates: Requirements 9.5**
  
  - [ ]* 16.4 Write unit tests for ContactForm
    - Test all form fields are rendered
    - Test validation errors display for invalid inputs
    - Test form submission is prevented when invalid
    - Test success state displays after submission
  
  - [ ] 16.5 Create Azure Function for form submission
    - Create HTTP trigger function in TypeScript
    - Implement server-side validation with Zod
    - Integrate Azure Communication Services for email delivery
    - Add error handling and logging
    - Return appropriate HTTP status codes
    - _Requirements: 9.3, 9.6_
  
  - [ ]* 16.6 Write property test for form submission integration
    - **Property 15: Form Submission Integration**
    - **Validates: Requirements 9.3**
  
  - [ ]* 16.7 Write property test for form success state
    - **Property 16: Form Success State**
    - **Validates: Requirements 9.4**
  
  - [ ]* 16.8 Write integration tests for form submission flow
    - Test form submits data to Azure Function
    - Test success response triggers success state
    - Test error response displays error message
    - Test retry logic on network failure

- [ ] 17. Implement Footer section
  - [ ] 17.1 Create Footer component
    - Add copyright text: "© 2026 Monica Neural Systems - Regina, Saskatchewan, Canada"
    - Implement subtle neural network pattern background (CSS or SVG)
    - Style with liquid glass aesthetic
    - _Requirements: 10.1, 10.2_
  
  - [ ]* 17.2 Write unit tests for Footer
    - Test copyright text is displayed
    - Test neural network pattern is rendered

- [ ] 18. Implement accessibility features
  - [ ] 18.1 Add keyboard navigation support
    - Ensure all interactive elements are keyboard accessible
    - Add visible focus indicators to all focusable elements
    - Implement skip-to-content link
    - Test tab order is logical
    - _Requirements: 12.4_
  
  - [ ] 18.2 Add ARIA labels and semantic HTML
    - Add aria-label to icon buttons and decorative elements
    - Use semantic HTML elements (nav, main, section, article)
    - Add aria-live regions for dynamic content updates
    - Ensure form inputs have associated labels
    - _Requirements: 12.5_
  
  - [ ] 18.3 Implement reduced motion support
    - Add prefers-reduced-motion media query support
    - Disable or simplify animations when reduced motion is preferred
    - Ensure core functionality works without animations
    - _Requirements: 12.1, 12.2_
  
  - [ ]* 18.4 Write property test for keyboard accessibility
    - **Property 19: Keyboard Accessibility**
    - **Validates: Requirements 12.4**
  
  - [ ]* 18.5 Write property test for ARIA label presence
    - **Property 20: ARIA Label Presence**
    - **Validates: Requirements 12.5**
  
  - [ ]* 18.6 Run automated accessibility tests
    - Use axe-core to test all pages
    - Fix any accessibility violations
    - Verify Lighthouse accessibility score is 90+
    - _Requirements: 12.2_

- [ ] 19. Integrate all sections into main page
  - [ ] 19.1 Create home page with all sections
    - Import and compose all section components in app/page.tsx
    - Ensure proper section ordering: Hero → Problem → Solution → Wellness → Technology → Data Sovereignty → Market → Contact → Footer
    - Verify smooth scrolling works across all sections
    - Test scroll-triggered animations activate correctly
    - _Requirements: All section requirements_
  
  - [ ]* 19.2 Write E2E tests for main page
    - Test page loads without errors
    - Test all sections are visible
    - Test scroll behavior and animations
    - Test navigation between sections
    - Test form submission end-to-end

- [ ] 20. Preserve existing content and configure routing
  - [ ] 20.1 Migrate existing content
    - Move pitch/ folder to public/pitch/
    - Move info/ folder to public/info/
    - Keep monica.agent.md and foundry_mcp.py in project root
    - _Requirements: 15.1, 15.2, 15.3, 15.4_
  
  - [ ] 20.2 Create routes for existing content
    - Create app/pitch/page.tsx to serve pitch content
    - Create app/info/page.tsx to serve info content
    - Update internal links to new structure
    - _Requirements: 15.1, 15.2_
  
  - [ ]* 20.3 Write unit tests for content preservation
    - Test pitch/ and info/ folders exist
    - Test monica.agent.md and foundry_mcp.py exist
    - Test routes serve correct content

- [ ] 21. Checkpoint - Verify complete application
  - Ensure all tests pass, ask the user if questions arise.

- [ ] 22. Performance optimization
  - [ ] 22.1 Optimize images and assets
    - Convert images to WebP format
    - Use Next.js Image component for automatic optimization
    - Implement lazy loading for below-fold images
    - Optimize font loading with font-display: swap
    - _Requirements: 12.3_
  
  - [ ] 22.2 Optimize animations for performance
    - Implement intersection observers to only animate visible elements
    - Use will-change CSS property strategically
    - Reduce particle count on mobile devices
    - Implement LOD for shader based on device capabilities
    - _Requirements: 12.1_
  
  - [ ] 22.3 Optimize bundle size
    - Implement code splitting for heavy components (Three.js, GSAP)
    - Use dynamic imports for below-fold components
    - Analyze bundle with @next/bundle-analyzer
    - Remove unused dependencies
    - _Requirements: 12.1_
  
  - [ ]* 22.4 Run Lighthouse performance tests
    - Test on desktop and mobile
    - Verify performance score is 90+
    - Fix any performance issues identified
    - _Requirements: 12.1_

- [ ] 23. Set up Azure deployment
  - [ ] 23.1 Configure Azure Static Web Apps or App Service
    - Create Azure Static Web App resource (or App Service if SSR needed)
    - Configure custom domain if available
    - Set up SSL certificate
    - Configure environment variables in Azure
    - _Requirements: 14.1, 14.3, 14.4_
  
  - [ ] 23.2 Create GitHub Actions workflow
    - Create .github/workflows/azure-deploy.yml
    - Configure workflow to build Next.js app
    - Run tests before deployment
    - Deploy to Azure on push to main branch
    - Set up preview deployments for pull requests
    - _Requirements: 14.2_
  
  - [ ] 23.3 Configure Azure Functions deployment
    - Deploy contact form Azure Function
    - Configure Azure Communication Services connection
    - Set up Application Insights for logging
    - Test function in production environment
    - _Requirements: 9.3, 9.6_
  
  - [ ]* 23.4 Write deployment verification tests
    - Test production URL is accessible
    - Test all sections load correctly
    - Test form submission works in production
    - Test Azure Function responds correctly

- [ ] 24. Final testing and quality assurance
  - [ ]* 24.1 Run full test suite
    - Run all unit tests
    - Run all property-based tests
    - Run all E2E tests
    - Verify all tests pass
  
  - [ ]* 24.2 Run visual regression tests
    - Capture screenshots of all sections
    - Compare with baseline screenshots
    - Fix any visual regressions
  
  - [ ]* 24.3 Run cross-browser testing
    - Test on Chrome, Firefox, Safari, Edge
    - Test on mobile browsers (iOS Safari, Chrome Mobile)
    - Fix any browser-specific issues
  
  - [ ]* 24.4 Run accessibility audit
    - Test with screen readers (NVDA, JAWS, VoiceOver)
    - Verify keyboard navigation works
    - Run axe-core and pa11y
    - Verify Lighthouse accessibility score is 90+
  
  - [ ]* 24.5 Run performance audit
    - Run Lighthouse on production URL
    - Verify performance score is 90+
    - Test on throttled network and CPU
    - Verify Core Web Vitals meet targets

- [ ] 25. Final checkpoint - Production ready
  - Ensure all tests pass, verify deployment is successful, ask the user if questions arise.

## Notes

- Tasks marked with `*` are optional testing tasks and can be skipped for faster MVP delivery
- Each task references specific requirements for traceability
- Checkpoints ensure incremental validation and provide opportunities to address issues early
- Property tests validate universal correctness properties across all inputs
- Unit tests validate specific examples, edge cases, and integration points
- The implementation follows a bottom-up approach: foundation → components → sections → integration
- All animations should respect prefers-reduced-motion for accessibility
- Performance optimization is integrated throughout, with a dedicated optimization phase before deployment
