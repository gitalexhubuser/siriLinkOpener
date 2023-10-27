from playsound import playsound # pip install playsound==1.2.2
import speech_recognition as sr # pip install SpeechRecognition # pip install pyaudio
import webbrowser
import keyboard # pip install keyboard
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

    elif result in ["автозагрузка"]:
        playsound("succes.mp3")
        # path = r"C:\Users\VisualCode\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
        # subprocess.Popen(f'explorer "{path}"')
        subprocess.Popen('start shell:startup', shell=True)

    elif result in ["часто забываю"]:
        playsound("succes.mp3")
        webbrowser.open("obsidian://open?vault=Lua&file=%D0%A7%D0%B0%D1%81%D1%82%D0%BE%20%D0%B7%D0%B0%D0%B1%D1%8B%D0%B2%D0%B0%D1%8E%20-%20Wow%20Api")
    
    elif result in ["git", "гит"]:
        playsound("succes.mp3")
        webbrowser.open("obsidian://open?vault=IT&file=git%2Fgithub%20-%20SSH")

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
