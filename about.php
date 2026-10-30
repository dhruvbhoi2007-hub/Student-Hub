<?php $pageTitle = 'About'; require 'includes/header.php'; ?>
<h1>About StudentHub</h1>
<p class="lead">A comprehensive full-stack student & campus event management portal developed for Web Development Frameworks (ITUE203) at CHARUSAT.</p>

<div class="card" style="margin-bottom:1.5rem; background:linear-gradient(135deg, rgba(108, 92, 231, 0.08), rgba(142, 68, 173, 0.04)); border-color:var(--border-focus)">
  <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:1rem">
    <div>
      <span class="section-label">Developer &amp; Submission Details</span>
      <h2 style="font-size:1.35rem; margin:0 0 0.35rem">Dhruv Bhoi</h2>
      <p style="margin:0; font-size:0.92rem; color:var(--text)">
        <strong>Student-ID:</strong> D26CE154 · <strong>Department:</strong> Computer Engineering (CSPIT-CE)<br>
        <strong>Faculty:</strong> Faculty of Technology and Engineering (FTE) · <strong>University:</strong> CHARUSAT<br>
        <strong>Subject:</strong> ITUE203 Web Development Frameworks · Semester 3, 2026–27 (ODD)
      </p>
    </div>
    <div style="text-align:right">
      <span class="badge admin">Final Project</span>
      <span class="badge active">15 Practicals Complete</span>
    </div>
  </div>
</div>

<div class="grid cols-2">
  <section class="card">
    <h2>User Roles &amp; Capabilities</h2>
    <ul>
      <li><strong>Visitor:</strong> Explore events, student directory, about, FAQs, and submit feedback or contact forms.</li>
      <li><strong>Student (Dhruv Bhoi):</strong> Interactive dashboard with timetable, circular metrics, notice board, self-service event registration, and profile updates.</li>
      <li><strong>Administrator:</strong> Full student CRUD (MySQLi), event publishing with poster uploads, system statistics, and audit trails.</li>
    </ul>
  </section>
  <section class="card">
    <h2>Full-Stack Technology Stack</h2>
    <ul>
      <li><strong>Frontend:</strong> HTML5 Semantic Landmarks, CSS3 Grid &amp; Flexbox (Acade UI Theme), Vanilla ES6+ JavaScript.</li>
      <li><strong>Backend:</strong> PHP 8.2 (Dual PDO Prepared Statements &amp; MySQLi Prepared Queries).</li>
      <li><strong>Database:</strong> MySQL / MariaDB (Normalized 3NF relational schema with 6 tables &amp; 2 stored procedures).</li>
      <li><strong>Integration:</strong> Asynchronous Fetch API with debounced live search and offline `localStorage` caching.</li>
    </ul>
  </section>
</div>

<section class="card" style="margin-top:1.5rem">
  <h2>Course Navigation Map</h2>
  <ul>
    <li><strong>Public Pages:</strong> Home, About, Events (JSON), Student Directory (Dependent Dropdowns), FAQ, Contact (CSV), Feedback (JSON), Login, Register.</li>
    <li><strong>Student Section:</strong> Dashboard, Profile Management, Live Events (AJAX CRUD).</li>
    <li><strong>Admin Control:</strong> Student Management (Soft Delete, CSV Export), Event Management (Poster Upload), Admin Dashboard (Stored Procedure Chart), Security Audit Log.</li>
  </ul>
</section>

<?php require 'includes/footer.php'; ?>
