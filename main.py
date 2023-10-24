import os
from gtts import gTTS
from playsound import playsound # pip install playsound==1.2.2
import speech_recognition as sr # pip install SpeechRecognition # pip install pyaudio
import webbrowser #pip install webbrowser
import random



# 1 Переменные 
greetings_question = ["привет", "хай", "салют", "ку", "здорова", "хелоу", "добрый день"]
greetings_answer = ["добрый день", "приветствую"]

test_question = ["test", "тест"]
google_tables_question = ["открой мои документы", "мои документы открой", "гугл документы", "гугл документы открой", "открой гугл документы", "мои гугл документы открой", "открой мои гугл документы", "google документы", "google документы открой", "открой google документы", "мои google документы открой", "открой мои google документы"] 
katrin_question = ["катя в вк",  "катя в vk",  "открой катю в vk",  "открой катю vk",  "открой катю вк", "открой катю в вк",  "открой катю в вконтакте",  "страница кати в vk",  "страница кати в вк", "страница кати в вконтакте",  "открой в vk катю",  "открой в vk страницу кати",  "открой в вк катю", 
"открой в вк страницу кати",  "открой вк катю",  "открой вк страницу кати",  "открой vk катю", "открой vk страницу кати",  "открой вконтакте катю",  "катя вк открой",  "катя vk открой", "катю вк открой",  "катю vk открой",  "вк катя",  "vk катя",  "вк катю",  "vk катю", "вк кати",  "vk кати",  "катя вк",  "катя vk",  "vk кате",  "вк кате",  "катю вконтакте"]


# 2 Функции
def JarvisSay(_text):
    tts = gTTS(text=_text, lang='ru')

    if os.path.exists("answer.mp3"):
        os.remove("answer.mp3")

    tts.save("answer.mp3")

    if os.path.exists("answer.mp3"):
        playsound('answer.mp3')

def JarvisRecord():
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

        # ---------------- Voice ----------------
        if ts in greetings_question:
            print("Привет\n")
            JarvisSay(random.choice(greetings_answer))

        if ts in test_question:
            print("тест пройден\n")
            JarvisSay("тест прйоден")
            webbrowser.open_new("https://docs.google.com/spreadsheets/u/0")

        if ts in google_tables_question:
            print("Перехожу на сайт docs.google.com\n")
            JarvisSay("открываю таблицы гугл")
            webbrowser.open_new("https://docs.google.com/spreadsheets/u/0")

        if ts in katrin_question:
            print("Перехожу в ВК на страницу Кати\n")
            JarvisSay("открываю страницу кати")
            webbrowser.open_new("https://vk.com/id182619532")

    except:
        pass


# 3 Цикл
while True:
    m = input("").lower()
    if m == ".":
        print("Jarvis: Внимательно слушаю вашу команду!")
        JarvisRecord()
    # elif m == "привет":
    elif m in greetings_answer:
        print("Привет\n")
        JarvisSay(random.choice(greetings_answer))
    else:
        print("User: " + m)
