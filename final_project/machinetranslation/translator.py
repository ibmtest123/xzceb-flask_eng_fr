"""
Translates text from English to French and vice versa.
"""

from deep_translator import MyMemoryTranslator

def en_to_fr(english_text):
    """
    Translates from English to French
    """
    french_text = MyMemoryTranslator(source='en-US', target='fr-FR').translate(english_text)
    return french_text

def fr_to_en(french_text):
    """
    Translates from French to English
    """
    english_text = MyMemoryTranslator(source='fr-FR', target='en-US').translate(french_text)
    return english_text
