# Motion System Reference

GSAP-based animation patterns with ScrollTrigger integration for scroll-driven effects.

## Required Libraries

Always load from jsDelivr CDN:

```html
<!-- GSAP Core -->
<script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/gsap.min.js"></script>

<!-- ScrollTrigger -->
<script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/ScrollTrigger.min.js"></script>

<!-- Observer (for snap) -->
<script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/Observer.min.js"></script>

<!-- Lenis Smooth Scroll -->
<script src="https://cdn.jsdelivr.net/npm/@studio-freight/lenis@1.0.42/dist/lenis.min.js"></script>
```

**Plugin Registration:**
```javascript
gsap.registerPlugin(ScrollTrigger, Observer);
```

**Reduced Motion Check:**
```javascript
const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
```

## Pattern 1: Multi-Layer Parallax

Data attributes map elements to scroll speeds:

```javascript
gsap.utils.toArray('[data-parallax]').forEach(element => {
  const speed = parseFloat(element.dataset.parallax) || 0.5;
  
  gsap.to(element, {
    y: () => speed * 100,
    ease: 'none',
    scrollTrigger: {
      trigger: element,
      start: 'top bottom',
      end: 'bottom top',
      scrub: true
    }
  });
});
```

```html
<img data-parallax="0.3" src="mountains.png">   <!-- Slow -->
<img data-parallax="0.6" src="trees.png">       <!-- Medium -->
<img data-parallax="1.0" src="foreground.png">  <!-- Fast -->
```

## Pattern 2: Pinned Sections (Window Over Window)

Sections remain fixed while internal content animates:

```javascript
const sections = gsap.utils.toArray('.pinned-section');

sections.forEach((section, i) => {
  ScrollTrigger.create({
    trigger: section,
    pin: true,
    start: 'top top',
    end: '+=150%', // Stay pinned for 1.5x viewport height
    scrub: 1
  });
  
  // Content animation while pinned
  gsap.from(section.querySelector('.content'), {
    opacity: 0,
    y: 50,
    scrollTrigger: {
      trigger: section,
      start: 'top top',
      end: '+=50%',
      scrub: true
    }
  });
});
```

## Pattern 3: Stacking Cards

Incrementing z-index with sticky positioning:

```javascript
const cards = gsap.utils.toArray('.stack-card');

cards.forEach((card, i) => {
  // Card slides in from bottom
  gsap.from(card, {
    y: window.innerHeight,
    scale: 0.8,
    filter: 'brightness(0.5)',
    scrollTrigger: {
      trigger: card,
      start: 'top bottom',
      end: 'top top',
      scrub: true
    }
  });
  
  // Previous cards scale down and darken
  if (i > 0) {
    gsap.to(cards[i - 1], {
      scale: 0.9,
      filter: 'brightness(0.3)',
      scrollTrigger: {
        trigger: card,
        start: 'top bottom',
        end: 'top center',
        scrub: true
      }
    });
  }
});
```

## Pattern 4: Scroll-Linked Timeline

One pixel = one frame:

```javascript
// Create timeline with paused state
const tl = gsap.timeline({ paused: true });

// Add animations
tl.to('.hero', { y: -100, scale: 0.8, duration: 1 })
  .to('.title', { opacity: 0, y: -50, duration: 0.5 }, 0.5)
  .to('.next-section', { opacity: 1, duration: 0.5 }, 0.8);

// Link to scroll
ScrollTrigger.create({
  trigger: '.scene',
  start: 'top top',
  end: '+=200%', // 2x viewport height = timeline duration
  scrub: 0.5,    // 0.5s smoothing
  onUpdate: (self) => {
    tl.progress(self.progress);
  }
});
```

## Pattern 5: Clip-Path Reveals

GPU-accelerated masking:

```javascript
// Horizontal wipe
gsap.from('.wipe-reveal', {
  clipPath: 'inset(0 100% 0 0)',
  scrollTrigger: {
    trigger: '.wipe-reveal',
    start: 'top 80%',
    end: 'top 20%',
    scrub: true
  }
});

// Circular iris
gsap.from('.iris-reveal', {
  clipPath: 'circle(0% at 50% 50%)',
  scrollTrigger: {
    trigger: '.iris-reveal',
    start: 'top 80%',
    end: 'top 20%',
    scrub: true
  }
});

// Window pane
gsap.from('.pane-reveal', {
  clipPath: 'polygon(0 0, 0 0, 0 100%, 0 100%)',
  scrollTrigger: {
    trigger: '.pane-reveal',
    start: 'top 80%',
    end: 'top 20%',
    scrub: true
  }
});
```

