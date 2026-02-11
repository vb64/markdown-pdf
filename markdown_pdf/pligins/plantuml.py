"""Plantunl plugin."""
from plantuml import PlantUML
from .helpers import get_key


def handler(params_dict, text, temp_files):
    """Translate plantunl marked text to png image."""
    url = get_key(params_dict, 'url', 'http://www.plantuml.com/plantuml/img/')
    image = PlantUML(url=url).processes('\n'.join(text.splitlines()[1:-1]))
    file_name = temp_files.new_name("png")

    with open(file_name, mode='wb') as out:
        out.write(image)

    return "\n![PlantUML image]({})\n".format(file_name)
