    </main>
    <footer class="site-footer">
      <div class="container footer-grid">
        <div>
          <strong style="color:var(--text); font-size:1.05rem">StudentHub</strong>
          <p style="margin-top:0.35rem">Modern campus management portal — CHARUSAT, ITUE203 Web Development Frameworks.</p>
        </div>
        <div>
          <strong style="color:var(--text)">Quick Links</strong><br>
          <a href="<?= base_url() ?>about.php">About Us</a><br>
          <a href="<?= base_url() ?>events.php">Events</a><br>
          <a href="<?= base_url() ?>faq.php">FAQ</a><br>
          <a href="<?= base_url() ?>contact.php">Contact</a>
        </div>
        <div>
          <strong style="color:var(--text)">Account & Feedback</strong><br>
          <a href="<?= base_url() ?>login.php">Login</a><br>
          <a href="<?= base_url() ?>register.php">Register</a><br>
          <a href="<?= base_url() ?>feedback.php">Feedback</a>
        </div>
      </div>
      <div class="container" style="margin-top:1.5rem; text-align:center"><small>&copy; <?= date('Y') ?> StudentHub. All rights reserved.</small></div>
    </footer>
  </div> <!-- /.app-main -->
</div> <!-- /.app-layout -->

<script src="<?= base_url() ?>assets/js/main.js"></script>
<?php foreach ($extraScripts ?? [] as $s): ?><script src="<?= base_url() . e($s) ?>"></script><?php endforeach; ?>
</body>
</html>
