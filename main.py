import speech_recognition as sr
import webbrowser
import playsound
import os
import random
from gtts import gTTS
import time
from time import ctime #get time details


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

r = sr.Recognizer() #initialise
#listen for audio and convert it to text:
def record_audio(ask=False):
    with sr.Microphone() as source: #use microphone
        if ask:
            audior(ask)
        audio = r.listen(source)  #listen for the audio
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio, None, "nl_NL")  #convert audio to text
        except sr.UnknownValueError: #error
            audior('Ik heb het niet begrepen')
        except sr.RequestError:
            audior('Sorry, the service werkt niet') #error
        print(f">> {voice_data.lower()}") #print spoken text
        return voice_data.lower()

#audio settings
def audior(audio_string):
    tts = gTTS(text=audio_string, lang='nl')  
    r = random.randint(0, 100000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)  
    print(f"Gemeente Rotterdam: {audio_string}")
    os.remove(audio_file) 

#response
def respond(voice_data):
    # 1: greeting
    if there_exists(['hey','hi','hello', 'hallo', 'hoi']):
        greetings = [f"Hallo, welkom in de booth van de gemeente rotterdam. Wat is uw naam?", "goedendag, welkom in de booth van de gemeente rotterdam. Wat is uw naam?", "Hallo meneer/mevrouw, welkom in de booth van de gemeente rotterdam. Wat is uw naam?"]
        greet = greetings[random.randint(0,len(greetings)-1)]
        audior(greet)

    if there_exists(["mijn naam is", "ik heet", "ik ben"]):
        person_name = voice_data.split("is")[-1].strip()
        audior(f"Welkom {person_name} in de booth van de gemeente rotterdam. U bevindt zich in één van de persoonlijke ruimtes van de Gemeente Rotterdam. Wij willen u vriendelijk vragen om niet te eten of te drinken binnen de ruimte. Wilt u gebruik maken van een spraak toelichting, spreek dan nu ja of nee in.")
        person_obj.setName(person_name)

    if there_exists(["ja", "graag", "ja uitleg"]):
        audior(f'De spraakassistent blijft ingeschakelt, De ruimte is voorzien van reliëftegels en geleidelijnen. Deze zullen u leiden naar twee zitplekken met een tafel en een computerscherm met cameravoorziening. Neem twee stappen naar voor en 1 stap naar rechts om plaats te nemen op één van de twee stoelen. De meubels zitten vast aan de ruimte en zijn gericht naar de camera toe. Zodra u plaatsneemt, recht tegen de leuning zit en naar voren kijkt, zal dit bevestigd worden met dit geluid of afgekeurd worden met dit geluid (Buzzer). Het systeem zal een gezichtsherkenning uitvoeren van 10 seconden. Wij willen u vriendelijk vragen om recht te blijven zitten en naar voren te blijven kijken tot u dit bevestigings geluid hoort (Ding-Dong). Gezichtsherkenning  wordt uitgevoerd. 10, 9, 8, 7, 6, 5, 4, 3, 2, 1 (Ding Dong). Gezichtsherkenning is gelukt. Voor u bevindt zich een tafel met drie draaiknoppen. Als u slecht ziet of kleurenblind bent, kunt u door middel van de 1e twee knoppen links de kleuren veranderen van de lampen in de ruimte evenals het dempen van de lampen. De middelste knop kunt u gebruiken om de tekstgrootte aan te passen en de rechterknop kunt u gebruiken voor het stellen van de schermhelderheid. In geval van een nood kunt u de noodknop links van u, binnen handbereik van uw zitplaats, vinden onder de tafel. Wilt u de uitleg nog een keer horen? Roep dan ja uitleg of nee uitleg')

    if there_exists(["nee", "nee dank je", "nee uitleg"]):
        audior(f'Hoe laat had u een afspraak?')

    if there_exists(["Ik had een afspraak om", "ik heb een afspraak", "afspraak om", "afspraak", "uur"]):
        person_time = voice_data.split("om")[+1].strip()
        audior(f"Bedankt u heeft dan een afspraak om {person_time} met Jan van den berg. De digitale balie maakt verbinding met de desbetreffende ambtenaar. Even geduld alstublieft. (Ding-Dong) Er zit nu een ambtenaar voor u klaar om u te helpen. Uw camera staat aan. Wij wensen u een prettig gesprek toe! Als u klaar bent roep dan klaar!")
        person_obj.setTime(person_time)

    if there_exists(["klaar", "ik ben klaar"]):
        audior(f'De verbinding wordt nu verbroken. U mag de ruimte verlaten. Vergeet uw persoonlijke eigendommen niet mee te nemen. Gemeente Rotterdam is niet verantwoordelijk voor eventueel verlies of diefstal. Ga voor meer informatie naar rotterdam.nl/rotterdamr Gemeente Rotterdam wenst u een fijne dag!')  
    
    if there_exists(["nood", "112"]):
        audior(f'Het alarmnummer wordt nu ingeschakelt. Er komt spoedig hulp aan. Blijf rustig en probeer niet te bewegen.')  
    
    #2 Other question and responses

    # 1: name
    if there_exists(["uw naam","hoe heet u","Vertel me eens hoe u heet"]):
        if person_obj.name:
            audior("Mijn naam is audior en ik ben van de Gemeente Rotterdam")
        else:
            audior("mijn naam is gemeente rotterdam. wat is uw naam?")

    # 2: greeting
    if there_exists(["hoe gaat het","hoe is het met u"]):
        audior(f"Het gaat goed en hoe is het met u {person_obj.name}")

    # 2: greeting response
    if there_exists(["met mij gaat het goed","gaat goed", " gaat slecht"]):
        audior(f"Dat is fijn om te horen! Kan ik u nog ergens mee helpen?")


    # 3: explain
    if there_exists(["hoe ziet deze ruimte eruit", "wat is het voor ruimte", "wat kan ik doen in deze ruimte"]):
        audior(f"In deze booth kunt u uw gemeente zaken regelen. Ik ben uw persoonlijke assistent en zal u helpen met het regelen van uw gemeente zaken{person_obj.name}")

    # 4: search gemeente rotterdam
    if there_exists(["zoek naar"]) and 'gemeente' not in voice_data:
        search_term = voice_data.split("for")[-1]
        url = f"https://www.rotterdam.nl"
        webbrowser.get().open(url)
        audior(f'Dit is wat ik vond voor {search_term} op google')

    # 5: search
    if there_exists(["gemeente wonen","gemeente leven","gemeente wonen leven"]):
        url = f"https://www.rotterdam.nl/wonen-leven/"
        webbrowser.get().open(url)
        audior(f'Dit is wat ik vond')

    # 6: search
    if there_exists(["gemeente werken","gemeente leren","gemeente werken en leren"]):
        url = f"https://www.rotterdam.nl/werken-leren/"
        webbrowser.get().open(url)
        audior(f'Dit is wat ik vond')

    # 7: search
    if there_exists(["bestuur","organisatie","bestuur en organisatie"]):
        url = f"https://www.rotterdam.nl/bestuur-organisatie/"
        webbrowser.get().open(url)
        audior(f'Dit is wat ik vond')

    # 9: help
    if there_exists(["help"]):
        audior(f'Voor u bevindt zich een tafel met drie draaiknoppen. Als u slecht ziet of kleurenblind bent, kunt u door middel van de 1e twee knoppen links de kleuren veranderen van de lampen in de ruimte evenals het dempen van de lampen. De middelste knop kunt u gebruiken om de tekstgrootte aan te passen en de rechterknop kunt u gebruiken voor het stellen van de schermhelderheid. In geval van een nood kunt u de noodknop links van u, binnen handbereik van uw zitplaats, vinden onder de tafel. Wilt u de uitleg nog een keer horen? Roep dan ja uitleg of nee uitleg')


time.sleep(1)
person_obj = person()
while(1):
    voice_data = record_audio() #get voice input
    respond(voice_data) #response