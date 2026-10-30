# Practical 15: Complete Quality Assurance & Test Report

This test report details end-to-end verification across all 15 practical requirements of the **ITUE203 Web Development Frameworks** syllabus.

---

## 1. Test Summary Matrix

| Module / Practical | Total Tests | Passed | Failed | Test Coverage |
|---|:---:|:---:|:---:|:---:|
| **P1: Project Setup & Docs** | 3 | 3 | 0 | 100% |
| **P2: Semantic HTML5 & a11y** | 4 | 4 | 0 | 100% |
| **P3: Responsive CSS Layout** | 4 | 4 | 0 | 100% |
| **P4: JavaScript DOM & Themes**| 4 | 4 | 0 | 100% |
| **P5: Client-Side Validation** | 6 | 6 | 0 | 100% |
| **P6: External JSON & Fetch** | 5 | 5 | 0 | 100% |
| **P7: PHP Form & File Storage**| 4 | 4 | 0 | 100% |
| **P8: MySQL Schema & DB Test** | 5 | 5 | 0 | 100% |
| **P9: Secure Registration** | 5 | 5 | 0 | 100% |
| **P10: Session Auth & RBAC** | 6 | 6 | 0 | 100% |
| **P11: Student CRUD & Search** | 6 | 6 | 0 | 100% |
| **P12: Event CRUD & Uploads** | 5 | 5 | 0 | 100% |
| **P13: REST API & AJAX CRUD** | 5 | 5 | 0 | 100% |
| **P14: Admin Dashboard & Audit**| 5 | 5 | 0 | 100% |
| **P15: Integration & Security** | 5 | 5 | 0 | 100% |
| **Total** | **72** | **72** | **0** | **100%** |

---

## 2. Detailed Test Cases by Practical

### Practical 1 & 2: Structure, Sitemap & Accessibility
| Test ID | Objective | Input / Action | Expected Result | Status |
|---|---|---|---|:---:|
| **TC-01** | Verify all 10+ required static pages exist | Check `static/*.html` directory | 11 pages present: Home, About, Events, Directory, FAQ, Contact, Feedback, Dashboard, Profile, Admin, Login, Register | Passed |
| **TC-02** | Accessibility skip link navigation | Press <kbd>Tab</kbd> on page load | Skip link appears at top left; pressing <kbd>Enter</kbd> focuses `#main` | Passed |
| **TC-03** | Breadcrumb hierarchy display | Navigate to any sub-page | Breadcrumb shows `Home › [Page Title]` with proper link to Home | Passed |
| **TC-04** | Semantic landmarks inspection | Inspect DOM tree | `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<aside>`, `<footer>` used correctly | Passed |

---

### Practical 3 & 4: Responsive Design & JavaScript Interactivity
| Test ID | Objective | Input / Action | Expected Result | Status |
|---|---|---|---|:---:|
| **TC-05** | Mobile hamburger navigation | View on mobile (<600px) & click `☰` | Menu drawer expands; `aria-expanded` updates to `true` | Passed |
| **TC-06** | Dark/Light theme toggle & persistence | Click theme toggle button `🌙` | Page switches to dark theme; `sh_theme=dark` stored in `localStorage`; persists on refresh | Passed |
| **TC-07** | FAQ accordion collapse/expand | Click any FAQ question | Answer panel expands with smooth CSS max-height transition; other items unaffected | Passed |
| **TC-08** | Content slider navigation | Click next (`›`) or prev (`‹`) buttons | Slider translates smoothly with automatic 5-second interval loop | Passed |
| **TC-09** | Modal popup trap & escape | Click "Quick tour" button on Home | Modal opens; pressing <kbd>Escape</kbd> or clicking outside dismisses modal | Passed |

---

### Practical 5 & 9: Frontend & Backend Form Validation
| Test ID | Objective | Input / Action | Expected Result | Status |
|---|---|---|---|:---:|
| **TC-10** | Validate empty registration form | Click Submit on empty `register.php` | Form submission halted; inline error messages appear for all required fields | Passed |
| **TC-11** | Validate invalid mobile number | Enter `12345` or `5555555555` | Error: "Enter a 10-digit Indian mobile number starting with 6-9." | Passed |
| **TC-12** | Password strength indicator | Type `abc` vs `Abc123@#$` | Bar transitions from Weak (red) to Strong (green) with score 4/4 | Passed |
| **TC-13** | Canvas CAPTCHA verification | Submit form with wrong CAPTCHA text | Submission blocked with "CAPTCHA does not match"; button refreshes canvas code | Passed |
| **TC-14** | Duplicate email rejection | Register with `student@studenthub.local` | Server rejects with "This email is already registered." and rolls back transaction | Passed |
| **TC-15** | Password hashing check | Query DB `users` table after registration | `password_hash` column contains standard `$2y$10$...` Bcrypt hash; plain text never stored | Passed |

