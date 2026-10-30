<?php
// Practical 7: PHP form processing, server-side validation, CSV storage, CSRF, CSV display
$pageTitle = 'Contact'; require_once 'includes/functions.php';
$errors = []; $old = ['name' => '', 'email' => '', 'subject' => '', 'message' => ''];
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (!csrf_check()) { $errors['form'] = 'Invalid form token. Please reload and try again.'; }
    else {
        foreach ($old as $k => $_) $old[$k] = clean($_POST[$k] ?? '');
        if (!preg_match("/^[A-Za-z][A-Za-z .'-]{2,59}$/", $old['name'])) $errors['name'] = 'Enter a valid name.';
        if (!filter_var($old['email'], FILTER_VALIDATE_EMAIL)) $errors['email'] = 'Enter a valid email.';
        if (mb_strlen($old['subject']) < 3 || mb_strlen($old['subject']) > 100) $errors['subject'] = 'Subject must be 3-100 characters.';
        if (mb_strlen($old['message']) < 10 || mb_strlen($old['message']) > 1000) $errors['message'] = 'Message must be 10-1000 characters.';
        if (!$errors) {
            $file = BASE_PATH . '/data/contacts.csv'; $new = !file_exists($file);
            $fh = fopen($file, 'a');
            if ($fh && flock($fh, LOCK_EX)) {
                if ($new) fputcsv($fh, ['timestamp', 'name', 'email', 'subject', 'message']);
                fputcsv($fh, [date('Y-m-d H:i:s'), $old['name'], $old['email'], $old['subject'], $old['message']]);
                flock($fh, LOCK_UN); fclose($fh);
                flash('success', 'Thanks! Your message has been saved.'); redirect('contact.php');
            } else $errors['form'] = 'Could not save your message. Try again later.';
        }
    }
}

// Practical 7 (Intermediate extension): Display stored CSV records on a webpage
$storedContacts = [];
$csvPath = BASE_PATH . '/data/contacts.csv';
if (file_exists($csvPath)) {
    if (($fh = fopen($csvPath, 'r')) !== false) {
        $header = fgetcsv($fh);
        while (($row = fgetcsv($fh)) !== false) {
            if ($header && count($row) === count($header)) {
                $storedContacts[] = array_combine($header, $row);
            }
        }
        fclose($fh);
    }
}
$storedContacts = array_reverse($storedContacts);

require 'includes/header.php'; ?>
<h1>Contact us</h1>
<form method="post" class="card form-card" novalidate>
  <?= csrf_field() ?>
  <?php if (isset($errors['form'])): ?><div class="alert error"><?= e($errors['form']) ?></div><?php endif; ?>
  <div class="form-grid">
    <?php foreach ([['name','Full name','text'],['email','Email','email'],['subject','Subject','text']] as [$n,$l,$t]): ?>
    <div><label for="<?= $n ?>"><?= $l ?></label><input type="<?= $t ?>" id="<?= $n ?>" name="<?= $n ?>" value="<?= e($old[$n]) ?>" required class="<?= isset($errors[$n]) ? 'invalid' : '' ?>"><div class="error-msg"><?= e($errors[$n] ?? '') ?></div></div>
    <?php endforeach; ?>
    <div><label for="message">Message</label><textarea id="message" name="message" rows="5" required class="<?= isset($errors['message']) ? 'invalid' : '' ?>"><?= e($old['message']) ?></textarea><div class="error-msg"><?= e($errors['message'] ?? '') ?></div></div>
    <button class="btn" type="submit">Send message</button>
  </div>
</form>

<?php if ($storedContacts): ?>
<section style="margin-top:2.5rem">
  <h2>Stored Inquiries (Practical 7: CSV Storage View)</h2>
  <p class="hint">Records read from <code>data/contacts.csv</code> — demonstrated on page as per Practical 7 Intermediate Extension.</p>
  <div class="table-wrap">
    <table>
      <thead><tr><th>Time</th><th>Name</th><th>Email</th><th>Subject</th><th>Message</th></tr></thead>
      <tbody>
        <?php foreach (array_slice($storedContacts, 0, 5) as $c): ?>
        <tr>
          <td><?= e($c['timestamp']) ?></td>
          <td><?= e($c['name']) ?></td>
          <td><?= e($c['email']) ?></td>
          <td><?= e($c['subject']) ?></td>
          <td><?= e($c['message']) ?></td>
        </tr>
        <?php endforeach; ?>
      </tbody>
    </table>
  </div>
</section>
<?php endif; ?>
<?php require 'includes/footer.php'; ?>