import pyttsx3
from tkinter import *

w = Tk()
w.title('Text to speech')
w.geometry('450x80')
w.resizable(0, 0)

l = Label(w, text = 'Enter text here : ', font = ('Kalinga', 15))
l.grid(row = 0, column = 0)

e = Entry(w, width = 45)
e.grid(row = 0, column = 1)

def cl() :
    e.delete(0, END)

def sp() :
    s = pyttsx3.init()
    s.say(e.get())
    s.runAndWait()

b1 = Button(w, text = 'Clear', font = ('Kalinga', 9), command = cl)
b1.grid(row = 1, column = 0)

b2 = Button(w, text = 'Speak', font = ('Kalinga', 9), command = sp)
b2.grid(row = 1, column = 1)

w.mainloop()