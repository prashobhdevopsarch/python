from gtts import gTTS
import os
language = 'en'
def speak(mytext):
    output = gTTS(text=mytext, lang=language, slow=False)
    output.save("outp.mp3")
    os.system("start outp.mp3")
speak("hi Guru")