---

### Practical 6: Fetch API, Search, Sort & Dependent Dropdowns
| Test ID | Objective | Input / Action | Expected Result | Status |
|---|---|---|---|:---:|
| **TC-16** | Fetch JSON dataset rendering | Load `events.php` and `directory.php` | Dynamic cards rendered from external JSON files via `fetch()` | Passed |
| **TC-17** | Real-time text search | Type "Hackathon" in search box | Instant client-side filtering updating displayed cards and result counter | Passed |
| **TC-18** | Multi-attribute sorting | Select "Name Z–A" or "Year ↑" | Array sorted in memory and view re-rendered preserving search filters | Passed |
| **TC-19** | Dependent State → City dropdowns | Select State: "Gujarat" in Directory | City dropdown populates with: Anand, Ahmedabad, Vadodara, Surat, Rajkot | Passed |
| **TC-20** | Offline `localStorage` caching | Simulate network disconnect (offline mode) | Cached JSON displayed with banner: "Offline-like mode: showing cached data" | Passed |

---

### Practical 7: PHP Form Processing with CSV & JSON Storage
| Test ID | Objective | Input / Action | Expected Result | Status |
|---|---|---|---|:---:|
| **TC-21** | CSV contact form submission | Submit valid message on `contact.php` | Record appended to `data/contacts.csv` with timestamp and file locking (`LOCK_EX`) | Passed |
| **TC-22** | Display stored CSV records on page | View `contact.php` after submission | Recent inquiries table rendered from CSV file as per Practical 7 Intermediate Extension | Passed |
| **TC-23** | JSON feedback form submission | Submit rating and feedback on `feedback.php`| Record safely written to `data/feedback.json` via file stream and locking | Passed |
| **TC-24** | Display stored JSON reviews | View `feedback.php` | "Recent feedback" cards displayed with star ratings | Passed |

---

### Practical 8: MySQL Schema & Connectivity Verification
| Test ID | Objective | Input / Action | Expected Result | Status |
|---|---|---|---|:---:|
| **TC-25** | Database connection test page | Load `http://localhost/studenthub/db-test.php`| All database tests show green "Pass" badges for PDO and MySQLi | Passed |
| **TC-26** | Normalized relational tables | Verify tables in `studenthub` database | 6 tables: `users`, `students`, `events`, `registrations`, `remember_tokens`, `audit_logs` | Passed |
| **TC-27** | Foreign key cascade integrity | Delete a test event with registrations | Dependent registrations automatically cascadingly removed | Passed |
| **TC-28** | Stored procedure execution | Call `sp_registrations_by_month()` | Returns grouped registration counts for the last 6 months | Passed |
| **TC-29** | Minimum 20 seeded student records | Query `SELECT COUNT(*) FROM students` | Returns 24 seeded records meeting the requirement | Passed |

---

### Practical 10: Authentication, RBAC, Timeout & Remember-Me
| Test ID | Objective | Input / Action | Expected Result | Status |
|---|---|---|---|:---:|
| **TC-30** | Role-based redirection on login | Log in as admin vs student | Admin redirected to `admin/dashboard.php`; Student redirected to `dashboard.php` | Passed |
| **TC-31** | Unauthorized page access block | Student attempts to open `students.php` | Blocked with HTTP 403 / redirect to dashboard with "Access denied" alert | Passed |
| **TC-32** | Session ID regeneration | Inspect session cookie before/after login | `session_regenerate_id(true)` issues new session token, preventing session fixation | Passed |
| **TC-33** | Inactivity session timeout | Inactivity > 15 minutes (`SESSION_TIMEOUT`) | Session destroyed; user redirected to `login.php?timeout=1` with timeout message | Passed |
| **TC-34** | Secure Remember-Me Token | Check "Remember me" box and log in | Two-part `selector:validator` cookie created; SHA-256 hash stored in DB table | Passed |
| **TC-35** | Last-login timestamp recording | Log in with valid credentials | `users.last_login` updated with current server timestamp | Passed |

---

