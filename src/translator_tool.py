from langchain.agents import tool

from src.helper import detect_lang,translate_to_english,translate_back


@tool
def detect_language(text:str)  -> str:
    """Detects the language of the input text."""
    return detect_lang(text)

@tool
def translate_to_english(text:str) -> str:
    """translates the given input text to English."""

    return translate_to_english(text)

@tool
def translate_back(text:str) ->str:
    """Translates English output back to the user's original language."""
    return translate_back(text)

