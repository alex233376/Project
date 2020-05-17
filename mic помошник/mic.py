import speech_recognition as sr

mic = sr.Microphone(device_index=1)

# list_mic = sr.Microphone.list_microphone_names()
# for i in range(0, len(list_mic)):
#     print(i, list_mic[i])

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Скажите число!")
    audio = r.listen(source)

try:
    a = r.recognize_google(audio, language="ru-RU")
    print("Google Speech Recognition считает, что вы сказали " + a)
except sr.UnknownValueError:
    print("Google Speech Recognition не может понять звук")
except sr.RequestError as e:
    print(
        "Не удалось запросить результаты из службы распознавания речи Google; {0}".format(e))

with sr.Microphone() as source:
    print("Скажите ещё одно число!")
    audio = r.listen(source)
try:
    b = r.recognize_google(audio, language="ru-RU")
    print("Google Speech Recognition считает, что вы сказали " + b)
except sr.UnknownValueError:
    print("Google Speech Recognition не может понять звук")
except sr.RequestError as e:
    print(
        "Не удалось запросить результаты из службы распознавания речи Google; {0}".format(e))
print('Сумма чисел равна ', (int(a) + int(b)))
