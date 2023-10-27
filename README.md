# windowsVoiceHelper

![Alt text](image.png)

## Описание

Помощник типа Siri (Apple), Алиса (Яндекс). Открыватель ссылок и программ. Ускоряет работу. Влияет на продуктивность!

Распознование речи с микрофона при зажатом `Ctrl`. 

Реализовано через 3 библиотеки (как онлайн, так и офлайн):

- Whisper openai (?)
- Vosk kaldi (офлайн)
- SpeechRecognition (онлайн)

Процесс кинул в [автозагрузку](https://youtu.be/wn3RTvgYbow?list=PLI_zmFp0iguCQY1ei_y6luSfU4Qvxktj-)!

---

## Возможности

- Открываем сайты, ссылки
- Открываем игры, приложения и ярлыки
- Проигрываем звуки
- Выполняем системные команды

---

## Примеры команд

... TODO

---

## Использование

### Gotham - онлайн

`gotham.py` - распознавание речи через Google api

`runGotham.bat` — ярлык для запуска

Зажимаем ctrl и говорим

### Vosk - офлайн

`main.py` - распознавание речи при помощи Vosk (Kaldi)

`run.bat` — ярлык для запуска

Зажимаем ctrl и говорим

> Нужны модели!

> vosk-model-small-ru-0.22 !!!

> vosk-model-ru-0.10

> vosk-model-ru-0.22

### Whisper - ?

Есть в комитах

... TODO

---

# Ссылки
| Описание | Ссылка |
| ------ | ------ |
Репо: | [github.com/gitalexhubuser/siriLinkOpener](https://github.com/gitalexhubuser/siriLinkOpener)
