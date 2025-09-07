# from markdown import markdown
# from weasyprint import HTML
# from pathlib import Path

# STYLE = """
# <style>
# body { font-family: -apple-system, system-ui, "Segoe UI", Roboto, "Helvetica Neue", Arial; line-height:1.6; padding: 20px; }
# h1, h2, h3 { color: #222; }
# code, pre { font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; }
# blockquote { border-left: 4px solid #ddd; padding-left: 12px; color: #555; }
# table { border-collapse: collapse; width: 100%; }
# th, td { border: 1px solid #ddd; padding: 6px; text-align:left; }
# </style>
# """

# def md_to_pdf(md_text: str, out_pdf_path: str) -> str:
#     html = STYLE + markdown(md_text, extensions=["fenced_code", "tables", "toc"])
#     HTML(string=html).write_pdf(out_pdf_path)
#     return out_pdf_path
from markdown import markdown
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from pathlib import Path
import html2text

def md_to_pdf(md_text: str, out_pdf_path: str) -> str:
    # Convert markdown to plain text paragraphs
    text_maker = html2text.HTML2Text()
    text_maker.ignore_links = False
    text_content = text_maker.handle(markdown(md_text, extensions=["fenced_code", "tables", "toc"]))

    doc = SimpleDocTemplate(out_pdf_path, pagesize=A4)
    styles = getSampleStyleSheet()
    story = []

    for line in text_content.split("\n"):
        if line.strip():
            story.append(Paragraph(line, styles["Normal"]))
            story.append(Spacer(1, 12))

    doc.build(story)
    return out_pdf_path
