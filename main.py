import os, pyaudio
from vosk import Model, KaldiRecognizer
import keyboard
import webbrowser
from playsound import playsound
import subprocess
import pyperclip
import pyautogui

# либы от сюда https://alphacephei.com/vosk/models

model = Model(r"E:\PythonProjects\windowsVoiceHelper\models\vosk-model-small-ru-0.22")
# model = Model(r"E:\PythonProjects\windowsVoiceHelper\models\vosk-model-ru-0.10")

recognizer = KaldiRecognizer(model, 16000)

 
def AdobePremierePro_Helper():
    # Путь к файлу, который нужно скопировать
    file_path1 = 'E:\\YandexDisk\\Python\[PR] auto-editor!!!\\dragAndDrop.cmd'
    # file_path2 = r'E:\YandexDisk\Python\[PR] auto-editor!!!\Untitled.prproj'

    pyperclip.copy(file_path1)
    # pyautogui.hotkey('ctrl', 'v')
    # pyperclip.paste()

# работает !
CHUNK = 4096 ## 4096 8192
mic = pyaudio.PyAudio()
# stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=CHUNK)
playsound("succes.mp3")


def process_result(result):
    if result in ["тест", "тэст"]:
        playsound("succes.mp3")
        webbrowser.open_new("https://www.youtube.com/@LuaNaZakaz")
    elif result in ["дота", "пота"]:
        playsound("succes.mp3")
        subprocess.Popen(r"D:\Steam\steamapps\common\dota 2 beta\game\bin\win64\dota2.exe")
    elif result in ["проект", "проекте", "проэкт"]:
        playsound("succes.mp3")

# Основной цикл
while True:
    if keyboard.is_pressed('ctrl'):
        data = stream.read(4096) # 4096

        if recognizer.AcceptWaveform(data):
            text = recognizer.Result()
            result = text[14:-3]
            print("result:", result)
            process_result(result)