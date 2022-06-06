import azure.cognitiveservices.speech as speechsdk


def recognize_from_mic():
    # Find your key and resource region under the 'Keys and Endpoint' tab in your Speech resource in Azure Portal
    # Remember to delete the brackets <> when pasting your key and region!
    speech_config = speechsdk.SpeechConfig(
        subscription="f84de8017053449791ad68f7383671a9", region="eastus")
    speech_config.speech_recognition_language = "zh-CN"

    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
    speech_recognizer = speechsdk.SpeechRecognizer(
        speech_config=speech_config, audio_config=audio_config)

    # Asks user for mic input and prints transcription result on screen
    print("Speak into your microphone.")
    speech_recognition_result = speech_recognizer.recognize_once_async().get()

    if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print("Recognized: {}".format(speech_recognition_result.text))
    elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
        print("1. No speech could be recognized: {}".format(
            speech_recognition_result.no_match_details))
    elif speech_recognition_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_recognition_result.cancellation_details
        print("2. Speech Recognition canceled: {}".format(
            cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("3. Error details: {}".format(
                cancellation_details.error_details))
            print("4. Did you set the speech resource key and region values?")
    print(speech_recognition_result.text)


recognize_from_mic()
