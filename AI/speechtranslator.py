import os
import azure.cognitiveservices.speech as speechsdk

speech_key, service_region = 'f84de8017053449791ad68f7383671a9', 'eastus'
from_language, to_languages = 'en-US', ['de', 'en', 'it', 'pt', 'zh-Hans']


def translate_speech_to_text():
    translation_config = speechsdk.translation.SpeechTranslationConfig(
        subscription=speech_key, region=service_region)

    translation_config.speech_recognition_language = from_language
    for lang in to_languages:
        translation_config.add_target_language(lang)

    recognizer = speechsdk.translation.TranslationRecognizer(
        translation_config=translation_config)

    print('Say something...')
    result = recognizer.recognize_once()
    synthesize_translations(result=result)


def synthesize_translations(result):
    language_to_voice_map = {
        "de": "de-DE-KatjaNeural",
        "en": "en-US-AriaNeural",
        "it": "it-IT-ElsaNeural",
        "pt": "pt-BR-FranciscaNeural",
        "zh-Hans": "zh-CN-XiaoxiaoNeural"
    }
    print(f'Recognized: "{result.text}"')

    for language in result.translations:
        translation = result.translations[language]
        print(f'Translated into "{language}": {translation}')

        speech_config = speechsdk.SpeechConfig(
            subscription=speech_key, region=service_region)
        speech_config.speech_synthesis_voice_name = language_to_voice_map.get(
            language)

        audio_config = speechsdk.audio.AudioOutputConfig(
            filename=f'{language}-translation.wav')
        speech_synthesizer = speechsdk.SpeechSynthesizer(
            speech_config=speech_config, audio_config=audio_config)
        speech_synthesizer.speak_text_async(translation).get()


translate_speech_to_text()