## Pattern 6: Horizontal Scroll Container

Vertical scroll drives horizontal movement:

```javascript
const container = document.querySelector('.horizontal-container');
const panels = gsap.utils.toArray('.horizontal-panel');

// Calculate total scroll distance
const totalWidth = container.scrollWidth - window.innerWidth;

gsap.to(container, {
  x: -totalWidth,
  ease: 'none',
  scrollTrigger: {
    trigger: container,
    pin: true,
    scrub: 1,
    end: () => '+=' + totalWidth
  }
});

// Snap calculations
const snapPoints = panels.map((_, i) => i / (panels.length - 1));
```

## Pattern 7: 3D Perspective Fly-In

Content approaches viewer:

```javascript
gsap.set('.perspective-container', { perspective: 1000 });

gsap.from('.fly-in', {
  z: -500,
  scale: 0.5,
  filter: 'blur(20px)',
  opacity: 0,
  scrollTrigger: {
    trigger: '.fly-in',
    start: 'top 80%',
    end: 'center center',
    scrub: true
  }
});
```

## Pattern 8: Full-Page Snap Sections

Observer plugin for scroll direction detection:

```javascript
let currentSection = 0;
const sections = gsap.utils.toArray('.snap-section');

Observer.create({
  type: 'wheel,touch,pointer',
  wheelSpeed: -1,
  onDown: () => {
    if (currentSection < sections.length - 1) {
      currentSection++;
      goToSection(currentSection);
    }
  },
  onUp: () => {
    if (currentSection > 0) {
      currentSection--;
      goToSection(currentSection);
    }
  },
  tolerance: 10,
  preventDefault: true
});

function goToSection(index) {
  gsap.to(window, {
    duration: 1,
    scrollTo: { y: sections[index], autoKill: false },
    ease: 'power3.out'
  });
}
```

## Pattern 9: Impact Physics

Elastic easing with bounce:

```javascript
gsap.from('.impact-element', {
  y: -200,
  duration: 1.2,
  ease: 'elastic.out(1, 0.5)',
  onComplete: () => {
    // Micro-rotation shake on landing
    gsap.to('.impact-element', {
      rotation: 3,
      duration: 0.1,
      yoyo: true,
      repeat: 3,
      ease: 'power2.out'
    });
  },
  scrollTrigger: {
    trigger: '.impact-element',
    start: 'top 80%'
  }
});
```

## Lenis Smooth Scroll Integration

```javascript
// Initialize Lenis
const lenis = new Lenis({
  duration: 1.2,
  easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
  orientation: 'vertical',
  gestureOrientation: 'vertical',
  smoothWheel: true
});

// Connect to GSAP ticker
lenis.on('scroll', ScrollTrigger.update);

gsap.ticker.add((time) => {
  lenis.raf(time * 1000);
});

gsap.ticker.lagSmoothing(0);
```

## IntersectionObserver Trigger

```javascript
const observerOptions = {
  threshold: 0.2,
  rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const el = entry.target;
      const animationType = el.dataset.animate;
      
      switch(animationType) {
        case 'fade':
          gsap.to(el, { opacity: 1, duration: 0.6 });
          break;
        case 'slide-up':
          gsap.fromTo(el, 
            { opacity: 0, y: 30 },
            { opacity: 1, y: 0, duration: 0.6 }
          );
          break;
        case 'scale':
          gsap.fromTo(el,
            { opacity: 0, scale: 0.8 },
            { opacity: 1, scale: 1, duration: 0.6 }
          );
          break;
      }
      
      observer.unobserve(el);
    }
  });
}, observerOptions);

document.querySelectorAll('[data-animate]').forEach(el => {
  observer.observe(el);
});
```

## Easing Reference

| Name | Usage |
|------|-------|
| `none` / `linear` | Scroll-linked, parallax |
| `power2.out` | Standard entrances |
| `power3.out` | Dramatic entrances |
| `power4.out` | Heavy impact |
| `elastic.out(1, 0.5)` | Playful, bouncy |
| `back.out(1.7)` | Overshoot |
| `circ.inOut` | Circular motion |
| `expo.inOut` | Fast acceleration |

## Performance Best Practices

1. **Always use `transform` and `opacity`** - Never animate layout properties
2. **`will-change: transform`** on animated elements
3. **`scrub: true`** for scroll-linked (or 0.5-1 for smoothing)
4. **`refreshPriority`** for complex layouts
5. **Limit simultaneous tweens** - Batch if possible
