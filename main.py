import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
#To resolve ALSA error in Linux
listener.energy_threshold = 1000
listener.dynamic_energy_threshold = True

engine = pyttsx3.init()
voices = engine.getProperty('voices')
#engine.setProperty('voice', 'english+f1')

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source :
            print("Listening...")
            voice = listener.listen(source)
            command= listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace("alexa","")
                print(command)

        
    except:
        pass #not do anything when exception happens

    return command

def run_Alexa():
    command = take_command()
    if 'play' in command: 
        song = command.replace("play","")
        talk('Playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        print(time)
        talk("Current time is : " + time)
    elif 'look for' in command:
        research = command.replace("look for", "")
        info = wikipedia.summary(research, 2)
        print(info)
        talk(info)
    elif 'bye-bye' in command : 
        talk("Have a nice day, good bye and take care")
        return False
    elif 'joke' in command : 
        talk("Okay wait a second")
        engine.runAndWait()
        talk(pyjokes.get_joke())
    else : 
        talk('Please, say that command again!')
while True:
    condition = run_Alexa()
    if condition == False:
        break
