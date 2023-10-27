import pyaudio
from vosk import Model, KaldiRecognizer # pip3 install vosk
# import os
# import json
import keyboard
import webbrowser
from playsound import playsound # pip install playsound==1.2.2

# либы от сюда https://alphacephei.com/vosk/models

model = Model(r"E:\PythonProjects\windowsVoiceHelper\vosk-model-small-ru-0.22")
# model = Model(r"O:\PythonProjects\Amanda-Lizard\vosk-model-ru-0.10")

recognizer = KaldiRecognizer(model, 16000)

# работает !
mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True,  frames_per_buffer=8192)

while True:
    try:
        data = stream.read(4096)
        if recognizer.AcceptWaveform(data):
            text = recognizer.Result()

            if keyboard.is_pressed('ctrl'):
                result = text[14:-3]
                print("result:", result)

                if result == "тест":
                    playsound("succes.mp3")
                    webbrowser.open_new("https://docs.google.com/spreadsheets/u/0")
    except:
        pass
