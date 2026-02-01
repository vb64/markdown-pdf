"""Plantunl plugin."""
from plantuml import PlantUML


def handler(params_dict, text, _temp_files):
    """Translate plantunl marked text to png image."""
    url = params_dict.get("url")
    if not url:
        return "No value for 'url' key in plantuml plugin paremeters: {}".format(params_dict)

    text = '\n'.join(text.splitlines()[1:-1])
    server = PlantUML(url=url)
    image = server.processes(text)

    return 'OK'
