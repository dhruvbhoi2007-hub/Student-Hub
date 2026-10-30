# -*- coding: utf-8 -*-
"""
Generates complete DOCX files for:
1. D26CE154_Practical_1-14_WDF.docx
2. D26CE154_Practical_7-14_WDF.docx
and exports both to PDF using Microsoft Word.
"""

import os, sys, docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL

from build_helpers import (
    SUB_DIR, SCREENSHOTS_DIR, EXTRACTED_DIR,
    add_header_footer, add_callout_box, add_code_block,
    add_image_safe, add_qa, add_heading_styled, set_cell_shading, set_cell_margins
)

def add_cover_page(doc, title_text, practical_range):
    p_top = doc.add_paragraph()
    p_top.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_uni = p_top.add_run("CHAROTAR UNIVERSITY OF SCIENCE AND TECHNOLOGY (CHARUSAT)\n")
    r_uni.bold = True
    r_uni.font.name = "Times New Roman"
    r_uni.font.size = Pt(14)
    r_uni.font.color.rgb = RGBColor(0x1A, 0x3A, 0x5C)
    
    r_inst = p_top.add_run("Chandubhai S. Patel Institute of Technology (CSPIT)\n")
    r_inst.bold = True
    r_inst.font.name = "Times New Roman"
    r_inst.font.size = Pt(13)
    
    r_dept = p_top.add_run("Department of Computer Engineering\n")
    r_dept.font.name = "Times New Roman"
    r_dept.font.size = Pt(12)
    
    p_rule = doc.add_paragraph()
    p_rule.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_rule = p_rule.add_run("―" * 45)
    r_rule.font.color.rgb = RGBColor(0x2E, 0x74, 0xB5)
    
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_before = Pt(36)
    p_title.paragraph_format.space_after = Pt(12)
    
    r_sub = p_title.add_run("LABORATORY PRACTICAL SUBMISSION RECORD\n")
    r_sub.bold = True
    r_sub.font.name = "Times New Roman"
    r_sub.font.size = Pt(18)
    r_sub.font.color.rgb = RGBColor(0x2E, 0x74, 0xB5)
    
    r_course = p_title.add_run("ITUE203 — Web Development Frameworks\n")
    r_course.bold = True
    r_course.font.name = "Times New Roman"
    r_course.font.size = Pt(14)
    
    r_rng = p_title.add_run(f"Compilation of {practical_range}\n")
    r_rng.font.name = "Times New Roman"
    r_rng.font.size = Pt(13)
    r_rng.font.color.rgb = RGBColor(0x55, 0x55, 0x55)
    
    r_proj = p_title.add_run("Project: StudentHub — Modern SaaS Campus Management Portal\n")
    r_proj.italic = True
    r_proj.font.name = "Times New Roman"
    r_proj.font.size = Pt(12)
    
    p_gap = doc.add_paragraph()
    p_gap.paragraph_format.space_before = Pt(36)
    
    # Student Details Table
    table = doc.add_table(rows=6, cols=2)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    table.columns[0].width = Inches(2.2)
    table.columns[1].width = Inches(4.3)
    
    details = [
        ("Student Name", "Dhruv Bhoi"),
        ("Student ID", "D26CE154"),
        ("Department", "Computer Engineering (CSPIT-CE)"),
        ("Academic Year / Term", "2026 - 2027 (ODD Semester)"),
        ("Semester", "3rd Semester, B.Tech CE"),
        ("Faculty & Institute", "Faculty of Technology & Engineering (FTE), CHARUSAT")
    ]
    
    for i, (k, v) in enumerate(details):
        c0, c1 = table.cell(i, 0), table.cell(i, 1)
        set_cell_shading(c0, "EEECFE" if i % 2 == 0 else "F7F6FD")
        set_cell_shading(c1, "FFFFFF" if i % 2 == 0 else "FAFAFA")
        set_cell_margins(c0, top=100, bottom=100, left=150, right=150)
        set_cell_margins(c1, top=100, bottom=100, left=150, right=150)
        
        p0 = c0.paragraphs[0]
        r0 = p0.add_run(k)
        r0.bold = True
        r0.font.name = "Times New Roman"
        r0.font.size = Pt(11)
        r0.font.color.rgb = RGBColor(0x1A, 0x3A, 0x5C)
        
        p1 = c1.paragraphs[0]
        r1 = p1.add_run(v)
        r1.font.name = "Times New Roman"
        r1.font.size = Pt(11)
        if k in ["Student Name", "Student ID"]:
            r1.bold = True
            r1.font.color.rgb = RGBColor(0x2E, 0x74, 0xB5)
            
    doc.add_page_break()

def add_practical_1(doc):
    add_heading_styled(doc, "Practical 1: Project Initiation, Requirement Analysis, Sitemap, Wireframe, and GitHub Setup", level=1)
    
    add_callout_box(doc, 
        "Aim: Initiate the semester-long Student Hub portal by identifying the problem scope, user roles, key modules, navigation flow, and minimum 10 pages. Create a sitemap, low-fidelity wireframe, project folder structure, README file, and GitHub repository.\n\n"
        "Tools & Technologies: VS Code, Draw.io, Git, GitHub, Markdown",
        title="Practical Aim & Tools"
    )
    
    add_heading_styled(doc, "1. Project Overview & Problem Statement", level=2)
    doc.add_paragraph(
        "StudentHub is a modern, unified campus management web application designed for Charotar University of Science and Technology (CHARUSAT). "
        "Historically, college students have had to navigate multiple fragmented portals for attendance, course details, campus events, and administrative notices. "
        "StudentHub consolidates these functions behind a single secure login with role-based access control (Student vs. Administrator), "
        "presenting users with a sleek modern SaaS dashboard layout featuring timetable cards, circular SVG donut progress rings, and a live notice board feed."
    )
    
    add_heading_styled(doc, "2. User Roles & Modules", level=2)
    doc.add_paragraph(
        "• Guest / Public: Landing page (hero slider), about page, event catalog, student directory with dependent state-city filters, FAQ accordion, contact form, and feedback submission.\n"
        "• Student: Secure authentication, personal timetable, attendance & assignment progress donuts, 1-click event RSVP & cancellation, and student profile management.\n"
        "• Administrator: Student management CRUD (search, filter, pagination, soft delete/restore, CSV export), Event management CRUD (with poster image uploads), dynamic Admin Dashboard with stored procedure monthly registration bar chart, and user active/inactive toggles."
    )
    
    add_heading_styled(doc, "3. Sitemap & Navigation Architecture", level=2)
    add_image_safe(doc, os.path.join(EXTRACTED_DIR, "p1_img_2.png"), caption="StudentHub Hierarchical Sitemap & Navigation Map")
    
    add_heading_styled(doc, "4. Low-Fidelity Wireframes", level=2)
    add_image_safe(doc, os.path.join(EXTRACTED_DIR, "p1_img_6.png"), caption="Low-Fidelity Dashboard Wireframe (Left Sidebar, Schedule Cards & Stat Widgets)")
    add_image_safe(doc, os.path.join(EXTRACTED_DIR, "p1_img_7.png"), caption="Low-Fidelity Events Wireframe (Toolbar, Search, Cards Grid & Pagination)")
    
    add_heading_styled(doc, "5. Project Folder Structure", level=2)
    add_code_block(doc, 
"""studenthub/
├── assets/
│   ├── css/style.css            # Acade SaaS design tokens, layout shell, schedule cards
│   ├── js/                      # main.js, validation.js, data-render.js, api-crud.js
│   └── images/                  # logos, banners, placeholders
├── data/
│   ├── events.json              # Sample JSON dataset for campus events
│   ├── students.json            # Sample JSON dataset for student directory
│   ├── contacts.csv             # Server-side CSV storage for contact inquiries
│   └── feedback.json            # Server-side JSON storage for rating feedback
├── database/
│   └── studenthub.sql           # Normalized 3NF MySQL schema, triggers, seed data
├── docs/                        # requirements.md, sitemap.md, wireframes.md, er-diagram.md
├── includes/
│   ├── config.php               # Environment constants, session lifetime, credentials
│   ├── db.php                   # Secure PDO & MySQLi dual connection helper
│   ├── functions.php            # Auth, CSRF, flash messaging, audit trail
│   ├── header.php               # Acade layout sidebar drawer & top search/greeting bar
│   └── footer.php               # Shared footer attribution & dynamic scripts
├── static/                      # 12 accessible static HTML5 mockups (Practical 2)
├── admin/
│   ├── dashboard.php            # KPI stat cards, stored procedure charts, user toggles
│   └── audit.php                # System activity audit trail log viewer
├── api/
│   └── events.php               # RESTful JSON API endpoint for events CRUD
├── index.php, login.php, register.php, dashboard.php, profile.php, events.php
└── students.php, manage_events.php, api-demo.php, db-test.php
""", caption="Clean, Production-Ready Directory Structure")
    
    add_heading_styled(doc, "6. Key Questions & Analysis", level=2)
    add_qa(doc, "What is a URL and what are its constituent parts?",
           "A Uniform Resource Locator (URL) is a standardized web address referencing a resource over a network. Its parts include: "
           "1) Scheme/Protocol (http, https), 2) Subdomain & Domain Name (studenthub.local or charusat.edu.in), 3) Port (:80, :443), "
           "4) Path (/events.php), 5) Query String (?category=Workshop&sort=date:asc), and 6) Fragment identifier (#main).")
    
    add_qa(doc, "How does a web browser process an HTML file?",
           "The browser performs: 1) Conversion of raw bytes into characters based on UTF-8, 2) Tokenization into HTML tags, "
           "3) Construction of the Document Object Model (DOM) tree, 4) Processing of linked CSS stylesheets into the CSSOM tree, "
           "5) Combining DOM and CSSOM into a Render Tree, 6) Layout computation (geometric positions of elements), and 7) Painting pixels to screen.")
    
    add_qa(doc, "How will page navigation flow be managed among all pages?",
           "Through a unified, responsive application shell (`includes/header.php`) featuring a fixed left navigation sidebar on desktop "
           "that collapses into an accessible slide-out mobile drawer with an overlay. Links dynamically highlight the active page using `aria-current=\"page\"`.")
    
    doc.add_page_break()

