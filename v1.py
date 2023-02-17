import speech_recognition as sr
import time
import pyttsx3
import name

r = sr.Recognizer()
engine = pyttsx3.init()

with sr.Microphone() as source:
    print("Speak now...")
    audio = r.listen(source, timeout=5, phrase_time_limit=5)
    print("Processing")
    said=r.recognize_google(audio)
    said=str(said)
try:
    print("You said: " + said)
    engine.say(said)
    engine.runAndWait()

except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
