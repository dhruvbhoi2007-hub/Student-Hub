# -*- coding: utf-8 -*-
"""
Full compilation of Practicals 1 to 14 for ITUE203 Web Development Frameworks.
Generates:
  1. D26CE154_Practical_1-14_WDF.docx & .pdf
  2. D26CE154_Practical_7-14_WDF.docx & .pdf
"""
import os, sys, docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

SUB_DIR = os.path.dirname(os.path.abspath(__file__))
SCREENSHOTS_DIR = os.path.join(SUB_DIR, "screenshots")
EXTRACTED_DIR = os.path.join(SUB_DIR, "assets_extracted")

def set_cell_shading(cell, color_hex):
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color_hex}"/>')
    cell._tc.get_or_add_tcPr().append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def add_header_footer(doc, student_id="D26CE154", student_name="Dhruv Bhoi"):
    for s in doc.sections:
        s.top_margin = Inches(1.0)
        s.bottom_margin = Inches(1.0)
        s.left_margin = Inches(1.0)
        s.right_margin = Inches(1.0)
        
        # Header
        h = s.header
        p1 = h.paragraphs[0]
        p1.text = f"Student-ID: {student_id}"
        p1.runs[0].font.name = "Times New Roman"
        p1.runs[0].font.size = Pt(10)
        
        p2 = h.add_paragraph()
        r1 = p2.add_run(f"Student-Name: {student_name}")
        r1.font.name = "Times New Roman"
        r1.font.size = Pt(10)
        r2 = p2.add_run("\t\tITUE203 WDF")
        r2.font.name = "Times New Roman"
        r2.font.size = Pt(10)
        
        # Footer
        f = s.footer
        pf = f.paragraphs[0]
        pf.text = "CSPIT-CE"
        pf.runs[0].font.name = "Times New Roman"
        pf.runs[0].font.size = Pt(10)

def add_callout_box(doc, text, title=None, bg_color="F4F6F9", border_color="2E74B5"):
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    table.columns[0].width = Inches(6.5)
    cell = table.cell(0, 0)
    set_cell_shading(cell, bg_color)
    set_cell_margins(cell, top=120, bottom=120, left=180, right=180)
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(2)
    if title:
        rt = p.add_run(f"{title}\n")
        rt.bold = True
        rt.font.name = "Times New Roman"
        rt.font.size = Pt(11)
        rt.font.color.rgb = RGBColor(0x2E, 0x74, 0xB5)
    rc = p.add_run(text)
    rc.font.name = "Consolas" if "<?php" in text or "SELECT" in text or "<!DOCTYPE" in text else "Times New Roman"
    rc.font.size = Pt(9.5) if rc.font.name == "Consolas" else Pt(11)

def add_code_block(doc, code_str, caption=None):
    if caption:
        p_cap = doc.add_paragraph()
        p_cap.paragraph_format.space_before = Pt(6)
        p_cap.paragraph_format.space_after = Pt(2)
        r = p_cap.add_run(f"Listing: {caption}")
        r.italic = True
        r.bold = True
        r.font.name = "Times New Roman"
        r.font.size = Pt(10)
        r.font.color.rgb = RGBColor(0x55, 0x55, 0x55)
    
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    table.columns[0].width = Inches(6.5)
    cell = table.cell(0, 0)
    set_cell_shading(cell, "F8F9FA")
    set_cell_margins(cell, top=100, bottom=100, left=140, right=140)
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.line_spacing = 1.05
    run = p.add_run(code_str.strip())
    run.font.name = "Consolas"
    run.font.size = Pt(8.5)
    run.font.color.rgb = RGBColor(0x20, 0x20, 0x20)

def add_image_safe(doc, img_path, caption=None, width=Inches(6.0)):
    if not os.path.exists(img_path):
        print(f"Warning: image not found: {img_path}")
        return
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(6)
    p.paragraph_format.space_after = Pt(2)
    run = p.add_run()
    run.add_picture(img_path, width=width)
    if caption:
        p_cap = doc.add_paragraph()
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap.paragraph_format.space_before = Pt(2)
        p_cap.paragraph_format.space_after = Pt(8)
        r = p_cap.add_run(f"Figure: {caption}")
        r.italic = True
        r.font.name = "Times New Roman"
        r.font.size = Pt(9.5)
        r.font.color.rgb = RGBColor(0x66, 0x66, 0x66)

def add_qa(doc, q, a):
    pq = doc.add_paragraph()
    pq.paragraph_format.space_before = Pt(6)
    pq.paragraph_format.space_after = Pt(2)
    rq = pq.add_run(f"Q: {q}")
    rq.bold = True
    rq.font.name = "Times New Roman"
    rq.font.size = Pt(11)
    rq.font.color.rgb = RGBColor(0x1A, 0x3A, 0x5C)
    
    pa = doc.add_paragraph()
    pa.paragraph_format.space_before = Pt(0)
    pa.paragraph_format.space_after = Pt(6)
    pa.paragraph_format.left_indent = Inches(0.2)
    ra = pa.add_run(f"Ans: {a}")
    ra.font.name = "Times New Roman"
    ra.font.size = Pt(11)

def add_heading_styled(doc, text, level=1):
    h = doc.add_heading(text, level=level)
    h.paragraph_format.keep_with_next = True
    h.paragraph_format.space_before = Pt(12)
    h.paragraph_format.space_after = Pt(4)
    run = h.runs[0]
    run.font.name = "Times New Roman"
    if level == 1:
        run.font.size = Pt(15)
        run.font.color.rgb = RGBColor(0x2E, 0x74, 0xB5)
    elif level == 2:
        run.font.size = Pt(13)
        run.font.color.rgb = RGBColor(0x2E, 0x74, 0xB5)
    else:
        run.font.size = Pt(11.5)
        run.font.color.rgb = RGBColor(0x33, 0x33, 0x33)
    return h

print("Helper definitions loaded.")

