

import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import pynews
import googlesearch
import pywhatkit as kt
import getpass as gp





listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.talk('what can i do for you')



def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)

    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)

    elif 'who is ' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'open instagram' in command:
        webbrowser.open_new_tab('https://www.instagram.com/')
        print('opening Instagram')

    elif 'date' in command:
        talk('sorry, I have a headache')

    elif 'are you single' in command:
        talk('I am in a relationship with wifi')

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    elif "open Google" in command:
        webbrowser.open("google.com")
        talk("opening")

    elif 'trending news' in command:
        top = pynews
        print(top)
        talk(top)

    elif 'open whatsapp' in command or 'whatsapp' in command:
        webbrowser.open_new_tab('https://web.whatsapp.com/')
        print('opening WhatsApp Web')

    elif 'search google for' in command:
        googlesearch.__all__(command)

    elif "where is" in command:
        ind = command.split().index("is")
        location = command[ind + 8:]
        url = "https://www.google.com/maps/place/" + "".join(location)
        talk("This is where i found, " + str(location))

    elif 'emergency' in command:
        print("Let's Automate Whatsapp!")
        p_num = 'the taget phone number goes here!'
        # or you can use getpass module to capture cell num
        p_num = gp.getpass(prompt='+phone.no: ', stream=None)
        msg = "emergency pls help"
        kt.sendwhatmsg(p_num, msg, 10, 25)

    else:
        talk('Please say the command again.')


while True:
    run_alexa()