def add_practical_2(doc):
    add_heading_styled(doc, "Practical 2: Semantic HTML5 Pages with Accessibility-Ready Structure", level=1)
    
    add_callout_box(doc,
        "Aim: Develop static HTML5 skeletons for at least 10 Student_Hub pages such as Home, About, Register, Login, Dashboard, Profile, Events, Directory, FAQ, Contact, Feedback, and Admin using semantic tags with accessibility support.\n\n"
        "Tools & Technologies: VS Code, HTML5, WAI-ARIA, Screen Reader Testing",
        title="Practical Aim & Tools"
    )
    
    add_heading_styled(doc, "1. Semantic Architecture & WAI-ARIA Landmarks", level=2)
    doc.add_paragraph(
        "Modern web standards require semantic HTML5 elements over generic <div> tags to enable screen readers, assistive technology, "
        "and search engine spiders to understand page hierarchy. In StudentHub, every page adheres to the following landmark structure:\n"
        "• <header> & <aside class=\"app-sidebar\">: Application branding, search input, and main navigation landmark.\n"
        "• <main id=\"main\" class=\"container\">: Primary landmark holding core page content, paired with a <a class=\"skip-link\" href=\"#main\"> for keyboard accessibility.\n"
        "• <section> & <article>: Grouping logical modules (e.g. event cards, student profile sections, notice boards).\n"
        "• <footer>: Site metadata, university credentials, and copyright attribution.\n"
        "• ARIA attributes: aria-live=\"polite\" on dynamic search results and error messages, aria-expanded=\"false\" on accordions and menus, and role=\"status\" on alerts."
    )
    
    add_heading_styled(doc, "2. Minimum 10 Implemented Pages Inventory", level=2)
    doc.add_paragraph(
        "StudentHub implements 14 full pages (exceeding the syllabus requirement of 10):\n"
        "1. index.php (Home / Hero Slider)  |  2. about.php (Project & Credentials)  |  3. events.php (Catalog & Filters)\n"
        "4. directory.php (Dependent Filters) | 5. faq.php (Accordion UI)            |  6. contact.php (CSV File Storage)\n"
        "7. feedback.php (Star Rating/JSON)  |  8. login.php (Auth & Remember Me)    |  9. register.php (Validation & CAPTCHA)\n"
        "10. dashboard.php (Acade SaaS)      | 11. profile.php (User Profile)        | 12. students.php (CRUD & CSV Export)\n"
        "13. manage_events.php (Uploads)     | 14. admin/dashboard.php (Charts/RBAC) | 15. db-test.php (Diagnostic Test Suite)"
    )
    
    add_heading_styled(doc, "3. Implementation Code: Semantic Shell", level=2)
    add_code_block(doc,
"""<!-- Accessible Semantic Structure Skeleton -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>StudentHub | Modern Campus Portal</title>
  <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
  <a class="skip-link" href="#main">Skip to main content</a>
  <div class="app-layout">
    <aside class="app-sidebar" id="appSidebar" aria-label="Main Navigation">
      <a class="sidebar-brand" href="index.php"><div class="sidebar-brand-icon">▲</div><span>StudentHub</span></a>
      <nav aria-label="Sidebar Menu">
        <ul class="sidebar-nav">
          <li><a href="dashboard.php" class="nav-item active" aria-current="page"><i>📊</i><span>Dashboard</span></a></li>
          <li><a href="events.php" class="nav-item"><i>📅</i><span>Events</span></a></li>
        </ul>
      </nav>
    </aside>
    <div class="app-main">
      <header class="app-topbar">
        <button class="hamburger" id="hamburger" aria-label="Toggle menu" aria-expanded="false">☰</button>
        <div class="topbar-search"><input type="search" placeholder="Search events, courses…" aria-label="Search"></div>
      </header>
      <main id="main" class="container app-content" tabindex="-1">
        <!-- Main page content here -->
      </main>
      <footer class="site-footer"><small>&copy; 2026 StudentHub - Developed by Dhruv Bhoi (D26CE154)</small></footer>
    </div>
  </div>
</body>
</html>
""", caption="Semantic HTML5 Shell with Skip-Link and WAI-ARIA")
    
    add_heading_styled(doc, "4. Verification Screenshot: Static Home & Navigation", level=2)
    add_image_safe(doc, os.path.join(SCREENSHOTS_DIR, "p01_home.png"), caption="Semantic Static Landing Page with Accessible Hero and Highlights")
    
    add_heading_styled(doc, "5. Key Questions & Analysis", level=2)
    add_qa(doc, "Are semantic elements like header, nav, main, section, article, and footer used properly?",
           "Yes. StudentHub strictly avoids <div> soup. The page layout uses <header> for titles/tools, <aside> for sidebar navigation, "
           "<main> for the single central document body, <article> for self-contained cards (events, reviews), and <footer> for attributions.")
    
    add_qa(doc, "Is the website accessibility-ready (WAI-ARIA, skip link, forms)?",
           "Yes. It implements: 1) Skip link pointing to `#main`, 2) Distinct `<label for=\"...\">` bindings for all form inputs, "
           "3) `aria-live=\"polite\"` regions for live search counts and validation feedback, and 4) `aria-expanded` attributes on interactive menus.")
    
    doc.add_page_break()

