# StudentHub — Student & Event Management Portal
**CHAROTAR UNIVERSITY OF SCIENCE AND TECHNOLOGY (CHARUSAT)**  
**FACULTY OF TECHNOLOGY AND ENGINEERING (FTE) · CSPIT-CE**  
**SUBJECT:** Web Development Frameworks (ITUE203) · Semester: 3rd, 2026-27 (ODD)

**Student Details:**  
- **Student Name:** Dhruv Bhoi  
- **Student ID:** D26CE154  
- **Department:** Computer Engineering (CSPIT-CE)  

StudentHub is an accessible, responsive, full-stack campus management portal built with HTML5, CSS3 (CSS Grid & Flexbox), Vanilla ES6+ JavaScript, PHP (PDO & MySQLi), and MySQL. Its UI is styled with a sleek modern SaaS dashboard layout featuring an application sidebar, timetable cards, circular SVG progress rings, a campus notice board, and a violet/lavender design system.

---

## Quick Setup Instructions (XAMPP)

1. **Deploy Project:**  
   Copy the `studenthub` folder to `C:\xampp\htdocs\studenthub`.
2. **Start Services:**  
   Open XAMPP Control Panel and start **Apache** and **MySQL**.
3. **Import Database:**  
   - Open <http://localhost/phpmyadmin/> in your browser.
   - Click **Import** → Choose `database/studenthub.sql` → Click **Import**.
   - This creates database `studenthub` with normalized tables, seed data, and stored procedures.
4. **Verify Configuration:**  
   Verify `includes/config.php` (defaults: host `localhost`, user `root`, empty password).
5. **Run DB Connection Test (Practical 8 Post-Lab):**  
   Open <http://localhost/studenthub/db-test.php> to verify PDO, MySQLi, tables, and stored procedures.
6. **Launch StudentHub:**  
   Visit <http://localhost/studenthub/>.

### Pre-Configured Demo Accounts
| Role | Name | Email Address | Password | Landing Page |
|---|---|---|---|---|
| **Administrator** | Administrator | `admin@studenthub.local` | `Admin@123` | `admin/dashboard.php` |
| **Student** | Dhruv Bhoi (D26CE154) | `student@studenthub.local` | `Student@123` | `dashboard.php` |

### Virtual Host Configuration (Practical 15 Intermediate Extension)
To access the application via `http://studenthub.local/`:
1. Open `C:\xampp\apache\conf\extra\httpd-vhosts.conf` and append:
   ```apache
   <VirtualHost *:80>
       ServerAdmin admin@studenthub.local
       DocumentRoot "C:/xampp/htdocs/studenthub"
       ServerName studenthub.local
       <Directory "C:/xampp/htdocs/studenthub">
           Options Indexes FollowSymLinks
           AllowOverride All
           Require all granted
       </Directory>
   </VirtualHost>
   ```
2. Open `C:\Windows\System32\drivers\etc\hosts` (as Administrator) and add:
   ```hosts
   127.0.0.1 studenthub.local
   ```
3. Restart Apache from the XAMPP Control Panel.

---

## Static HTML Pages (`static/`)
Directory `static/` contains standalone accessible HTML5 pages (`index.html`, `about.html`, `events.html`, `directory.html`, `faq.html`, `contact.html`, `feedback.html`, `dashboard.html`, `profile.html`, `admin.html`, `login.html`, `register.html`) satisfying Practicals 2 through 6.

---

## Detailed Practical Mapping Matrix (1 to 15)

