# Check the versions of libraries

#Python version
import sys
print('Python: {}'.format(sys.version))
#Logging version
import logging
print('Logging: {}'.format(logging.__version__))
#PyAudio version
import pyaudio
print('PyAudion: {}'.format(pyaudio.__version__))
#SpeechRecognition version
import speech_recognition
print('SpeechRecognition: {}'.format(speech_recognition.__version__))

print('Logs file name: {}'.format(logging.__file__))
