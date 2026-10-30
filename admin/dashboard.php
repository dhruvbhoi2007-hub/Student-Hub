<?php
// Practical 14: Admin dashboard - SQL aggregation, RBAC, dynamic menu, latest registrations, chart
$pageTitle = 'Admin Dashboard';
require_once __DIR__ . '/../includes/functions.php';
require_once __DIR__ . '/../includes/db.php';
try_remember_login($pdo);
require_role('admin');

if ($_SERVER['REQUEST_METHOD'] === 'POST' && ($_POST['do'] ?? '') === 'toggle') {
    if (csrf_check()) {
        $id = (int)$_POST['id'];
        if ($id !== current_user()['id']) {
            $pdo->prepare("UPDATE users SET status = IF(status='active','inactive','active') WHERE id=?")->execute([$id]);
            audit($pdo, 'user_status_toggle', "user id $id");
            flash('success', 'User status updated.');
        } else {
            flash('error', 'You cannot deactivate yourself.');
        }
    }
    redirect('dashboard.php');
}

$stats = $pdo->query("SELECT (SELECT COUNT(*) FROM users) users, (SELECT COUNT(*) FROM students WHERE status='active') students, (SELECT COUNT(*) FROM events) events, (SELECT COUNT(*) FROM registrations) regs")->fetch();
$latest = $pdo->query('SELECT s.name, e.title, r.registered_at FROM registrations r JOIN students s ON s.id=r.student_id JOIN events e ON e.id=r.event_id ORDER BY r.registered_at DESC, r.id DESC LIMIT 6')->fetchAll();
$byEvent = $pdo->query('SELECT e.title, COUNT(r.id) c FROM events e LEFT JOIN registrations r ON r.event_id=e.id GROUP BY e.id ORDER BY c DESC LIMIT 6')->fetchAll();
$byCourse = $pdo->query("SELECT course, COUNT(*) c FROM students WHERE status='active' GROUP BY course ORDER BY c DESC")->fetchAll();

// Monthly analytics via stored procedure
$monthly = [];
try {
    $st = $pdo->query('CALL sp_registrations_by_month()');
    $monthly = $st->fetchAll();
    $st->closeCursor();
} catch (PDOException $e) {
    error_log($e->getMessage());
}
$mmax = max(1, ...array_map(fn($r) => (int)$r['total'], $monthly ?: [['total' => 1]]));
$users = $pdo->query('SELECT id,name,email,role,status,last_login FROM users ORDER BY id')->fetchAll();
$max = max(1, ...array_map(fn($r) => (int)$r['c'], $byEvent ?: [['c' => 1]]));

require __DIR__ . '/../includes/header.php';
?>

<!-- ================= KPI METRIC CARDS ================= -->
<span class="section-label">Campus Overview &amp; Metrics</span>
<div class="grid cols-4" style="margin-bottom:1.75rem">
  <div class="card stat">
    <div class="num"><?= (int)$stats['users'] ?></div>
    <span style="font-size:0.85rem; font-weight:700; color:var(--text)">Total Users</span>
  </div>
  <div class="card stat">
    <div class="num"><?= (int)$stats['students'] ?></div>
    <span style="font-size:0.85rem; font-weight:700; color:var(--text)">Active Students</span>
  </div>
  <div class="card stat">
    <div class="num"><?= (int)$stats['events'] ?></div>
    <span style="font-size:0.85rem; font-weight:700; color:var(--text)">Campus Events</span>
  </div>
  <div class="card stat">
    <div class="num"><?= (int)$stats['regs'] ?></div>
    <span style="font-size:0.85rem; font-weight:700; color:var(--text)">Total RSVPs</span>
  </div>
</div>

<!-- ================= ANALYTICS & CHARTS ================= -->
<div class="grid cols-2" style="margin-bottom:1.75rem">
  <div class="card">
    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.75rem">
      <h3 style="font-size:1.1rem; margin:0">Registrations by Event</h3>
      <span style="font-size:0.78rem; color:var(--muted)">Top 6 Popular</span>
    </div>
    <div class="bar-chart" role="img" aria-label="Bar chart of registrations by event">
      <?php foreach ($byEvent as $b): ?>
        <div class="bar" style="height:<?= max(8, round($b['c'] / $max * 100)) ?>%" title="<?= e($b['title']) ?> (<?= (int)$b['c'] ?>)">
          <span><?= (int)$b['c'] ?></span>
          <small><?= e(mb_substr($b['title'], 0, 7)) ?></small>
        </div>
      <?php endforeach; ?>
    </div>
  </div>

  <div class="card">
    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1rem">
      <h3 style="font-size:1.1rem; margin:0">Student Distribution</h3>
      <span style="font-size:0.78rem; color:var(--muted)">By Academic Course</span>
    </div>
    <div style="display:flex; flex-direction:column; gap:0.65rem">
      <?php foreach ($byCourse as $c): ?>
      <div>
        <div style="display:flex; justify-content:space-between; font-size:0.85rem; font-weight:600; margin-bottom:0.25rem">
          <span><?= e($c['course']) ?></span>
          <span><?= (int)$c['c'] ?> students</span>
        </div>
        <div style="height:6px; background:var(--surface-subtle); border-radius:99px; overflow:hidden">
          <div style="height:100%; width:<?= min(100, round($c['c'] / max(1, (int)$stats['students']) * 100)) ?>%; background:var(--primary); border-radius:99px"></div>
        </div>
      </div>
      <?php endforeach; ?>
    </div>
  </div>
