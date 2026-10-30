# Practical 1 & 13: REST-Style Route Plan & API Specifications

**Student-ID:** D26CE154  
**Student-Name:** Dhruv Bhoi  
**Department:** CSPIT-CE, Faculty of Technology and Engineering (FTE)  
**Subject:** Web Development Frameworks (ITUE203) — Semester 3, 2026-27 (ODD)  
**Institution:** CHAROTAR UNIVERSITY OF SCIENCE AND TECHNOLOGY (CHARUSAT)  

---

## 1. REST Architecture Principles Applied
The StudentHub backend exposes both traditional web application routes and asynchronous JSON endpoints following standard REST conventions:
- Predictable URI routing paths.
- Proper HTTP verbs (`GET`, `POST`).
- Appropriate HTTP response status codes (`200 OK`, `201 Created`, `400 Bad Request`, `401 Unauthorized`, `403 Forbidden`, `404 Not Found`, `422 Unprocessable Entity`, `500 Internal Server Error`).
- Secure header enforcement (`Content-Type: application/json; charset=utf-8`, CSRF protection token).

---

## 2. API Endpoints Specification

### 1. List / Search Events
- **Route:** `GET /api/events.php`
- **Access Level:** Authenticated Users (Student, Admin)
- **Query Parameters:**
  - `q` *(optional, string)*: Search substring matched against `title`, `venue`, or `category`.
- **Response Format:**
```json
{
  "success": true,
  "data": [
    {
      "id": 1,
      "title": "HackCharusat",
      "category": "Technical",
      "event_date": "2026-11-03",
      "venue": "Seminar Hall A",
      "status": "open"
    }
  ]
}
```
- **Status Codes:** `200 OK`, `401 Unauthorized`.

---

### 2. Create Event (Asynchronous)
- **Route:** `POST /api/events.php`
- **Access Level:** Admin Only
- **Headers Required:**
  - `Content-Type: application/json`
  - `X-CSRF-Token: <token>`
- **Request Body Payload:**
```json
{
  "action": "create",
  "title": "Full-Stack Web Summit",
  "category": "Technical",
  "event_date": "2026-12-15",
  "venue": "Audi 1",
  "status": "open"
}
```
- **Success Response:**
```json
{
  "success": true,
  "message": "Event created.",
  "id": 19
}
```
- **Status Codes:** `201 Created`, `400 Bad Request`, `403 Forbidden`, `422 Unprocessable Entity`.

---

### 3. Update Event (Asynchronous)
- **Route:** `POST /api/events.php`
- **Access Level:** Admin Only
- **Headers Required:**
  - `Content-Type: application/json`
  - `X-CSRF-Token: <token>`
- **Request Body Payload:**
```json
{
  "action": "update",
  "id": 19,
  "title": "Full-Stack Web Summit 2026",
  "category": "Technical",
  "event_date": "2026-12-18",
  "venue": "Audi 2",
  "status": "open"
}
```
- **Success Response:**
```json
{
  "success": true,
  "message": "Event updated."
}
```
- **Status Codes:** `200 OK`, `400 Bad Request`, `403 Forbidden`, `422 Unprocessable Entity`.

---

### 4. Delete Event (Asynchronous)
- **Route:** `POST /api/events.php`
- **Access Level:** Admin Only
- **Headers Required:**
  - `Content-Type: application/json`
  - `X-CSRF-Token: <token>`
- **Request Body Payload:**
```json
{
  "action": "delete",
  "id": 19
}
```
- **Success Response:**
```json
{
  "success": true,
  "message": "Event deleted."
}
```
- **Status Codes:** `200 OK`, `403 Forbidden`, `404 Not Found`, `422 Unprocessable Entity`.

---

## 3. Web Application Route Plan
| Method | Route | Description | Auth Required |
|---|---|---|:---:|
| `GET` | `/index.php` | Landing page with hero, carousel & modal | Public |
| `GET` | `/about.php` | About university & project | Public |
| `GET` | `/faq.php` | Interactive FAQ accordion | Public |
| `GET/POST`| `/contact.php` | Contact inquiry form with CSV storage | Public |
| `GET/POST`| `/feedback.php`| User feedback rating form with JSON storage | Public |
| `GET` | `/events.php` | Catalog powered by `data/events.json` | Public |
| `GET` | `/directory.php`| Profiles powered by `data/students.json` | Public |
| `GET/POST`| `/register.php`| Registration with client & server validation | Public |
| `GET/POST`| `/login.php` | Login session creation & remember cookie | Public |
| `GET` | `/logout.php` | Session destroy & cookie revocation | Authenticated |
| `GET/POST`| `/dashboard.php`| Student personal event registrations | Student |
| `GET/POST`| `/profile.php` | Self-profile update form | Authenticated |
| `GET` | `/api-demo.php`| Live AJAX event management interface | Authenticated |
| `GET/POST`| `/students.php`| Admin student CRUD, soft-delete & CSV export | Admin |
| `GET/POST`| `/manage_events.php` | Admin event CRUD with poster upload | Admin |
| `GET/POST`| `/admin/dashboard.php`| Metrics, charts, user toggle | Admin |
| `GET` | `/admin/audit.php` | System audit activity log | Admin |
| `GET` | `/db-test.php` | Database connection & schema test harness | Public / Dev |

