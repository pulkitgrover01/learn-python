import pyttsx3
import datetime
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
set_voice = engine.getProperty('voices')
engine.setProperty('voice', set_voice[0].id)
# print(set_voice[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning Sir!")

    elif 12 <= hour < 18:
        speak("Good Afternoon Sir!")

    else:
        speak("Good Evening Sir!")

    speak("I am Jarvis. How may i assist you.")

def takeCommand():
    #It takes speech commends from the users and return string inputs.
    r = sr.recognizers
    with sr.Microphone as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language= 'en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print("Say that again please.....")
        return "None"




if __name__ == "__main__":
    wishMe()
    # speak("How are you doing?")
    takeCommand()



