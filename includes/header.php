<?php
// Shared layout header. Inspired by modern SaaS dashboard (Acade UI).
require_once __DIR__ . '/functions.php';
check_timeout();
$pageTitle = $pageTitle ?? 'StudentHub';
$root = base_url();
$cur = basename($_SERVER['SCRIPT_NAME']);
$user = current_user();

// Navigation items: [href, label, icon, badge]
$nav = [
    ['index.php', 'Home', '🏠', null],
    ['about.php', 'About', 'ℹ️', null],
    ['events.php', 'Events', '📅', null],
    ['directory.php', 'Directory', '👥', null],
    ['faq.php', 'FAQ', '❓', null],
    ['contact.php', 'Contact', '✉️', null],
    ['feedback.php', 'Feedback', '💬', null],
];

if ($user) {
    array_splice($nav, 1, 0, [['dashboard.php', 'Dashboard', '📊', null]]);
    $nav[] = ['profile.php', 'Profile', '👤', null];
    $nav[] = ['api-demo.php', 'Live Events', '⚡', 'AJAX'];
}

if ($user && $user['role'] === 'admin') {
    $nav[] = ['students.php', 'Students', '👩‍🎓', null];
    $nav[] = ['manage_events.php', 'Manage Events', '🛠️', null];
    $nav[] = ['admin/dashboard.php', 'Admin Panel', '📈', 'Pro'];
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="StudentHub - modern student & campus event management portal">
<title><?= e($pageTitle) ?> | StudentHub</title>
<link rel="stylesheet" href="<?= $root ?>assets/css/style.css">
<script>try{var t=localStorage.getItem('sh_theme');if(t)document.documentElement.setAttribute('data-theme',t);}catch(e){}</script>
</head>
<body>
<a class="skip-link" href="#main">Skip to main content</a>

<div class="app-layout">
  <!-- Left Sidebar (Acade UI Inspired) -->
  <aside class="app-sidebar" id="appSidebar" aria-label="Main Navigation">
    <a class="sidebar-brand" href="<?= $root ?>index.php">
      <div class="sidebar-brand-icon">▲</div>
      <div class="sidebar-brand-title">Student<span>Hub</span></div>
    </a>
    
    <ul class="sidebar-nav" id="navMenu">
      <?php foreach ($nav as [$href, $label, $icon, $badge]): 
        $isActive = ($cur === basename($href));
      ?>
      <li class="sidebar-nav-item">
        <a href="<?= $root . $href ?>" class="<?= $isActive ? 'active' : '' ?>" <?= $isActive ? 'aria-current="page"' : '' ?>>
          <span class="nav-icon" aria-hidden="true"><?= $icon ?></span>
          <span><?= e($label) ?></span>
          <?php if ($badge): ?>
            <span class="sidebar-badge <?= strtolower($badge) === 'new' ? 'new' : '' ?>"><?= e($badge) ?></span>
          <?php endif; ?>
        </a>
      </li>
      <?php endforeach; ?>
    </ul>

    <div class="sidebar-card">
      <div class="sidebar-card-title">🚀 Campus Portal</div>
      <p style="font-size:0.75rem; margin:0 0 0.5rem; color:var(--muted)">Explore tech fests, workshops & campus registrations.</p>
      <a href="<?= $root ?>events.php">Browse Events &rarr;</a>
    </div>

    <div class="sidebar-footer">
      <?php if ($user): ?>
        <a href="<?= $root ?>profile.php"><span class="nav-icon" aria-hidden="true">⚙️</span> Settings</a>
        <a href="<?= $root ?>faq.php"><span class="nav-icon" aria-hidden="true">❓</span> Help & FAQ</a>
        <a href="<?= $root ?>logout.php" style="color:var(--danger)"><span class="nav-icon" aria-hidden="true">🚪</span> Logout</a>
      <?php else: ?>
        <a href="<?= $root ?>login.php"><span class="nav-icon" aria-hidden="true">🔑</span> Log In</a>
        <a href="<?= $root ?>register.php"><span class="nav-icon" aria-hidden="true">📝</span> Create Account</a>
      <?php endif; ?>
    </div>
  </aside>

  <!-- Right App Main Body -->
  <div class="app-main">
    <!-- Topbar -->
    <header class="app-topbar">
      <div class="topbar-left">
        <button class="hamburger" id="hamburger" aria-label="Toggle navigation drawer" aria-expanded="false">&#9776;</button>
        <h1 class="topbar-greeting">
          <?php if ($user && in_array($cur, ['dashboard.php', 'index.php'])): ?>
            Welcome, <?= e(explode(' ', $user['name'])[0]) ?> 👋
          <?php else: ?>
            <?= e($pageTitle) ?>
          <?php endif; ?>
        </h1>
      </div>

      <div class="topbar-right">
        <div class="topbar-search">
          <span style="opacity:0.6; font-size:0.9rem">🔍</span>
          <input type="search" placeholder="Search events, courses…" onkeydown="if(event.key==='Enter'){location.href='<?= $root ?>events.php?q='+encodeURIComponent(this.value)}">
        </div>

        <button class="icon-btn" id="themeToggle" aria-label="Toggle light/dark theme">🌙</button>
        <a class="icon-btn" href="<?= $root ?>events.php" aria-label="Notifications" title="Announcements">🔔</a>

        <?php if ($user): ?>
          <a class="user-pill" href="<?= $root ?>profile.php">
            <div class="user-avatar"><?= e(strtoupper(substr($user['name'], 0, 1) . (strpos($user['name'], ' ') ? substr(explode(' ', $user['name'])[1], 0, 1) : ''))) ?></div>
            <span class="user-pill-name"><?= e($user['name']) ?></span>
            <span style="font-size:0.7rem; color:var(--muted)">▾</span>
          </a>
        <?php else: ?>
          <a class="btn small" href="<?= $root ?>login.php">Log In</a>
          <a class="btn small secondary" href="<?= $root ?>register.php">Sign Up</a>
        <?php endif; ?>
      </div>
    </header>

    <div class="banner" id="banner" role="status">
      <div class="container">
        <span>🎉 Annual Tech Fest registrations are live! Visit the Events tab to register.</span>
        <button id="bannerClose" aria-label="Dismiss notification">&times;</button>
      </div>
    </div>

    <?php if ($cur !== 'index.php'): ?>
    <div class="container" style="padding-top:0.6rem">
      <nav class="breadcrumb" aria-label="Breadcrumb"><a href="<?= $root ?>index.php">Home</a> › <span><?= e($pageTitle) ?></span></nav>
    </div>
    <?php endif; ?>

    <main id="main" class="content-body">
      <?php show_flash(); ?>