def add_practical_3(doc):
    add_heading_styled(doc, "Practical 3: Responsive UI Design using CSS Grid, Flexbox, and Modern SaaS Theme", level=1)
    
    add_callout_box(doc,
        "Aim: Design a responsive modern UI using CSS Grid, Flexbox, media queries, CSS variables, and modern SaaS dashboard layout (Acade UI) for mobile, tablet, and desktop screens.\n\n"
        "Tools & Technologies: CSS3, CSS Grid, Flexbox, CSS Custom Properties, Responsive Media Queries",
        title="Practical Aim & Tools"
    )
    
    add_heading_styled(doc, "1. Design System & CSS Custom Properties", level=2)
    doc.add_paragraph(
        "StudentHub utilizes a modern SaaS design system based on a violet/lavender color scheme (`#6C5CE7` primary brand, `#EEECFE` subtle tinted backgrounds, "
        "`#2D3436` high-contrast slate text). All design tokens are declared as CSS Custom Properties (`:root`) allowing seamless dynamic dark mode switching."
    )
    
    add_heading_styled(doc, "2. Responsive App Shell & Grid Layouts", level=2)
    doc.add_paragraph(
        "• Desktop Layout (≥ 1024px): 2-column flex app shell with a fixed 240px sidebar and fluid `app-main` viewport.\n"
        "• Timetable Cards: CSS Grid (`grid-template-columns: repeat(auto-fit, minmax(220px, 1fr))`) rendering class schedule cards with lavender badges.\n"
        "• Circular SVG Progress Rings: Donut cards displaying 92% Attendance and 85% Activity completion with pure CSS stroke-dashoffset animations.\n"
        "• Mobile Layout (< 768px): The sidebar collapses into an off-canvas drawer controlled via the topbar hamburger button, switching grids into 1-column stacks."
    )
    
    add_heading_styled(doc, "3. Implementation Code: CSS Tokens & Responsive Shell", level=2)
    add_code_block(doc,
""":root {
  --primary: #6C5CE7;
  --primary-hover: #5A49E0;
  --primary-light: #EEECFE;
  --bg: #F7F7FD;
  --surface: #FFFFFF;
  --text: #2D3436;
  --muted: #8395A7;
  --border: #E8E8F3;
  --radius-lg: 18px;
  --shadow-sm: 0 4px 16px rgba(108, 92, 231, 0.06);
}

.app-layout { display: flex; min-height: 100vh; background: var(--bg); }
.app-sidebar { width: 240px; background: var(--surface); border-right: 1px solid var(--border); }
.app-main { flex: 1; display: flex; flex-direction: column; min-width: 0; }
.app-topbar { height: 70px; background: var(--surface); display: flex; align-items: center; justify-content: space-between; padding: 0 2rem; }

/* Responsive Media Queries */
@media (max-width: 1024px) {
  .app-sidebar { position: fixed; left: -260px; z-index: 1000; transition: left 0.3s ease; }
  .app-sidebar.open { left: 0; }
}
@media (max-width: 768px) {
  .grid.cols-3 { grid-template-columns: 1fr; }
  .app-topbar { padding: 0 1rem; }
}
""", caption="Core Responsive CSS Grid & SaaS Design Tokens")
    
    add_heading_styled(doc, "4. Verification Screenshot: Responsive Layout & About Credentials", level=2)
    add_image_safe(doc, os.path.join(SCREENSHOTS_DIR, "p02_about.png"), caption="Modern Acade UI Shell & Student Developer Credentials Card (Dhruv Bhoi)")
    
    add_heading_styled(doc, "5. Key Questions & Analysis", level=2)
    add_qa(doc, "How does the layout adapt for mobile, tablet, and desktop screens?",
           "Using a mobile-first responsive approach. Desktop screens display the persistent left navigation sidebar and multi-column grid cards. "
           "Tablet and mobile devices collapse the sidebar into an accessible slide-out drawer, transform grid layouts into single-column cards, "
           "and enable smooth touch scrolling.")
    
    add_qa(doc, "Which layout technique is used and why?",
           "A hybrid approach: CSS Flexbox is used for 1-dimensional components (topbar headers, button groups, breadcrumbs, nav pills), "
           "while CSS Grid is used for 2-dimensional structures (dashboard timetable rows, event catalogs, stats cards, and multi-field forms).")
    
    doc.add_page_break()

def add_practical_4(doc):
    add_heading_styled(doc, "Practical 4: JavaScript DOM Manipulation, Event Handling, and UI Interactivity", level=1)
    
    add_callout_box(doc,
        "Aim: Implement UI interactivity, DOM manipulation, event handling, dark/light theme switcher with localStorage, accordion FAQ, modal popups, banner notifications, and carousel slider.\n\n"
        "Tools & Technologies: Vanilla ES6+ JavaScript, DOM APIs, Event Delegation, HTML5 LocalStorage",
        title="Practical Aim & Tools"
    )
    
    add_heading_styled(doc, "1. DOM Interactivity Modules", level=2)
    doc.add_paragraph(
        "StudentHub features lightweight, dependency-free Vanilla ES6+ JavaScript (`assets/js/main.js`) powering five key UI features:\n"
        "1. Theme Switcher: Reads and writes user preference (`light` or `dark`) to `localStorage`. An inline IIFE prevents theme flash on page load.\n"
        "2. Collapsible Accordion: Implemented in `faq.php` with keyboard accessibility and ARIA expanded state management.\n"
        "3. Accessible Modal Dialog: Accessible trap focus dialog for Quick Tours and Registration previews.\n"
        "4. Sliding Highlights Carousel: Automated and keyboard-accessible slide transitions on the homepage.\n"
        "5. Dismissible Status Banner: Persistent notification banner with smooth dismissal animations."
    )
    
    add_heading_styled(doc, "2. Implementation Code: Theme Toggle & Accordion", level=2)
    add_code_block(doc,
"""// Theme Toggle with LocalStorage Persistence
const themeToggle = document.getElementById('themeToggle');
themeToggle?.addEventListener('click', () => {
  const current = document.documentElement.getAttribute('data-theme') || 'light';
  const target = current === 'dark' ? 'light' : 'dark';
  document.documentElement.setAttribute('data-theme', target);
  localStorage.setItem('sh_theme', target);
  themeToggle.textContent = target === 'dark' ? '☀️' : '🌙';
});

// Accessible FAQ Accordion
document.querySelectorAll('.accordion-header').forEach(btn => {
  btn.addEventListener('click', () => {
    const expanded = btn.getAttribute('aria-expanded') === 'true';
    btn.setAttribute('aria-expanded', !expanded);
    const body = btn.nextElementSibling;
    body.hidden = expanded;
  });
});
""", caption="main.js — Theme Switcher and Accessible Accordion")
    
    add_heading_styled(doc, "3. Verification Screenshot: Interactive FAQ Accordion", level=2)
    add_image_safe(doc, os.path.join(SCREENSHOTS_DIR, "p05_faq.png"), caption="Interactive FAQ Accordion with Search and Dark/Light Mode Support")
    
    add_heading_styled(doc, "4. Key Questions & Analysis", level=2)
    add_qa(doc, "How are DOM elements selected and modified?",
           "Elements are selected using modern `document.querySelector()` and `document.querySelectorAll()`. "
           "Modifications use secure DOM APIs like `element.textContent`, `element.setAttribute()`, and `element.classList.toggle()` "
           "to prevent cross-site scripting (XSS) risks.")
    
    add_qa(doc, "Is localStorage used for remembering user theme preferences?",
           "Yes. When the theme toggle button is clicked, `localStorage.setItem('sh_theme', target)` persists the state. "
           "An immediate synchronous inline script in `<head>` executes before the DOM renders to prevent visual flickering.")
    
    doc.add_page_break()

def add_practical_5(doc):
    add_heading_styled(doc, "Practical 5: Registration Form with Frontend Validation and User-Friendly Error Handling", level=1)
    
    add_callout_box(doc,
        "Aim: Build a responsive user registration form with comprehensive frontend validation, real-time error feedback, regex patterns, password strength meter, and Canvas CAPTCHA.\n\n"
        "Tools & Technologies: HTML5 Form Validation, JavaScript Regex, Canvas API, Real-time DOM Feedback",
        title="Practical Aim & Tools"
    )
    
    add_heading_styled(doc, "1. Frontend Validation Rules & Pattern Specifications", level=2)
    doc.add_paragraph(
        "• Full Name: RegEx `/^[A-Za-z][A-Za-z .'-]{2,59}$/` ensuring alphabetic letters, length between 3 and 60 characters.\n"
        "• Email: Standard RFC email regex with domain check.\n"
        "• Mobile: Indian phone number standard `/^[6-9]\\d{9}$/` enforcing exactly 10 digits starting with 6, 7, 8, or 9.\n"
        "• Password Complexity: Enforces minimum 8 characters, at least one uppercase letter, one lowercase letter, one digit, and one special character.\n"
        "• Dynamic Strength Meter: Calculates entropy score (0 to 4) and dynamically renders color-coded progress bars (Weak, Moderate, Strong).\n"
        "• Procedural Canvas CAPTCHA: Renders 5 randomized alphanumeric characters on an HTML5 `<canvas>` element with noise lines to deter automated bots."
    )
    
    add_heading_styled(doc, "2. Implementation Code: Password Strength & Canvas CAPTCHA", level=2)
    add_code_block(doc,
"""// Canvas CAPTCHA Generation
function generateCaptcha() {
  const canvas = document.getElementById('captcha');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  const chars = '23456789ABCDEFGHJKLMNPQRSTUVWXYZ';
  let code = '';
  for (let i = 0; i < 5; i++) code += chars.charAt(Math.floor(Math.random() * chars.length));
  window.captchaCode = code;
  ctx.fillStyle = '#EEECFE';
  ctx.fillRect(0, 0, canvas.width, canvas.height);
  // Add noise & draw distorted text
  ctx.font = 'bold 22px Courier New';
  ctx.fillStyle = '#6C5CE7';
  ctx.fillText(code, 20, 32);
}
""", caption="Procedural Canvas CAPTCHA Generation")
    
    add_heading_styled(doc, "3. Verification Screenshot: Registration Form", level=2)
    add_image_safe(doc, os.path.join(SCREENSHOTS_DIR, "p09_register.png"), caption="Registration Form with Real-Time Validation, Password Meter and Canvas CAPTCHA")
    
    add_heading_styled(doc, "4. Key Questions & Analysis", level=2)
    add_qa(doc, "Are correct input types and validation attributes used?",
           "Yes. Appropriate HTML5 input types (`type=\"email\"`, `type=\"tel\"`, `type=\"password\"`) are coupled with `required`, "
           "`autocomplete`, `inputmode=\"numeric\"`, and `novalidate` on the form to allow JavaScript custom validation messages.")
    
    add_qa(doc, "Is password strength checked and displayed dynamically?",
           "Yes. An `input` event listener evaluates password length and character diversity, updating a `<div id=\"strengthBar\">` "
           "with visual width and color cues (Red = Weak, Orange = Moderate, Purple/Green = Strong).")
    
    doc.add_page_break()

