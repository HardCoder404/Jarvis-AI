import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import requests
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import cv2  # pip install opencv-python


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def playSongOnYouTube(song,autoplay=False):
    speak(f"Okay, playing {song} for you, sir")
    webbrowser.open(f"https://www.youtube.com/results?search_query={song}")
    time.sleep(2)
    # This part can be improved using Selenium for automatic click if needed
    speak("Here are the results. Please play the song.")

    if autoplay:
        webbrowser.open("https://www.youtube.com/results?search_query=Sajani+Re")  # Replace the link with actual song link



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning Prince!")
    elif 12 <= hour < 18:
        speak("Good Afternoon Prince!")
    else:
        speak("Good Evening Prince!")
    speak("I am Jarvis. How may I help you")

def takeCommand():
    # It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        speak("Sorry sir, I am not able to hear you, can you please repeat?")
        return "None"
    return query


def searchGoogle(query):
    speak(f"Searching {query} on Google, sir")
    webbrowser.open(f"https://www.google.com/search?q={query}")


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'open the camera' in query:
            speak("Opening the camera, sir")
            cap = cv2.VideoCapture(0)
            while True:
                ret, frame = cap.read()
                cv2.imshow('Camera', frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            cap.release()
            cv2.destroyAllWindows()
            
            
         # Logic for executing tasks based on query
        if 'how are you' in query:
            speak("I am good sir, how about you?")
            response = takeCommand()
            if any(word in response for word in ['good', 'fine', 'better', 'very good']):
                speak("Okay, nice to hear!")
            else:
                speak("I hope you have a good day!")

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'youtube' in query and 'open' in query:
            speak("Opening YouTube, sir")
            webbrowser.open("https://www.youtube.com/")

        elif 'hear' in query:
            speak("Yes sir, you are audible")
        
        elif 'instagram' in query and 'open' in query:
            speak("Opening YouTube, sir")
            webbrowser.open("https://www.instagram.com/")

        elif 'google' in query and 'open' in query:
            speak("Opening Google, sir")
            webbrowser.open("google.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"Sir, the time is {strTime}")

        elif 'play' in query:
            speak("Which would you like to hear sir?")
            song = takeCommand()
            playSongOnYouTube(song)

        elif 'how are you' in query:
            speak("I am good sir how about you")

        elif 'search' in query:
            search_query = query.replace("search", "").strip()
            searchGoogle(search_query)  

        elif 'wait' in query:
            speak("Okay sir, I am waiting")
            time.sleep(10)
            speak("Hello sir, I am back Is there anything else that i can help you")


        elif 'take rest' in query:
            speak("Okay sir, I am taking rest. See You!")
            exit()