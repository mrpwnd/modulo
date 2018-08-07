#!/bin/bash

########################################
# This will install necessary packages #
########################################

# set up bash to handle errors more aggressively - a "strict mode" of sorts
  set -e
  set -u
  set -o

  pip install pyaudio

  pip install SpeechRecognition
  #test if all packages are installed
  python tests/test.py