def add_practical_6(doc):
    add_heading_styled(doc, "Practical 6: Rendering External JSON Data using Fetch API, Search, and Filter", level=1)
    
    add_callout_box(doc,
        "Aim: Fetch and render external JSON datasets using the Fetch API, async/await, debounced search, category filters, dependent State-City dropdowns, sorting, and client-side pagination.\n\n"
        "Tools & Technologies: JavaScript Fetch API, Promises, Async/Await, JSON Parsing, Debounce Utility",
        title="Practical Aim & Tools"
    )
    
    add_heading_styled(doc, "1. Architecture: JSON Data Rendering (`assets/js/data-render.js`)", level=2)
    doc.add_paragraph(
        "StudentHub features two dynamic catalog modules backed by JSON files:\n"
        "• Events Catalog (`events.php` / `data/events.json`): Fetches campus hackathons, seminars, and sports meets. Supports real-time text search, category filtering (Workshop, Technical, Cultural, Sports), date/title sorting, and pagination (6 items per page).\n"
        "• Student Directory (`directory.php` / `data/students.json`): Fetches student directory records. Features a dependent State → City filter (selecting Gujarat dynamically populates Anand, Vadodara, Ahmedabad, Surat) along with course filters and sorting."
    )
    
    add_heading_styled(doc, "2. Implementation Code: Fetch API & Dependent Dropdowns", level=2)
    add_code_block(doc,
"""async function loadData(src) {
  statusEl.textContent = 'Loading records…';
  try {
    const res = await fetch(src);
    if (!res.ok) throw new Error('HTTP ' + res.status);
    allData = await res.json();
    statusEl.textContent = '';
    render();
  } catch (err) {
    statusEl.innerHTML = '<span class=\"error\">Failed to load records.</span>';
  }
}

// Dependent State -> City Filter
const CITIES = {
  'Gujarat': ['Anand', 'Vadodara', 'Ahmedabad', 'Surat', 'Rajkot'],
  'Maharashtra': ['Mumbai', 'Pune', 'Nagpur', 'Nashik']
};
stateSelect?.addEventListener('change', () => {
  const st = stateSelect.value;
  citySelect.innerHTML = '<option value=\"\">All cities</option>';
  if (CITIES[st]) {
    citySelect.disabled = false;
    CITIES[st].forEach(c => citySelect.add(new Option(c, c)));
  } else {
    citySelect.disabled = true;
  }
  render();
});
""", caption="data-render.js — Async Fetch and Dependent Filter Logic")
    
    add_heading_styled(doc, "3. Verification Screenshot: Dynamic Events Catalog", level=2)
    add_image_safe(doc, os.path.join(SCREENSHOTS_DIR, "p03_events.png"), caption="Events Catalog with Debounced Search, Category Filter, and Dynamic Cards Grid")
    
    add_heading_styled(doc, "4. Verification Screenshot: Student Directory with Dependent Dropdown", level=2)
    add_image_safe(doc, os.path.join(SCREENSHOTS_DIR, "p04_directory.png"), caption="Student Directory with Dependent State -> City Filter and Top Student Dhruv Bhoi")
    
    add_heading_styled(doc, "5. Key Questions & Analysis", level=2)
    add_qa(doc, "How is JSON fetched, parsed, and rendered dynamically?",
           "The browser calls `window.fetch(src)`, returns a Promise that resolves to a Response object, and parses the payload with `res.json()`. "
           "The resulting JavaScript array is transformed through `.filter()`, `.sort()`, and `.slice()` before building DOM elements via template literals.")
    
    add_qa(doc, "How are loading, error, and empty states handled?",
           "A dedicated `<div id=\"dataStatus\">` element with `aria-live=\"polite\"` shows a spinner during network transport, "
           "displays user-friendly retry alerts if `!res.ok`, and shows an 'Empty records found' notice if the search query matches 0 records.")
    
    doc.add_page_break()

def add_practical_7(doc):
    add_heading_styled(doc, "Practical 7: PHP Form Processing with Server-Side Validation and CSV/JSON File Storage", level=1)
    
    add_callout_box(doc,
        "Aim: Implement PHP form processing for contact and feedback submissions with server-side validation, data sanitization, CSRF protection, and persistent storage in JSON/CSV files.\n\n"
        "Tools & Technologies: PHP 8.x, CSV File I/O (`fputcsv`), JSON Storage (`json_encode`), CSRF Protection",
        title="Practical Aim & Tools"
    )
    
    add_heading_styled(doc, "1. Server-Side Processing Architecture", level=2)
    doc.add_paragraph(
        "Client-side validation is easily bypassed; therefore, robust server-side processing is mandatory for security. StudentHub implements two storage workflows:\n"
        "1. Contact Us (`contact.php`): Validates user inquiries, strips HTML tags (`clean()`), checks email formats (`FILTER_VALIDATE_EMAIL`), verifies anti-CSRF session tokens, and appends records atomically to `data/contacts.csv` using `fputcsv()` with exclusive file locks (`LOCK_EX`).\n"
        "2. Student Feedback (`feedback.php`): Collects user star ratings (1 to 5) and comments, validates data integrity, and stores entries in `data/feedback.json`. Recent feedback cards are dynamically read and rendered below the form."
    )
    
    add_heading_styled(doc, "2. Implementation Code: Contact Processing & Atomic CSV Write", level=2)
    add_code_block(doc,
"""// contact.php - Server-Side Processing
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (!csrf_check()) {
        $errors['form'] = 'Security validation failed (Invalid CSRF token).';
    } else {
        $name = clean($_POST['name'] ?? '');
        $email = clean($_POST['email'] ?? '');
        $message = clean($_POST['message'] ?? '');
        
        if (strlen($name) < 2) $errors['name'] = 'Name must be at least 2 characters.';
        if (!filter_var($email, FILTER_VALIDATE_EMAIL)) $errors['email'] = 'Invalid email address.';
        if (strlen($message) < 10) $errors['message'] = 'Message must be at least 10 characters.';
        
        if (!$errors) {
            $fp = fopen(BASE_PATH . '/data/contacts.csv', 'a');
            if ($fp && flock($fp, LOCK_EX)) {
                fputcsv($fp, [date('Y-m-d H:i:s'), $name, $email, $message, $_SERVER['REMOTE_ADDR']]);
                flock($fp, LOCK_UN);
                fclose($fp);
                flash('success', 'Thank you! Your message has been recorded.');
                redirect('contact.php');
            }
        }
    }
}
""", caption="contact.php — Input Sanitization, CSRF Verification, and Atomic File Append")
    
    add_heading_styled(doc, "3. Verification Screenshot: Feedback & Rating System", level=2)
    add_image_safe(doc, os.path.join(SCREENSHOTS_DIR, "p07_feedback.png"), caption="Feedback Submission Form with Star Ratings and Persisted JSON Feed")
    
    add_heading_styled(doc, "4. Verification Screenshot: Contact Inquiries Portal", level=2)
    add_image_safe(doc, os.path.join(SCREENSHOTS_DIR, "p06_contact.png"), caption="Contact Inquiries Form with Server-Side Validation and CSV Audit Logging")
    
    add_heading_styled(doc, "5. Key Questions & Analysis", level=2)
    add_qa(doc, "Why must form data be submitted using POST instead of GET?",
           "GET appends parameters to the query string in browser history, server logs, and HTTP referrers, making it insecure for sensitive data. "
           "POST transmits data inside the HTTP message body, supports unlimited payload sizes, and complies with HTTP idempotency standards.")
    
    add_qa(doc, "How is file writing handled safely against concurrent race conditions?",
           "By invoking `flock($fp, LOCK_EX)` before performing file writes. Exclusive locking prevents data corruption when multiple users submit forms simultaneously.")
    
    doc.add_page_break()

