# Project Guidelines

## Code Style
- Keep this repo framework-free and static-first; do not add bundlers, npm tooling, or SPA routing.
- Follow the current split: structure in `index.html`, styling in `css/styles.css`, behavior in `js/script.js`, backend form handling in `contact.php`.
- Preserve JS hook selectors and ARIA contracts used by scripts (`#primary-menu`, `.menu-toggle`, `#contact-form`, `#form-message`, `#service-filter`, `#image-modal`).
- Keep the existing palette/tokens in `css/styles.css` (notably `#002f6c` and `#da1212`) unless a rebrand is explicitly requested.

## Architecture
- Single-page marketing site; `index.html` contains nav, services, projects/testimonials, and contact section.
- Contact flow: `#contact-form` in `index.html` -> `fetch('contact.php')` in `js/script.js` -> JSON response from `contact.php`.
- Frontend expects `{ success: true, message: ... }` on success and `{ error: ... }` on failure.
- Service filtering/autocomplete reads each `.service` cards `h3` and text content; keep service card structure consistent.

## Build and Test
- No build step. Quick static preview: open `index.html` directly.
- Full local behavior (required for form POST): `php -S localhost:8000` then open `http://localhost:8000`.
- Static server alternative (no PHP form handling): `python -m http.server 8000`.
- Useful checks agents can run:
  - `php -l contact.php`
  - `curl -i http://localhost:8000/contact.php` (expect `405`)
  - `curl -i -X POST -d "name=Test&email=test@example.com&message=Hello" http://localhost:8000/contact.php`
- Manual verification focus: mobile menu open/close + outside click + `Esc`, service filtering + inline autocomplete, project image modal, contact form success/error messaging.

## Project Conventions
- Make surgical edits; avoid broad HTML/CSS rewrites for single-section changes.
- Do not rename form fields (`name`, `email`, `message`) unless both `js/script.js` and `contact.php` are updated together.
- Keep accessibility behavior intact (`aria-expanded`, `aria-invalid`, `aria-live`, modal `aria-hidden`).
- `scripts/update_services_icons.py` rewrites service icons in `index.html`; when changing service titles, update `emoji_map` accordingly.
- If touching that script, prefer repo-relative paths; it currently uses a hard-coded absolute path and has a `sys.exit(...)` path without importing `sys`.

## Integration Points
- Analytics events are centralized via `trackConversion()` in `js/script.js` (`window.gtag` first, `dataLayer` fallback).
- External dependencies are hosted/CDN resources (Google Fonts, Google Analytics, Unsplash image URLs).
- Keep endpoint contract stable for frontend/backend interoperability.

## Security
- `contact.php` currently enforces POST-only requests, field presence, email validation, and JSON responses.
- Do not commit credentials or secrets; mail and domain config must stay environment-specific.
- Production hardening note: CSRF protection, rate limiting, and abuse controls are not implemented in this repo; do not imply they exist.
