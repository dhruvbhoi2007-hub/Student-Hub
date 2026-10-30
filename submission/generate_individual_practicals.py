# -*- coding: utf-8 -*-
"""
Generates individual submission documents (DOCX and PDF) for each of Practicals 1 to 14.
Stored in: d:/Dhruv/Degree/wdf/studenthub/submission/individual_practicals/
Format:
  - Practical-1.docx / Practical-1.pdf (and D26CE154_Practical_1.docx / .pdf)
  - ... up to Practical-14.docx / Practical-14.pdf
"""

import os, sys, shutil, docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT

import generate_full_reports as gfr
from build_helpers import (
    SUB_DIR, SCREENSHOTS_DIR, EXTRACTED_DIR,
    add_header_footer, add_callout_box, add_code_block,
    add_image_safe, add_qa, add_heading_styled, set_cell_shading, set_cell_margins
)

INDIV_DIR = os.path.join(SUB_DIR, "individual_practicals")
os.makedirs(INDIV_DIR, exist_ok=True)

PRACTICAL_INFO = {
    1: {
        "title": "Practical 1: Project Initiation, Requirement Analysis, Sitemap, Wireframe, and GitHub Setup",
        "func": gfr.add_practical_1,
        "conclusion": "Successfully initiated the StudentHub campus portal. The problem definition, functional and non-functional requirements, user roles (Student, Admin, Guest), modular hierarchical sitemap, low-fidelity wireframes, structured directory layout, and GitHub version control repository were successfully established."
    },
    2: {
        "title": "Practical 2: Semantic HTML5 Pages with Accessibility-Ready Structure",
        "func": gfr.add_practical_2,
        "conclusion": "Successfully developed semantic, accessible HTML5 page skeletons for all 14 core modules of StudentHub (exceeding the syllabus requirement of 10). Implemented WAI-ARIA landmarks, keyboard skip links, accessible form labels, and live status regions."
    },
    3: {
        "title": "Practical 3: Responsive UI Design using CSS Grid, Flexbox, and Modern SaaS Theme",
        "func": gfr.add_practical_3,
        "conclusion": "Engineered a modern, responsive user interface utilizing CSS Grid, Flexbox, media queries, and CSS variables. Redesigned the portal to match the Acade SaaS dashboard theme, featuring timetable schedule cards, circular SVG progress rings, a notice feed, and mobile off-canvas drawer navigation."
    },
    4: {
        "title": "Practical 4: JavaScript DOM Manipulation, Event Handling, and UI Interactivity",
        "func": gfr.add_practical_4,
        "conclusion": "Implemented rich client-side interactivity using Vanilla ES6+ JavaScript. Features include persistent dark/light theme switching via localStorage, accessible FAQ accordion panels, modal dialog popups with focus traps, and animated highlight sliders."
    },
    5: {
        "title": "Practical 5: Registration Form with Frontend Validation and User-Friendly Error Handling",
        "func": gfr.add_practical_5,
        "conclusion": "Constructed a comprehensive user registration form with real-time regular expression validation, dynamic password strength meter (entropy evaluation), visual error indicators, and procedural HTML5 Canvas CAPTCHA generation."
    },
    6: {
        "title": "Practical 6: Rendering External JSON Data using Fetch API, Search, and Filter",
        "func": gfr.add_practical_6,
        "conclusion": "Leveraged the Fetch API and Async/Await to fetch, parse, and render external JSON datasets for Events and the Student Directory. Implemented debounced text search, category filters, dependent State-City cascading dropdowns, multi-field sorting, and client-side pagination."
    },
    7: {
        "title": "Practical 7: PHP Form Processing with Server-Side Validation and CSV/JSON File Storage",
        "func": gfr.add_practical_7,
        "conclusion": "Implemented secure server-side PHP form processing for contact inquiries and student feedback. Applied rigorous data sanitization, anti-CSRF token verification, and atomic file persistence using fputcsv with exclusive locks (LOCK_EX) and JSON encoding."
    },
    8: {
        "title": "Practical 8: MySQL Schema Design, ER Model, Database Connectivity, and Diagnostics",
        "func": gfr.add_practical_8,
        "conclusion": "Designed a normalized (3NF) relational database schema for StudentHub across 6 tables and 2 stored procedures. Configured dual PDO and MySQLi database drivers with UTF-8MB4 encoding and verified connectivity through an automated 6-point diagnostic test suite (db-test.php)."
    },
    9: {
        "title": "Practical 9: Secure User Registration with Database Insert, Duplicate Email Check, and Password Hashing",
        "func": gfr.add_practical_9,
        "conclusion": "Engineered an enterprise user registration pipeline featuring server-side regex validation, duplicate email verification queries, cryptographically secure Bcrypt password hashing (password_hash), and ACID database transactions with rollback capabilities."
    },
    10: {
        "title": "Practical 10: Secure Login/Logout with Sessions, Role-Based Access, Timeout, and Remember-Me Token",
        "func": gfr.add_practical_10,
        "conclusion": "Implemented secure user authentication utilizing PHP sessions, session fixation countermeasures (session_regenerate_id), 15-minute inactivity timeouts, role-based access control (RBAC), and split-token remember-me persistent cookies with SHA-256 database hashing."
    },
    11: {
        "title": "Practical 11: Student Management CRUD with Search, Filter, Pagination, Soft Delete, and CSV Export",
        "func": gfr.add_practical_11,
        "conclusion": "Developed full administrative Student Management CRUD operations utilizing MySQLi prepared statements. Implemented multi-field search, course filtering, LIMIT/OFFSET pagination, non-destructive soft delete/restore mechanisms, and streaming CSV export."
    },
    12: {
        "title": "Practical 12: Event Management CRUD with Poster Upload and File Validation",
        "func": gfr.add_practical_12,
        "conclusion": "Built an Event Management administrative CRUD interface with secure file upload handling. Implemented MIME magic-byte verification (finfo), 2MB file size restrictions, cryptographic filename randomization, and path traversal mitigations."
    },
    13: {
        "title": "Practical 13: PHP JSON API and AJAX/Fetch-Based CRUD without Page Reload",
        "func": gfr.add_practical_13,
        "conclusion": "Constructed a RESTful PHP JSON API endpoint (api/events.php) and built a Single-Page Application (SPA) client interface (api-demo.php). Integrated asynchronous Fetch CRUD operations, custom X-CSRF-Token headers, and dynamic DOM rendering without full page reloads."
    },
    14: {
        "title": "Practical 14: Admin Dashboard with Role-Based Access Control, Dynamic Menu, and Audit Log",
        "func": gfr.add_practical_14,
        "conclusion": "Developed an executive Admin Dashboard featuring real-time KPI metric calculation, stored procedure execution (sp_registrations_by_month) with CSS bar charts, user active/inactive toggles, and an immutable security audit trail (admin/audit.php)."
    }
}

