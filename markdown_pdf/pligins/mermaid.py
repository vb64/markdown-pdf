"""Mermaid plugin."""
import base64
import requests


def handler(params_dict, text, temp_files):
    """Translate mermaid marked text to png image."""
    url = params_dict.get("url")
    if not url:
        return "No value for 'url' key in mermaid plugin parameters: {}".format(params_dict)

    text = '\n'.join(text.splitlines()[1:-1])
    response = requests.get(
      "{}{}".format(
        url,
        base64.urlsafe_b64encode(text.encode("utf-8")).decode("ascii"),
      ),
      params={"format": "png"},
      timeout=5
    )

    file_name = temp_files.new_name("png")
    with open(file_name, mode='wb') as out:
        out.write(response.content)

    return "\n![Mermaid scheme]({})\n".format(file_name)
