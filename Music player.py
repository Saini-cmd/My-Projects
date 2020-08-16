from tkinter import *
from tkinter import filedialog
from pygame import mixer as m
import mutagen.mp3 as mu

# Define window
w = Tk()
w.title('Music Player')
w.resizable(1, 0)
w.geometry('400x80')

x = StringVar()          # For song name
play = False             # For play ckeck
pause = False            # For pause check
stop = True              # For stop check

# Define button functions
def browse() :
    global x, pause, stop
    if stop == True :
        x = filedialog.askopenfilename(filetype = [('MP3 Format Sound', '*.mp3')])
        l2.config(text = x)
        l4.config(text = 'Music Loaded')
        pause = True
        stop = False
        if x == '' :
            l2.config(text = '----------')
            l4.config(text = 'Please select mp3 file')
            pause = False
            stop = True

def play() :
    global x, play, pause
    if pause == True :
        f = mu.MP3(x)
        m.init(frequency = f.info.sample_rate)
        m.music.load(x)
        m.music.play()
        l4.config(text = 'Playing Music')
        play = True
        pause = False

def pause() :
    global play, pause, stop
    if play == True and stop == False :
        m.music.pause()
        l4.config(text = 'Music Paused')
        b3.config(text = '▶')
        play = False
    elif pause == False and stop == False :
        m.music.unpause()
        l4.config(text = 'Playing Music')
        b3.config(text = '❚❚')
        play = True

def end() :
    global play, pause, stop
    if play == True :
        m.music.stop()
        l4.config(text = 'Process Stopped')
        play = False
        pause = False
        stop = True

# Define user interface
l1 = Label(w, text = 'Now Playing :')
l1.grid(row = 0, column = 0)

l2 = Label(w, text = '----------')
l2.grid(row = 0, column = 1)

l3 = Label(w, text = 'Status :')
l3.grid(row = 1, column = 0)

l4 = Label(w, text = '----------')
l4.grid(row = 1, column = 1)

b1 = Button(w, text = 'Browse', command = browse)
b1.grid(row = 2, column = 0)

b2 = Button(w, text = 'Play', command = play)
b2.grid(row = 2, column = 1)

b3 = Button(w, text = '❚❚', command = pause)
b3.grid(row = 2, column = 2)

b4 = Button(w, text = '●', command = end)
b4.grid(row = 2, column = 3, padx = 15)

w.mainloop()