def add_individual_title_block(doc, p_num, p_info):
    p_inst = doc.add_paragraph()
    p_inst.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_inst.paragraph_format.space_before = Pt(0)
    p_inst.paragraph_format.space_after = Pt(2)
    
    r_uni = p_inst.add_run("CHAROTAR UNIVERSITY OF SCIENCE AND TECHNOLOGY (CHARUSAT)\n")
    r_uni.bold = True
    r_uni.font.name = "Times New Roman"
    r_uni.font.size = Pt(13)
    r_uni.font.color.rgb = RGBColor(0x1A, 0x3A, 0x5C)
    
    r_sub = p_inst.add_run("CSPIT — Department of Computer Engineering · ITUE203 Web Development Frameworks\n")
    r_sub.font.name = "Times New Roman"
    r_sub.font.size = Pt(10.5)
    
    # Metadata Table
    table = doc.add_table(rows=2, cols=4)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    table.columns[0].width = Inches(1.3)
    table.columns[1].width = Inches(2.2)
    table.columns[2].width = Inches(1.2)
    table.columns[3].width = Inches(1.8)
    
    cells_data = [
        [("Student Name", True), ("Dhruv Bhoi", False), ("Student ID", True), ("D26CE154", True)],
        [("Academic Year", True), ("2026–27 (ODD)", False), ("Semester", True), ("3rd Semester, B.Tech CE", False)]
    ]
    
    for r_idx, row in enumerate(cells_data):
        for c_idx, (text, is_bold) in enumerate(row):
            c = table.cell(r_idx, c_idx)
            set_cell_shading(c, "EEECFE" if is_bold else "FFFFFF")
            set_cell_margins(c, top=80, bottom=80, left=100, right=100)
            p = c.paragraphs[0]
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)
            r = p.add_run(text)
            r.bold = is_bold
            r.font.name = "Times New Roman"
            r.font.size = Pt(9.5)
            if is_bold and text in ["Student Name", "Student ID", "D26CE154"]:
                r.font.color.rgb = RGBColor(0x2E, 0x74, 0xB5)
                
    p_div = doc.add_paragraph()
    p_div.paragraph_format.space_before = Pt(4)
    p_div.paragraph_format.space_after = Pt(6)
    r_line = p_div.add_run("―" * 58)
    r_line.font.color.rgb = RGBColor(0x2E, 0x74, 0xB5)

