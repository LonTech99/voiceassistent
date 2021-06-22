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

    time = ''
    def setTime(self, time):
        self.time = time

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
        greetings = [f"Hallo, welkom in de booth van de gemeente rotterdam. Wat is uw naam?", "goedendag, welkom in de booth van de gemeente rotterdam. Wat is uw naam?", "Hallo meneer/mevrouw, welkom in de booth van de gemeente rotterdam. Wat is uw naam?"]
        greet = greetings[random.randint(0,len(greetings)-1)]
        alexis_speak(greet)

    if there_exists(["mijn naam is", "ik heet", "ik ben"]):
        person_name = voice_data.split("is")[-1].strip()
        alexis_speak(f"Welkom {person_name} in de booth van de gemeente rotterdam. U bevindt zich in één van de persoonlijke ruimtes van de Gemeente Rotterdam. Wij willen u vriendelijk vragen om niet te eten of te drinken binnen de ruimte. Wilt u gebruik maken van een spraak toelichting, spreek dan nu ja of nee in.")
        person_obj.setName(person_name) # remember name in person object

    if there_exists("nee"):
        alexis_speak(f'De spraakassistent is uitgeschakeld. Als u mij weer wil activeren zeg dan RotterdamR')

    if there_exists(["ja", "graag"]):
        alexis_speak(f'De spraakassistent blijft ingeschakelt, De ruimte is voorzien van reliëftegels en geleidelijnen. Deze zullen u leiden naar twee zitplekken met een tafel en een computerscherm met cameravoorziening. Neem twee stappen naar voor en 1 stap naar rechts om plaats te nemen op één van de twee stoelen. De meubels zitten vast aan de ruimte en zijn gericht naar de camera toe. Zodra u plaatsneemt, recht tegen de leuning zit en naar voren kijkt, zal dit bevestigd worden met dit geluid {sound.play_effect} of afgekeurd worden met dit geluid (Buzzer). Het systeem zal een gezichtsherkenning uitvoeren van 30 seconden. Wij willen u vriendelijk vragen om recht te blijven zitten en naar voren te blijven kijken tot u dit bevestigings geluid hoort (Ding-Dong). Gezichtsherkenning  wordt uitgevoerd. 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1 (Ding Dong). Gezichtsherkenning is gelukt. Voor u bevindt zich een tafel met drie draaiknoppen. Als u slecht ziet of kleurenblind bent, kunt u door middel van de 1e twee knoppen links de kleuren veranderen van de lampen in de ruimte evenals het dempen van de lampen. De middelste knop kunt u gebruiken om de tekstgrootte aan te passen en de rechterknop kunt u gebruiken voor het stellen van de schermhelderheid. In geval van een nood kunt u de noodknop binnen handbereik van uw zitplaats vinden onder de tafel of u roept nood. Wilt u de uitleg nog een keer horen? Roep dan ja uitleg of nee uitleg')

    if there_exists(["uitleg", "graag uitleg"]):
        alexis_speak(f'De ruimte is voorzien van reliëftegels en geleidelijnen. Deze zullen u leiden naar twee zitplekken met een tafel en een computerscherm met cameravoorziening. Neem twee stappen naar voor en 1 stap naar rechts om plaats te nemen op één van de twee stoelen. De meubels zitten vast aan de ruimte en zijn gericht naar de camera toe. Zodra u plaatsneemt, recht tegen de leuning zit en naar voren kijkt, zal dit bevestigd worden met dit geluid (Ding Dong) of afgekeurd worden met dit geluid (Buzzer). Het systeem zal een gezichtsherkenning uitvoeren van 30 seconden. Wij willen u vriendelijk vragen om recht te blijven zitten en naar voren te blijven kijken tot u dit bevestigings geluid hoort (Ding-Dong). Gezichtsherkenning  wordt uitgevoerd. 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1 (Ding Dong). Gezichtsherkenning is gelukt. Voor u bevindt zich een tafel met drie draaiknoppen. Als u slecht ziet of kleurenblind bent, kunt u door middel van de 1e twee knoppen links de kleuren veranderen van de lampen in de ruimte evenals het dempen van de lampen. De middelste knop kunt u gebruiken om de tekstgrootte aan te passen en de rechterknop kunt u gebruiken voor het stellen van de schermhelderheid. In geval van een nood kunt u de noodknop binnen handbereik van uw zitplaats vinden onder de tafel of u roept nood. Wilt u de uitleg nog een keer horen? Roep dan uitleg. Hoe laat had u een afspraak?')

    if there_exists(["Ik had een afspraak om", "ik heb een afspraak", "een afspraak om"]):
        person_time = voice_data.split("is")[-1].strip()
        alexis_speak(f"Bedankt {person_name} u heeft dan een afspraak om {person_time} met Jan van den berg. De digitale balie maakt verbinding met de desbetreffende ambtenaar. Even geduld alstublieft. (Ding-Dong) Er zit nu een ambtenaar voor u klaar om u te helpen. Uw camera staat aan. Wij wensen u een prettig gesprek toe!")
        person_obj.setTime(person_time) # remember time van persoon
    
    
    
    
    
    if there_exists(["uitleg","kunt u me uitleg geven","hoe ziet het eruit"]):
        alexis_speak(f'welkom in de booth van de gemeente rotterdam. U bevindt zich in één van de persoonlijke ruimtes van de Gemeente Rotterdam. Wij willen u vriendelijk vragen om niet te eten of te drinken binnen de ruimte en het schoon achter te laten. Wilt u gebruik maken van een spraak toelichting, spreek dan nu ja of nee rotterdam in')

    if there_exists(["niet bellen","ik wil niet bellen","geen medewerker","heb geen medewerker nodig"]):
        alexis_speak(f'Dat is goed. U kunt zelf uw zaken regelen. Mocht u nog vragen hebben dan ben ik beschikbaar')

    # 2: name
    if there_exists(["uw naam","Hoe heet u","Vertel me eens hoe u heet"]):
        if person_obj.name:
            alexis_speak("Mijn naam is Gemeente Rotterdam")
        else:
            alexis_speak("mijn naam is gemeente rotterdam. wat is uw naam?")

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