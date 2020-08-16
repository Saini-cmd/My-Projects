from turtle import *
from random import *
setup(width = 1200, height = 700)
speed(5)
pensize(3)
hideturtle()

penup()
goto(-300, -300)
pendown()
for i in range(4) :
    forward(600)
    left(90)
penup()
goto(-200, -200)
pendown()
forward(100)
goto(-150, -200)
left(90)
forward(450)
right(90)
forward(150)
right(90)
forward(50)

def head() :
    penup()
    goto(0, 100)
    left(90)
    pendown()
    circle(50)
    right(90)
    
def body() :
    penup()
    goto(0, 100)
    pendown()
    forward(150)
    
def lefthand() :
    penup()
    goto(0, 100)
    right(45)
    pendown()
    forward(75)
    left(45)
    
def righthand() :
    penup()
    goto(0, 100)
    left(45)
    pendown()
    forward(75)
    right(45)

def leftleg() :
    penup()
    goto(0, -50)
    right(45)
    pendown()
    forward(75)
    left(45)
    
def rightleg():
    penup()
    goto(0, -50)
    left(45)
    pendown()
    forward(75)
    right(45)

def draw() :
    if cd == 0 :
        head()
    elif cd == 1 :
        body()
    elif cd == 2 :
        lefthand()
    elif cd == 3 :
        righthand()
    elif cd == 4 :
        leftleg()
    else :
        rightleg()

m = -500
n = 0
p = 0
q = -200
ch = 0
cd = 0
t = 0
i = 0
z = ['pencil', 'orange', 'spider', 'parrot', 'spring', 'office']
y = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth']
x = z[randint(0, 5)]

penup()
goto(400, 200)
write('Hint :')
if x == z[0] :
    goto(400, 180)
    write('Wooden stick used for writing.')
elif x == z[1] :
    goto(400, 180)
    write('A colour and a fruit.')
elif x == z[2] :
    goto(400, 180)
    write('Web spinning insect.')
elif x == z[3] :
    goto(400, 180)
    write('Green coloured bird.')
elif x == z[4] :
    goto(400, 180)
    write('Blooming season.')
else :
    goto(400, 180)
    write('Place of work for employees.')

while ch < 6 and cd < 6:
    a = textinput('Hangman', 'Enter ' + y[i] + ' letter.')
    if a == x[i] :
        penup()
        goto(m, n)
        n -= 10
        write('Letter correct.')
        goto(p, q)
        p += 10
        write(x[i])
        ch += 1
        i += 1
    else :
        draw()
        cd += 1

if ch == 6 :
    penup()
    goto(400, 160)
    write('You won.')
else :
    penup()
    goto(400, 160)
    write('You lost.')
exitonclick()