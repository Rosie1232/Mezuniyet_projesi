# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr


def record_speech():
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)


# recognize speech using Google Speech Recognition
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
    return r.recognize_google(audio)

