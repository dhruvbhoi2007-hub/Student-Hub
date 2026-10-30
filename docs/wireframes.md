# Practical 1 & 3: UI Wireframes & Responsive Layout Specifications

**Student-ID:** D26CE154  
**Student-Name:** Dhruv Bhoi  
**Department:** CSPIT-CE, Faculty of Technology and Engineering (FTE)  
**Subject:** Web Development Frameworks (ITUE203) — Semester 3, 2026-27 (ODD)  
**Institution:** CHAROTAR UNIVERSITY OF SCIENCE AND TECHNOLOGY (CHARUSAT)  

---

## 1. Global App Shell Anatomy (Acade SaaS Inspired)
Every page in StudentHub follows a modern app-shell layout with a persistent left navigation sidebar and a top utility header:

```
┌─────────────────┬──────────────────────────────────────────────────────────────┐
│ [Sidebar]       │ <header class="app-topbar">                                  │
│                 │  [☰ Menu]  "Welcome, Dhruv 👋"  [🔍 Search] [🌙] [🔔] [Avatar]│
│  ▲ StudentHub   ├──────────────────────────────────────────────────────────────┤
│                 │ <div class="banner"> Announcements / Notifications [✕]       │
│  📊 Dashboard   ├──────────────────────────────────────────────────────────────┤
│  🏠 Home        │ <main id="main" class="content-body">                        │
│  ℹ️ About       │                                                              │
│  📅 Events      │  ┌────────────────────────────────────────────────────────┐  │
│  👥 Directory   │  │ Section Label / Header                                 │  │
│  ⚡ Live Events │  │ Interactive Cards / Schedules / Circular Donut Metrics │  │
│  ❓ FAQ         │  │ Data Tables / Action Buttons                           │  │
│  ✉️ Contact     │  └────────────────────────────────────────────────────────┘  │
│  💬 Feedback    ├──────────────────────────────────────────────────────────────┤
│                 │ <footer class="site-footer">                                 │
│  [Promo Widget] │  StudentHub · Developed by Dhruv Bhoi (D26CE154)             │
│  ⚙️ Settings    │                                                              │
│  🚪 Logout      │                                                              │
└─────────────────┴──────────────────────────────────────────────────────────────┘
```

---

## 2. Low-Fidelity Wireframes for Key Pages

