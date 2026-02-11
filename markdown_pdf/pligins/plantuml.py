"""Plantunl plugin."""
from plantuml import PlantUML


def handler(params_dict, text, temp_files):
    """Translate plantunl marked text to png image."""
    url = params_dict.get("url")
    if not url:
        return "No value for 'url' key in plantuml plugin parameters: {}".format(params_dict)

    image = PlantUML(url=url).processes('\n'.join(text.splitlines()[1:-1]))
    file_name = temp_files.new_name("png")

    with open(file_name, mode='wb') as out:
        out.write(image)

    return "\n![PlantUML scheme]({})\n".format(file_name)
