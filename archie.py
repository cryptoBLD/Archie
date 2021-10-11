"""
Author: Yann Gaspoz
Date: 11/10/2021
Description: AI Desktop Assistant named Archie
"""

import speech_recognition as sr
import pyttsx3
import datetime
import pyaudio
import wikipedia
import webbrowser
import os
import time
import subprocess
import wolframalpha
import json
import requests

# Creating speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', 'voices[0].id')


# speak function to turn text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Hello,Good Morning Sir")
        print("Hello,Good Morning Sir")
    elif 12 <= hour < 18:
        speak("Hello,Good Afternoon Sir")
        print("Hello,Good Afternoon Sir")
    else:
        speak("Hello,Good Evening Sir")
        print("Hello,Good Evening Sir")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=5)
        audio = r.listen(source)

        try:
            statement = r.recognize_google(audio, language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement


print("Loading your AI personal assistant Archie")
speak("Loading your AI personal assistant Archie")
wishMe()

if __name__ == '__main__':

    while True:
        statement = takeCommand().lower()
        if statement == 0:
            continue

        # Wait until one says Archie
        if "archie" in statement:
            speak("Yes Sir")
            print("Yes Sir")
            statement = takeCommand().lower()

            # Commands go here



        else:
            continue
