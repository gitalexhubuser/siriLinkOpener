import os
import speech_recognition as sr # pip install SpeechRecognition # pip install pyaudio
import webbrowser
import whisper

# 1 Переменные 
greetings_question = ["привет", "хай", "салют", "ку", "здорова", "хелоу", "добрый день"]
greetings_answer = ["добрый день", "приветствую"]

model = whisper.load_model("base")

def JarvisRecord():
    # r = sr.Recognizer()
    # with sr.Microphone() as source:
        # print("Говори в микрофон:")
        # audio = r.listen(source)

        # if os.path.exists("answer.mp3"):
        #     os.remove("answer.mp3")

        # r.save("answer.mp3")

    result = model.transcribe("E:/PythonProjects\\windowsVoiceHelper\\answer.mp3", fp16=False)
    # print("audio", audio)
    print(result["text"])



# 3 Цикл
while True:
    m = input("").lower()
    if m == ".":
        print("Jarvis: Внимательно слушаю вашу команду!")
        JarvisRecord()
    # elif m == "привет":
    elif m in greetings_answer:
        print("Привет\n")
 
    else:
        print("User: " + m)
