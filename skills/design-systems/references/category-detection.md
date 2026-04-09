# Category Detection Reference

## Detection Algorithm

Scan project files for category indicators with weighted scoring.

### Category Indicators

```python
category_signals = {
    'saas-landing': {
        'keywords': [
            ('pricing', 3.0),
            ('signup', 2.5),
            ('get started', 2.5),
            ('features', 2.0),
            ('testimonials', 2.0),
            ('integration', 1.5),
            ('api', 1.0),
            ('demo', 2.0),
            ('free trial', 2.5),
        ],
        'file_patterns': [
            'pricing.html',
            'features.jsx',
            'testimonials.vue',
            'landing.*',
            'hero.*',
        ],
        'css_indicators': [
            '.pricing-',
            '.feature-',
            '.testimonial-',
            '.cta-',
        ]
    },
    
    'dashboard-app': {
        'keywords': [
            ('dashboard', 3.0),
            ('chart', 2.0),
            ('graph', 2.0),
            ('table', 1.5),
            ('sidebar', 2.0),
            ('widget', 2.0),
            ('metric', 1.5),
            ('analytics', 2.0),
            ('report', 1.5),
        ],
        'file_patterns': [
            'dashboard.*',
            'sidebar.*',
            'chart.*',
            'widget.*',
            'analytics.*',
        ],
        'css_indicators': [
            '.dashboard-',
            '.sidebar-',
            '.chart-',
            '.widget-',
            '.metric-',
        ]
    },
    
    'e-commerce': {
        'keywords': [
            ('product', 2.0),
            ('cart', 3.0),
            ('checkout', 3.0),
            ('shop', 2.5),
            ('buy', 2.0),
            ('price', 2.0),
            ('add to cart', 3.0),
            ('inventory', 2.0),
            ('shipping', 1.5),
        ],
        'file_patterns': [
            'product.*',
            'cart.*',
            'checkout.*',
            'shop.*',
            'catalog.*',
        ],
        'css_indicators': [
            '.product-',
            '.cart-',
            '.checkout-',
            '.price-',
            '.add-to-cart',
        ]
    },
    
    'portfolio': {
        'keywords': [
            ('portfolio', 3.0),
            ('gallery', 2.5),
            ('project', 2.0),
            ('work', 2.0),
            ('creative', 1.5),
            ('art', 1.5),
            ('design', 1.0),
            ('photography', 2.0),
            ('case study', 2.0),
        ],
        'file_patterns': [
            'portfolio.*',
            'gallery.*',
            'project.*',
            'work.*',
            'creative.*',
        ],
        'css_indicators': [
            '.portfolio-',
            '.gallery-',
            '.project-',
            '.work-',
        ]
    },
    
    'content-publication': {
        'keywords': [
            ('blog', 3.0),
            ('article', 2.5),
            ('post', 2.0),
            ('content', 1.5),
            ('newsletter', 2.5),
            ('subscribe', 2.0),
            ('author', 1.5),
            ('category', 1.0),
            ('tags', 1.0),
        ],
        'file_patterns': [
            'blog.*',
            'article.*',
            'post.*',
            'content.*',
            'newsletter.*',
        ],
        'css_indicators': [
            '.blog-',
            '.article-',
            '.post-',
            '.content-',
            '.author-',
        ]
    },
    
    'service-business': {
        'keywords': [
            ('service', 2.5),
            ('contact', 2.0),
            ('process', 2.0),
            ('team', 1.5),
            ('about us', 1.5),
            ('consulting', 2.5),
            ('agency', 2.0),
            ('client', 1.5),
            ('testimonial', 1.5),
        ],
        'file_patterns': [
            'services.*',
            'contact.*',
            'about.*',
            'team.*',
            'process.*',
        ],
        'css_indicators': [
            '.service-',
            '.contact-',
            '.team-',
            '.process-',
            '.about-',
        ]
    },
    
    'developer-tool': {
        'keywords': [
            ('api', 2.5),
            ('docs', 2.5),
            ('documentation', 2.5),
            ('code', 1.5),
            ('terminal', 2.0),
            ('github', 1.5),
            ('cli', 2.0),
            ('sdk', 2.0),
            ('developer', 2.0),
            ('npm', 1.5),
        ],
        'file_patterns': [
            'docs.*',
            'api.*',
            'reference.*',
            'guide.*',
            'cli.*',
        ],
        'css_indicators': [
            '.docs-',
            '.api-',
            '.code-',
            '.terminal-',
            '.syntax-',
        ]
    }
}
```

## Scoring Algorithm

```python
def detect_category(project_files, project_content):
    """
    Analyze project and return category with confidence score
    """
    scores = {}
    
    for category, indicators in category_signals.items():
        score = 0
        evidence = []
        
        # Check keywords in content
        for keyword, weight in indicators['keywords']:
            count = project_content.lower().count(keyword.lower())
            if count > 0:
                score += weight * min(count, 3)  # Cap at 3 occurrences
                evidence.append(f"'{keyword}' found {count}x (weight: {weight})")
        
        # Check file patterns
        for pattern in indicators['file_patterns']:
            matches = [f for f in project_files if pattern.replace('.*', '') in f.lower()]
            if matches:
                score += 2.0 * len(matches)
                evidence.append(f"Files matching '{pattern}': {matches}")
        
        # Check CSS class indicators
        for css_class in indicators['css_indicators']:
            if css_class in project_content:
                score += 1.5
                evidence.append(f"CSS class '{css_class}' detected")
        
        scores[category] = {
            'score': score,
            'evidence': evidence
        }
    
    # Find highest score
    if scores:
        best_category = max(scores.items(), key=lambda x: x[1]['score'])
        total_possible = sum(max(w for _, w in ind['keywords']) for ind in category_signals.values())
        confidence = best_category[1]['score'] / (total_possible * 0.3)  # 30% of max = high confidence
        
        return {
            'category': best_category[0],
            'confidence': min(confidence, 1.0),
            'score': best_category[1]['score'],
            'evidence': best_category[1]['evidence']
        }
    
    return None
```

## Confidence Levels

| Confidence | Action |
|------------|--------|
| > 0.75 | Auto-apply top match |
| 0.50 - 0.75 | Suggest top 3 matches for user choice |
| < 0.50 | Ask user explicitly |

## Edge Cases

**Multi-category projects:**
- Blog + SaaS landing → Ask: "Is this a content site or product site?"
- Portfolio + Services → Suggest: service-business with portfolio section

**Ambiguous signals:**
- "Product" could be SaaS or e-commerce
- Check for: cart/checkout (e-commerce) vs features/demo (SaaS)

**No signals:**
- Generic "index.html" with minimal content
- Ask user: "What type of site is this?"

## Recommended Design Systems by Category

| Category | Primary | Alternatives |
|------------|---------|--------------|
| saas-landing | linear.app | vercel.com, supabase.com, stripe.com |
| dashboard-app | linear.app (UI) | github.com, vercel.com/dashboard |
| e-commerce | apple.com | shopify.com, nike.com |
| portfolio | framer.com | webflow.com, cargo.site |
| content-publication | medium.com | substack.com, stripe.com/blog |
| service-business | cursor.com | intercom.com, webflow.com |
| developer-tool | vercel.com | github.com, docs.rs |
| brand-showcase | tesla.com | apple.com, nike.com |

## Validation

After detection, validate by checking:
1. Does detected category match user's stated intent?
2. Are there conflicting signals? (e.g., "cart" in a blog)
3. Is confidence high enough to proceed?
