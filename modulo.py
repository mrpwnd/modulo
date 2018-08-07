from model import mdl as md

import logging as log
import speech_recognition as sr

log = log.getLogger(__name__)

GOOGLE_SPEECH_RECOGNITION_API_KEY = None

def transcription():
    rec = sr.Recognizer()
    with sr.Microphone() as source:

        while True:
            log.debug("Waiting for input ...")
            audio = rec.listen(source)

            log.debug("Transcription taking place, please wait.")

            try:
                result = rec.recognize_google(audio, key=GOOGLE_SPEECH_RECOGNITION_API_KEY)
                md.handle_action(result)
            except rec.UnknownValueError:
                log.debug("Could not understand audio.")
            except rec.RequestError as error:
                log.warn("Something went wrong: %s", error)
            except Exception as exc:
                log.error("Could not process: %s", exc)

def main():
    FORMAT = '%(asctime)s %(levelname)s %(message)s'
    log.basicConfig(level=log.DEBUG, format=FORMAT, filename='model.log', filemode='w')

    transcription()

if __name__ == '__main__':
    main()
