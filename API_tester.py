import requests
from sub.constant import Constant


#  ? [key=<API-ключ>]
#  & [text=<переводимый текст>]
#  & [lang=<направление перевода>]
#  & [format=<формат текста>]
#  & [options=<опции перевода>]
#  & [callback=<имя callback-функции>]

def get_translate(lang_in, lang_out, text):
	"""

	:param lang_in: the language original
	:param lang_out: the target language
	:param text: text on original language
	:return: the translated text
	"""
	r = requests.post(f"{Constant.TRANSLATOR_REFERENCE}",
	                  data={
		                  "key": Constant.TRANSLATOR_API_KEY,
		                  "text": f'{text}',
		                  "lang": f'{lang_in}-{lang_out}',
		                  'format': 'plain',
		                  "options": '1'
	                  })
	return r.json()['text'][0]
