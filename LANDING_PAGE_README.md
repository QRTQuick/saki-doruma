# Saki-Doruma Landing Page

Professional landing page website for Saki-Doruma expense management software.

## Files Included

- `index.html` — Main landing page with hero, features, pricing, testimonials, and CTA sections
- `styles.css` — Professional business styling with dark mode support, animations, and responsive design
- `script.js` — Interactive features: smooth scrolling, scroll animations, form handling, email validation

## Features

✨ **Modern Design**
- Professional color scheme with gradients
- Dark/light mode support (respects system preference)
- Smooth animations and transitions
- Fully responsive (mobile, tablet, desktop)

📱 **Responsive Layout**
- Mobile-first design
- Grid-based feature cards
- Flexible navigation
- Touch-friendly buttons

🎯 **Business-Grade Content**
- Compelling value proposition
- Clear feature showcase with icons
- Benefits section highlighting ROI
- Three-tier pricing model
- Customer testimonials
- Strong call-to-action (CTA)

⚡ **Interactive Elements**
- Smooth scroll navigation
- Scroll-triggered animations
- Form email validation
- Hover effects on cards and buttons
- Active navigation indicator

## How to Use

### Local Development

1. **Open in Browser** — Simply open `index.html` in your web browser. No server required.
   ```bash
   # On Windows, double-click index.html, or use PowerShell:
   start index.html
   ```

2. **Live Server (Optional)** — For live editing, use a local server:
   ```bash
   # Using Python (3.x):
   python -m http.server 8000
   
   # Or with Node.js (if installed):
   npx http-server
   ```
   Then visit `http://localhost:8000` in your browser.

### Deployment

- **GitHub Pages** — Push this folder to GitHub, enable Pages in settings, and the site goes live.
- **Any Web Host** — Upload `index.html`, `styles.css`, and `script.js` to any web server.
- **Static Hosting** — Compatible with Vercel, Netlify, AWS S3, or any static hosting service.

## Customization

### Colors
Edit the CSS variables in `styles.css` (`:root` section):
```css
--primary: #0066cc;           /* Main brand color */
--secondary: #00b4d8;         /* Accent color */
--accent: #f77f00;            /* Highlight color */
```

### Content
Edit `index.html` to update:
- Company name and logo
- Feature descriptions
- Pricing tiers and features
- Testimonials
- Contact email or form handler

### Fonts
Change the font family in `styles.css`:
```css
font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, ...
```

## Browser Support

- Chrome, Edge, Firefox, Safari (latest versions)
- Mobile browsers: iOS Safari, Chrome Android
- Responsive down to 320px width

## Performance

- **Lightweight** — No frameworks or heavy dependencies
- **Fast Load** — Pure HTML, CSS, and vanilla JavaScript
- **Accessibility** — Semantic HTML, WCAG-friendly structure
- **SEO-Friendly** — Meta tags, semantic markup, clear hierarchy

## Future Enhancements

Consider adding:
- Blog section (`/blog`)
- Knowledge base or FAQ
- Case studies page
- Team/About page
- Email signup integration (Mailchimp, ConvertKit, etc.)
- Analytics (Google Analytics, Hotjar)
- Live chat widget
- Video demos (YouTube embeds)

## License

© 2025 Saki-Doruma. All rights reserved.