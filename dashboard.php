<?php
// Student dashboard: Acade UI SaaS Dashboard Theme
$pageTitle = 'Dashboard';
require_once 'includes/functions.php';
require_once 'includes/db.php';
try_remember_login($pdo);
require_login();
if (is_admin()) redirect('admin/dashboard.php');

$uid = current_user()['id'];
$st = $pdo->prepare('SELECT id, name, course, year FROM students WHERE user_id=?');
$st->execute([$uid]);
$student = $st->fetch();
$sid = $student['id'] ?? null;

// Event registration handling
if ($_SERVER['REQUEST_METHOD'] === 'POST' && $sid) {
    if (!csrf_check()) flash('error', 'Invalid token.');
    else {
        $eid = (int)($_POST['event_id'] ?? 0);
        if (($_POST['action'] ?? '') === 'register') {
            $ev = $pdo->prepare("SELECT id FROM events WHERE id=? AND status='open'");
            $ev->execute([$eid]);
            if (!$ev->fetch()) flash('error', 'That event is closed or does not exist.');
            else {
                try {
                    $pdo->prepare('INSERT INTO registrations (student_id,event_id) VALUES (?,?)')->execute([$sid, $eid]);
                    flash('success', 'Registered for the event!');
                } catch (PDOException $e) {
                    flash('error', 'You are already registered for this event.');
                }
            }
        } elseif (($_POST['action'] ?? '') === 'cancel') {
            $pdo->prepare('DELETE FROM registrations WHERE student_id=? AND event_id=?')->execute([$sid, $eid]);
            flash('success', 'Registration cancelled.');
        }
    }
    redirect('dashboard.php');
}

$my = [];
if ($sid) {
    $q = $pdo->prepare('SELECT e.*, r.registered_at FROM registrations r JOIN events e ON e.id=r.event_id WHERE r.student_id=? ORDER BY e.event_date');
    $q->execute([$sid]);
    $my = $q->fetchAll();
}
$open = $pdo->query("SELECT * FROM events WHERE status='open' AND event_date >= CURDATE() ORDER BY event_date LIMIT 6")->fetchAll();
$myIds = array_column($my, 'id');

require 'includes/header.php';
?>

<!-- ================= TODAY'S TIMETABLE ================= -->
<span class="section-label">Today's Timetable</span>
<div class="schedule-grid">
  <div class="schedule-card">
    <span class="schedule-time">9:00 a.m – 10:00 a.m</span>
    <h3 class="schedule-title">Database Management</h3>
    <p class="schedule-sub">FD's and Normalisation · Lab 4</p>
  </div>
  <div class="schedule-card">
    <span class="schedule-time">10:00 a.m – 11:00 a.m</span>
    <h3 class="schedule-title">Web Dev Frameworks</h3>
    <p class="schedule-sub">ITUE203 Full-Stack Session · Comp Lab 2</p>
  </div>
  <div class="schedule-card">
    <span class="schedule-time">11:00 a.m – 12:00 p.m</span>
    <h3 class="schedule-title">Algorithms & DS</h3>
    <p class="schedule-sub">Stacks, Queues & Graph Traversal</p>
  </div>
  <div class="schedule-card">
    <span class="schedule-time">12:00 p.m – 1:00 p.m</span>
    <h3 class="schedule-title">AI & Machine Learning</h3>
    <p class="schedule-sub">Supervised Models & Gradient Descent</p>
  </div>
</div>

<!-- ================= METRICS & NOTICE BOARD LAYOUT ================= -->
<div class="grid cols-3" style="align-items:start; margin-bottom:2rem">
  
  <!-- Column 1: Circular Progress Metric (Attendance) -->
  <div class="card donut-card">
    <h3 style="font-size:1.05rem; margin-bottom:0.25rem">Attendance</h3>
    <span style="font-size:0.8rem; color:var(--muted)">This Semester</span>
    <div class="donut-wrap">
      <svg class="donut-svg" viewBox="0 0 100 100">
        <circle class="donut-bg" cx="50" cy="50" r="40" />
        <circle class="donut-val" cx="50" cy="50" r="40" stroke-dasharray="251.2" stroke-dashoffset="20.1" />
      </svg>
      <div class="donut-text">92%</div>
    </div>
    <div class="donut-legend">
      <span><i class="dot purple"></i> Present</span>
      <span><i class="dot yellow"></i> Not marked</span>
      <span><i class="dot gray"></i> Absent</span>
    </div>
  </div>

  <!-- Column 2: Circular Progress Metric (Assignment / Activity Completion) -->
  <div class="card donut-card">
    <h3 style="font-size:1.05rem; margin-bottom:0.25rem">Activity Completion</h3>
    <span style="font-size:0.8rem; color:var(--muted)">Campus & Academic</span>
    <div class="donut-wrap">
      <svg class="donut-svg" viewBox="0 0 100 100">
        <circle class="donut-bg" cx="50" cy="50" r="40" />
        <circle class="donut-val" cx="50" cy="50" r="40" stroke-dasharray="251.2" stroke-dashoffset="37.6" />
      </svg>
      <div class="donut-text">85%</div>
    </div>
    <div class="donut-legend">
      <span><i class="dot purple"></i> Completed</span>
      <span><i class="dot yellow"></i> Pending</span>
      <span><i class="dot gray"></i> Inactive</span>
    </div>
  </div>

  <!-- Column 3: Notice Board Widget (from Acade UI) -->
  <div class="card">
    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1rem">
      <h3 style="font-size:1.05rem; margin:0">Notice Board</h3>
      <span style="font-size:0.75rem; color:var(--primary); font-weight:700"><?= date('jS M Y') ?></span>
    </div>
    <div class="notice-feed">
      <div class="notice-item">
        <div class="notice-header">
          <span class="notice-author">Prof. Parmar</span>
          <span class="notice-time">15 mins ago</span>
        </div>
        <p class="notice-body">ITUE203 practical submissions are scheduled. Ensure your GitHub commits are pushed.</p>
      </div>
      <div class="notice-item" style="border-left-color:var(--accent-yellow)">
        <div class="notice-header">
          <span class="notice-author">Campus Admin</span>
          <span class="notice-time">1 hour ago</span>
        </div>
        <p class="notice-body">HackCharusat hackathon registrations closing this Friday. Check Events to RSVP.</p>
      </div>
      <div class="notice-item" style="border-left-color:var(--success)">
        <div class="notice-header">
          <span class="notice-author">Library Desk</span>
          <span class="notice-time">3 hours ago</span>
        </div>
        <p class="notice-body">New digital reference books for Web Development Frameworks are now accessible online.</p>
      </div>
    </div>
  </div>

