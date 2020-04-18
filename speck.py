from gtts import gTTS
import os
from tkinter import *
root = Tk()
e = Entry(root, width=50)
e.pack()
language = 'en'
def myClick():
    myLabel = Label(root, text=e.get())
    myLabel.pack()
myButton = Button(root, text="Enter your name", command=myClick)
myButton.pack()
def speak(myClick):
    output = gTTS(text=myClick(), lang=language, slow=False)
    output.save("outp.mp3")
    os.system("start outp.mp3")
root.mainloop()
speak("hi Guru")


