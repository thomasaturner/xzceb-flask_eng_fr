
"""translator instance, english to french, french to english functions"""
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']


authenticator = IAMAuthenticator('Cn6BpxJseLB7WhwhmGcilPLB_oFhX_0YslJgDm4oYH7I')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(
    'https://api.us-south.language-translator.watson.cloud.ibm.com/instances/43a69715-42ae-44a4-ab3d-0b61b916d98b'
)


def english_to_french(english_text):
    """translates english test to french text."""
    french_text = language_translator.translate(
        text = english_text,
        model_id='en-fr').get_result()

    return french_text.get('translations')[0].get('translation')


def french_to_english(french_text):
    """translates french text to english text."""
    english_text = language_translator.translate(
        text = french_text,
        model_id='fr-en').get_result()
    return english_text.get('translations')[0].get('translation')

