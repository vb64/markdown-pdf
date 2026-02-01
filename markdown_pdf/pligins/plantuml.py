"""Plantunl plugin."""
import os
import tempfile
from plantuml import PlantUML


def handler(params_dict, text, temp_files):
    """Translate plantunl marked text to png image."""
    url = params_dict.get("url")
    if not url:
        return "No value for 'url' key in plantuml plugin parameters: {}".format(params_dict)

    text = '\n'.join(text.splitlines()[1:-1])
    server = PlantUML(url=url)
    image = server.processes(text)
    file_name = ''

    with tempfile.NamedTemporaryFile(mode='wb', delete=False, suffix=".png") as tmp_file:
        file_name = os.path.basename(tmp_file.name)
        temp_files.append(tmp_file.name)

    with open(file_name, mode='wb') as out:
        temp_files.append(file_name)
        out.write(image)

    return "\n![PlantUML scheme]({})\n".format(file_name)
