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
            voice_data = r.recognize_google(audio, None, "nl_NL")  # convert audio to text
        except sr.UnknownValueError: # error: recognizer does not understand
            alexis_speak('Ik heb het niet begrepen')
        except sr.RequestError:
            alexis_speak('Sorry, the service werkt niet') # error: recognizer is not connected
        print(f">> {voice_data.lower()}") # print what user said
        return voice_data.lower()

def alexis_speak(audio_string):
    tts = gTTS(text=audio_string, lang='nl')    
    r = random.randint(1, 100000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)  
    print(f"Gemeente Rotterdam: {audio_string}")
    os.remove(audio_file) 

def respond(voice_data):
    # 1: greeting
    if there_exists(['hey','hi','hello', 'hallo']):
        greetings = [f"Hallo, welkom in de booth van de gemeente rotterdam. hier kunt u uw gemeente zaken regelen. Als u meer informatie wilt over de booth kunt u om hulp vragen. hoe kan ik u helpen{person_obj.name}", f"Goedendag. welkom in de booth van de gemeente rotterdam. hier kunt u uw gemeente zaken regelen. Als u meer informatie wilt over de booth kunt u om hulp vragen. Kan ik u ergens mee helpen? {person_obj.name}"]
        greet = greetings[random.randint(0,len(greetings)-1)]
        alexis_speak(greet)

    if there_exists(["uitleg","kunt u me uitleg geven","hoe ziet het eruit"]):
        alexis_speak(f'U bevind zich in de booth van de gemeente rotterdam. Voor u staat een stoel met een beeldscherm. hierop kunt u bellen met een medewerker van de gemeente en uw gemeente zaken regelen. als u andere vragen heeft of liever niet belt met iemand dan kunt u dat aan mij laten weten')

    if there_exists(["niet bellen","ik wil niet bellen","geen medewerker","heb geen medewerker nodig"]):
        alexis_speak(f'Dat is goed. U kunt zelf uw zaken regelen. Mocht u nog vragen hebben dan ben ik beschikbaar')

    # 2: name
    if there_exists(["uw naam","Hoe heet u","Vertel me eens hoe u heet"]):
        if person_obj.name:
            alexis_speak("Mijn naam is Gemeente Rotterdam")
        else:
            alexis_speak("mijn naam is gemeente rotterdam. wat is uw naam?")

    if there_exists(["mijn naam is"]):
        person_name = voice_data.split("is")[-1].strip()
        alexis_speak(f"Oke, ik ga dat onthouden {person_name}")
        person_obj.setName(person_name) # remember name in person object

    # 3: greeting
    if there_exists(["hoe gaat het","hoe is het met u"]):
        alexis_speak(f"Het gaat goed en hoe is het met u {person_obj.name}")

            # 3: greeting
    if there_exists(["Hoe ziet deze ruimte eruit", "wat is het voor ruimte", "wat kan ik doen in deze ruimte"]):
        alexis_speak(f"In deze booth kunt u uw gemeente zaken regelen. Ik ben uw persoonlijke assistent en zal u helpen met het regelen van uw gemeente zaken{person_obj.name}")

    # 5: search google
    if there_exists(["zoek naar"]) and 'youtube' not in voice_data:
        search_term = voice_data.split("for")[-1]
        url = f"https://google.com/search?q={search_term}"
        webbrowser.get().open(url)
        alexis_speak(f'Dit is wat ik vond voor {search_term} op google')

    # 5: search gemeente rotterdam
    if there_exists(["zoek naar"]) and 'gemeente' not in voice_data:
        search_term = voice_data.split("for")[-1]
        url = f"https://www.rotterdam.nl"
        webbrowser.get().open(url)
        alexis_speak(f'Dit is wat ik vond voor {search_term} op google')

    # 6: search youtube
    if there_exists(["youtube"]):
        search_term = voice_data.split("for")[-1]
        url = f"https://www.youtube.com/results?search_query={search_term}"
        webbrowser.get().open(url)
        alexis_speak(f'Here is what I found for {search_term} on youtube')

            # 3: greeting
    if there_exists(["gemeente wonen","gemeente leven","gemeente wonen leven"]):
        url = f"https://www.rotterdam.nl/wonen-leven/"
        webbrowser.get().open(url)
        alexis_speak(f'Dit is wat ik vond')

                    # 3: greeting
    if there_exists(["gemeente werken","gemeente leren","gemeente werken en leren"]):
        url = f"https://www.rotterdam.nl/werken-leren/"
        webbrowser.get().open(url)
        alexis_speak(f'Dit is wat ik vond')

    if there_exists(["bestuur","organisatie","bestuur en organisatie"]):
        url = f"https://www.rotterdam.nl/bestuur-organisatie/"
        webbrowser.get().open(url)
        alexis_speak(f'Dit is wat ik vond')

    if there_exists(["bestuur","organisatie","bestuur en organisatie"]):
        url = f"https://www.rotterdam.nl/bestuur-organisatie/"
        webbrowser.get().open(url)
        alexis_speak(f'Dit is wat ik vond')


time.sleep(1)
person_obj = person()
while(1):
    voice_data = record_audio() #get the voice input
    respond(voice_data) #respond