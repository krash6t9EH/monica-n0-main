# Requirements Document: Monica Premium Rebuild

## Introduction

This document specifies the requirements for rebuilding Monica Neural Systems as an ultra-premium 2026 website featuring a "Liquid Glass Medical-Tech" aesthetic. The website will showcase Monica's AI companion technology for the senior care market with cutting-edge visual design, smooth animations, and interactive elements that convey trust, innovation, and premium quality.

## Glossary

- **Website**: The Monica Neural Systems marketing and information website
- **Hero_Section**: The full-viewport landing section with shader background
- **Liquid_Glass**: Visual design pattern using frosted glass effects with depth, refraction, and blur
- **GLSL_Shader**: OpenGL Shading Language program for animated neural network background
- **View_Transitions_API**: Browser API for smooth page-to-page transitions
- **GSAP**: GreenSock Animation Platform for scroll-triggered animations
- **Lenis**: Smooth scrolling library
- **ScrollTrigger**: GSAP plugin for scroll-driven animations
- **Wellness_Simulator**: Interactive component showing health impact metrics
- **Azure_AI_Foundry**: Microsoft Azure's AI development platform
- **WebNN**: Web Neural Network API for offline AI capabilities
- **Contact_Form**: User input form for inquiries and demo requests
- **CTA_Button**: Call-to-action button (e.g., "Request a Demo")
- **Trust_Badge**: Visual indicator of compliance or certification
- **Animated_Counter**: Number that animates from zero to target value
- **Liquid_Glass_Card**: Card component with frosted glass aesthetic
- **Neural_Network_Diagram**: Animated visualization of technology architecture

## Requirements

### Requirement 1: Liquid Glass Visual System

**User Story:** As a visitor, I want to experience a premium liquid glass interface, so that I perceive Monica as a cutting-edge, trustworthy technology company.

#### Acceptance Criteria

