# markdown-pdf
[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/vb64/markdown-pdf/pep257.yml?label=Pep257&style=plastic&branch=main)](https://github.com/vb64/markdown-pdf/actions?query=workflow%3Apep257)
[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/vb64/markdown-pdf/py3.yml?label=Python%203.8-3.11&style=plastic&branch=main)](https://github.com/vb64/markdown-pdf/actions?query=workflow%3Apy3)

This is a small Python class that links two libraries: [markdown-it-py](https://github.com/executablebooks/markdown-it-py) and [PyMuPDF](https://github.com/pymupdf/PyMuPDF).
This class will create a PDF file from your set of `markdown` files.

## Installation

```bash
pip install markdown-pdf
```

## Usage

```python
from markdown_pdf import Section, MarkdownPdf

pdf = MarkdownPdf(toc_level=2)

pdf.add_section(Section("# Title\n", toc=False))
pdf.add_section(Section("# Head1\n\nbody\n"))
pdf.add_section(Section("## Head2\n\n### Head3\n\n"))

pdf.save("with_toc.pdf")
```

![Pdf](img/with_toc.png)

The `Section` class defines a portion of `markdown` data, which is processed according to the same rules.
The next `Section` data starts on a new page.

The `Section` class can set the following attributes.

-   toc: whether to include the headers `<h1>` - `<h6>` of this section in the TOC. Default is True.
-   root: the name of the root directory from which the image file paths starts in markdown. Default ".".
-   paper_size: name of paper size, [as described here](https://pymupdf.readthedocs.io/en/latest/functions.html#paper_size). Default "A4".
-   borders: size of borders. Default (36, 36, -36, -36).