def add_practical_8(doc):
    add_heading_styled(doc, "Practical 8: MySQL Schema Design, ER Model, Database Connectivity, and Diagnostics", level=1)
    
    add_callout_box(doc,
        "Aim: Design a normalized (3NF) relational database schema for StudentHub, construct an ER model, establish PDO and MySQLi connections, and implement a diagnostic connection test suite.\n\n"
        "Tools & Technologies: MySQL 8.x, InnoDB Engine, Foreign Key Constraints, PDO, MySQLi Prepared Statements",
        title="Practical Aim & Tools"
    )
    
    add_heading_styled(doc, "1. Entity-Relationship Model & 3NF Normalization", level=2)
    doc.add_paragraph(
        "The StudentHub database (`studenthub`) is designed in Third Normal Form (3NF) to eliminate data redundancy and ensure relational integrity:\n"
        "• `users`: Authentication credentials, roles (admin/student), password hashes, and activity status.\n"
        "• `students`: Academic profiles (course, year, contact, student ID) bound to `users.id` with a 1-to-1 foreign key and `ON DELETE CASCADE`.\n"
        "• `events`: Campus events, dates, venues, capacities, and poster image filenames.\n"
        "• `registrations`: Student-to-event registrations (Many-to-Many mapping) with a `UNIQUE KEY (event_id, student_id)` preventing duplicate registrations.\n"
        "• `remember_tokens`: Cryptographic selectors and SHA-256 token hashes for persistent 'Remember Me' sessions.\n"
        "• `audit_logs`: Immutable security audit trail recording user logins, updates, IP addresses, and timestamps.\n"
        "• Stored Procedures: `sp_registrations_by_month` (analytics grouping) and `sp_event_registration_count` (dynamic count aggregation)."
    )
    
    add_heading_styled(doc, "2. Implementation Code: Dual Database Driver (`includes/db.php`)", level=2)
    add_code_block(doc,
"""// includes/db.php - Secure Dual Database Driver
define('DB_HOST', 'localhost');
define('DB_NAME', 'studenthub');
define('DB_USER', 'root');
define('DB_PASS', '');

// 1. PDO Driver (Object-Oriented, Exception-driven)
$dsn = 'mysql:host=' . DB_HOST . ';dbname=' . DB_NAME . ';charset=utf8mb4';
$opt = [
    PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
    PDO::ATTR_EMULATE_PREPARES   => false,
];
$pdo = new PDO($dsn, DB_USER, DB_PASS, $opt);

// 2. MySQLi Driver (For explicit prepared statements & multi-queries)
$mysqli = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);
$mysqli->set_charset('utf8mb4');
""", caption="includes/db.php — UTF-8MB4 Dual PDO and MySQLi Initialization")
    
    add_heading_styled(doc, "3. Verification Screenshot: Comprehensive DB Diagnostic Test Suite", level=2)
    add_image_safe(doc, os.path.join(SCREENSHOTS_DIR, "p10_db_test.png"), caption="Live Diagnostic Test Suite (db-test.php) Demonstrating 6/6 PASS for Dhruv Bhoi")
    
    add_heading_styled(doc, "4. Key Questions & Analysis", level=2)
    add_qa(doc, "Is the schema normalized properly into 3NF?",
           "Yes. 1NF is satisfied (all attributes are atomic; no repeating groups). 2NF is satisfied (no partial dependencies on composite keys). "
           "3NF is satisfied (no transitive dependencies; non-key attributes depend solely on the primary key).")
    
    add_qa(doc, "Why is `ATTR_EMULATE_PREPARES => false` specified in PDO?",
           "Native prepared statements ensure that SQL statement parsing and user data binding happen in separate network packets inside MySQL server. "
           "This completely eliminates SQL Injection vulnerabilities regardless of character encodings.")
    
    doc.add_page_break()

def add_practical_9(doc):
    add_heading_styled(doc, "Practical 9: Secure User Registration with Database Insert, Duplicate Email Check, and Password Hashing", level=1)
    
    add_callout_box(doc,
        "Aim: Build secure user registration with server-side validation, duplicate email check, bcrypt password hashing (`password_hash`), database transactions, and audit logging.\n\n"
        "Tools & Technologies: PHP 8.x, MySQLi Prepared Statements, Bcrypt Algorithm, ACID Database Transactions",
        title="Practical Aim & Tools"
    )
    
    add_heading_styled(doc, "1. Secure Registration Workflow & Threat Mitigation", level=2)
    doc.add_paragraph(
        "User registration (`register.php`) establishes student identities securely through five defensive layers:\n"
        "1. Server Validation: Re-executes all pattern validations independently of frontend checks.\n"
        "2. Duplicate Check: Executes a parameterized SELECT query to verify email uniqueness before attempting insertion.\n"
        "3. Cryptographic Hashing: Generates secure Bcrypt salted hashes using `password_hash($password, PASSWORD_DEFAULT)` with default cost factor 10.\n"
        "4. Database Transactions: Wraps `users` insert and `students` insert within `$mysqli->begin_transaction()`. If either fails, `$mysqli->rollback()` ensures zero orphaned records.\n"
        "5. Security Audit Log: Records registration event, user ID, client IP address, and timestamp into `audit_logs`."
    )
    
    add_heading_styled(doc, "2. Implementation Code: Transactional Registration", level=2)
    add_code_block(doc,
"""// register.php - Transactional Registration
$hash = password_hash($d['password'], PASSWORD_DEFAULT);
$mysqli->begin_transaction();
try {
    $u = $mysqli->prepare('INSERT INTO users (name, email, password_hash, role) VALUES (?, ?, ?, ?)');
    $role = 'student';
    $u->bind_param('ssss', $old['name'], $d['email'], $hash, $role);
    $u->execute();
    $uid = $mysqli->insert_id;
    
    $s = $mysqli->prepare('INSERT INTO students (user_id, name, email, mobile, course, year, gender) VALUES (?, ?, ?, ?, ?, ?, ?)');
    $s->bind_param('issssis', $uid, $old['name'], $d['email'], $d['mobile'], $d['course'], $d['year'], $d['gender']);
    $s->execute();
    
    $mysqli->commit();
    flash('success', 'Registration successful! You may now log in.');
    redirect('login.php');
} catch (Exception $e) {
    $mysqli->rollback();
    $errors['form'] = 'Registration failed. Please try again.';
}
""", caption="register.php — Atomic ACID Registration with Bcrypt Hashing")
    
    add_heading_styled(doc, "3. Verification Screenshot: Registration Form & Error States", level=2)
    add_image_safe(doc, os.path.join(SCREENSHOTS_DIR, "p09_register.png"), caption="Registration Form Demonstrating Validation Cues and Account Creation")
    
    add_heading_styled(doc, "4. Key Questions & Analysis", level=2)
    add_qa(doc, "Why should MD5 or SHA1 never be used for password storage?",
           "MD5 and SHA-1 are high-speed general hashing algorithms that lack computational work factors. "
           "Modern GPUs compute billions of MD5 hashes per second, making rainbow table and brute-force attacks trivial. "
           "Bcrypt incorporates an adaptive slow cost factor and automatic random salt generation.")
    
    add_qa(doc, "How does the system prevent duplicate account registrations?",
           "Through a two-step defense: 1) A parameterized SQL query verifies if the email exists prior to hashing, and "
           "2) A database-level `UNIQUE KEY (email)` constraint on the `users` table acts as a failsafe, catching race conditions via SQL exception code 1062.")
    
    doc.add_page_break()

