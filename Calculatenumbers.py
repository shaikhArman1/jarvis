import wolframalpha
import pyttsx3
import speech_recognition

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",200)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def Wolframalpha(query):
    apikey = "5T2HRR-PKQ7P347L9"
    requester = wolframalpha.Client(apikey)
    requested = requester.query(query)
    
    try:
        answer = next(requested.results).text
        return answer
    except:
        speak("the value is too weird sir!")

def Calc(query):
    Term = str(query)
    Term = Term.replace("jarvis", "")
    Term = Term.replace("what is", "")
    Term = Term.replace("plus", "")
    Term = Term.replace("minus", "")
    Term = Term.replace("into", "")
    Term = Term.replace("by", "")
    
    Final = str(Term)
    try:
        results = Wolframalpha(Final)
        print(f"{results}")
        speak(results)
        
    except:
        speak("The value is too weird")
    
    
    
    