</div>

<!-- ================= MY REGISTERED EVENTS ================= -->
<div class="card" style="margin-bottom:2rem">
  <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1rem">
    <div>
      <h2 style="font-size:1.25rem; margin:0 0 0.2rem 0">My Registered Events</h2>
      <span style="font-size:0.85rem; color:var(--muted)">Events you have confirmed your seat for</span>
    </div>
    <a class="btn small secondary" href="events.php">Browse All Events &rarr;</a>
  </div>

  <?php if (!$my): ?>
    <p class="hint" style="padding:1.5rem 0; text-align:center">You haven't registered for any events yet. Explore upcoming campus events below!</p>
  <?php else: ?>
    <div class="table-wrap">
      <table>
        <thead>
          <tr>
            <th>Event</th>
            <th>Date</th>
            <th>Category</th>
            <th>Venue</th>
            <th>Action</th>
          </tr>
        </thead>
        <tbody>
          <?php foreach ($my as $r): ?>
          <tr>
            <td><strong><?= e($r['title']) ?></strong></td>
            <td><?= e($r['event_date']) ?></td>
            <td><span class="badge"><?= e($r['category']) ?></span></td>
            <td><?= e($r['venue']) ?></td>
            <td>
              <form method="post" style="display:inline">
                <?= csrf_field() ?>
                <input type="hidden" name="action" value="cancel">
                <input type="hidden" name="event_id" value="<?= $r['id'] ?>">
                <button class="btn danger small" data-confirm="Cancel registration for <?= e($r['title']) ?>?">Cancel</button>
              </form>
            </td>
          </tr>
          <?php endforeach; ?>
        </tbody>
      </table>
    </div>
  <?php endif; ?>
</div>

<!-- ================= OPEN CAMPUS EVENTS ================= -->
<span class="section-label">Upcoming Campus Opportunities</span>
<div class="grid cols-3" style="margin-bottom:2.5rem">
  <?php foreach ($open as $ev): ?>
  <article class="card">
    <?php if ($ev['poster']): ?>
      <img class="poster" src="<?= UPLOAD_URL . e($ev['poster']) ?>" alt="Poster for <?= e($ev['title']) ?>" loading="lazy" style="height:150px; border-radius:12px; margin-bottom:0.75rem">
    <?php endif; ?>
    <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:0.4rem">
      <h3 style="font-size:1.1rem; margin:0"><?= e($ev['title']) ?></h3>
      <span class="badge open"><?= e($ev['category']) ?></span>
    </div>
    <p style="font-size:0.85rem; color:var(--muted); margin:0 0 0.85rem">📅 <?= e($ev['event_date']) ?> · 📍 <?= e($ev['venue']) ?></p>
    
    <?php if (!in_array($ev['id'], $myIds)): ?>
      <form method="post">
        <?= csrf_field() ?>
        <input type="hidden" name="action" value="register">
        <input type="hidden" name="event_id" value="<?= $ev['id'] ?>">
        <button class="btn small btn-block">Register Seat</button>
      </form>
    <?php else: ?>
      <span class="badge active" style="display:block; text-align:center; padding:0.4rem">✔ Seat Reserved</span>
    <?php endif; ?>
  </article>
  <?php endforeach; ?>
</div>

<!-- Floating Action Button (FAB from Acade UI) -->
<button class="fab-btn" onclick="location.href='events.php'" title="Quick Explore Events" aria-label="Explore Events">+</button>

<?php require 'includes/footer.php'; ?>
