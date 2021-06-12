import speech_recognition as sr
import webbrowser
from time import ctime

r = sr.Recognizer()

def record_audio(ask = False):

    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
            print(voice_data)
        except sr.UnknownValueError:
            print('Sorry, ik heb dat niet begrepen')
        except sr.RequestError:
            print('Sorry, er is iets misgegaan')
        return voice_data

def respond(voice_data):
    if 'what is your name' in voice_data:
        print('My name is test')
    if 'what time is it' in voice_data:
        print(ctime())
    if 'search' in voice_data:
        search = record_audio('What do you want to search for')        
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        print('Dit is wat ik vond' + search)

print('Hoe kan ik je helpen?')
voice_data = record_audio()
respond(voice_data)