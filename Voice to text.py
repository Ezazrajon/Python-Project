




import speech_recognition as sr
import pyautogui
import time
import pyttsx3
import pywhatkit

poltu = pyttsx3.init("sapi5")
voices = poltu.getProperty("voices")
poltu.setProperty("voice", voices[1].id)
poltu.runAndWait()

def mic():
    python = sr.Recognizer()
    with sr.Microphone() as m:
        print("Listening...")
        sound = python.listen(m)
        try:
            qu = python.recognize_google(sound, language="en-in")
            print(qu)
            return qu.lower()
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that.")
            return ""
        except sr.RequestError:
            print("Sorry, I'm unable to access the Google API.")
            return ""

while True:
    command = mic()
    time.sleep(1)
    if command:
        pyautogui.typewrite(command)
        time.sleep(1)
        pyautogui.press('enter')





