/**
 * StudentHub - Practical 3 (Advanced Extension)
 * Reusable UI layout components using JavaScript / jQuery-compatible design pattern.
 * Provides programmatic constructors for cards, modals, alerts, and badges.
 */
(function (global) {
  'use strict';

  const esc = s => String(s ?? '').replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));

  const StudentHubUI = {
    /**
     * Create a card layout component
     * @param {Object} options { title, content, badge, badgeClass, image, actions: [{ label, onClick, className }] }
     */
    createCard: function (options) {
      const card = document.createElement('article');
      card.className = 'card ' + (options.className || '');

      let html = '';
      if (options.image) {
        html += `<img class="poster" src="${esc(options.image)}" alt="${esc(options.title || 'Image')}" loading="lazy">`;
      }
      if (options.title) {
        html += `<h3>${esc(options.title)}</h3>`;
      }
      if (options.badge) {
        html += `<span class="badge ${esc(options.badgeClass || '')}">${esc(options.badge)}</span>`;
      }
      if (options.content) {
        html += `<div class="card-content">${options.content}</div>`;
      }
      card.innerHTML = html;

      if (options.actions && Array.isArray(options.actions)) {
        const actionWrap = document.createElement('div');
        actionWrap.className = 'card-actions';
        actionWrap.style.marginTop = '0.8rem';
        actionWrap.style.display = 'flex';
        actionWrap.style.gap = '0.5rem';

        options.actions.forEach(act => {
          const btn = document.createElement('button');
          btn.type = 'button';
          btn.className = 'btn small ' + (act.className || 'secondary');
          btn.textContent = act.label;
          if (typeof act.onClick === 'function') {
            btn.addEventListener('click', act.onClick);
          }
          actionWrap.appendChild(btn);
        });
        card.appendChild(actionWrap);
      }

      return card;
    },

    /**
     * Create an accessible notification alert
     * @param {string} type 'success' | 'error' | 'info'
     * @param {string} message Text message
     */
    createAlert: function (type, message, autoHideMs = 5000) {
      const el = document.createElement('div');
      el.className = `alert ${esc(type)}`;
      el.setAttribute('role', 'alert');
      el.textContent = message;

      if (autoHideMs > 0) {
        setTimeout(() => {
          el.style.opacity = '0';
          el.style.transition = 'opacity 0.4s';
          setTimeout(() => el.remove(), 400);
        }, autoHideMs);
      }
      return el;
    },

    /**
     * Create a modal popup programmatically
     */
    createModal: function (id, title, content) {
      let modal = document.getElementById(id);
      if (modal) return modal;

      modal = document.createElement('div');
      modal.id = id;
      modal.className = 'modal-backdrop';
      modal.setAttribute('role', 'dialog');
      modal.setAttribute('aria-modal', 'true');
      modal.innerHTML = `
        <div class="modal">
          <h2>${esc(title)}</h2>
          <div class="modal-body">${content}</div>
          <div style="margin-top:1rem; text-align:right">
            <button class="btn" type="button" data-close>Close</button>
          </div>
        </div>
      `;
      document.body.appendChild(modal);
      return modal;
    }
  };

  // Optional jQuery / $ plugin wrapper if jQuery is available
  if (global.jQuery) {
    global.jQuery.fn.studentHubCard = function (opts) {
      return this.each(function () {
        this.appendChild(StudentHubUI.createCard(opts));
      });
    };
  }

  global.StudentHubUI = StudentHubUI;
})(window);

