# Practical 1: StudentHub Sitemap & Navigation Architecture

**Student-ID:** D26CE154  
**Student-Name:** Dhruv Bhoi  
**Department:** CSPIT-CE, Faculty of Technology and Engineering (FTE)  
**Subject:** Web Development Frameworks (ITUE203) — Semester 3, 2026-27 (ODD)  
**Institution:** CHAROTAR UNIVERSITY OF SCIENCE AND TECHNOLOGY (CHARUSAT)  

---

## 1. Complete Site Tree & Route Hierarchy
```
StudentHub Root
│
├── Public Section (Unauthenticated)
│   ├── Home (index.php / static/index.html)
│   ├── About Us (about.php / static/about.html)
│   ├── Events Catalog (events.php / static/events.html) [Fetch API]
│   ├── Student Directory (directory.php / static/directory.html) [Fetch API + Dependent Dropdowns]
│   ├── FAQ Accordion (faq.php / static/faq.html)
│   ├── Contact Us (contact.php / static/contact.html) [CSV Storage]
│   ├── Feedback (feedback.php / static/feedback.html) [JSON Storage]
│   ├── Register (register.php / static/register.html) [Regex + Canvas CAPTCHA]
│   └── Login (login.php / static/login.html)
│
├── Authenticated Student Portal (Role: student)
│   ├── Student Dashboard (dashboard.php) [Timetable, Donut Rings, Notices, Event RSVP]
│   ├── Student Profile (profile.php) [Academic Details, Achievements, Profile Edit]
│   ├── Live AJAX Events (api-demo.php) [Asynchronous REST CRUD]
│   └── Logout (logout.php)
│
└── Authenticated Admin Panel (Role: admin)
    ├── Admin Dashboard (admin/dashboard.php) [KPI Counters, Stored Procedure Analytics]
    ├── Student Management (students.php) [MySQLi CRUD, Search, Filter, Soft Delete, CSV Export]
    ├── Event Management (manage_events.php) [Poster Upload, MIME Validation, Filters]
    ├── Security Audit Trail (admin/audit.php) [Action Logs, Timestamps, IPs]
    └── Database Test Suite (db-test.php) [Connection Verification & Schema Inspector]
```

---

## 2. Navigation Flow & Role-Based Access
1. **Public Visitor:** Lands on Home → Browses Catalog, Directory & FAQs → Enters Registration or Login.
2. **Student Journey:** Authenticates via `login.php` → Redirected to `dashboard.php` → Views Timetable & Notice Board → Confirms event seats → Edits academic profile in `profile.php`.
3. **Admin Journey:** Authenticates via `login.php` → Redirected to `admin/dashboard.php` → Moderates students in `students.php` → Publishes events with posters in `manage_events.php` → Reviews security logs in `admin/audit.php`.
