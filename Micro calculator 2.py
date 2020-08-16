from tkinter import *
from tkinter import messagebox

w = Tk()
w.geometry('250x400')
w.resizable(0, 0)
w.title('Calculator')

v = ''
a = 0
op = ''

# Defination for buttons
def b1_click() :
    global v
    v = v + '1'
    d.set(v)

def b2_click() :
    global v
    v = v + '2'
    d.set(v)

def b3_click() :
    global v
    v = v + '3'
    d.set(v)
    
def b4_click() :
    global v
    v = v + '4'
    d.set(v)
    
def b5_click() :
    global v
    v = v + '5'
    d.set(v)
    
def b6_click() :
    global v
    v = v + '6'
    d.set(v)
    
def b7_click() :
    global v
    v = v + '7'
    d.set(v)

def b8_click() :
    global v
    v = v + '8'
    d.set(v)
    
def b9_click() :
    global v
    v = v + '9'
    d.set(v)
    
def b0_click() :
    global v
    v = v + '0'
    d.set(v)

def b_plus_click() :
    global v, a, op
    a = int(v)
    op = '+'
    v = v + '+'
    d.set(v)

def b_minus_click() :
    global v, a, op
    a = int(v)
    op = '-'
    v = v + '-'
    d.set(v)

def b_multiply_click() :
    global v, a, op
    a = int(v)
    op = '*'
    v = v + '*'
    d.set(v)

def b_divide_click() :
    global v, a, op
    a = int(v)
    op = '/'
    v = v + '/'
    d.set(v)

def b_clear_click() :
    global v, a, op
    v = ''
    a = 0
    op = ''
    d.set(v)

def b_equal_click() :
    global v, a, op
    v2 = v
    if op == '+' :
        b = int((v2.split('+')[1]))
        c = a + b
        v = str(c)
        d.set(v)
    elif op == '-' :
        b = int((v2.split('-')[1]))
        c = a - b
        v = str(c)
        d.set(v)
    elif op == '*' :
        b = int((v2.split('*')[1]))
        c = a * b
        v = str(c)
        d.set(v)
    elif op == '/' :
        b = int((v2.split('/')[1]))
        if b == 0 :
            messagebox.showerror('Error', 'Division by 0 not supported')
            v = ''
            a = 0
            d.set(v)
        else :
            c = a / b
            d.set(c)

# Data entry space setup
d = StringVar()
l = Label(
    w,
    anchor = SE,
    font = ('Kalinga', 20),
    textvariable = d,
    background = '#ffffff',
    fg = '#000000'
    )
l.pack(expand = True, fill = 'both')

# Frame setup
r1 = Frame(w)
r1.pack(expand = True, fill = 'both')
r2 = Frame(w)
r2.pack(expand = True, fill = 'both')
r3 = Frame(w)
r3.pack(expand = True, fill = 'both')
r4 = Frame(w)
r4.pack(expand = True, fill = 'both')

# Button setup
b1 = Button(r1, text = '1', font = ('Kalinga', 20), relief = GROOVE, border = 0, background = '#736f6e', fg = '#ffffff', command = b1_click)
b1.pack(side = LEFT, expand = True, fill = 'both')

b2 = Button(r1, text = '2', font = ('Kalinga', 20), relief = GROOVE, border = 0, background = '#736f6e', fg = '#ffffff', command = b2_click)
b2.pack(side = LEFT, expand = True, fill = 'both')

b3 = Button(r1, text = '3', font = ('Kalinga', 20), relief = GROOVE, border = 0, background = '#736f6e', fg = '#ffffff', command = b3_click)
b3.pack(side = LEFT, expand = True, fill = 'both')

b_plus = Button(r1, text = '+', font = ('Kalinga', 20), relief = GROOVE, border = 0, background = '#736f6e', fg = '#ffffff', command = b_plus_click)
b_plus.pack(side = LEFT, expand = True, fill = 'both')

b4 = Button(r2, text = '4', font = ('Kalinga', 20), relief = GROOVE, border = 0, background = '#736f6e', fg = '#ffffff', command = b4_click)
b4.pack(side = LEFT, expand = True, fill = 'both')

b5 = Button(r2, text = '5', font = ('Kalinga', 20), relief = GROOVE, border = 0, background = '#736f6e', fg = '#ffffff', command = b5_click)
b5.pack(side = LEFT, expand = True, fill = 'both')

b6 = Button(r2, text = '6', font = ('Kalinga', 20), relief = GROOVE, border = 0, background = '#736f6e', fg = '#ffffff', command = b6_click)
b6.pack(side = LEFT, expand = True, fill = 'both')

b_minus = Button(r2, text = '-', font = ('Kalinga', 20), relief = GROOVE, border = 0, background = '#736f6e', fg = '#ffffff', command = b_minus_click)
b_minus.pack(side = LEFT, expand = True, fill = 'both')

b7 = Button(r3, text = '7', font = ('Kalinga', 20), relief = GROOVE, border = 0, background = '#736f6e', fg = '#ffffff', command = b7_click)
b7.pack(side = LEFT, expand = True, fill = 'both')

b8 = Button(r3, text = '8', font = ('Kalinga', 20), relief = GROOVE, border = 0, background = '#736f6e', fg = '#ffffff', command = b8_click)
b8.pack(side = LEFT, expand = True, fill = 'both')

b9 = Button(r3, text = '9', font = ('Kalinga', 20), relief = GROOVE, border = 0, background = '#736f6e', fg = '#ffffff', command = b9_click)
b9.pack(side = LEFT, expand = True, fill = 'both')

b_multiply = Button(r3, text = '*', font = ('Kalinga', 20), relief = GROOVE, border = 0, background = '#736f6e', fg = '#ffffff', command = b_multiply_click)
b_multiply.pack(side = LEFT, expand = True, fill = 'both')

b_clear = Button(r4, text = 'C', font = ('Kalinga', 20), relief = GROOVE, border = 0, background = '#736f6e', fg = '#ffffff', command = b_clear_click)
b_clear.pack(side = LEFT, expand = True, fill = 'both')

b0 = Button(r4, text = '0', font = ('Kalinga', 20), relief = GROOVE, border = 0, background = '#736f6e', fg = '#ffffff', command = b0_click)
b0.pack(side = LEFT, expand = True, fill = 'both')

b_equal = Button(r4, text = '=', font = ('Kalinga', 20), relief = GROOVE, border = 0, background = '#736f6e', fg = '#ffffff', command = b_equal_click)
b_equal.pack(side = LEFT, expand = True, fill = 'both')

b_divide = Button(r4, text = '/', font = ('Kalinga', 20), relief = GROOVE, border = 0, background = '#736f6e', fg = '#ffffff', command = b_divide_click)
b_divide.pack(side = LEFT, expand = True, fill = 'both')

w.mainloop()