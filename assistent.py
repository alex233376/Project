import pyttsx3                                    # преобразует текст в речь
import datetime                                   # работа с датой и временем
import speech_recognition as sr                   # перевод голоса в текст
import wikipedia                                  # работа с wikipedia
import webbrowser                                 # требуется для открытия запрошенного приложения в веб-браузере
import os.path                                    # требуется для извлечения содержимого из указанной папки/каталога
import smtplib                                    # требуется для работы с запросами по электронной почте


engine = pyttsx3.init('sapi5')                    # sapi5 — это API и технология распознавания и синтеза голоса, предоставляемая Microsoft.
voices = engine.getProperty('voices') # дает вам подробную информацию о текущих голосах

#engine.setProperty('voice',voices[1].id)          # если установленны голоса 0-мужской голос , 1-женский голос



def speak(audio):                                # функция для помощника говорить
    engine.say(audio)
    engine.runAndWait()                          # Без этой команды мы не услышим речь



def wishme():                                    # помощник будет приветствовать нас в зависимости от времени на компьютере
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Доброе утро')

    elif hour>12 and hour<18:
        speak('Добрый день')

    else:
        speak('Добрый вечер')

    speak('Привет я бармалей чего надо')


def takecommand():                               # функция для приема аудиовхода от пользователя
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Слушаю...')
        r.pause_threshold = 2
        audio = r.listen(source)


    try:                                            # обработка ошибок
        print('Понял...')
        query = r.recognize_google(audio_data=audio,language = 'ru-RU')  # использование google для распознавания голоса
        print(f'Ты сказал: {query}\n')

    except Exception as e :
        print('Повторите, пожалуйста...')        # если не распознал
        return 'None'  
    return query

def sendemail(to,content):                       # функция отправки электронной почты
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('senders_eamil@gmail.com','senders_password')
    server.sendmail('senders_email@gmail.com',to,content)
    server.close()


if __name__ == '__main__' :                      # функция запуска
    wishme()
    while True:
        query = takecommand().lower()  # преобразует запрос пользователя в нижний регистр

        # Вся логика выполнения задач на основе пользовательского запроса

        if 'поиск' in query :
            speak('Поиск в Википедии....')
            query = query.replace('wikipedia','')
            results = wikipedia.summary(query, sentences = 5)
            print(results)
            speak(results)

        elif 'youtube' in query :
            webbrowser.open('youtube.com')

        elif 'google' in query :
            webbrowser.open('google.com')

        elif 'играть музыку' in query :
            speak('хорошо босс')
            music_dir = 'music_dir_of_the_user'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[0]))


        elif 'время' in query :
            strtime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f'время {strtime}')


        elif 'open stack overflow' in query :
            webbrowser.open('stackoverflow.com')

        elif 'open free code camp' in query :
            webbrowser.open('freecodecamp.org')

        elif 'pycharm' in query :
            codepath = 'pycharm_directory_of_your_computer'
            os.startfile(codepath)

        elif 'email' in query :
            try:
                speak('что я должен написать в электронном письме?')
                content = takecommand()
                to = 'reciever_email@gmail.com'
                sendemail(to, content)
                speak('письмо было отправлено')
            except Exception as e:
                print(e)
                speak('Извините, я не могу отправить это письмо')

        elif 'стоп' in query:
            speak('хорошо босс')
            quit()

            
