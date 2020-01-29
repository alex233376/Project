import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone(device_index=5) as source:
    print("Скажите что то....")
    audio = r.listen(source)

query = r.recognize_google(audio, language="ru-RU")
print("Вы сказали " + query.lower())