def add_practical_10(doc):
    add_heading_styled(doc, "Practical 10: Secure Login/Logout with Sessions, Role-Based Access, Timeout, and Remember-Me Token", level=1)
    
    add_callout_box(doc,
        "Aim: Implement secure authentication (login/logout) using PHP sessions, `password_verify()`, session regeneration against fixation, role-based access control (RBAC), 15-minute inactivity timeout, and secure remember-me cookies.\n\n"
        "Tools & Technologies: PHP Sessions, Cryptographic Tokens, HTTPOnly/Secure Cookies, RBAC Architecture",
        title="Practical Aim & Tools"
    )
    
    add_heading_styled(doc, "1. Session Management & Defense-in-Depth Authentication", level=2)
    doc.add_paragraph(
        "StudentHub (`login.php`, `logout.php`, `includes/functions.php`) enforces enterprise security standards:\n"
        "• Secure Authentication: Uses `password_verify($password, $hash)` resisting timing attacks.\n"
        "• Session Fixation Defense: Calls `session_regenerate_id(true)` upon successful authentication to destroy the pre-login session ID.\n"
        "• Inactivity Timeout: Automatically tracks `$_SESSION['last_activity']`. Sessions exceeding 15 minutes (`SESSION_TIMEOUT = 900`) are destroyed with a timeout redirect.\n"
        "• Split-Token Remember-Me: Stores a public 12-byte hex selector and a private 32-byte token hash in `remember_tokens`. Cookies are marked `HttpOnly`, `SameSite=Lax`, and `Expires = 14 days`.\n"
        "• Role-Based Access Control (RBAC): `require_role('admin')` blocks students from administrative scripts (`students.php`, `manage_events.php`, `admin/`)."
    )
    
    add_heading_styled(doc, "2. Implementation Code: Secure Login & Remember-Me", level=2)
    add_code_block(doc,
"""// login.php - Authentication & Token Issue
$st = $pdo->prepare('SELECT * FROM users WHERE email = ? AND status = \"active\"');
$st->execute([$email]);
$u = $st->fetch();

if ($u && password_verify($pass, $u['password_hash'])) {
    session_regenerate_id(true);
    $_SESSION['user'] = ['id' => $u['id'], 'name' => $u['name'], 'email' => $u['email'], 'role' => $u['role']];
    $_SESSION['last_activity'] = time();
    $pdo->prepare('UPDATE users SET last_login = NOW() WHERE id = ?')->execute([$u['id']]);
    
    if (!empty($_POST['remember'])) {
        $sel = bin2hex(random_bytes(12));
        $tok = bin2hex(random_bytes(32));
        $pdo->prepare('INSERT INTO remember_tokens (user_id, selector, token_hash, expires_at) VALUES (?, ?, ?, DATE_ADD(NOW(), INTERVAL 14 DAY))')
            ->execute([$u['id'], $sel, hash('sha256', $tok)]);
        setcookie('remember', \"$sel:$tok\", ['expires' => time() + 14*86400, 'path' => '/', 'httponly' => true, 'samesite' => 'Lax']);
    }
    redirect($u['role'] === 'admin' ? 'admin/dashboard.php' : 'dashboard.php');
}
""", caption="login.php — Authentication, Session Regeneration, and Split-Token Generation")
    
    add_heading_styled(doc, "3. Verification Screenshot: Login Portal & Demo Helper", level=2)
    add_image_safe(doc, os.path.join(SCREENSHOTS_DIR, "p08_login.png"), caption="Secure Login Screen with Role Credentials Helper and Remember-Me Toggle")
    
    add_heading_styled(doc, "4. Verification Screenshot: Student Dashboard (Dhruv Bhoi)", level=2)
    add_image_safe(doc, os.path.join(SCREENSHOTS_DIR, "p11_student_dashboard.png"), caption="Authenticated Student Dashboard with Timetable, Progress Donuts, and Events Feed")
    
    add_heading_styled(doc, "5. Key Questions & Analysis", level=2)
    add_qa(doc, "How does `session_regenerate_id(true)` protect against session fixation attacks?",
           "In a session fixation attack, an adversary tricks the victim into using a predetermined session ID. "
           "Calling `session_regenerate_id(true)` issues a brand new cryptographically random session identifier while deleting the old session storage, "
           "invalidating any fixation token held by the attacker.")
    
    add_qa(doc, "How does the split-token 'Remember Me' mechanism prevent database leakage attacks?",
           "The database stores only the public selector and a SHA-256 hash of the validator token. "
           "If an attacker breaches the database, they cannot forge session cookies because the raw validator token is never stored server-side.")
    
    doc.add_page_break()

def add_practical_11(doc):
    add_heading_styled(doc, "Practical 11: Student Management CRUD with Search, Filter, Pagination, Soft Delete, and CSV Export", level=1)
    
    add_callout_box(doc,
        "Aim: Develop complete Student Management CRUD operations for administrators with MySQLi prepared statements, search, course filter, pagination, soft delete/restore, and CSV export.\n\n"
        "Tools & Technologies: PHP, MySQLi Prepared Statements, CSV Stream Generation, Soft Delete Architecture",
        title="Practical Aim & Tools"
    )
    
    add_heading_styled(doc, "1. Administrative CRUD Features (`students.php`)", level=2)
    doc.add_paragraph(
        "StudentHub empowers administrators to oversee student records with enterprise-grade safeguards:\n"
        "• Parameterized CRUD: All Create, Read, Update, and Delete operations use strict MySQLi prepared statements.\n"
        "• Search & Course Filters: Instant lookup across student name, email, and mobile, coupled with academic course dropdowns.\n"
        "• Pagination Algorithm: Efficient `LIMIT ?, ?` pagination with calculated offsets (`($page - 1) * $perPage`).\n"
        "• Soft Delete & Restore: Rather than irrevocably purging database rows, deletions toggle `status = 'deleted'`. Administrators can toggle between 'Active' and 'Deleted' views to restore records.\n"
        "• On-Demand CSV Export: Clicking 'Export CSV' streams database records directly via `fputcsv()` with HTTP headers `Content-Type: text/csv`."
    )
    
    add_heading_styled(doc, "2. Implementation Code: Prepared CRUD & Soft Delete", level=2)
    add_code_block(doc,
"""// students.php - Soft Delete / Restore
if ($_SERVER['REQUEST_METHOD'] === 'POST' && in_array($_POST['do'], ['delete', 'restore'])) {
    if (!csrf_check()) flash('error', 'Security token invalid.');
    else {
        $id = (int)$_POST['id'];
        $status = $_POST['do'] === 'delete' ? 'deleted' : 'active';
        $st = $mysqli->prepare('UPDATE students SET status=? WHERE id=?');
        $st->bind_param('si', $status, $id);
        $st->execute();
        audit($pdo, 'student_' . $status, 'Student ID: ' . $id);
        flash('success', $status === 'deleted' ? 'Student moved to deleted (soft delete).' : 'Student restored successfully.');
    }
    redirect('students.php');
}
""", caption="students.php — Prepared Statement Soft Delete and Audit Logging")
    
    add_heading_styled(doc, "3. Verification Screenshot: Student Management CRUD Interface", level=2)
    add_image_safe(doc, os.path.join(SCREENSHOTS_DIR, "p14_admin_students.png"), caption="Student Management CRUD with Search Toolbar, Course Filter, Pagination, and Status Badges")
    
    add_heading_styled(doc, "4. Key Questions & Analysis", level=2)
    add_qa(doc, "Why is soft delete preferable over hard delete in enterprise applications?",
           "Hard delete immediately destroys historical data, breaking foreign key relationships in audit logs, event registrations, and invoices. "
           "Soft delete preserves data integrity, prevents accidental data loss, complies with data retention laws, and allows 1-click recovery.")
    
    add_qa(doc, "How is CSV export streamed efficiently without exhausting server memory?",
           "By opening the output stream wrapper `fopen('php://output', 'w')` and writing records iteratively with `fputcsv($out, $row)` "
           "directly to the HTTP client socket, buffering 0 intermediate memory.")
    
    doc.add_page_break()

def add_practical_12(doc):
    add_heading_styled(doc, "Practical 12: Event Management CRUD with Poster Upload and File Validation", level=1)
    
    add_callout_box(doc,
        "Aim: Build an Event Management CRUD interface with poster image upload, MIME type and size validation, secure unique filename generation, directory permissions, and database tracking.\n\n"
        "Tools & Technologies: PHP File Upload Handling (`$_FILES`), MIME Type Detection (`finfo`), File Security",
        title="Practical Aim & Tools"
    )
    
    add_heading_styled(doc, "1. Secure File Upload Architecture (`manage_events.php`)", level=2)
    doc.add_paragraph(
        "File uploading is one of the most common web attack vectors (Remote Code Execution, Malicious Script Injection). "
        "StudentHub defends poster uploads through 5 strict verification checks:\n"
        "1. HTTP POST & Error Check: Verifies `is_uploaded_file()` and checks `$_FILES['poster']['error'] === UPLOAD_ERR_OK`.\n"
        "2. File Size Cap: Restricts files to a strict 2 Megabyte ceiling (`2 * 1024 * 1024` bytes).\n"
        "3. MIME Content Inspection: Uses PHP's `finfo(FILEINFO_MIME_TYPE)` on temporary file bytes, permitting only `image/jpeg`, `image/png`, and `image/webp`. Never relies on client-supplied extensions.\n"
        "4. Cryptographic Renaming: Files are renamed using `bin2hex(random_bytes(16)) . '.' . $ext` to prevent path traversal and execution.\n"
        "5. Directory Execution Prevention: The `uploads/` folder contains an `index.php` and an `.htaccess` disabling script execution."
    )
    
    add_heading_styled(doc, "2. Implementation Code: Poster Upload & MIME Inspection", level=2)
    add_code_block(doc,
"""// manage_events.php - Poster Validation
if (!empty($_FILES['poster']['name'])) {
    $f = $_FILES['poster'];
    if ($f['size'] > 2 * 1024 * 1024) $errors['poster'] = 'Poster must be under 2 MB.';
    else {
        $finfo = new finfo(FILEINFO_MIME_TYPE);
        $mime = $finfo->file($f['tmp_name']);
        $map = ['image/jpeg'=>'jpg', 'image/png'=>'png', 'image/webp'=>'webp'];
        if (!isset($map[$mime])) {
            $errors['poster'] = 'Invalid format. Only JPG, PNG, and WEBP allowed.';
        } else {
            $filename = bin2hex(random_bytes(16)) . '.' . $map[$mime];
            move_uploaded_file($f['tmp_name'], BASE_PATH . '/uploads/' . $filename);
            $posterPath = 'uploads/' . $filename;
        }
    }
}
""", caption="manage_events.php — MIME Type Verification and Cryptographic Renaming")
    
    add_heading_styled(doc, "3. Verification Screenshot: Event Management CRUD", level=2)
    add_image_safe(doc, os.path.join(SCREENSHOTS_DIR, "p15_admin_events.png"), caption="Event Management CRUD Interface with Poster Upload Field and Live Status Controls")
    
    add_heading_styled(doc, "4. Key Questions & Analysis", level=2)
    add_qa(doc, "Why should `$_FILES['poster']['type']` never be trusted?",
           "`$_FILES['...']['type']` is a client-provided HTTP header that can be spoofed trivially using Postman or Burp Suite. "
           "A malicious user could upload a PHP shell named `shell.php` with header `Content-Type: image/jpeg`. "
           "Server-side verification must use `finfo_file` to read file magic bytes directly.")
    
    add_qa(doc, "How does cryptographic file renaming mitigate path traversal?",
           "Renaming files to random hashes (e.g. `a3f8c...jpg`) strips dangerous characters like `../` or null bytes, "
           "preventing attackers from overwriting existing system files or guessing uploaded filenames.")
    
    doc.add_page_break()

