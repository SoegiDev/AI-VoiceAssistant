import speech_recognition as sr
from datetime import datetime
from gtts import gTTS
import os
from playsound import playsound
from Library.Zelanda import GenericAssistant

from Zelanda.features import date_time
from Zelanda.features import current_location
from Zelanda.features import wikipedia

version = "testing_zelandav1.0.0"
assistant = GenericAssistant('intents.json', model_name=version)
assistant.train_model()
assistant.save_model()

class ZelandaAsisstant:
    def __init__(self):
        pass

    def mic_input(self):
        global part1
        """
        Fetch input from mic
        return: user's voice input as text if true, false if fail
        """
        try:
            r = sr.Recognizer()
            # r.pause_threshold = 1
            # r.adjust_for_ambient_noise(source, duration=1)
            with sr.Microphone() as source:
                print("Listening....")
                r.energy_threshold = 3000
                audio = r.listen(source,phrase_time_limit = 5)
            try:
                print("Recognizing...")
                command = r.recognize_google(audio, language='id-ID',show_all=True)
                part1 = command['alternative'][0]['transcript']
                print(F'belajar : {part1}')
                print(F'belajar full: {command}')
            except:
                # speak(random.choice(Cannot_hear_RES))
                print('Please try again')
                command = self.mic_input()
            return part1
        except Exception as e:
            print(e)
            return  False

    def tts(self, text):
        try:
            language = 'id'
            my_obj = gTTS(text=text, lang=language, slow=False,tld='com') 
            now = datetime.now()
            filename_audio= f'question{now.strftime("%d%m%Y%H%M%S")}.mp3'
            my_obj.save(filename_audio)
            root_dir = os.getcwd()
            bg_path = os.path.join(root_dir, filename_audio)
            filesound = bg_path
            playsound(filesound)
            os.remove(filesound)
            return True
        except:
            t = "Sorry I couldn't understand and handle this input"
            print(t)
            return False
    def response_assistant(self,text):
            sound = assistant.request(text)
            zelanda = Zelanda_brand()
            p1 = MyLocation()
            p2 = Wikipedia()
            if sound == "lokasi" : return p1.m()
            if sound == "wikipedia" : return p2.m(sound)
            zelanda.tell(sound)

    def tell_time(self):
        return date_time.time()

class Zelanda_brand(ZelandaAsisstant):
    def tell(self,sound):
        try:
            language = 'id'
            my_obj = gTTS(text=sound, lang=language, slow=False,tld='com') 
            now = datetime.now()
            filename_audio= f'question{now.strftime("%d%m%Y%H%M%S")}.mp3'
            my_obj.save(filename_audio)
            root_dir = os.getcwd()
            bg_path = os.path.join(root_dir, filename_audio)
            filesound = bg_path
            playsound(filesound)
            os.remove(filesound)
        except Exception as e:
            print(e)

class MyLocation(ZelandaAsisstant):
    def m(self):
        try:
            city, state, country = current_location.my_location()
            print(city, state, country)
        except Exception as e:
            print(e)

class Wikipedia(ZelandaAsisstant):
    def m(self,sound):
        try:
            topic = sound.split(' ')[-1]
            wiki_res = wikipedia.tell_me_about(topic)
            print(wiki_res)
        except Exception as e:
            print(e)