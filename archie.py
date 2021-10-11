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
import ctypes
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
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

        try:
            statement = r.recognize_google(audio, language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
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
            if 'wikipedia' in statement:
                speak('Searching Wikipedia...')
                statement = statement.replace("wikipedia", "")
                statement = statement.replace("search", "")
                results = wikipedia.summary(statement, sentences=3)
                speak("According to Wikipedia")
                print(results)
                speak(results)

            elif 'start' in statement:
                statement = statement.replace("start", "")
                statement = statement.replace(" ", "")
                TheApp = statement.capitalize()
                os.startfile('C:\\Users\\cryptoBLD\\Desktop\\applications\\' + TheApp)

            elif 'open' in statement:
                term = statement.replace('open', '')
                webbrowser.open_new_tab(f"https://www.{term}.com")
                speak(f"Opening {term} now")

            elif 'what can you do' in statement:
                speak("I have multiple capabilities like opening various Webpages, starting applications, searching "
                      "the web")

            elif 'who created you' in statement:
                speak("my creator is crypto blade, i will open his github page for you")
                webbrowser.open_new_tab("https://www.github.com/cryptoBLD")

            elif 'google' in statement:
                statement = statement.replace('google', '')
                term = statement
                speak(f"Opening {term} now")
                webbrowser.open_new_tab(statement)

            elif "weather" in statement:
                api_key = "16c80670876ad902383b30fbcd0f867d"
                base_url = "https://api.openweathermap.org/data/2.5/weather?"
                speak("what is the city name")
                city_name = takeCommand()
                complete_url = base_url + "appid=" + api_key + "&q=" + city_name
                response = requests.get(complete_url)
                x = response.json()
                if x["cod"] != "404":
                    y = x["main"]
                    current_temperature = y["temp"]
                    current_humidiy = y["humidity"]
                    z = x["weather"]
                    weather_description = z[0]["description"]
                    speak(" Temperature in kelvin unit is " +
                          str(current_temperature) +
                          "\n humidity in percentage is " +
                          str(current_humidiy) +
                          "\n description  " +
                          str(weather_description))
                    print(" Temperature in kelvin unit = " +
                          str(current_temperature) +
                          "\n humidity (in percentage) = " +
                          str(current_humidiy) +
                          "\n description = " +
                          str(weather_description))

                elif 'logout' in statement:
                    speak('logging you out')
                    ctypes.windll.user32.LockWorkStation()

                elif "shutdown" in statement:
                    speak("Shutting down your pc")
                    os.system('shutdown /p /f')

        else:
            continue
