import os
from tkinter import *

# Define window
w = Tk()
w.title('Contact Manager')
w.geometry('320x200')

# Define frames in window
f1 = Frame(w)
f1.pack(expand = True, fill = 'both')
f2 = Frame(w)
f2.pack(expand = True, fill = 'both')
f3 = Frame(w)
f3.pack(expand = True, fill = 'both')

a = False     # For add button
d = False     # For delete button

# Function to clear frame 3 for next button
def remove() :
    global f4, a, d
    if a == True or d == True :
        f4.destroy()
        a = False
        d = False

# Function for add button
def b1_click() :
    global f4, a, d
    b1.config(bg = '#00bfff')
    b2.config(bg = '#ffffff')
    b3.config(bg = '#ffffff')
    w.geometry('320x400')
    remove()
    f4 = Frame(f3)
    f4.pack(expand = True, fill = 'both')
    def add() :
        book = open('Contact Book.txt', 'a+')
        book.write('Name : ' + str(e1.get('1.0', 'end') + 'Phone : ' + str(e2.get('1.0', 'end'))))
        book.write('\n')
        book.close()
        e1.delete('1.0', 'end')
        e2.delete('1.0', 'end')
    if a == False :
        tip1 = Label(f4, text = 'Enter Name and Phone number to be added', font = ('Kalinga', 10))
        tip1.pack()
        space1 = Label(f4, text = '')
        space1.pack()
        
        l1 = Label(f4, text = 'Name :', font = ('Kalinga', 10))
        l1.pack()
        e1 = Text(f4, width = 30, height = 1)
        e1.pack()
        space2 = Label(f4, text = '')
        space2.pack()
        
        l2 = Label(f4, text = 'Phone :', font = ('Kalinga', 10))
        l2.pack()
        e2 = Text(f4, width = 30, height = 1)
        e2.pack()
        space3 = Label(f4, text = '')
        space3.pack()
        
        add = Button(f4, text = 'Add', font = ('Kalinga', 10), width = 8, bg = '#ffffff', command = add)
        add.pack()
        
        a = True
        d = False

# Function for delete button
def b2_click() :
    global f4, a, d
    b1.config(bg = '#ffffff')
    b2.config(bg = '#00bfff')
    b3.config(bg = '#ffffff')
    w.geometry('320x400')
    remove()
    f4 = Frame(f3)
    f4.pack(expand = True, fill = 'both')
    def delete() :
        count = 0
        with open('Contact Book.txt', 'r') as z :
            data = z.readlines()
        with open('Contact Book.txt', 'w') as z :
            for i in data :
                if i != 'Name : ' + str(e3.get('1.0', 'end')) and i != 'Phone : ' + str(e4.get('1.0', 'end')) and i != '\n' :
                    z.write(i)
                    count += 1
                    if count % 2 == 0 :
                        z.write('\n')
            z.close()
        e3.delete('1.0', 'end')
        e4.delete('1.0', 'end')
    if d == False :
        tip2 = Label(f4, text = 'Enter Name and Phone number to be deleted', font = ('Kalinga', 10))
        tip2.pack()
        space1 = Label(f4, text = '')
        space1.pack()
        
        l3 = Label(f4, text = 'Name :', font = ('Kalinga', 10))
        l3.pack()
        e3 = Text(f4, width = 30, height = 1)
        e3.pack()
        space2 = Label(f4, text = '')
        space2.pack()
        
        l4 = Label(f4, text = 'Phone :', font = ('Kalinga', 10))
        l4.pack()
        e4 = Text(f4, width = 30, height = 1)
        e4.pack()
        space3 = Label(f4, text = '')
        space3.pack()
        
        delete = Button(f4, text = 'Delete', font = ('Kalinga', 10), width = 8, bg = '#ffffff', command = delete)
        delete.pack()
        
        a = False
        d = True

# Function for view button
def b3_click() :
    global f4, a, d
    b1.config(bg = '#ffffff')
    b2.config(bg = '#ffffff')
    b3.config(bg = '#00bfff')
    remove()
    book = open('Contact Book.txt', 'a+')
    book.close()
    os.startfile('Contact Book.txt')

# Design and layout of window
l = Label(f1, text = 'Contact Manager', font = ('Kalinga', 20))
l.pack(side = LEFT, expand = True)

b1 = Button(f2, text = 'Add', font = ('Kalinga', 10), width = 8, bg = '#ffffff', command = b1_click)
b1.pack(side = LEFT, expand = True)

b2 = Button(f2, text = 'Delete', font = ('Kalinga', 10), width = 8, bg = '#ffffff', command = b2_click)
b2.pack(side = LEFT, expand = True)

b3 = Button(f2, text = 'View', font = ('Kalinga', 10), width = 8, bg = '#ffffff', command = b3_click)
b3.pack(side = LEFT, expand = True)

w.mainloop()