def build_single_practical_docx(p_num):
    info = PRACTICAL_INFO[p_num]
    print(f"Generating Practical {p_num} DOCX: {info['title'][:50]}...")
    doc = docx.Document()
    add_header_footer(doc)
    add_individual_title_block(doc, p_num, info)
    
    # Call the content generator function
    info["func"](doc)
    
    # Add Conclusion section
    add_heading_styled(doc, f"Practical {p_num} Conclusion & Learning Outcomes", level=2)
    p_c = doc.add_paragraph(info["conclusion"])
    p_c.paragraph_format.space_before = Pt(4)
    p_c.paragraph_format.space_after = Pt(12)
    p_c.runs[0].font.name = "Times New Roman"
    p_c.runs[0].font.size = Pt(11)
    
    out_name = f"Practical-{p_num}.docx"
    out_path = os.path.join(INDIV_DIR, out_name)
    doc.save(out_path)
    
    # Also save with student ID prefix
    out_id_name = f"D26CE154_Practical_{p_num}.docx"
    shutil.copyfile(out_path, os.path.join(INDIV_DIR, out_id_name))
    
    print(f"Saved {out_name} & {out_id_name} ({os.path.getsize(out_path)} bytes)")
    return out_path

def convert_all_to_pdf():
    import win32com.client
    print("\nStarting batch PDF conversion via Microsoft Word...")
    word = win32com.client.Dispatch("Word.Application")
    word.Visible = False
    
    try:
        for p_num in range(1, 15):
            docx_name = f"Practical-{p_num}.docx"
            pdf_name = f"Practical-{p_num}.pdf"
            docx_path = os.path.join(INDIV_DIR, docx_name)
            pdf_path = os.path.join(INDIV_DIR, pdf_name)
            
            print(f"Converting Practical {p_num} to PDF...")
            wb = word.Documents.Open(os.path.abspath(docx_path))
            wb.SaveAs(os.path.abspath(pdf_path), FileFormat=17) # 17 = wdFormatPDF
            wb.Close()
            
            # Copy to student ID named PDF
            pdf_id_name = f"D26CE154_Practical_{p_num}.pdf"
            shutil.copyfile(pdf_path, os.path.join(INDIV_DIR, pdf_id_name))
            
            print(f" -> Generated {pdf_name} and {pdf_id_name} ({os.path.getsize(pdf_path)} bytes)")
    finally:
        word.Quit()
        print("Batch Word PDF conversion complete.")

if __name__ == "__main__":
    for p_num in range(1, 15):
        build_single_practical_docx(p_num)
        
    convert_all_to_pdf()
    print("\nAll 14 individual practical documents successfully generated and converted!")

