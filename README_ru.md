# markdown-pdf

[На английском](README.md)

Бесплатный, с открытым исходным кодом Python модуль `markdown-pdf` позволит создать PDF файл из вашего контента в формате `markdown`.

При создании PDF файла вы можете:

- Использовать в `markdown` текст на любом языке в кодировке `UTF-8`
- Встраивать используемые в `markdown` картинки
- Разбивать текст на страницы в нужном порядке
- Создавать оглавление (bookmarks) из заголовков markdown
- Оформлять нужные элементы при помощи вашего CSS кода

Модуль реализован как надстройка над двумя замечательными библиотеками.

- [markdown-it-py](https://github.com/executablebooks/markdown-it-py) для преобразования `markdown` в `html`.
- [PyMuPDF](https://github.com/pymupdf/PyMuPDF) для преобразования `html` в `pdf`.

## Установка

```bash
pip install markdown-pdf
```

## Использование

Создаем pdf с оглавлением (bookmarks) из заголовков до 2 уровня.

```python
from markdown_pdf import MarkdownPdf

pdf = MarkdownPdf(toc_level=2)
```

Добавляем в pdf три секции markdown.
Каждая секция начинается с новой страницы.
Заголовки из первой секции не включаем в оглавление.
Заголовок второй секции центрируется при помощи CSS и на страницу встраивается изображение из файла `img/python.png`.

```python
from markdown_pdf import Section

pdf.add_section(Section("# Title\n", toc=False))
pdf.add_section(
  Section("# Head1\n\n![python](img/python.png)\nbody\n"),
  user_css="h1 {text-align:center;}"
)
pdf.add_section(Section("## Head2\n\n### Head3\n\n"))
```

Устанавливаем свойства pdf документа.

```python
pdf.meta["title"] = "Руководство пользователя"
pdf.meta["author"] = "Виталий Богомолов"
```

Сохраняем в файл.

```python
pdf.save("guide.pdf")
```

![Pdf](img/with_toc.png)

Класс `Section` задает порцию данных `markdown`, которые обрабатываются по единым правилам.
Данные следующего `Section` начинаются с новой страницы.

У класса `Section` можно задавать следующие атрибуты.

- toc: нужно ли включать заголовки `<h1>` - `<h6>` этой секции в TOC. По умолчанию True.
- root: имя корневого каталога, от которого начинаются пути файлов картинок в markdown. По умолчанию ".".
- paper_size: название размера бумаги, [как описано здесь](https://pymupdf.readthedocs.io/en/latest/functions.html#paper_size). По умолчанию "A4".
- borders: размер полей. По умолчанию (36, 36, -36, -36).

Для присвоения доступны следующие свойства документа (словарь `MarkdownPdf.meta`) с указанными значениями по умолчанию.

- `creationDate`: текущая дата
- `modDate`: текущая дата
- `creator`: "PyMuPDF library: https://pypi.org/project/PyMuPDF"
- `producer`: ""
- `title`: ""
- `author`: ""
- `subject`: ""
- `keywords`: ""
