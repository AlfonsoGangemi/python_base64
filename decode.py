import base64
import re
import webbrowser

import pyperclip

encodedTag = pyperclip.paste()

encodedStr = re.sub(r"</?bytes>", "", encodedTag)
decodedStr = str(base64.b64decode(encodedStr), "utf-8")

with open("page.html", "w") as html_file:
    print(decodedStr, file=html_file)

webbrowser.get('firefox').open_new("page.html")

