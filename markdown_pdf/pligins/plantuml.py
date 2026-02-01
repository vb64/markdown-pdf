"""Plantunl plugin."""
import tempfile
from plantuml import PlantUML


def handler(params_dict, text, temp_files):
    """Translate plantunl marked text to png image."""
    url = params_dict.get("url")
    if not url:
        return "No value for 'url' key in plantuml plugin paremeters: {}".format(params_dict)

    text = '\n'.join(text.splitlines()[1:-1])
    server = PlantUML(url=url)
    image = server.processes(text)
    file_name = ''

    with tempfile.NamedTemporaryFile(mode='wb', delete=False, suffix=".png") as tmp_file:
        file_name = tmp_file.name
        temp_files.append(file_name)
        tmp_file.write(image)

    return "\n![Image]({})\n".format(file_name)
