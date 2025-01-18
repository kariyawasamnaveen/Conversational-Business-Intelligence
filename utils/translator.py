from googletrans import Translator

class TranslatorUtility:
    def __init__(self):
        self.translator = Translator()

    def translate_to_sinhala(self, text):
        try:
            translated_text = self.translator.translate(text, src='en', dest='si').text
            return translated_text
        except Exception as e:
            print(f"Translation error: {e}")
            return text  # If translation fails, return the original text
