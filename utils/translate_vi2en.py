from googletrans import Translator

def translate_vi2en(text):
    translator = Translator()
    translation = translator.translate(text, src='vi', dest='en')
    return translation.text
