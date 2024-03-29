import os
from AppKit import NSPasteboard, NSStringPboardType
import pyperclip as pc
from googletrans import Translator

def notify(title, text):
    os.system(f"osascript -e 'display notification \"{title}\" with title \"{text}\"'")

# pip install googletrans==3.1.0a0

pb = NSPasteboard.generalPasteboard()
pbstring = pb.stringForType_(NSStringPboardType)

translator = Translator()
translation = translator.translate(pbstring).text

applescript = """
display dialog "
""" + translation + """" ¬
with title "This is a pop-up window" ¬
with icon caution ¬
buttons {"OK"}
"""

# os.system(f"osascript -e '{applescript}'")

pc.copy(translation)