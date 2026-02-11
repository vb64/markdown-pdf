"""Mermaid plugin."""
import base64
import requests

from .helpers import get_key


def handler(params_dict, text, temp_files):
    """Translate mermaid marked text to png image."""
    url = get_key(params_dict, 'url', 'https://mermaid.ink/img/')
    code = '\n'.join(text.splitlines()[1:-1])
    response = requests.get(
      "{}{}".format(
        url,
        base64.urlsafe_b64encode(code.encode("utf-8")).decode("ascii"),
      ),
      params={"format": "png"},
      timeout=5
    )

    file_name = temp_files.new_name(ext="png")
    with open(file_name, mode='wb') as out:
        out.write(response.content)

    return "\n![Mermaid image]({})\n".format(file_name)