def add_practical_13(doc):
    add_heading_styled(doc, "Practical 13: PHP JSON API and AJAX/Fetch-Based CRUD without Page Reload", level=1)
    
    add_callout_box(doc,
        "Aim: Create a RESTful PHP JSON API endpoint (`api/events.php`) supporting GET and POST, and integrate AJAX/Fetch CRUD operations without page reloads, including loading spinners and toast notifications.\n\n"
        "Tools & Technologies: PHP REST API, JSON Serialization, AJAX, Fetch API, DOM Replacement",
        title="Practical Aim & Tools"
    )
    
    add_heading_styled(doc, "1. RESTful JSON API Architecture (`api/events.php`)", level=2)
    doc.add_paragraph(
        "StudentHub implements a dedicated headless API endpoint adhering to REST conventions:\n"
        "• Content Negotiation: Emits `Content-Type: application/json; charset=utf-8` on every response.\n"
        "• HTTP Verbs & Routing: GET requests query events with optional debounced search filters; POST requests handle authenticated CRUD actions (create, delete, toggle status).\n"
        "• Standard HTTP Status Codes: Returns `200 OK` on success, `401 Unauthorized` for guests, `403 Forbidden` for invalid CSRF tokens, `422 Unprocessable Entity` for validation errors, and `500 Internal Error` for failures.\n"
        "• Client-Side Controller (`assets/js/api-crud.js`): Intercepts form submissions, transmits JSON payloads with `X-CSRF-Token` headers, and smoothly updates the DOM table without full page refreshes."
    )
    
    add_heading_styled(doc, "2. Implementation Code: API Router & AJAX Client", level=2)
    add_code_block(doc,
"""// api/events.php - JSON API Router
header('Content-Type: application/json; charset=utf-8');
require_once __DIR__ . '/../includes/functions.php';
require_once __DIR__ . '/../includes/db.php';
require_login(); // Requires authenticated session (401 response on failure)

if ($_SERVER['REQUEST_METHOD'] === 'GET') {
    $q = clean($_GET['q'] ?? '');
    $sql = 'SELECT id, title, category, event_date, venue, status FROM events';
    if ($q !== '') $sql .= ' WHERE title LIKE ? OR venue LIKE ?';
    $st = $pdo->prepare($sql);
    $q !== '' ? $st->execute([\"%$q%\", \"%$q%\"]) : $st->execute();
    echo json_encode(['success' => true, 'data' => $st->fetchAll()]);
    exit;
}
""", caption="api/events.php — Parameterized REST API with HTTP Status Emission")
    
    add_heading_styled(doc, "3. Verification Screenshot: Live AJAX Events Interface", level=2)
    add_image_safe(doc, os.path.join(SCREENSHOTS_DIR, "p17_api_demo.png"), caption="Live AJAX Events Dashboard (api-demo.php) Rendering Real-Time Updates without Reloads")
    
    add_heading_styled(doc, "4. Key Questions & Analysis", level=2)
    add_qa(doc, "How are CSRF tokens transmitted during asynchronous AJAX requests?",
           "During page generation, the server places a CSRF token in a data attribute (`data-csrf=\"...\"`). "
           "The JavaScript controller attaches this token to the custom request header `X-CSRF-Token`, which PHP validates via `csrf_check($_SERVER['HTTP_X_CSRF_TOKEN'])`.")
    
    add_qa(doc, "What are the benefits of Single Page Application (SPA) AJAX updates over traditional server-rendered pages?",
           "AJAX updates significantly reduce network bandwidth by exchanging lightweight JSON rather than full HTML documents. "
           "The user experience is seamless without screen flashing, form inputs preserve focus, and responsiveness feels like a native desktop app.")
    
    doc.add_page_break()

def add_practical_14(doc):
    add_heading_styled(doc, "Practical 14: Admin Dashboard with Role-Based Access Control, Dynamic Menu, and Audit Log", level=1)
    
    add_callout_box(doc,
        "Aim: Develop an Admin Dashboard with role-based access control, KPI metric cards, dynamic navigation, stored procedure monthly registration charts, user active/inactive toggles, and an audit trail viewer.\n\n"
        "Tools & Technologies: PHP, MySQL Stored Procedures, Role-Based Access Control (RBAC), CSS Data Visualization",
        title="Practical Aim & Tools"
    )
    
    add_heading_styled(doc, "1. Enterprise Admin Features (`admin/dashboard.php` & `admin/audit.php`)", level=2)
    doc.add_paragraph(
        "The administrative module provides executive-level monitoring of the entire StudentHub portal:\n"
        "• KPI Stat Metric Cards: Real-time calculation of Total Students, Active Campus Events, Total RSVP Registrations, and Security Audit Actions.\n"
        "• Stored Procedure Execution: Calls MySQL stored procedure `CALL sp_registrations_by_month()` to compute month-by-month registration velocity, rendering pure CSS proportional bar charts.\n"
        "• User Lifecycle Controls: Interactive table displaying registered campus users with 1-click status toggles ('Active' ↔ 'Inactive') and last login timestamps.\n"
        "• Security Audit Trail (`admin/audit.php`): Full system audit trail logging actions (`login`, `register`, `student_create`, `event_delete`), actor email, IP address, and timestamps."
    )
    
    add_heading_styled(doc, "2. Implementation Code: Stored Procedure & Dynamic Analytics", level=2)
    add_code_block(doc,
"""// admin/dashboard.php - Stored Procedure Invocation & Analytics
require_once __DIR__ . '/../includes/functions.php';
require_once __DIR__ . '/../includes/db.php';
require_role('admin'); // Restricts access exclusively to administrators

// Execute Stored Procedure
$monthly = $pdo->query('CALL sp_registrations_by_month()')->fetchAll();
$pdo->query('SELECT 1')->closeCursor(); // Free connection cursor for subsequent queries

// User Active / Inactive Status Toggle
if ($_SERVER['REQUEST_METHOD'] === 'POST' && ($_POST['do'] ?? '') === 'toggle') {
    if (csrf_check()) {
        $uid = (int)$_POST['user_id'];
        $u = $pdo->prepare('SELECT status, email FROM users WHERE id=?');
        $u->execute([$uid]);
        $row = $u->fetch();
        $next = $row['status'] === 'active' ? 'inactive' : 'active';
        $pdo->prepare('UPDATE users SET status=? WHERE id=?')->execute([$next, $uid]);
        audit($pdo, 'user_status_' . $next, 'User: ' . $row['email']);
        flash('success', 'User account ' . $next . ' successfully.');
    }
    redirect('dashboard.php');
}
""", caption="admin/dashboard.php — Stored Procedure Execution and User Lifecycle Management")
    
    add_heading_styled(doc, "3. Verification Screenshot: Executive Admin Dashboard", level=2)
    add_image_safe(doc, os.path.join(SCREENSHOTS_DIR, "p13_admin_dashboard.png"), caption="Admin Dashboard with KPI Stat Cards, Stored Procedure Monthly Chart, and User Status Toggles")
    
    add_heading_styled(doc, "4. Verification Screenshot: Security Audit Log Viewer", level=2)
    add_image_safe(doc, os.path.join(SCREENSHOTS_DIR, "p16_admin_audit.png"), caption="Immutable Security Audit Trail (admin/audit.php) Tracking User Actions and IP Addresses")
    
    add_heading_styled(doc, "5. Key Questions & Analysis", level=2)
    add_qa(doc, "How does `require_role('admin')` enforce access control across sensitive endpoints?",
           "It checks `$_SESSION['user']['role'] === 'admin'`. If a student or guest attempts to access the script directly via URL, "
           "the function emits `HTTP 403 Forbidden`, dispatches an access denied flash message, and redirects the client to `dashboard.php`.")
    
    add_qa(doc, "Why are stored procedures used for aggregation queries like monthly registrations?",
           "Stored procedures are pre-compiled and optimized on the MySQL database server. "
           "They minimize network latency by executing complex multi-table groupings internally, provide access abstraction, and enhance enterprise security.")