</div>

<!-- ================= MONTHLY STORED PROCEDURE CHART ================= -->
<div class="card" style="margin-bottom:2rem">
  <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.75rem">
    <div>
      <h3 style="font-size:1.1rem; margin:0 0 0.2rem">Registration Growth Trend</h3>
      <span style="font-size:0.82rem; color:var(--muted)">Generated via MySQL Stored Procedure: <code>sp_registrations_by_month()</code></span>
    </div>
    <span class="badge admin">Stored Procedure</span>
  </div>
  <?php if (!$monthly): ?>
    <p class="hint" style="padding:1.5rem 0; text-align:center">No monthly trend data available.</p>
  <?php else: ?>
    <div class="bar-chart" style="height:160px" role="img" aria-label="Monthly registration chart">
      <?php foreach ($monthly as $m): ?>
        <div class="bar" style="height:<?= max(8, round($m['total'] / $mmax * 100)) ?>%" title="<?= e($m['month']) ?>: <?= (int)$m['total'] ?>">
          <span><?= (int)$m['total'] ?></span>
          <small><?= e($m['month']) ?></small>
        </div>
      <?php endforeach; ?>
    </div>
  <?php endif; ?>
</div>

<!-- ================= LATEST REGISTRATIONS TABLE ================= -->
<div class="card" style="margin-bottom:2rem">
  <h3 style="font-size:1.15rem; margin:0 0 1rem">Recent Registrations</h3>
  <div class="table-wrap">
    <table>
      <thead>
        <tr>
          <th>Student Name</th>
          <th>Event Title</th>
          <th>Registration Timestamp</th>
        </tr>
      </thead>
      <tbody>
        <?php foreach ($latest as $l): ?>
        <tr>
          <td><strong><?= e($l['name']) ?></strong></td>
          <td><span class="badge"><?= e($l['title']) ?></span></td>
          <td style="color:var(--muted); font-size:0.88rem"><?= e($l['registered_at']) ?></td>
        </tr>
        <?php endforeach; ?>
      </tbody>
    </table>
  </div>
</div>

<!-- ================= USER MANAGEMENT & TOGGLES ================= -->
<div class="card">
  <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1rem">
    <div>
      <h3 style="font-size:1.15rem; margin:0 0 0.2rem">Portal Users</h3>
      <span style="font-size:0.85rem; color:var(--muted)">Manage role accounts and toggle active/inactive status</span>
    </div>
  </div>
  <div class="table-wrap">
    <table>
      <thead>
        <tr>
          <th>User</th>
          <th>Email Address</th>
          <th>Role</th>
          <th>Status</th>
          <th>Last Login</th>
          <th>Action</th>
        </tr>
      </thead>
      <tbody>
        <?php foreach ($users as $u): ?>
        <tr>
          <td><strong><?= e($u['name']) ?></strong></td>
          <td><?= e($u['email']) ?></td>
          <td><span class="badge <?= e($u['role']) ?>"><?= e($u['role']) ?></span></td>
          <td><span class="badge <?= e($u['status']) ?>"><?= e($u['status']) ?></span></td>
          <td style="color:var(--muted); font-size:0.85rem"><?= e($u['last_login'] ?? 'Never') ?></td>
          <td>
            <form method="post" style="display:inline">
              <?= csrf_field() ?>
              <input type="hidden" name="do" value="toggle">
              <input type="hidden" name="id" value="<?= $u['id'] ?>">
              <button class="btn small secondary" <?= $u['id'] == current_user()['id'] ? 'disabled' : '' ?>>
                <?= $u['status'] === 'active' ? 'Deactivate' : 'Activate' ?>
              </button>
            </form>
          </td>
        </tr>
        <?php endforeach; ?>
      </tbody>
    </table>
  </div>
</div>

<?php require __DIR__ . '/../includes/footer.php'; ?>
