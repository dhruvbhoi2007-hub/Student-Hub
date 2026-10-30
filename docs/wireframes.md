# Practical 1 & 3: UI Wireframes & Responsive Layout Specifications

## 1. Global Page Anatomy
Every page in StudentHub follows a standardized, accessibility-compliant structural layout:

```
┌────────────────────────────────────────────────────────────────────────┐
│ [Skip to main content link - hidden until keyboard focus]              │
├────────────────────────────────────────────────────────────────────────┤
│ <header class="site-header">                                           │
│   ┌───────────────────┬─────────────────────────────┬────────────────┐ │
│   │ Brand / Logo      │ Navigation Menu Links       │ Theme Toggle   │ │
│   │ StudentHub        │ Home | About | Events | ... │ 🌙 / ☀️        │ │
│   └───────────────────┴─────────────────────────────┴────────────────┘ │
├────────────────────────────────────────────────────────────────────────┤
│ <div class="banner"> Notification Announcement Bar [Dismiss ✕]         │
├────────────────────────────────────────────────────────────────────────┤
│ <nav class="breadcrumb"> Home › Section › Current Page                 │
├────────────────────────────────────────────────────────────────────────┤
│ <main id="main" class="container">                                     │
│   ┌──────────────────────────────────────────────────────────────────┐ │
│   │ Flash Message Alerts (Success / Error / Info)                    │ │
│   ├──────────────────────────────────────────────────────────────────┤ │
│   │ Page Title (H1) & Sub-heading Lead Paragraph                     │ │
│   ├──────────────────────────────────────────────────────────────────┤ │
│   │ Dynamic Page Content: Cards Grid / Data Tables / Input Forms     │ │
│   └──────────────────────────────────────────────────────────────────┘ │
├────────────────────────────────────────────────────────────────────────┤
│ <footer class="site-footer">                                           │
│   ┌─────────────────────┬──────────────────────┬─────────────────────┐ │
│   │ Project Info & Dept │ Navigation Links     │ Account Shortcuts   │ │
│   └─────────────────────┴──────────────────────┴─────────────────────┘ │
│   (c) 2026 StudentHub · CHARUSAT FTE ITUE203                           │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Low-Fidelity Wireframes for Key Pages

### Page 1: Home Page (`index.php`)
```
Desktop View (min-width: 900px):
┌────────────────────────────────────────────────────────────────────────┐
│  ┌───────────────────────────────┐  ┌────────────────────────────────┐ │
│  │ Hero Headline                 │  │ Aside "Why StudentHub?"        │ │
│  │ "Your campus, connected."     │  │  - Secure login with roles     │ │
│  │ Lead description paragraph... │  │  - One-click registration      │ │
│  │ [Get Started] [Browse Events] │  │  - Admin audit trail           │ │
│  └───────────────────────────────┘  └────────────────────────────────┘ │
├────────────────────────────────────────────────────────────────────────┤
│  [‹] Highlight Slider (Tech Fest / Placements / Cultural Week)     [›] │
├────────────────────────────────────────────────────────────────────────┤
│  Feature Cards Grid (3 Columns)                                        │
│  ┌──────────────────┐  ┌──────────────────┐  ┌───────────────────────┐ │
│  │ 👩‍🎓 Student Records │  │ 📅 Events        │  │ 🔐 Secure Access      │ │
│  │ Admin CRUD & CSV │  │ Browse & Register│  │ RBAC & Hashed Session │ │
│  └──────────────────┘  └──────────────────┘  └───────────────────────┘ │
└────────────────────────────────────────────────────────────────────────┘
```

### Page 2: Student Directory with Dependent Dropdowns (`directory.php`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ Toolbar Filter Bar:                                                    │
│ [ Search input... ] [ Course: All ▾ ] [ State: All ▾ ] [ City ▾ ] [Sort]│
├────────────────────────────────────────────────────────────────────────┤
│ Student Cards Grid (Repeat 3 columns on desktop, 1 on mobile):         │
│ ┌─────────────────────────┐  ┌─────────────────────────┐               │
│ │ Student Name            │  │ Student Name            │               │
│ │ [Course Badge] [Yr]     │  │ [Course Badge] [Yr]     │               │
│ │ ✉ email@domain.com      │  │ ✉ email@domain.com      │               │
│ │ 📞 9876543210           │  │ 📞 9876543210           │               │
│ │ 📍 City, State          │  │ 📍 City, State          │               │
│ └─────────────────────────┘  └─────────────────────────┘               │
├────────────────────────────────────────────────────────────────────────┤
│ Pagination: [ < Prev ] [ 1 ] [ 2 ] [ 3 ] [ Next > ]                    │
└────────────────────────────────────────────────────────────────────────┘
```

### Page 3: Admin Dashboard (`admin/dashboard.php`)
```
┌─────────────────┬──────────────────────────────────────────────────────┐
│ Sidebar Menu    │ Metric KPI Cards:                                    │
│ 📊 Overview     │ ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌───────────┐ │
│ 👩‍🎓 Students     │ │ 2 Users  │ │ 24 Stdnts│ │ 18 Events│ │ 40 Regs   │ │
│ 📅 Events       │ └──────────┘ └──────────┘ └──────────┘ └───────────┘ │
│ 🧾 Audit Log    │ Charts Section:                                      │
│ ⚡ Live Events  │ ┌─────────────────────────┐ ┌──────────────────────┐ │
│                 │ │ Registrations by Event  │ │ Students by Course   │ │
│                 │ │ █  █  █  █  █           │ │ • CE: 6  • IT: 5     │ │
│                 │ └─────────────────────────┘ └──────────────────────┘ │
│                 │ Monthly Stored Procedure Analytics:                  │
│                 │ [ June: 8 | July: 6 | Aug: 11 | Sept: 9 | Oct: 6 ]   │
│                 │ Latest Registrations Table + User Status Toggles     │
└─────────────────┴──────────────────────────────────────────────────────┘
```

---

## 3. Responsive Breakpoints & Layout Adaptations

StudentHub utilizes modern CSS Grid and Flexbox techniques without bloated third-party CSS frameworks.

| Viewport Category | Screen Width | Nav Menu Behavior | Grid Columns | Typography Scaling |
|---|:---:|:---:|:---:|:---:|
| **Mobile** | `< 600px` | Collapsed hamburger drawer | 1 Column (`1fr`) | `clamp(1.75rem, 5vw, 2.2rem)` |
| **Tablet / Phablet**| `600px - 899px` | Collapsed hamburger | 2 Columns (`repeat(2, 1fr)`) | `clamp(2rem, 4vw, 2.6rem)` |
| **Desktop / Laptop**| `≥ 900px` | Horizontal flex row | 3-4 Columns (`repeat(3, 1fr)`) | `clamp(2.4rem, 5vw, 3.2rem)` |
| **Wide Screen** | `≥ 1200px` | Horizontal flex row with max-width container (`1140px`) | Up to 4 Columns | Full display size |

### Mobile Breakpoint Adaptations
1. **Header & Navigation:** The hamburger menu button (`#hamburger`) is visible; navigation links are hidden by default and toggle with smooth class transition.
2. **Form Layouts:** Two-column grid form rows (`.form-grid.two`) collapse automatically to a single column for comfortable mobile tapping.
3. **Data Tables:** Horizontal scrolling wrapper (`.table-wrap`) preserves table layout readability without breaking container viewport boundaries.
4. **Hero Area:** Two-column hero collapses to single vertical stack with Call-to-Action buttons styled with full tap targets.
