from translate import Translator
import os

from AppKit import NSPasteboard, NSStringPboardType
import pyperclip as pc

"""

  Python command line tool to make online translations

  Example:

       $ translate-cli -t zh the book is on the table
       碗是在桌子上。

  Available languages:

       https://en.wikipedia.org/wiki/ISO_639-1
       Examples: (e.g. en, ja, ko, pt, zh, zh-TW, ...)


"""

def notify(title, text):
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))


from_lang = 'autodetect'
to_lang = 'en'


pb = NSPasteboard.generalPasteboard()
pbstring = pb.stringForType_(NSStringPboardType)


translator = Translator(provider='microsoft', 
                        from_lang=from_lang,
                        to_lang=to_lang)


translation = translator.translate(pbstring)

notify("Translation", translation)