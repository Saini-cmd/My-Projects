from turtle import *
setup(width = 1200, height = 700)
speed(9)
pensize(3)
hideturtle()

penup()
goto(-100, 300)
right(90)
pendown()
forward(600)
penup()
goto(100, -300)
right(180)
pendown()
forward(600)
penup()
goto(300, 100)
left(90)
pendown()
forward(600)
penup()
goto(-300, -100)
left(180)
pendown()
forward(600)

def o() :
    penup()
    right(90)
    forward(70)
    left(90)
    pendown()
    circle(70)

def x() :
    penup()
    left(135)
    forward(100)
    pendown()
    backward(200)
    left(45)
    penup()
    forward(140)
    right(135)
    pendown()
    forward(200)
    right(45)
    
def ai() :
    penup()
    goto(-200, 200)
    
def bi() :
    penup()
    goto(0, 200)

def ci() :
    penup()
    goto(200, 200)
    
def di() :
    penup()
    goto(-200, 0)
    
def ei() :
    penup()
    goto(0, 0)
    
def fi() :
    penup()
    goto(200, 0)
    
def gi() :
    penup()
    goto(-200, -200)
    
def hi() :
    penup()
    goto(0, -200)
    
def ii() :
    penup()
    goto(200, -200)

def exm() :
    global win
    global br
    while True :
        if f1==f2==f3==1 or f4==f5==f6==1 or f7==f8==f9==1 or f1==f4==f7==1 or f2==f5==f8==1 or f3==f6==f9==1 or f1==f5==f9==1 or f3==f5==f7==1 :
            penup()
            goto(m, n)
            write('Player 1 won.')
            win += 1
            br += 1
            break
        elif f1==f2==f3==2 or f4==f5==f6==2 or f7==f8==f9==2 or f1==f4==f7==2 or f2==f5==f8==2 or f3==f6==f9==2 or f1==f5==f9==2 or f3==f5==f7==2 :
            penup()
            goto(m, n)
            write('Player 2 won.')
            win += 1
            br += 1
            break
        elif win == 0 and count == 9:
            penup()
            goto(m, n)
            write('Nobody won. Match draw.')
            br += 1
            break
        else :
            penup()
            break

f1 = f2 = f3 = f4 = f5 = f6 = f7 = f8 = f9 = 0
m = -500
n = 0
win = 0
br = 0
count = 1

while count < 10 :
    if count % 2 != 0 :
        q = 'Player 1'
    else :
        q = 'Player 2'
    a = int(textinput('Field Selection Box', q + ', choose your field.'))

    if a > 9 or a < 1 :
        penup()
        goto(m, n)
        write('Enter number from 1 to 9.')
        n -= 10
    
    elif count % 2 != 0 and a == 1 and f1 == 0 :
        ai()
        o()
        f1 = 1
        exm()

    elif count % 2 != 0 and a == 2 and f2 == 0 :
        bi()
        o()
        f2 = 1
        exm()

    elif count % 2 != 0 and a == 3 and f3 == 0 :
        ci()
        o()
        f3 = 1
        exm()

    elif count % 2 != 0 and a == 4 and f4 == 0 :
        di()
        o()
        f4 = 1
        exm()

    elif count % 2 != 0 and a == 5 and f5 == 0 :
        ei()
        o()
        f5 = 1
        exm()
        
    elif count % 2 != 0 and a == 6 and f6 == 0 :
        fi()
        o()
        f6 = 1
        exm()
        
    elif count % 2 != 0 and a == 7 and f7 == 0 :
        gi()
        o()
        f7 = 1
        exm()
        
    elif count % 2 != 0 and a == 8 and f8 == 0 :
        hi()
        o()
        f8 = 1
        exm()
        
    elif count % 2 != 0 and a == 9 and f9 == 0 :
        ii()
        o()
        f9 = 1
        exm()

    elif count % 2 == 0 and a == 1 and f1 == 0 :
        ai()
        x()
        f1 = 2
        exm()

    elif count % 2 == 0 and a == 2 and f2 == 0 :
        bi()
        x()
        f2 = 2
        exm()

    elif count % 2 == 0 and a == 3 and f3 == 0 :
        ci()
        x()
        f3 = 2
        exm()

    elif count % 2 == 0 and a == 4 and f4 == 0 :
        di()
        x()
        f4 = 2
        exm()

    elif count % 2 == 0 and a == 5 and f5 == 0 :
        ei()
        x()
        f5 = 2
        exm()
        
    elif count % 2 == 0 and a == 6 and f6 == 0 :
        fi()
        x()
        f6 = 2
        exm()
        
    elif count % 2 == 0 and a == 7 and f7 == 0 :
        gi()
        x()
        f7 = 2
        exm()
        
    elif count % 2 == 0 and a == 8 and f8 == 0 :
        hi()
        x()
        f8 = 2
        exm()
        
    elif count % 2 == 0 and a == 9 and f9 == 0 :
        ii()
        x()
        f9 = 2
        exm()
           
    else :
        penup()
        goto(m, n)
        write('Field is taken. Choose an empty field.')
        count -= 1
        n -= 10
    count += 1
    
    if br == 1:
        break

exitonclick()