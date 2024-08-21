import speech_recognition as sr
import webbrowser
import pyttsx3 
import musicLibrary as ML

recognizer = sr.Recognizer()
engine = pyttsx3.init()

import musicLibrary as ml

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(command):
    if "open google" in command.lower():
        webbrowser.open("https://google.com")
    elif "open instagram" in command.lower():
        webbrowser.open("https://instagram.com")
    elif "open github" in command.lower():
        webbrowser.open("https://github.com")
    elif "open portfolio website" in command.lower():
        webbrowser.open("https://portfoliosiddharth.netlify.app")
    elif "open youtube" in command.lower():
        webbrowser.open("https://youtube.com")
    elif command.lower().startswith("play"):
        song = command.lower().split(" ")[1]
        link = ML.music[song]
        webbrowser.open(link)
    

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) 


engine.setProperty('rate', 150) 

engine.setProperty('volume', 1.0) 

if __name__ == "__main__":
    speak("Initializing Sid...")

    while True:
        r = sr.Recognizer()
        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source,timeout=3,phrase_time_limit=1)

            word = r.recognize_google(audio)
            if(word.lower() == "hello siri"):
                speak("Yes Sir")

            with sr.Microphone() as source:
                print("Siri Active... ")
                audio = r.listen(source)
                command = r.recognize_google(audio)

            processCommand(command)


        except Exception as e:
            print("Error:", e)



