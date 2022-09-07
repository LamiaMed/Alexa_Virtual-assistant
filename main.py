import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()
#To resolve ALSA error in Linux
listener.energy_threshold = 420
listener.dynamic_energy_threshold = True

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say("Hello! It's Alexa")
engine.say("What can i do for you")
engine.runAndWait()
try:
    with sr.Microphone() as source :
        print("Listening...")
        voice = listener.listen(source)
        command= listener.recognize_google(voice)
        command = command.lower()
        if 'alexa' in command:
           
            print(command)

    
except:
   pass #not do anything when exception happens
