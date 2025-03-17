# Module markdown-pdf

[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/vb64/markdown-pdf/pep257.yml?label=Pep257&style=plastic&branch=main)](https://github.com/vb64/markdown-pdf/actions?query=workflow%3Apep257)
[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/vb64/markdown-pdf/py3.yml?label=Python%203.8-3.13&style=plastic&branch=main)](https://github.com/vb64/markdown-pdf/actions?query=workflow%3Apy3)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/27b53043bff34f07bfb79ee1672b7ba0)](https://app.codacy.com/gh/vb64/markdown-pdf/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)
[![Codacy Badge](https://app.codacy.com/project/badge/Coverage/27b53043bff34f07bfb79ee1672b7ba0)](https://app.codacy.com/gh/vb64/markdown-pdf/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_coverage)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/markdown-pdf?label=pypi%20installs)](https://pypistats.org/packages/markdown-pdf)

The free, open source Python module `markdown-pdf` will create a PDF file from your content in `markdown` format.

When creating a PDF file you can:

- Use `UTF-8` encoded text in `markdown` in any language
- Embed images used in `markdown`
- Break text into pages in the desired order
- Create a TableOfContents (bookmarks) from markdown headings
- Tune the necessary elements using your CSS code
- Use different page sizes within single pdf
- Create tables in `markdown`

The module utilizes the functions of two great libraries.

- [markdown-it-py](https://github.com/executablebooks/markdown-it-py) to convert `markdown` to `html`.
- [PyMuPDF](https://github.com/pymupdf/PyMuPDF) to convert `html` to `pdf`.

## Installation

```bash
pip install markdown-pdf
```
