from googletrans import Translator

translator =Translator()



##fn

def detect_lang(text:str) ->str:
    return translator.detect(text).lang


#any language to english
def translate_to_english(text:str) ->str:
    return translator.translate(text, dest="en").text


def translate_back(text:str, target:str)-> str:
    return translator.translate(text, dest=target).text