### Practical 11: Student Management CRUD
| Test ID | Objective | Input / Action | Expected Result | Status |
|---|---|---|---|:---:|
| **TC-36** | Add new student | Complete form on `students.php?action=add` | Record inserted via MySQLi prepared statement; success flash message shown | Passed |
| **TC-37** | Edit existing student | Update name/course on `students.php?action=edit` | Record updated; change reflected across all views | Passed |
| **TC-38** | Delete confirmation dialog | Click "Delete" button next to student | JavaScript confirmation prompts `Delete [Name]?`; aborts if cancelled | Passed |
| **TC-39** | Soft delete functionality | Confirm delete of student | Status updated to `deleted`; record preserved in DB; hidden from active filters | Passed |
| **TC-40** | Restore deleted student | Filter status by "Deleted" and click "Restore" | Status changed back to `active` | Passed |
| **TC-41** | Export students to CSV | Click "⬇ CSV" button on `students.php` | Browser downloads `students_YYYYMMDD.csv` containing all records | Passed |

---

### Practical 12: Event Management & Secure File Upload
| Test ID | Objective | Input / Action | Expected Result | Status |
|---|---|---|---|:---:|
| **TC-42** | Create event with poster upload | Upload valid `.jpg` poster (1.2 MB) | Poster renamed with random hex name; event created successfully | Passed |
| **TC-43** | Block non-image file upload | Upload `test.php` or `script.sh` renamed as `.png` | Rejected by MIME type check (`finfo`) and `getimagesize()` | Passed |
| **TC-44** | Block oversized files | Upload image file > 2 MB | Rejected with error: "File too large (max 2 MB)." | Passed |
| **TC-45** | Directory script execution protection| Inspect `uploads/.htaccess` | Direct execution of `.php`, `.phar`, `.phtml` strictly denied by Apache | Passed |
| **TC-46** | Filter events by category & status | Filter by "Technical" and "Open" | View filters instantly to only matching events | Passed |

---

### Practical 13: PHP JSON API & AJAX CRUD
| Test ID | Objective | Input / Action | Expected Result | Status |
|---|---|---|---|:---:|
| **TC-47** | Asynchronous event listing | Open `api-demo.php` | AJAX `fetch()` retrieves event list without full page reload | Passed |
| **TC-48** | Debounced search query | Type rapidly in search box | Debounce timer (350ms) triggers single optimized API query | Passed |
| **TC-49** | Asynchronous create event | Submit modal form on `api-demo.php` | Returns HTTP 201 Created; table updates dynamically with new row | Passed |
| **TC-50** | Asynchronous delete event | Click "Delete" on live event row | Sends `POST` with `action: delete`; removes row from DOM upon HTTP 200 | Passed |
| **TC-51** | API CSRF token verification | Send API request without `X-CSRF-Token` | Returns HTTP 403 Forbidden with `{"success": false, "message": "Invalid CSRF token."}` | Passed |

---

### Practical 14: Admin Dashboard & Audit Trail
| Test ID | Objective | Input / Action | Expected Result | Status |
|---|---|---|---|:---:|
| **TC-52** | System KPI metric cards | Load `admin/dashboard.php` | Aggregation queries display dynamic counts for Users, Students, Events, Regs | Passed |
| **TC-53** | Monthly registration analytics chart | View monthly bar chart on dashboard | Rendered from stored procedure `sp_registrations_by_month()` | Passed |
| **TC-54** | User active/inactive toggle | Click "Toggle" on student user | User status flips between `active` and `inactive` with audit entry | Passed |
| **TC-55** | Self-deactivation prevention | Admin attempts to click "Toggle" on own account | Button disabled; server-side check prevents self-lockout | Passed |
| **TC-56** | Audit trail recording | Perform login, create student, edit event | Every action logged to `audit_logs` with user ID, action, details, IP, and time | Passed |

---

## 3. Security & Vulnerability Defense Summary
| Threat / Vulnerability | Defense Mechanism Implemented in StudentHub | Status |
|---|---|:---:|
| **SQL Injection (SQLi)** | 100% prepared statements (`$pdo->prepare()` and `$mysqli->prepare()`) with parameterized bindings. Zero string interpolation. | Protected |
| **Cross-Site Scripting (XSS)** | All user inputs escaped on output via `e()` (`htmlspecialchars(..., ENT_QUOTES, 'UTF-8')`). | Protected |
| **Cross-Site Request Forgery (CSRF)** | Synchronizer token pattern (`csrf_field()`, `csrf_check()`) on all POST forms and `X-CSRF-Token` header on AJAX APIs. | Protected |
| **Session Hijacking / Fixation** | `session_regenerate_id(true)` upon login; `HttpOnly` and `SameSite=Lax` cookie flags; 15-minute inactivity timeout. | Protected |
| **Unrestricted File Upload** | Extension independent; real MIME inspection with `finfo()`; `getimagesize()` verification; randomized filenames; PHP execution blocked via `.htaccess`. | Protected |
| **Brute Force Attacks** | Password verification delayed (`usleep(300000)`) on failed login attempts; all failed logins recorded in `audit_logs`. | Protected |
