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
import wikipedia
import wolframalpha
import time
import datetime




def speak(text):
	tts = gTTS(text=text, lang='en')
	filename = "voice.mp3"
	tts.save(filename)
	playsound.playsound(filename)
   
