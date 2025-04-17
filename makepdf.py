import sys
from markdown_pdf import MarkdownPdf, Section

pdf = MarkdownPdf(toc_level=4, optimize=True)
pdf.add_section(Section(open(sys.argv[1], encoding='utf-8').read()))
pdf.meta["title"] = "MarkdownPdf module"
pdf.save(sys.argv[2])
