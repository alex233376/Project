import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone(device_index=16) as source:
    print("Скажите что нибудь ...")
    audio = r.listen(source)

queri = r.recognize_google(audio, language="ru-RU")
print("Вы сказали: " + queri.lower())
