import turtle

t1 = turtle.Turtle()#클래스와 생성자
t1.shape("turtle")
t1.forward(100)
t1.backward(200)
t1.right(90)
t1.goto(-100, 100)
t1.up()
t1.goto(200,300)
t1.color('red')
t1.fillcolor('yellow')
t1.circle(50)
t1.pendown()
t1.circle(50)
t1.begin_fill()
t1.circle(50)
t1.end_fill()
t1.goto(0,0)
t1.setheading(0)#거북이 머리 방향 바꾸기, 오른쪽
t1.setheading(90)
t1.stamp()
t1.forward(100)
t1.speed(1)#스피드는 0이 가장 빠르고 가장 늦는 것은 1
for i in range(4) :
    t1.forward(100)
    t1.right(90)
t1.speed(0)
for i in range(3):
    t1.forward(100)
    t1.right(120)#삼각형, 외각형을 기준으로..

t1.hideturtle()
t1.showturtle()
turtle.bgcolor("black")#배경색 바꾸기

turtle.done()#내가 닫을때까지 닫지마.
