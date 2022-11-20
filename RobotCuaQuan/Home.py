from datetime import datetime
import speech_recognition as sr
import speech_recognition as sr
from gtts import gTTS
import os
import time
import pyaudio
import playsound
import wikipedia
import webbrowser as web

r= sr.Recognizer()
now = datetime.now()

def speak (text):
    tts = gTTS(text=text, lang='vi')
    filename = 'voice.mp3'
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)
def hello():
    hour = datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Chào buổi sáng nhé")
    elif hour >= 12 and hour < 18:
        speak("Chào buổi trưa nhé")
    elif hour >= 18 and hour < 21:
        speak("Chào buổi tối nhé")
    elif hour >= 21 and hour < 23:
        speak("Ngủ đi má")
    speak("Bây giờ là"+ now.strftime("%d/%m/%Y"))
while True:
    with sr.Microphone() as source:
        audio=r.record(source,duration=5)
        hello()
        continue
        speak("Hãy nói gì đó ...")
        try:
            text = r.recognize_google(audio, language='vi')
        except:
            text = ""
        print(text)
        if text == "":
            robot_quan = "Mày muốn nói gì với tao thế"
            print(robot_quan)
            speak(robot_quan)
        elif "Xin Chào" and "chào" in text:
            robot_quan = "Xin chào Sếp"
            print(robot_quan)
            speak(robot_quan)
        elif "ngày bao nhiên" in text:
            robot_quan =now.strftime("Hôm nay là ngày %d/%m/%Y")
            print(robot_quan)
            speak(robot_quan)
        elif "Stop" and "Dừng" in text:
            robot_quan = "Tạm biệt Mày"
            print(robot_quan)
            speak(robot_quan)
            break
        else:
            speak("Ngoài phạm vi hoạt động")