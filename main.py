from datetime import datetime
from Zelanda import ZelandaAsisstant
obj = ZelandaAsisstant()
def speak(text):
    obj.tts(text)


def zelanda_response(text):
    obj.response_assistant(text)

def wish():
    hour = int(datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Selamat Pagi")
    elif hour>12 and hour<18:
        speak("Selamat Siang")
    else:
        speak("Selamat Sore")
    c_time = obj.tell_time()
    speak(f"Saat ini {c_time}")
    speak("Apa yang bisa saya bantu ?")
if __name__ == "__main__":
        wish()
        time = 0
        while True:
            command = obj.mic_input()
            zelanda_response(command)