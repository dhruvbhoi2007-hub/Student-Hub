# Practical 2: Accessibility (a11y) & Semantic HTML5 Checklist

**Student-ID:** D26CE154  
**Student-Name:** Dhruv Bhoi  
**Department:** CSPIT-CE, Faculty of Technology and Engineering (FTE)  
**Subject:** Web Development Frameworks (ITUE203) — Semester 3, 2026-27 (ODD)  
**Institution:** CHAROTAR UNIVERSITY OF SCIENCE AND TECHNOLOGY (CHARUSAT)  

---

This checklist verifies the compliance of StudentHub against the **W3C Web Content Accessibility Guidelines (WCAG) 2.1 AA** standards.

---

## 1. Semantic Tag Usage Matrix
Every page across both the static (`static/*.html`) and dynamic (`*.php`) suites incorporates structural HTML5 elements:

| Semantic Element | Implemented In | Purpose & Accessibility Role | Status |
|---|---|---|:---:|
| `<header>` | All pages (`includes/header.php`, `static/*.html`) | Landmark for top branding and site utilities | Passed |
| `<nav>` | Header, breadcrumbs, pagination | Navigation landmarks (`aria-label="Main navigation"`, `aria-label="Breadcrumb"`, `aria-label="Pagination"`) | Passed |
| `<main>` | All pages (`id="main"`) | Primary content landmark targeted by skip link | Passed |
| `<section>` | Hero, feature grids, dashboard sections | Grouping distinct logical thematic blocks | Passed |
| `<article>` | Event cards, student profiles, feedback items | Self-contained, independently distributable content items | Passed |
| `<aside>` | Hero sidecard, admin navigation drawer | Complementary sidebar landmark | Passed |
| `<footer>` | All pages (`includes/footer.php`, `static/*.html`) | Landmark for copyright, secondary navigation, and legal links | Passed |

---

## 2. Accessibility Verification Checklist

### Principle 1: Perceivable
- [x] **Text Alternatives (`alt` attributes):** All images provide descriptive `alt` text (e.g. `alt="Poster for HackCharusat"`).
- [x] **Form Labels:** Every `<input>`, `<select>`, and `<textarea>` has an associated `<label>` element with matching `for` and `id` attributes.
- [x] **Color Contrast:** Foreground text and background colors meet the minimum 4.5:1 contrast ratio in both Light and Dark mode.
- [x] **Scalable Typography:** Font sizes use system fonts and scalable units (`rem`, `clamp()`) respecting browser zoom levels up to 200%.

### Principle 2: Operable
- [x] **Skip to Content Link:** An accessible skip link (`<a class="skip-link" href="#main">`) allows keyboard users to bypass redundant navigation headers.
- [x] **Keyboard Navigation:** All interactive controls (buttons, links, form inputs, modal dialogs) are reachable and operable via <kbd>Tab</kbd>, <kbd>Enter</kbd>, and <kbd>Space</kbd>.
- [x] **Visible Focus Indicator:** High-contrast focus rings (`:focus-visible { outline: 3px solid var(--accent); outline-offset: 2px; }`) clearly indicate active element focus.
- [x] **Modal Trap & Escape:** Modals can be closed via the <kbd>Escape</kbd> key or backdrop click.

### Principle 3: Understandable
- [x] **Language Specification:** Every document root specifies `<html lang="en">`.
- [x] **Breadcrumb Navigation (Intermediate Extension):** Breadcrumb trails with `aria-label="Breadcrumb"` orient users within the hierarchy.
- [x] **Predictable Form Feedback:** Inline error messages (`.error-msg`) are linked directly below invalid input controls and carry `aria-live="polite"` or `role="alert"`.
- [x] **Confirmation Dialogs:** Destructive actions (deleting students, deleting events, cancelling registrations) require user confirmation before execution.

### Principle 4: Robust
- [x] **Valid HTML5:** Validated markup using standard document type `<!DOCTYPE html>`.
- [x] **ARIA Landmarks and States:**
  - `aria-current="page"` on current navigation tab.
  - `aria-expanded="false"` / `"true"` on hamburger menu and FAQ accordion items.
  - `aria-controls` referencing corresponding region IDs.
  - `role="status"` and `role="alert"` for real-time announcements (toast alerts, loading status).
  - `role="dialog"` and `aria-modal="true"` on modal overlays.

