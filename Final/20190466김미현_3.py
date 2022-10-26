import turtle
import random

#별찍기
def draw(x, y):
    up_pen()
    t1.goto(x, y)
    t1.begin_fill()
    num = random.randint(15, 31)
    for i in range(10):
        if i % 2 == 0:
            t1.right(144)
        else:
            t1.right(72)
        t1.forward(num)
    t1.end_fill()
    down_pen()

#키보드 입력
def turn_left():
    t1.setheading(180)
    t1.forward(30)

def turn_right():
    t1.setheading(0)
    t1.write("반짝")
    t1.forward(30)
    
def turn_up():
    t1.setheading(90)
    t1.forward(30)

def turn_down():
    t1.setheading(-90)#또는 270도
    t1.forward(30)

def up_pen():
    t1.up()
    
def down_pen():
    t1.down()



t1 = turtle.Turtle()
t1.color("yellow","yellow")
turtle.bgcolor("black")

screen = turtle.Screen()
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.onkey(turn_up, "Up")
screen.onkey(turn_down, "Down")
screen.onkey(up_pen, "u")
screen.onkey(down_pen, "d")

screen.onscreenclick(draw)
screen.listen()
screen.mainloop()
