import os
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.us-east.language-translator.watson.cloud.ibm.com')
#languages = language_translator.list_languages().get_result()
#print(json.dumps(languages, indent=2))
#print("english text: ")
#english_text = input()
#print(type(english_text))

def english_to_french(english_text):
    if not english_text:
        english_text = None
        french_text = None
        return french_text
    else:
        french_text = language_translator.translate(text = english_text, model_id='en-fr').get_result()
        #print(json.dumps(frenchText, indent=2, ensure_ascii=False))
        return french_text

def french_to_english(french_text):
    if not french_text:
        french_text = None
        english_text = None
        return english_text
    else:
        english_text = language_translator.translate(text = french_text, model_id='fr-en').get_result()
        #print(json.dumps(englishText, indent=2, ensure_ascii=False))
        return english_text

#french = english_to_french(english_text)
#print(french['translations'][0]['translation'])
#english = french_to_english(french['translations'][0]['translation'])
#print(english['translations'][0]['translation'])
