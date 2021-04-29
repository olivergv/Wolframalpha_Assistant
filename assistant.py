import subprocess
import pyttsx3 
import json
import random
import speech_recognition as sr
import os
import time
import webbrowser
import smtplib
from gtts import gTTS
import playsound
import pyaudio
import wolframalpha
import time




def speak(text):
	tts = gTTS(text=text, lang='en')
	filename = "voice.mp3"
	tts.save(filename)
	playsound.playsound(filename)
	

def takeCommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language ='en-in')
        print("you said"+ query)

    except Exception as e:
        print(e)
        print("Unable to Recognizing your voice.")
        return "None"

    return query



while True:
	
	query = takeCommand()
	client = 'WJU3L2-QAGA3PJGEU'
	question = query
        client = wolframalpha.Client('WJU3L2-QAGA3PJGEU')
        res = client.query(question)
        answer = next(res.results).text
        speak(answer)
	print(answer)
