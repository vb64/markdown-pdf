# markdown-pdf

Это маленький класс Python, связывающий две библиотеки: [markdown-it-py](https://github.com/executablebooks/markdown-it-py) и [PyMuPDF](https://github.com/pymupdf/PyMuPDF).
Он позволит создать PDF файл из вашего набора файлов markdown.

## Установка

```bash
pip install markdown-pdf
```

## Использование

```python
from markdown_pdf import Section, MarkdownPdf

pdf = MarkdownPdf(toc_level=2)

pdf.add_section(Section("# Title\n", toc=False))
pdf.add_section(Section("# Head1\n\nbody\n"))
pdf.add_section(Section("## Head2\n\n### Head3\n\n"))

pdf.save("with_toc.pdf")
```

![Pdf](img/with_toc.png)

Класс `Section` задает порцию данных `markdown`, которые обрабатываются по единым правилам.
Данные следующего `Section` начинаются с новой страницы.

У класса `Section` можно задавать следующие атрибуты.

-   toc: нужно ли включать заголовки `<h1>` - `<h6>` этой секции в TOC. По умолчанию True.
-   root: имя корневого каталога, от которого начинаются пути файлов картинок в markdown. По умолчанию ".".
-   paper_size: название размера бумаги, [как описано здесь](https://pymupdf.readthedocs.io/en/latest/functions.html#paper_size). По умолчанию "A4".
-   borders: размер полей. По умолчанию (36, 36, -36, -36).
