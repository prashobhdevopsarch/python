from gtts import gTTS
import os
import time
language = 'en'
localtime = time.asctime( time.localtime(time.time()) )
#val = input("Enter your value: ") 
def speak(mytext):
    output = gTTS(text=mytext, lang=language, slow=False)
    output.save("outp.mp3")
    os.system("start outp.mp3")
speak(localtime)