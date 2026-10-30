# Practical 1: Project Initiation, Requirement Analysis, Sitemap, Wireframe, and GitHub Setup

## 1. Project Overview & Scope
**StudentHub** is an integrated, full-stack student and campus event management portal. It solves the fragmentation caused by scattered spreadsheets, isolated event signups, and manual record-keeping across university departments.

- **Institution:** CHAROTAR UNIVERSITY OF SCIENCE AND TECHNOLOGY (CHARUSAT)
- **Faculty:** Faculty of Technology and Engineering (FTE)
- **Subject:** Web Development Frameworks (ITUE203) — Semester 3, 2026-27 (Odd)
- **Target Audience:** University students, club leaders, event organizers, faculty, and administrative staff.

---

## 2. Key Analysis Questions & Answers

### Q1: What is a URL and what are its constituent parts?
A **Uniform Resource Locator (URL)** is a standard web address that specifies the location of a resource on a computer network and the mechanism for retrieving it.
```
  https://studenthub.local:8080/events.php?category=Technical&sort=date#list
  └──┬──┘ └────────┬─────┘ └─┬─┘ └───┬────┘ └───────────┬───────────────┘ └─┬┘
   Scheme       Host       Port    Path             Query String        Fragment
```
1. **Scheme/Protocol (`http`, `https`):** Specifies the protocol used to communicate (e.g., HTTPS encrypts traffic via TLS/SSL).
2. **Host/Domain (`studenthub.local`):** The domain name or IP address resolving to the target server.
3. **Port (`:80`, `:443`, `:8080`):** The port number on the server host (defaults: 80 for HTTP, 443 for HTTPS).
4. **Path (`/events.php`):** The hierarchical path identifying the specific file, route, or resource on the server.
5. **Query String (`?category=Technical&sort=date`):** Key-value parameter pairs passed to the application backend.
6. **Fragment/Hash (`#list`):** Identifies a specific section or element anchor within the document, processed client-side.

### Q2: How is an HTML file processed in a web browser?
Browsers process HTML through the **Critical Rendering Path (CRP)**:
1. **Fetching & Tokenization:** The browser engine (Blink/Gecko) reads raw bytes over HTTP/HTTPS, decodes them according to charset (`UTF-8`), and converts them into tokens (`<html>`, `<body>`, `<div>`).
2. **DOM Tree Construction:** Tokens are converted into Node objects structured into the **Document Object Model (DOM)** tree.
3. **CSSOM Tree Construction:** Linked stylesheets and `<style>` blocks are parsed into the **CSS Object Model (CSSOM)** tree.
4. **Render Tree Generation:** The DOM and CSSOM are combined into a Render Tree, ignoring non-visible nodes (e.g., `<head>`, elements with `display: none`).
5. **Layout (Reflow):** Browser calculates the exact geometry, position, and dimensions of each element on the viewport.
6. **Painting & Compositing:** Visual elements (backgrounds, borders, text, shadows) are drawn onto screen layers and composited onto the display GPU-accelerated.
7. **JavaScript Execution:** Inline and external scripts manipulate the DOM and CSSOM dynamically via event loops and microtask queues.

### Q3: How is page navigation flow managed among all HTML pages?
- Consistent navigation bar with semantic `<nav>` and `<ul class="nav-menu">`.
- Breadcrumb trails (`<nav class="breadcrumb">`) indicating the hierarchical depth from Home.
- `aria-current="page"` indicating the active tab to screen readers.
- Role-based navigation: public users see public links; logged-in students see their Dashboard and Profile; admins see management menus.

### Q4: How will GitHub commits be maintained after each practical?
- The project follows a modular Git workflow with semantic commit messages corresponding to each practical number:
  - `git commit -m "feat(p01): requirements, sitemap, wireframes and repository setup"`
  - `git commit -m "feat(p02): semantic HTML5 layout with accessibility tags"`
  - `git commit -m "feat(p03): responsive CSS grid and flexbox layout"`
  - `git commit -m "feat(p04): JavaScript DOM interactions, theme switch, and modal"`
  - `git commit -m "feat(p05): client-side registration validation with regex and canvas CAPTCHA"`
  - `git commit -m "feat(p06): JSON data rendering via Fetch API with search, sort, and dependent filter"`
  - `git commit -m "feat(p07): server-side form processing with CSV and JSON file storage"`
  - `git commit -m "feat(p08): MySQL normalized relational schema and PDO/MySQLi connection"`
  - `git commit -m "feat(p09): secure registration with duplicate checks and password_hash"`
  - `git commit -m "feat(p10): session auth, RBAC redirection, timeout, and remember tokens"`
  - `git commit -m "feat(p11): student CRUD with MySQLi, CSV export, and soft delete"`
  - `git commit -m "feat(p12): event management with poster upload validation and MIME checks"`
  - `git commit -m "feat(p13): PHP JSON REST API with debounced AJAX fetch CRUD"`
  - `git commit -m "feat(p14): admin dashboard with role-based widgets, charts, and audit trail"`
  - `git commit -m "feat(p15): full-stack integration, security audit, test suite, and deployment docs"`

---

