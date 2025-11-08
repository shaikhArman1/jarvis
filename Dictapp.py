import os
import pyautogui
import webbrowser # type: ignore
import pyttsx3
from time import sleep

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",200)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
dictapp = {"commandprompt":"cmd","paint":"paint","word":"winword","excel":"excel","firefox":"firefox","vscode":"code", "powerpoint":"powerpnt"}

def openappweb(query):
    speak("In 3,2,1")
    if ".com" in query or ".co.in" in query or ".org" in query:
        query = query.replace("open","")
        query = query.replace("jarvis","")
        query = query.replace("launch","")
        query = query.replace(" ","")
        webbrowser.open(f"https://wwww.{query}")
    
    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"start {dictapp[app]}")
                
def closeappweb(query):
    speak("Closing, Sir")
    if "one tab" in query or "1 tab" in query:
        pyautogui.hotkey("ctrl","w")
    elif "2 tabs" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("Done!")
    elif "3 tabs" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("Done!")
        
    else:
        keys = list(dictapp.keys)
        for app in keys:
            if app in query:
                os.system(f"taskkill /f /im {dictapp[app]}.exe")
                
                
                
        
        
                