| Practical No. | Core Title & Concepts | Implemented Source Files | Documentation & Deliverables |
|:---:|---|---|---|
| **1** | Project Initiation, Sitemap, Wireframe, Git | Project directory, folder structure | [`docs/requirements.md`](file:///d:/Dhruv/Degree/wdf/studenthub/docs/requirements.md), [`docs/sitemap.md`](file:///d:/Dhruv/Degree/wdf/studenthub/docs/sitemap.md), [`docs/wireframes.md`](file:///d:/Dhruv/Degree/wdf/studenthub/docs/wireframes.md), [`docs/er-diagram.md`](file:///d:/Dhruv/Degree/wdf/studenthub/docs/er-diagram.md), [`docs/api-routes.md`](file:///d:/Dhruv/Degree/wdf/studenthub/docs/api-routes.md) |
| **2** | Semantic HTML5 & Accessibility | `includes/header.php`, `includes/footer.php`, `static/*.html` | Skip link, ARIA landmarks, breadcrumbs, [`docs/accessibility-checklist.md`](file:///d:/Dhruv/Degree/wdf/studenthub/docs/accessibility-checklist.md) |
| **3** | Responsive UI (CSS Grid, Flexbox, Mobile-First) | `assets/css/style.css`, `assets/js/components.js` | App shell layout, sidebar drawer, schedule cards, reusable UI components |
| **4** | DOM Manipulation, Events & LocalStorage | `assets/js/main.js` | Collapsible FAQ, modal popup, image/content slider, banner dismissal, light/dark theme toggle |
| **5** | Registration Form Frontend Validation | `register.php`, `static/register.html`, `assets/js/validation.js` | Regex checks, password strength meter, Canvas CAPTCHA, real-time feedback |
| **6** | Rendering External JSON with Fetch API | `events.php`, `directory.php`, `assets/js/data-render.js`, `data/*.json` | Dynamic fetch, search, filter, sort, pagination, dependent State → City dropdowns, offline cache |
| **7** | PHP Form Processing & CSV/JSON Storage | `contact.php` (CSV), `feedback.php` (JSON) | POST validation, sanitization, file locking (`LOCK_EX`), on-page display of stored records, CSRF protection |
| **8** | MySQL Schema Design, ER & DB Connections | `database/studenthub.sql`, `includes/db.php`, `db-test.php` | Normalized 3NF schema, foreign keys, PDO prepared statements, MySQLi, stored procedures |
| **9** | Secure Registration & Password Hashing | `register.php`, `includes/functions.php` | MySQLi prepared statement, duplicate email check, `password_hash()`, audit logging, DB transactions |
| **10** | Session Login/Logout, RBAC & Remember-Me | `login.php`, `logout.php`, `includes/functions.php` | `password_verify()`, `session_regenerate_id()`, RBAC redirect, 15-min timeout, selector/hash remember token, last-login timestamp |
| **11** | Student Management CRUD & Search | `students.php` | Full MySQLi CRUD, search by name/email/course, delete confirmation modal, CSV export, soft delete (`status` column) |
| **12** | Event CRUD & Validated Poster Upload | `manage_events.php`, `uploads/.htaccess` | Poster upload with real MIME type check (`finfo`), size limit (<= 2MB), randomized filename, PHP execution blocked, category filter |
| **13** | PHP JSON API & AJAX CRUD without Reload | `api/events.php`, `api-demo.php`, `assets/js/api-crud.js` | REST JSON endpoints, HTTP status codes, debounced search, asynchronous DOM update without page reload |
| **14** | Admin Dashboard, RBAC Menu & Audit Log | `admin/dashboard.php`, `admin/audit.php` | Aggregation KPI counters, monthly registration chart via stored procedure, active/inactive user toggle, security audit trail |
| **15** | Final Integration, Testing & Deployment | Full project codebase | [`docs/test-report.md`](file:///d:/Dhruv/Degree/wdf/studenthub/docs/test-report.md), VirtualHost deployment instructions, complete test coverage |

---

## Security Architecture & Best Practices
- **SQL Injection Prevention:** 100% parameterized queries with prepared statements in both PDO and MySQLi. Zero raw query concatenation.
- **Cross-Site Scripting (XSS) Prevention:** Context-aware output escaping via `e()` (`htmlspecialchars(..., ENT_QUOTES, 'UTF-8')`).
- **Cross-Site Request Forgery (CSRF):** Cryptographically strong tokens (`bin2hex(random_bytes(32))`) validated on all POST form submissions and AJAX requests.
- **Session Security:** `session_regenerate_id(true)` upon authentication, `HttpOnly` and `SameSite=Lax` cookies, automatic session destruction after 15 minutes of inactivity.
- **Credential Storage:** `password_hash()` using Bcrypt algorithm; persistent authentication implemented with selector and SHA-256 hashed validator tokens.
- **Upload Hardening:** MIME validation via file inspection (`finfo`), image header verification (`getimagesize()`), non-executable storage directory protected with `.htaccess` (`Require all denied` for script execution).
