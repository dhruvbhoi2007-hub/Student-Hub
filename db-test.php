<?php
// Practical 8: Database Connection & Schema Test Page
// Used for Practical 8 Post-Lab Submission: "Submit SQL dump, db.php file, and connection test screenshot."
$pageTitle = 'Database Connection Test';
require_once 'includes/config.php';
require_once 'includes/functions.php';

$tests = [];
$allOk = true;

// 1. PDO Connection
try {
    $pdo = new PDO('mysql:host=' . DB_HOST . ';dbname=' . DB_NAME . ';charset=utf8mb4', DB_USER, DB_PASS, [
        PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
        PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
        PDO::ATTR_EMULATE_PREPARES => false,
    ]);
    $tests[] = ['name' => 'PHP Data Objects (PDO) Connection', 'status' => 'Pass', 'details' => 'Connected successfully to ' . DB_NAME . ' on ' . DB_HOST];
} catch (Throwable $e) {
    $allOk = false;
    $tests[] = ['name' => 'PHP Data Objects (PDO) Connection', 'status' => 'Fail', 'details' => $e->getMessage()];
}

// 2. MySQLi Connection
try {
    $mysqli = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);
    if ($mysqli->connect_error) throw new Exception($mysqli->connect_error);
    $mysqli->set_charset('utf8mb4');
    $tests[] = ['name' => 'MySQLi Prepared Connection', 'status' => 'Pass', 'details' => 'MySQLi connection active (charset: utf8mb4)'];
} catch (Throwable $e) {
    $allOk = false;
    $tests[] = ['name' => 'MySQLi Prepared Connection', 'status' => 'Fail', 'details' => $e->getMessage()];
}

// 3. Schema & Seed Verification
$expectedTables = [
    'users' => 2,
    'students' => 20,
    'events' => 15,
    'registrations' => 15,
    'remember_tokens' => 0,
    'audit_logs' => 1
];

if (isset($pdo)) {
    foreach ($expectedTables as $table => $minCount) {
        try {
            $cnt = (int)$pdo->query("SELECT COUNT(*) FROM `$table`")->fetchColumn();
            $pass = $cnt >= $minCount;
            $tests[] = [
                'name' => "Table: `$table`",
                'status' => $pass ? 'Pass' : 'Warning',
                'details' => "$cnt row(s) found (minimum expected: $minCount)"
            ];
        } catch (Throwable $e) {
            $allOk = false;
            $tests[] = ['name' => "Table: `$table`", 'status' => 'Fail', 'details' => 'Table missing or inaccessible: ' . $e->getMessage()];
        }
    }

    // 4. Stored Procedure sp_registrations_by_month
    try {
        $st = $pdo->query('CALL sp_registrations_by_month()');
        $rows = $st->fetchAll();
        $st->closeCursor();
        $tests[] = [
            'name' => 'Stored Procedure: `sp_registrations_by_month()`',
            'status' => 'Pass',
            'details' => 'Executed successfully. Returned ' . count($rows) . ' monthly bucket(s).'
        ];
    } catch (Throwable $e) {
        $tests[] = [
            'name' => 'Stored Procedure: `sp_registrations_by_month()`',
            'status' => 'Warning',
            'details' => 'Could not call procedure: ' . $e->getMessage()
        ];
    }

    // 5. Stored Procedure sp_event_registration_count
    try {
        $st = $pdo->prepare('CALL sp_event_registration_count(?)');
        $st->execute([1]);
        $res = $st->fetch();
        $st->closeCursor();
        $tests[] = [
            'name' => 'Stored Procedure: `sp_event_registration_count(1)`',
            'status' => 'Pass',
            'details' => 'Executed successfully for event: ' . ($res['title'] ?? 'N/A') . ' (count: ' . ($res['total'] ?? 0) . ')'
        ];
    } catch (Throwable $e) {
        $tests[] = [
            'name' => 'Stored Procedure: `sp_event_registration_count()`',
            'status' => 'Warning',
            'details' => 'Could not call procedure: ' . $e->getMessage()
        ];
    }
}

require 'includes/header.php';
?>
<h1>Practical 8 — Database Connection &amp; Schema Test</h1>
<p class="lead">Verification report for PDO, MySQLi, schema normalization, seed data and stored procedures.</p>

<div class="alert <?= $allOk ? 'success' : 'error' ?>" role="status">
  <strong>Status:</strong> <?= $allOk ? 'All core database connections and tables are operational! Ready for screenshots.' : 'Some tests did not pass. Ensure MySQL is running in XAMPP and studenthub.sql is imported.' ?>
</div>

<div class="grid cols-3" style="margin-bottom:1.5rem">
  <div class="card stat"><div class="num"><?= DB_HOST ?></div>Database Host</div>
  <div class="card stat"><div class="num"><?= DB_NAME ?></div>Database Name</div>
  <div class="card stat"><div class="num">utf8mb4</div>Character Set</div>
</div>

<div class="table-wrap">
  <table>
    <thead>
      <tr>
        <th>Component / Test</th>
        <th>Result</th>
        <th>Details</th>
      </tr>
    </thead>
    <tbody>
      <?php foreach ($tests as $t): ?>
      <tr>
        <td><strong><?= e($t['name']) ?></strong></td>
        <td>
          <span class="badge <?= $t['status'] === 'Pass' ? 'active' : ($t['status'] === 'Warning' ? 'admin' : 'deleted') ?>">
            <?= e($t['status']) ?>
          </span>
        </td>
        <td><?= e($t['details']) ?></td>
      </tr>
      <?php endforeach; ?>
    </tbody>
  </table>
</div>

<div class="card" style="margin-top:2rem">
  <h3>Post Laboratory Submission Checklist</h3>
  <ul>
    <li>✔ <strong>SQL Dump:</strong> Located at <code>database/studenthub.sql</code></li>
    <li>✔ <strong>Connection File:</strong> Located at <code>includes/db.php</code></li>
    <li>✔ <strong>Connection Test Screenshot:</strong> Take a screenshot of this page (<a href="db-test.php">db-test.php</a>)</li>
    <li>✔ <strong>Normalization:</strong> 3NF relational schema with <code>users</code>, <code>students</code>, <code>events</code>, <code>registrations</code>, <code>audit_logs</code>, and <code>remember_tokens</code></li>
  </ul>
</div>

<?php require 'includes/footer.php'; ?>
