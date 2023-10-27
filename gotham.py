import os
from gtts import gTTS # pip install gtts
from playsound import playsound #pip install playsound==1.2.2
import speech_recognition as sr #pip install SpeechRecognition #pip install pyaudio
import webbrowser #pip install webbrowser
import keyboard
import subprocess

def process_result(result):
    if result in ["тест", "тэст", "test"]:
        playsound("succes.mp3")
        webbrowser.open_new("https://www.youtube.com/@LuaNaZakaz")
    elif result in ["дота", "пота", "dota"]:
        playsound("succes.mp3")
        subprocess.Popen(r"D:\Steam\steamapps\common\dota 2 beta\game\bin\win64\dota2.exe")
    elif result in ["проект", "проекте", "проэкт"]:
        playsound("succes.mp3")

# Основной цикл
while True:
    if keyboard.is_pressed('ctrl'):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Говори в микрофон:")
            audio = r.listen(source)
        try:
            # print("Text: " + r.recognize_google(audio, None, "ru-RU"))
            # voice_result = r.recognize_google(audio, None, "ru-RU")
            voice_result = r.recognize_google(audio, show_all=True, language="ru-RU")
            ts = voice_result['alternative'][0]['transcript'].lower() # transcript_value
            print("Gotham: распознал следующие слова:", ts)
            process_result(ts)
        except:
            pass
