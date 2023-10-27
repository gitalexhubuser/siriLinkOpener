from playsound import playsound # pip install playsound==1.2.2
import ctypes
import keyboard # pip install keyboard
import speech_recognition as sr # pip install SpeechRecognition # pip install pyaudio
import subprocess
import webbrowser

soundFile = r"E:\PythonProjects\windowsVoiceHelper\Assets\succes.mp3"

def process_result(result):
    # if result in ["тест", "тест тест", "тэст", "test"]:
    if result in ["ютуб", "youtube"]:
        playsound(soundFile)
        webbrowser.open_new("https://www.youtube.com/@LuaNaZakaz")

    elif result in ["алекс", "саша", "alex"]:
        playsound(soundFile)
        webbrowser.open_new("https://www.youtube.com/channel/UCjDdSdLJbbV0UBtzKpClmig")

    elif result in ["дота", "пота", "dota"]:
        playsound(soundFile)
        subprocess.Popen(r"D:\Steam\steamapps\common\dota 2 beta\game\bin\win64\dota2.exe")

    elif result in ["проект", "проекте", "проэкт"]:
        playsound(soundFile)

    elif result in ["автозагрузка"]:
        playsound(soundFile)
        # path = r"C:\Users\VisualCode\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
        # subprocess.Popen(f'explorer "{path}"')
        subprocess.Popen('start shell:startup', shell=True)

    elif result in ["часто забываю"]:
        playsound(soundFile)
        webbrowser.open("obsidian://open?vault=Lua&file=%D0%A7%D0%B0%D1%81%D1%82%D0%BE%20%D0%B7%D0%B0%D0%B1%D1%8B%D0%B2%D0%B0%D1%8E%20-%20Wow%20Api")
    
    elif result in ["git", "гит", "repo", "репо", "репа"]:
        playsound(soundFile)
        webbrowser.open("obsidian://open?vault=IT&file=git%2Fgithub%20-%20SSH")

    elif result in ["wow", "вов", "byster", "бустер", "пустер", "варкрафт", "warcraft"]:
        playsound(soundFile)
        shortcut_path = r"C:\Users\VisualCode\OneDrive\Desktop\[byster] ad2.lnk"
        shell = ctypes.windll.shell32
        shell.ShellExecuteW(None, "open", shortcut_path, None, None, 1)

    elif result in ["богатов", "леша", "лёша", "енот", "енотик"]:
        playsound(soundFile)
        webbrowser.open("https://vk.com/im?sel=139021021")

    # Калькулятор
    # Бабки деньги долары
    # Ники ник nick никнейм nickname
    # Премьер. Адоб. Адоб премьер. Адоб премьер про. Adobe premiere pro
    # Фотошоп. Photoshop

    elif result in ["заказ", "заказы", "закасы", "закас", "order"]:
        playsound(soundFile)
        webbrowser.open("obsidian://open?vault=IT&file=Lua")


# Основной цикл
if __name__ == "__main__":
    r = sr.Recognizer()

    while True:
        if keyboard.is_pressed('ctrl'):
            # r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Говори в микрофон:")
                audio = r.listen(source)
                try:
                    voice_result = r.recognize_google(audio, show_all=True, language="ru-RU")
                    if voice_result:
                        ts = voice_result['alternative'][0]['transcript'].lower() # transcript_value
                        print("Gotham: распознал следующие слова:", ts)
                        process_result(ts)
                except sr.UnknownValueError:
                    print("Gotham: Не удалось распознать речь")
                except sr.RequestError:
                    print("Gotham: Ошибка при обращении к сервису распознавания речи")
