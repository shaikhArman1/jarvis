import pyttsx3
import speech_recognition 
import requests
from bs4 import BeautifulSoup
import datetime  # type: ignore
import random # type: ignore
import webbrowser # type: ignore

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",200)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("Understanding..")
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            from GreetMe import greetMe
            greetMe()
            
            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("Ok sir, I'm here when you need me!")
                    break
                
                elif "sab" in query:
                    speak("yes sir how are you?")
                elif "i am fine" in query:
                    speak("that's great sir")
                elif "how are you" in query:
                    speak("When did you start to care about me?")
                elif "thank you" in query:
                    speak("you're welcome sir!")
                    
                
                    
                elif "open" in query:
                    from Dictapp import openappweb
                    openappweb(query)
                elif "close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)
                    
                    
                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)
                    
                elif "calculate" in query:
                    from Calculatenumbers import Wolframalpha
                    from Calculatenumbers import Calc
                    query = query.replace("calculate","")
                    query = query.replace("jarvis","")
                    Calc(query)
                
                
                elif "temperature" in query:
                    search = "temperature in kolkata"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ ="BNeawe").text
                    speak(f"current{search} is {temp}")
                    
                elif "weather" in query:
                    search = "weather in kolkata"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")
                    
                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")    
                    speak(f"It's {strTime}")
                
                elif "music" in query:
                    speak("Playing your favourite songs")
                    a = (1,2,3)
                    b = random.choice(a)
                    if b==1:
                        webbrowser.open("https://music.youtube.com/watch?v=mz7AFVEco4o&si=mBDZKx4G5RlzM25h&t=74")
                    elif b==2:
                        webbrowser.open("https://youtu.be/3ly6_w9uAkw?si=yTFz5jBAC2hs8QVm&t=35")
                    elif b==3:
                        webbrowser.open("https://music.youtube.com/watch?v=5U5Ru0nTiUM&si=IVl5UEIr4_GDOVIY&t=6")
                    
                elif "distracted" in query:
                    speak("I know what you need sir!")
                    webbrowser.open("https://www.youtube.com/watch?v=22oJCkJ00UU&list=PLBij-QDR_3cP1VvbCB3O3GeUJc8o3R3Kv&index=40")
                
                elif "message" in query:
                    speak("Sure opening WhatsApp")
                    webbrowser.open("https://web.whatsapp.com/")
                
                elif "physics" in query:
                    speak("Sure, here are the lectures you might need")
                    webbrowser.open("https://www.youtube.com/playlist?list=PLBij-QDR_3cNa32HG4MDXqL3AMRO9pM6C")
                    
                elif "design" in query:
                    speak("launching designing interface")
                    webbrowser.open("https://www.canva.com/")
                    
                elif "question" in query:
                    speak("Sir Im a bit Dumb, launching chai GPT for you!")
                    webbrowser.open("https://chat.openai.com/")
                
                elif "screenshot" in query:
                     import pyautogui 
                     im = pyautogui.screenshot()
                     im.save("ss.jpg")
                
                elif "finally sleep" in query:
                    speak("Ok sir! bye")
                    exit()
                    
                
        
                
                    
                    