### Page 1: Modern Student Dashboard (`dashboard.php`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ TODAY'S TIMETABLE                                                      │
│ ┌────────────────┐ ┌────────────────┐ ┌────────────────┐ ┌───────────┐ │
│ │ 9:00 - 10:00am │ │ 10:00 - 11:00am│ │ 11:00 - 12:00pm│ │ 12 - 1:00pm│ │
│ │ Database Mgmt  │ │ Web Dev (WDF)  │ │ Algorithms     │ │ AI & ML   │ │
│ │ Lab 4          │ │ Comp Lab 2     │ │ Stacks/Queues  │ │ Models    │ │
│ └────────────────┘ └────────────────┘ └────────────────┘ └───────────┘ │
├────────────────────────────────────────────────────────────────────────┤
│ METRICS & NOTICE BOARD GRID (3 Columns)                                │
│ ┌──────────────────┐  ┌──────────────────┐  ┌────────────────────────┐ │
│ │ Attendance       │  │ Activity Rate    │  │ Notice Board           │ │
│ │     ( 92% )      │  │     ( 85% )      │  │ • Prof. Parmar: WDF... │ │
│ │ ● Present        │  │ ● Completed      │  │ • HackCharusat Closing │ │
│ │ ● Not marked     │  │ ● Pending        │  │ • Library Tech Books   │ │
│ └──────────────────┘  └──────────────────┘  └────────────────────────┘ │
├────────────────────────────────────────────────────────────────────────┤
│ MY REGISTERED EVENTS (Table with 1-Click Cancellation)                 │
│ ┌───────────────┬────────────┬─────────────┬─────────────┬───────────┐ │
│ │ Event         │ Date       │ Category    │ Venue       │ Action    │ │
│ │ HackCharusat  │ 2026-11-03 │ Cultural    │ Seminar A   │ [Cancel]  │ │
│ └───────────────┴────────────┴─────────────┴─────────────┴───────────┘ │
├────────────────────────────────────────────────────────────────────────┤
│ UPCOMING CAMPUS OPPORTUNITIES (Cards Grid with 1-Click Register)       │
│ ┌─────────────────────────┐  ┌─────────────────────────┐               │
│ │ Web Dev Bootcamp        │  │ Annual Cultural Fest    │               │
│ │ 📅 2026-11-05 · 📍 Lab 3 │  │ 📅 2026-11-07 · 📍 Ground│               │
│ │ [Register Seat Button]  │  │ [Register Seat Button]  │   [ + FAB ]   │
│ └─────────────────────────┘  └─────────────────────────┘               │
└────────────────────────────────────────────────────────────────────────┘
```

### Page 2: Student Directory with Dependent Dropdowns (`directory.php`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ Search & Dependent Filters Toolbar:                                    │
│ [ 🔍 Search name… ] [ Course: All ▾ ] [ State: Gujarat ▾ ] [ City ▾ ]   │
├────────────────────────────────────────────────────────────────────────┤
│ Student Cards Grid:                                                    │
│ ┌─────────────────────────┐  ┌─────────────────────────┐               │
│ │ Dhruv Bhoi              │  │ Aarav Patel             │               │
│ │ [B.Tech CE] [Year 2]    │  │ [B.Tech CE] [Year 1]    │               │
│ │ ✉ student@studenthub... │  │ ✉ aarav.patel@...       │               │
│ │ 📞 9876543210           │  │ 📞 8260181590           │               │
│ │ 📍 Anand, Gujarat       │  │ 📍 Anand, Gujarat       │               │
│ └─────────────────────────┘  └─────────────────────────┘               │
└────────────────────────────────────────────────────────────────────────┘
```

### Page 3: Admin Dashboard (`admin/dashboard.php`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ CAMPUS OVERVIEW & METRICS                                              │
│ ┌──────────────┐ ┌──────────────┐ ┌──────────────┐ ┌─────────────────┐ │
│ │ 3 Users      │ │ 25 Students  │ │ 18 Events    │ │ 40 Registrations│ │
│ └──────────────┘ └──────────────┘ └──────────────┘ └─────────────────┘ │
├────────────────────────────────────────────────────────────────────────┤
│ ANALYTICS & CHARTS                                                     │
│ ┌─────────────────────────────┐  ┌───────────────────────────────────┐ │
│ │ Registrations by Event      │  │ Student Distribution by Course    │ │
│ │ █  █  █  █  █               │  │ • CE: 7  • IT: 5  • CSE: 4        │ │
│ └─────────────────────────────┘  └───────────────────────────────────┘ │
├────────────────────────────────────────────────────────────────────────┤
│ MONTHLY REGISTRATIONS CHART (MySQL Stored Procedure)                   │
│ ┌────────────────────────────────────────────────────────────────────┐ │
│ │  sp_registrations_by_month() Trend: [ Jun: 8 | Jul: 6 | Aug: 11 ]  │ │
│ └────────────────────────────────────────────────────────────────────┘ │
│ Recent Registrations Table + User Active/Inactive Toggle Switches      │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Responsive Breakpoints & Adaptations

| Viewport Category | Screen Width | Sidebar Navigation | Layout Adjustments |
|---|:---:|:---:|:---:|
| **Mobile** | `< 900px` | Off-canvas drawer sliding in via `☰` hamburger | Single column grid; horizontal table scroll |
| **Tablet** | `900px - 1100px` | Fixed slim sidebar | 2 columns for schedule & metric cards |
| **Desktop** | `≥ 1100px` | Full width persistent left sidebar (`240px`) | 3-4 column grid; full top navigation |