## 3. User Roles & Permissions Matrix
| Feature / Page | Visitor (Guest) | Student | Administrator |
|---|:---:|:---:|:---:|
| Home (`index.php`, `static/index.html`) | Read | Read | Read |
| About (`about.php`, `static/about.html`) | Read | Read | Read |
| FAQ (`faq.php`, `static/faq.html`) | Read | Read | Read |
| Contact (`contact.php`, `static/contact.html`) | Submit | Submit | Submit & View Stored CSV |
| Feedback (`feedback.php`, `static/feedback.html`) | Submit & View | Submit & View | Submit & View |
| Events Catalog (`events.php`, `static/events.html`) | Read | Read | Read |
| Student Directory (`directory.php`) | Read | Read | Read |
| Register (`register.php`, `static/register.html`) | Create Account | Redirect | Redirect |
| Login (`login.php`, `static/login.html`) | Authenticate | Redirect | Redirect |
| Dashboard (`dashboard.php`, `static/dashboard.html`)| No Access | Full (Own events) | Redirect to Admin |
| Profile (`profile.php`, `static/profile.html`) | No Access | Edit Own Profile | Edit Own Profile |
| Live Events AJAX (`api-demo.php`) | No Access | Read & Register | Full AJAX CRUD |
| Student Management (`students.php`) | No Access | No Access | Full CRUD, Soft Delete, CSV Export |
| Event Management (`manage_events.php`) | No Access | No Access | Full CRUD + Poster Upload |
| Admin Dashboard (`admin/dashboard.php`) | No Access | No Access | Full (Stats, Charts, User Toggle) |
| Audit Trail (`admin/audit.php`) | No Access | No Access | View All Logs |

---

## 4. Minimum 10 Required Pages (Implemented: 14 Pages)
1. **Home (`index.php`, `static/index.html`):** Hero section, feature cards, highlight carousel, welcome modal.
2. **About (`about.php`, `static/about.html`):** University mission, curriculum, system architecture.
3. **Register (`register.php`, `static/register.html`):** 10-field form, regex validation, strength meter, canvas CAPTCHA.
4. **Login (`login.php`, `static/login.html`):** Session authentication, remember-me token, timeout recovery.
5. **Student Dashboard (`dashboard.php`, `static/dashboard.html`):** Active registrations counter, event cancellation, upcoming list.
6. **Events Catalog (`events.php`, `static/events.html`):** Fetch API catalog with client-side search, sort, and pagination.
7. **Student Directory (`directory.php`, `static/directory.html`):** Dynamic student profiles with dependent dropdown filtering.
8. **User Profile (`profile.php`, `static/profile.html`):** User and student profile details update form.
9. **Contact Us (`contact.php`, `static/contact.html`):** Inquiries form storing to `data/contacts.csv` with admin view.
10. **Feedback (`feedback.php`, `static/feedback.html`):** Rating and testimonial form storing to `data/feedback.json`.
11. **FAQ (`faq.php`, `static/faq.html`):** Accessible accordion interface for common questions.
12. **Student Management (`students.php`):** Admin CRUD with MySQLi, live search, soft delete, and CSV export.
13. **Event Management (`manage_events.php`):** Admin event publisher with poster upload, MIME verification, category filters.
14. **Admin Dashboard (`admin/dashboard.php`):** System metrics, registration charts, monthly analytics, user activation toggle.

---

## 5. Functional & Non-Functional Requirements

### Functional Requirements (FR)
- **FR1 (Public Discovery):** Visitors can explore campus information, upcoming events, student directory, and FAQs.
- **FR2 (Client Validation):** Registration forms validate user inputs in real time (name, email, phone, passwords, terms).
- **FR3 (Authentication & Sessions):** Users can log in securely, retain sessions across tabs, auto-timeout after 15 minutes of inactivity, and persist authentication via secure cookie tokens.
- **FR4 (Self-Service Dashboard):** Students can view their registered events and cancel registrations in real time.
- **FR5 (Administrative Student CRUD):** Admins can search, filter, paginate, create, edit, soft-delete, and export student records to CSV.
- **FR6 (Event Management & Media Upload):** Admins can create and edit events, uploading posters with file size (<= 2MB) and MIME type checks.
- **FR7 (Single-Page AJAX CRUD):** Users interact with event data asynchronously via JSON API endpoints without whole-page refresh.
- **FR8 (Audit Trail):** Every security-sensitive action (login, logout, registration, updates, deletions) is captured in `audit_logs`.

### Non-Functional Requirements (NFR)
- **NFR1 (Security):** All queries use prepared statements (PDO & MySQLi); passwords hashed with `bcrypt`; CSRF tokens on all POST requests; secure session parameters.
- **NFR2 (Accessibility - WCAG 2.1 AA):** High-contrast color scheme, keyboard focus rings, semantic tags, skip link, ARIA live regions, and descriptive alt text.
- **NFR3 (Responsiveness):** Mobile-first layouts adapting cleanly across mobile (320px+), tablet (768px+), and desktop (1024px+).
- **NFR4 (Performance):** Zero heavy frontend dependencies; vanilla ES6+; optimized queries and indexed foreign keys.
- **NFR5 (Resilience):** Offline-ready fallback for JSON data rendering using browser `localStorage` caching.
