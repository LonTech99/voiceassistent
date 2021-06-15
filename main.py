from enum import auto
import speech_recognition as sr
import webbrowser
import playsound
import os
import random
from gtts import gTTS
import time

class person:
    name = ''
    def setName(self, name):
        self.name = name

def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True

r = sr.Recognizer() # initialise a recogniser
# listen for audio and convert it to text:
def record_audio(ask=False):
    with sr.Microphone() as source: # microphone as source
        if ask:
            alexis_speak(ask)
        audio = r.listen(source)  # listen for the audio via source
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)  # convert audio to text
        except sr.UnknownValueError: # error: recognizer does not understand
            alexis_speak('I did not get that')
        except sr.RequestError:
            alexis_speak('Sorry, the service is down') # error: recognizer is not connected
        print(f">> {voice_data.lower()}") # print what user said
        return voice_data.lower()

def alexis_speak(audio_string):
    tts = gTTS(text=audio_string, lang='nl')    
    r = random.randint(1, 100000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)  
    print(audio_string)
    os.remove(audio_file) 

def respond(voice_data):
        # 1: greeting
    if there_exists(['hoi','hey','hallo']):
        greetings = [f"goedendag, hoe gaat het? {person_obj.name}", f"Hallo, hoe gaat het met u? {person_obj.name}", f"Waar kan ik u mee helpen? {person_obj.name}", f"Kan ik u ergens mee helpen? {person_obj.name}"]
        greet = greetings[random.randint(0,len(greetings)-1)]
        alexis_speak(greet)

            # 2: name
    if there_exists(["Wat is uw naam?"]):
        if person_obj.name:
            alexis_speak("Ik ben de Voice assistent van de Gemeente Rotterdam")
        else:
            alexis_speak("Ik ben de Voice assistent van de Gemeente Rotterdam en wie bent u?")

    if there_exists(["mijn naam is"]):
        person_name = voice_data.split("is")[-1].strip()
        alexis_speak(f"Mooie naam {person_name}")
        person_obj.setName(person_name) # remember name in person object

    # 3: greeting
    if there_exists(["Hoe is het","Hoe gaat het met je"]):
        alexis_speak(f"Gaat zeer goed, bedankt voor het vragen {person_obj.name}")
    if 'Waar ben ik nu?' in voice_data:
        alexis_speak('In Rotterdam')
    if 'Wat kan ik hier precies doen?' in voice_data:
        alexis_speak('Uw gemeentezaken regelen')
    if 'search' in voice_data:
        search = record_audio('Waar wil u naar zoeken')        
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        alexis_speak('Dit is wat ik vond' + search)

time.sleep(1)
person_obj = person()
while(1):
    voice_data = record_audio() # get the voice input
    respond(voice_data) # respond