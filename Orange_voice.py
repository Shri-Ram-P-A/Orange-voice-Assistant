import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import calendar
import pyjokes
import pyaudio

# Initialize recognizer and text-to-speech engine
listen = sr.Recognizer()
engine = pyttsx3.init()

# Set the voice property
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say("Yes, I am Orange")
engine.say("I am here")
engine.runAndWait()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    command = ""
    try:
        with sr.Microphone() as source:
            listen.adjust_for_ambient_noise(source)
            print("Orange is listening...")
            voice = listen.listen(source)
            command = listen.recognize_google(voice)
            command = command.lower()
            if 'orange' in command:
                command = command.replace('orange', '')
                print(command)
    except:
        pass
    return command

def run_orange():
    command = take_command()
    if command:
        print(command)
        if 'play video' in command:
            song = command.replace('play video', '')
            talk('playing ' + song)
            pywhatkit.playonyt(song)
        elif 'date' in command:
            now = datetime.datetime.now()
            talk("Current date is")
            print(now.strftime("%Y-%m-%d %H:%M:%S"))
            talk(now.strftime("%Y-%m-%d %H:%M:%S"))
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            time1 = datetime.datetime.now().strftime('%H:%M')
            talk('Current time is ' + time)
            talk("In Railway timing is " + time1)
        elif 'what is' in command:
            person = command.replace('what is', '')
            info = wikipedia.summary(person, sentences=1)
            print(info)
            talk(info)
        elif 'who is' in command:
            person = command.replace('who is', '')
            info = wikipedia.summary(person, sentences=1)
            print(info)
            talk(info)
        elif 'print calendar' in command:
            year = int(input("Enter year: "))
            month = int(input("Enter month: "))
            x = calendar.month(year, month)
            print(x)
            talk("Here is the calendar")
        elif 'joke' in command:
            talk(pyjokes.get_joke())
        elif 'shall we date' in command:
            talk('Sorry, I have a headache')
        elif 'are you single' in command:
            talk('I am in a relationship with wifi')
        elif 'tell about you' in command:
            talk("I was created by the legend")
        else:
            talk('I cannot understand the command')
    else:
        talk('I cannot hear you. Please try again.')

run_orange()
