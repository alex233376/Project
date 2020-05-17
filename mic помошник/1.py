import pyaudio
p = pyaudio.PyAudio()
import datetime
import time
now = datetime.datetime.now()
print("Сейчас " + str(now.hour) + ":" + str(now.minute))