   
import speech_recognition as sr
import webbrowser
import pyttsx3

poltu=pyttsx3.init("sapi5")
import pywhatkit
voices=poltu.getProperty("voices")
poltu.setProperty("voice",voices[1].id)
poltu.runAndWait()
while True:
    def mic():
        python=sr.Recognizer()
        with sr.Microphone() as m:
            print("listening......")
            sound=python.listen(m)
            qu=python.recognize_google(sound,language=("en-in"))
            print(qu)
            return(qu.lower())
    com=mic()
    
    if"facebook"in com:
        poltu.say("ok,let me opening facebook")
        poltu.say("wait just a second,we are in facebook")
        poltu.runAndWait()
        webbrowser.open("facebook.com")
    
    if "weather"in com:
        poltu.say("location please, ")  
        poltu.runAndWait() 
        com=mic() 
        poltu.say("wait a second please")
        poltu.runAndWait()
        webbrowser.open(f"https://www.google.com/search?q={com}+weather+today")
    if"search"in com:
        poltu.say("what should i  search!") 
        
        poltu.runAndWait() 
        com=mic()
        if"youtube" in com:
          poltu.say("ok,opening youtube sir!!! which song do you want to litsen sirr!!?")
        poltu.runAndWait()
        
        com=mic() 
        pywhatkit.playonyt(com)