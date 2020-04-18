from gtts import gTTS
import os
from tkinter import *
def speak(mytext):
    language = 'en'
    output = gTTS(text=mytext, lang=language, slow=False)
    output.save("outp.mp3")
    os.system("start outp.mp3")
top = Tk()  
  
top.geometry("400x250")  
  
#buttonCal = tk.Button(root, text="speak", command=e2).grid(row=3, column=0)  
#val = input("Enter your value: ") 
name = Label(top, text = "say anything..").place(x = 30,y = 50)  
e2 = Entry(top).place(x = 80, y = 90) 

top.mainloop()

speak("ho")


 