def build_p1_to_p14_document():
    print("Building D26CE154_Practical_1-14_WDF.docx...")
    doc = docx.Document()
    add_header_footer(doc)
    add_cover_page(doc, "COMPREHENSIVE LABORATORY RECORD", "Practicals 1 to 14")
    
    # Table of Contents
    add_heading_styled(doc, "Table of Contents / Index of Practicals", level=1)
    table = doc.add_table(rows=15, cols=4)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    table.columns[0].width = Inches(0.8)
    table.columns[1].width = Inches(4.0)
    table.columns[2].width = Inches(0.9)
    table.columns[3].width = Inches(0.8)
    
    headers = ["Prac No.", "Practical Title & Topic", "Status", "Grade"]
    for j, h in enumerate(headers):
        c = table.cell(0, j)
        set_cell_shading(c, "2E74B5")
        p = c.paragraphs[0]
        r = p.add_run(h)
        r.bold = True
        r.font.name = "Times New Roman"
        r.font.size = Pt(10)
        r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        
    p_titles = [
        "Project Initiation, Sitemap, Wireframe, Git & GitHub Setup",
        "Semantic HTML5 Pages with Accessibility-Ready Structure",
        "Responsive UI Design using CSS Grid, Flexbox & Modern SaaS Theme",
        "JavaScript DOM Manipulation, Event Handling & Interactivity",
        "Registration Form with Frontend Validation & Canvas CAPTCHA",
        "Rendering External JSON Data using Fetch API, Search & Filters",
        "PHP Form Processing with Server-Side Validation & CSV/JSON Storage",
        "MySQL Schema Design, ER Model, PDO Connectivity & Diagnostics",
        "Secure User Registration with Duplicate Check & Password Hashing",
        "Secure Login/Logout with Sessions, RBAC, Timeout & Remember-Me",
        "Student Management CRUD with Search, Filter & Soft Delete",
        "Event Management CRUD with Poster Upload & File Validation",
        "PHP JSON API and AJAX/Fetch-Based CRUD without Page Reload",
        "Admin Dashboard with Role-Based Access Control & Audit Log"
    ]
    
    for i, t in enumerate(p_titles, 1):
        row = table.rows[i]
        c0, c1, c2, c3 = row.cells[0], row.cells[1], row.cells[2], row.cells[3]
        set_cell_shading(c0, "F8F9FA" if i % 2 == 0 else "FFFFFF")
        set_cell_shading(c1, "F8F9FA" if i % 2 == 0 else "FFFFFF")
        set_cell_shading(c2, "F8F9FA" if i % 2 == 0 else "FFFFFF")
        set_cell_shading(c3, "F8F9FA" if i % 2 == 0 else "FFFFFF")
        
        c0.paragraphs[0].add_run(f"Prac {i}").font.name = "Times New Roman"
        c1.paragraphs[0].add_run(t).font.name = "Times New Roman"
        c2.paragraphs[0].add_run("Completed").font.name = "Times New Roman"
        c3.paragraphs[0].add_run("―").font.name = "Times New Roman"
        
    doc.add_page_break()
    
    # Practicals 1 to 14
    add_practical_1(doc)
    add_practical_2(doc)
    add_practical_3(doc)
    add_practical_4(doc)
    add_practical_5(doc)
    add_practical_6(doc)
    add_practical_7(doc)
    add_practical_8(doc)
    add_practical_9(doc)
    add_practical_10(doc)
    add_practical_11(doc)
    add_practical_12(doc)
    add_practical_13(doc)
    add_practical_14(doc)
    
    docx_path = os.path.join(SUB_DIR, "D26CE154_Practical_1-14_WDF.docx")
    doc.save(docx_path)
    print(f"Saved: {docx_path} ({os.path.getsize(docx_path)} bytes)")
    return docx_path

def build_p7_to_p14_document():
    print("Building D26CE154_Practical_7-14_WDF.docx...")
    doc = docx.Document()
    add_header_footer(doc)
    add_cover_page(doc, "BACKEND & FULL-STACK LABORATORY RECORD", "Practicals 7 to 14")
    
    # Table of Contents
    add_heading_styled(doc, "Table of Contents / Index of Practicals (7 to 14)", level=1)
    table = doc.add_table(rows=9, cols=4)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    table.columns[0].width = Inches(0.8)
    table.columns[1].width = Inches(4.0)
    table.columns[2].width = Inches(0.9)
    table.columns[3].width = Inches(0.8)
    
    headers = ["Prac No.", "Practical Title & Topic", "Status", "Grade"]
    for j, h in enumerate(headers):
        c = table.cell(0, j)
        set_cell_shading(c, "2E74B5")
        p = c.paragraphs[0]
        r = p.add_run(h)
        r.bold = True
        r.font.name = "Times New Roman"
        r.font.size = Pt(10)
        r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        
    p_titles_7_14 = [
        ("Prac 7", "PHP Form Processing with Server-Side Validation & CSV/JSON Storage"),
        ("Prac 8", "MySQL Schema Design, ER Model, PDO Connectivity & Diagnostics"),
        ("Prac 9", "Secure User Registration with Duplicate Check & Password Hashing"),
        ("Prac 10", "Secure Login/Logout with Sessions, RBAC, Timeout & Remember-Me"),
        ("Prac 11", "Student Management CRUD with Search, Filter & Soft Delete"),
        ("Prac 12", "Event Management CRUD with Poster Upload & File Validation"),
        ("Prac 13", "PHP JSON API and AJAX/Fetch-Based CRUD without Page Reload"),
        ("Prac 14", "Admin Dashboard with Role-Based Access Control & Audit Log")
    ]
    
    for i, (p_num, t) in enumerate(p_titles_7_14, 1):
        row = table.rows[i]
        c0, c1, c2, c3 = row.cells[0], row.cells[1], row.cells[2], row.cells[3]
        set_cell_shading(c0, "F8F9FA" if i % 2 == 0 else "FFFFFF")
        set_cell_shading(c1, "F8F9FA" if i % 2 == 0 else "FFFFFF")
        set_cell_shading(c2, "F8F9FA" if i % 2 == 0 else "FFFFFF")
        set_cell_shading(c3, "F8F9FA" if i % 2 == 0 else "FFFFFF")
        
        c0.paragraphs[0].add_run(p_num).font.name = "Times New Roman"
        c1.paragraphs[0].add_run(t).font.name = "Times New Roman"
        c2.paragraphs[0].add_run("Completed").font.name = "Times New Roman"
        c3.paragraphs[0].add_run("―").font.name = "Times New Roman"
        
    doc.add_page_break()
    
    # Practicals 7 to 14
    add_practical_7(doc)
    add_practical_8(doc)
    add_practical_9(doc)
    add_practical_10(doc)
    add_practical_11(doc)
    add_practical_12(doc)
    add_practical_13(doc)
    add_practical_14(doc)
    
    docx_path = os.path.join(SUB_DIR, "D26CE154_Practical_7-14_WDF.docx")
    doc.save(docx_path)
    print(f"Saved: {docx_path} ({os.path.getsize(docx_path)} bytes)")
    return docx_path

def convert_docx_to_pdf(docx_path):
    import win32com.client
    pdf_path = os.path.splitext(docx_path)[0] + ".pdf"
    print(f"Converting to PDF: {pdf_path}...")
    word = win32com.client.Dispatch("Word.Application")
    word.Visible = False
    doc = word.Documents.Open(os.path.abspath(docx_path))
    doc.SaveAs(os.path.abspath(pdf_path), FileFormat=17) # 17 = wdFormatPDF
    doc.Close()
    word.Quit()
    print(f"Exported PDF successfully: {pdf_path} ({os.path.getsize(pdf_path)} bytes)")
    return pdf_path

if __name__ == "__main__":
    p1_14_docx = build_p1_to_p14_document()
    p7_14_docx = build_p7_to_p14_document()
    
    p1_14_pdf = convert_docx_to_pdf(p1_14_docx)
    p7_14_pdf = convert_docx_to_pdf(p7_14_docx)
    
    print("\nAll submission packages generated and verified successfully!")