1. THE Website SHALL apply frosted glass effects with backdrop-blur to all Liquid_Glass_Card components
2. WHEN a user hovers over interactive elements, THE Website SHALL provide tactile feedback through lift animations and shadow changes
3. THE Website SHALL use the specified color system: deep navy primary (#0a1628), soft blue accent (#3b82f6), subtle purple secondary (#7c3aed), and glass overlays with rgba(255,255,255,0.05)
4. THE Website SHALL use Cal Sans font for headings and Inter font for body text
5. THE Website SHALL NOT use flat design or skeuomorphic design patterns

### Requirement 2: Hero Section with Shader Background

**User Story:** As a visitor, I want to see an impressive animated hero section, so that I immediately understand Monica is innovative and technologically advanced.

#### Acceptance Criteria

1. THE Hero_Section SHALL occupy the full viewport height
2. THE Hero_Section SHALL display a GLSL_Shader background with animated neural network particles
3. WHEN a user moves their mouse, THE GLSL_Shader SHALL react to mouse position
4. THE Hero_Section SHALL animate the main heading "The First AI That Never Forgets." sliding into view on page load
5. THE Hero_Section SHALL animate the subtitle "Engineered for the $3T Silver Economy" fading in with a delay after the heading
6. THE Hero_Section SHALL display two CTA_Button components: "Investor Pitch Deck" and "Request a Demo"
7. THE Hero_Section SHALL display a pulsing scroll indicator at the bottom
8. WHEN a user clicks a CTA_Button, THE Website SHALL use View_Transitions_API for smooth navigation

### Requirement 3: Problem Section with Scroll Animations

**User Story:** As a visitor, I want to see compelling statistics about senior care problems, so that I understand the market need Monica addresses.

#### Acceptance Criteria

1. WHEN a user scrolls the Problem section into view, THE Website SHALL trigger GSAP ScrollTrigger animations
2. THE Website SHALL display an Animated_Counter showing "42% of seniors experience dangerous loneliness"
3. THE Website SHALL display an Animated_Counter showing "30,000+ medication error deaths annually"
4. THE Website SHALL animate counters sequentially with emotional pacing between reveals
5. THE Website SHALL apply subtle parallax effects to the background during scroll

### Requirement 4: Solution Feature Grid

**User Story:** As a visitor, I want to understand Monica's key features through an elegant visual grid, so that I can quickly grasp the product's value proposition.

#### Acceptance Criteria

1. THE Website SHALL display 6 Liquid_Glass_Card components in a grid layout
2. WHEN the Solution section scrolls into view, THE Website SHALL stagger-animate cards into view
3. THE Website SHALL display these features: Persistent Memory, Medication Management, Emotional Companionship, Family Dashboard, Offline Capable (WebNN), Clinical Integration (HIPAA)
4. WHEN a user hovers over a Liquid_Glass_Card, THE Website SHALL lift the card with shadow and subtle glow effects
5. THE Website SHALL display an icon, title, and description on each Liquid_Glass_Card

### Requirement 5: Interactive Wellness Simulator

**User Story:** As a visitor, I want to interact with a wellness simulator, so that I can see the quantifiable impact of using Monica.

#### Acceptance Criteria

1. THE Wellness_Simulator SHALL display an interactive slider labeled "Hours with Monica per day"
2. WHEN a user adjusts the slider, THE Wellness_Simulator SHALL update three animated circular gauges in real-time
3. THE Wellness_Simulator SHALL display a Happiness Index gauge that increases with slider value
4. THE Wellness_Simulator SHALL display a Medication Error Risk gauge that decreases with slider value
5. THE Wellness_Simulator SHALL display a Clinical Care Need gauge that decreases with slider value
6. THE Wellness_Simulator SHALL be contained within a Liquid_Glass panel
7. THE Wellness_Simulator SHALL use GSAP animations for gauge fill transitions

### Requirement 6: Technology Architecture Diagram

**User Story:** As a technical visitor or investor, I want to see Monica's technology stack visualized, so that I understand the technical foundation and Azure integration.

#### Acceptance Criteria

1. THE Neural_Network_Diagram SHALL display technology nodes: Azure AI Foundry, Monica Brain, Azure Voice Live, Monica Speaks, WebNN, Offline Mode, Cosmos DB, Memory Storage
2. THE Neural_Network_Diagram SHALL NOT reference NVIDIA
3. WHEN the Technology section scrolls into view, THE Website SHALL animate nodes and connection lines building progressively
4. THE Neural_Network_Diagram SHALL display pulsing animations on nodes
5. THE Neural_Network_Diagram SHALL display animated connection lines between related nodes

### Requirement 7: Data Sovereignty Section

**User Story:** As a privacy-conscious visitor, I want to see clear data sovereignty messaging, so that I trust Monica with sensitive health information.

#### Acceptance Criteria

1. THE Website SHALL display a Canadian flag visual accent in the Data Sovereignty section
2. THE Website SHALL display a shield icon within a Liquid_Glass_Card
3. THE Website SHALL display the message "Your data never leaves Canada"
4. THE Website SHALL display Trust_Badge components for HIPAA, SOC2, and PIPEDA compliance
5. WHEN the Data Sovereignty section scrolls into view, THE Website SHALL animate Trust_Badge components into view
6. THE Website SHALL apply subtle parallax effects to the section background

### Requirement 8: Market Opportunity Section

**User Story:** As an investor, I want to see market size and growth data, so that I understand the business opportunity.

#### Acceptance Criteria

1. THE Website SHALL display an Animated_Counter showing "$3T" market size
2. THE Website SHALL display a growth chart with GSAP draw animation
3. THE Website SHALL display key market statistics in Liquid_Glass_Card components
4. WHEN the Market section scrolls into view, THE Website SHALL trigger all animations via ScrollTrigger

### Requirement 9: Contact Form

**User Story:** As a potential customer or investor, I want to submit my contact information, so that I can request a demo or get more information.

#### Acceptance Criteria

1. THE Contact_Form SHALL display input fields for Name, Email, Company, and Message
2. THE Contact_Form SHALL be styled with Liquid_Glass aesthetic
3. WHEN a user submits the Contact_Form, THE Website SHALL send data to Azure Functions backend
4. WHEN submission succeeds, THE Contact_Form SHALL display an animated success state
5. WHEN a user enters invalid data, THE Contact_Form SHALL display validation feedback with micro-animations
6. THE Contact_Form SHALL use Azure Communication Services for email delivery

### Requirement 10: Footer Section

**User Story:** As a visitor, I want to see company information in the footer, so that I know who operates Monica and where they're located.

#### Acceptance Criteria

1. THE Website SHALL display "© 2026 Monica Neural Systems - Regina, Saskatchewan, Canada" in the footer
2. THE Website SHALL display a subtle neural network pattern background in the footer

### Requirement 11: Smooth Scrolling and Transitions

**User Story:** As a visitor, I want smooth, premium scrolling and page transitions, so that the website feels polished and high-quality.

#### Acceptance Criteria

1. THE Website SHALL use Lenis for smooth scrolling throughout
2. THE Website SHALL use View_Transitions_API for page-to-page navigation
3. THE Website SHALL use GSAP ScrollTrigger for all scroll-driven animations
4. THE Website SHALL use Framer Motion for micro-interactions on interactive elements

### Requirement 12: Performance and Accessibility

**User Story:** As any visitor, I want the website to load quickly and be accessible, so that I can access content regardless of my device or abilities.

#### Acceptance Criteria

1. THE Website SHALL achieve a Lighthouse performance score of 90 or higher
2. THE Website SHALL achieve a Lighthouse accessibility score of 90 or higher
3. THE Website SHALL optimize all assets for fast load times
4. THE Website SHALL be keyboard navigable
5. THE Website SHALL provide appropriate ARIA labels for interactive elements

### Requirement 13: Technology Stack Implementation

**User Story:** As a developer, I want the website built with modern, maintainable technologies, so that it's easy to update and extend.

#### Acceptance Criteria

1. THE Website SHALL be built with Next.js 15 or higher using React Server Components
2. THE Website SHALL use TypeScript for type safety
3. THE Website SHALL use TailwindCSS v4 for styling
4. THE Website SHALL use GSAP ScrollTrigger for scroll animations
5. THE Website SHALL use Framer Motion for micro-interactions
6. THE Website SHALL use Lenis for smooth scrolling
7. THE Website SHALL use Three.js or GLSL shaders for the hero background
8. THE Website SHALL implement View Transitions API for page transitions
9. WHERE AI chat functionality is needed, THE Website SHALL use Vercel AI SDK v5 for streaming

### Requirement 14: Azure Deployment

**User Story:** As a system administrator, I want the website deployed on Azure infrastructure, so that it integrates with existing Monica services.

#### Acceptance Criteria

1. THE Website SHALL be deployed to Azure Static Web Apps or Azure App Service
2. THE Website SHALL use GitHub Actions for continuous deployment
3. WHERE server-side rendering is required, THE Website SHALL use Azure App Service
4. WHERE static generation is sufficient, THE Website SHALL use Azure Static Web Apps

### Requirement 15: Content Preservation

**User Story:** As a stakeholder, I want existing project assets preserved, so that we don't lose important documentation and configuration.

#### Acceptance Criteria

1. THE Website SHALL preserve the pitch/ folder and its contents
2. THE Website SHALL preserve the info/ folder and its contents
3. THE Website SHALL preserve the monica.agent.md file
4. THE Website SHALL preserve the foundry_mcp.py file
