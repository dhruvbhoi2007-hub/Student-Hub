<?php
// User & Student Profile Page: Includes Academic Information (D26CE154 - Dhruv Bhoi)
$pageTitle = 'Profile';
require_once 'includes/functions.php';
require_once 'includes/db.php';
try_remember_login($pdo);
require_login();

$uid = current_user()['id'];
$st = $pdo->prepare('SELECT u.*, s.mobile, s.course, s.year, s.gender, s.state, s.city, s.id sid FROM users u LEFT JOIN students s ON s.user_id=u.id WHERE u.id=?');
$st->execute([$uid]);
$p = $st->fetch();
$errors = [];

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (!csrf_check()) $errors['form'] = 'Invalid token.';
    else {
        $name = clean($_POST['name'] ?? '');
        $mobile = clean($_POST['mobile'] ?? '');
        $course = $_POST['course'] ?? '';
        $year = (int)($_POST['year'] ?? 0);
        if (!preg_match("/^[A-Za-z][A-Za-z .'-]{2,59}$/", $name)) $errors['name'] = 'Invalid name.';
        if ($p['sid']) {
            if (!preg_match('/^[6-9]\d{9}$/', $mobile)) $errors['mobile'] = 'Invalid mobile.';
            if (!in_array($course, COURSES, true)) $errors['course'] = 'Invalid course.';
            if ($year < 1 || $year > 4) $errors['year'] = 'Invalid year.';
        }
        if (!$errors) {
            $pdo->prepare('UPDATE users SET name=? WHERE id=?')->execute([$name, $uid]);
            if ($p['sid']) $pdo->prepare('UPDATE students SET name=?, mobile=?, course=?, year=? WHERE id=?')->execute([$name, $mobile, $course, $year, $p['sid']]);
            $_SESSION['user']['name'] = $name;
            audit($pdo, 'profile_update', $p['email']);
            flash('success', 'Profile updated successfully.');
            redirect('profile.php');
        }
    }
}
require 'includes/header.php';
?>

<!-- Academic Profile Header Card -->
<div class="card" style="margin-bottom:1.5rem; background:linear-gradient(135deg, rgba(108, 92, 231, 0.08), rgba(142, 68, 173, 0.04)); border-color:var(--border-focus)">
  <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:1rem">
    <div style="display:flex; align-items:center; gap:1.2rem">
      <div style="width:68px; height:68px; border-radius:50%; background:linear-gradient(135deg, var(--primary), #9B8EF8); color:#fff; display:flex; align-items:center; justify-content:center; font-size:1.6rem; font-weight:800; box-shadow:0 6px 16px var(--primary-glow)">
        <?= e(strtoupper(substr($p['name'], 0, 1) . (strpos($p['name'], ' ') ? substr(explode(' ', $p['name'])[1], 0, 1) : ''))) ?>
      </div>
      <div>
        <h1 style="font-size:1.5rem; margin:0 0 0.25rem"><?= e($p['name']) ?></h1>
        <div style="display:flex; gap:0.5rem; flex-wrap:wrap; align-items:center">
          <span class="badge admin">Student-ID: D26CE154</span>
          <span class="badge active">Role: <?= e($p['role']) ?></span>
          <span class="badge">CSPIT-CE · Semester 3</span>
        </div>
      </div>
    </div>
    <div style="text-align:right">
      <span style="font-size:0.8rem; color:var(--muted)">Account Status</span><br>
      <span class="badge <?= $p['status'] === 'active' ? 'open' : 'closed' ?>"><?= strtoupper($p['status']) ?></span>
    </div>
  </div>
</div>

<!-- Academic Highlights Grid (from Dhruv's Practical Wireframe) -->
<div class="grid cols-3" style="margin-bottom:1.75rem">
  <div class="card">
    <span class="section-label">Academic Details</span>
    <p style="margin:0.2rem 0; font-size:0.9rem"><strong>Institute:</strong> CSPIT, CHARUSAT</p>
    <p style="margin:0.2rem 0; font-size:0.9rem"><strong>Course:</strong> <?= e($p['course'] ?? 'B.Tech CE') ?></p>
    <p style="margin:0.2rem 0; font-size:0.9rem"><strong>Academic Year:</strong> 2026 - 2027</p>
    <p style="margin:0.2rem 0; font-size:0.9rem"><strong>Semester:</strong> 3rd (ODD)</p>
  </div>
  
  <div class="card">
    <span class="section-label">Achievements</span>
    <div style="display:flex; flex-direction:column; gap:0.5rem">
      <div style="font-size:0.85rem">🏆 Dean's List, Academic Year 2025–26</div>
      <div style="font-size:0.85rem">💻 Finalist — Charusat Hackathon 2026</div>
      <div style="font-size:0.85rem">⭐ ITUE203 WDF Semester Project Lead</div>
    </div>
  </div>

  <div class="card">
    <span class="section-label">Recent Activity</span>
    <div class="notice-feed" style="max-height:140px">
      <div class="notice-item">
        <span class="notice-author">Session</span> · <span class="notice-time">Today</span>
        <p class="notice-body">Logged in to StudentHub campus portal.</p>
      </div>
      <div class="notice-item" style="border-left-color:var(--success)">
        <span class="notice-author">Registration</span> · <span class="notice-time">Recent</span>
        <p class="notice-body">RSVP submitted for HackCharusat.</p>
      </div>
    </div>
  </div>
</div>

<!-- Edit Profile Form -->
<div class="card form-card">
  <h2 style="font-size:1.25rem; margin:0 0 1.25rem">Edit Profile Information</h2>
  <form method="post" novalidate>
    <?= csrf_field() ?>
    <?php if (isset($errors['form'])): ?><div class="alert error"><?= e($errors['form']) ?></div><?php endif; ?>
    
    <div class="form-grid">
      <div>
        <label for="email">Email (Primary Account Identifier)</label>
        <input id="email" value="<?= e($p['email']) ?>" disabled style="background:var(--surface-subtle); color:var(--muted)">
        <small class="hint">Email address cannot be changed directly.</small>
      </div>

      <div>
        <label for="name">Full Name</label>
        <input id="name" name="name" value="<?= e($p['name']) ?>" required>
        <div class="error-msg"><?= e($errors['name'] ?? '') ?></div>
      </div>

      <?php if ($p['sid']): ?>
      <div>
        <label for="mobile">Mobile Number (10 digits)</label>
        <input id="mobile" name="mobile" value="<?= e($p['mobile']) ?>" maxlength="10">
        <div class="error-msg"><?= e($errors['mobile'] ?? '') ?></div>
      </div>

      <div class="form-grid two">
        <div>
          <label for="course">Enrolled Course</label>
          <select id="course" name="course">
            <?php foreach (COURSES as $c): ?>
              <option <?= $p['course'] === $c ? 'selected' : '' ?>><?= e($c) ?></option>
            <?php endforeach; ?>
          </select>
        </div>

        <div>
          <label for="year">Year of Study</label>
          <select id="year" name="year">
            <?php for ($y = 1; $y <= 4; $y++): ?>
              <option value="<?= $y ?>" <?= $p['year'] == $y ? 'selected' : '' ?>>Year <?= $y ?></option>
            <?php endfor; ?>
          </select>
        </div>
      </div>
      <?php endif; ?>

      <div style="display:flex; justify-content:space-between; align-items:center; margin-top:0.5rem">
        <button class="btn" type="submit">Save Changes</button>
        <span style="font-size:0.8rem; color:var(--muted)">Last login: <?= e($p['last_login'] ?? 'Never') ?></span>
      </div>
    </div>
  </form>
</div>

<?php require 'includes/footer.php'; ?>
