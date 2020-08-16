from tkinter import *

w = Tk()
w.title('Micro Calculator')

e = Entry(w, width = 50, borderwidth = 5)
e.grid(row = 0, column = 0, columnspan = 4, padx = 10, pady = 10)

# Arithematic fuctions
def button_click(number) :
    c = e.get()
    e.delete(0, END)
    e.insert(0, str(c) + str(number))

def button_clear() :
    e.delete(0, END)

def button_equal() :
    s_num = e.get()
    e.delete(0, END)
    if a == 'add' :
        e.insert(0, f_num + int(s_num))
    elif a == 'subtract' :
        e.insert(0, f_num - int(s_num))
    elif a == 'multiply' :
        e.insert(0, f_num * int(s_num))
    else :
        e.insert(0, f_num / int(s_num))

def button_add() :
    first_num = e.get()
    if e.get() == '' :
        first_num = 0
    global a
    a = 'add'
    global f_num
    f_num = int(first_num)
    e.delete(0, END)

def button_subtract() :
    first_num = e.get()
    if e.get() == '' :
        first_num = 0
    global a
    a = 'subtract'
    global f_num
    f_num = int(first_num)
    e.delete(0, END)

def button_multiply() :
    first_num = e.get()
    if e.get() == '' :
        first_num = 0
    global a
    a = 'multiply'
    global f_num
    f_num = int(first_num)
    e.delete(0, END)

def button_divide() :
    first_num = e.get()
    if e.get() == '' :
        first_num = 0
    global a
    a = 'divide'
    global f_num
    f_num = int(first_num)
    e.delete(0, END)

# Button definition
b1 = Button(w, text = '1', padx = 40, pady = 20, command = lambda : button_click(1))
b2 = Button(w, text = '2', padx = 40, pady = 20, command = lambda : button_click(2))
b3 = Button(w, text = '3', padx = 40, pady = 20, command = lambda : button_click(3))
b4 = Button(w, text = '4', padx = 40, pady = 20, command = lambda : button_click(4))
b5 = Button(w, text = '5', padx = 40, pady = 20, command = lambda : button_click(5))
b6 = Button(w, text = '6', padx = 40, pady = 20, command = lambda : button_click(6))
b7 = Button(w, text = '7', padx = 40, pady = 20, command = lambda : button_click(7))
b8 = Button(w, text = '8', padx = 40, pady = 20, command = lambda : button_click(8))
b9 = Button(w, text = '9', padx = 40, pady = 20, command = lambda : button_click(9))
b0 = Button(w, text = '0', padx = 40, pady = 20, command = lambda : button_click(0))
b_clear = Button(w, text = 'Clear', padx = 30, pady = 20, command = button_clear)
b_equal = Button(w, text = '=', padx = 39, pady = 20, command = button_equal)
b_add = Button(w, text = '+', padx = 38, pady = 20, command = button_add)
b_subtract = Button(w, text = '-', padx = 39, pady = 20, command = button_subtract)
b_multiply = Button(w, text = '*', padx = 39, pady = 20, command = button_multiply)
b_divide = Button(w, text = '/', padx = 39, pady = 20, command = button_divide)

# Button placement
b1.grid(row = 3, column = 0)
b2.grid(row = 3, column = 1)
b3.grid(row = 3, column = 2)
b4.grid(row = 2, column = 0)
b5.grid(row = 2, column = 1)
b6.grid(row = 2, column = 2)
b7.grid(row = 1, column = 0)
b8.grid(row = 1, column = 1)
b9.grid(row = 1, column = 2)
b0.grid(row = 4, column = 1)
b_clear.grid(row = 4, column = 0)
b_equal.grid(row = 4, column = 2)
b_add.grid(row = 4, column = 3)
b_subtract.grid(row = 3, column = 3)
b_multiply.grid(row = 2, column = 3)
b_divide.grid(row = 1, column = 3)

w.mainloop()