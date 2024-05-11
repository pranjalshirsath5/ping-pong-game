import turtle


#create a screen
sc = turtle.Screen()
sc.title("Ping Pong Game")
sc.bgcolor("Black")
sc.setup(width=800 , height=600)
sc.tracer()

#creating left paddle a
paddle_a=turtle.Turtle()  # t small for margin and capital t for class name
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("Red")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

#creating right paddle b
paddle_b=turtle.Turtle()  # t small for margin and capital t for class name
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("Blue")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

#creating a ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 2
ball.dy = -2

#initialize the condition
score_a=0
score_b=0

#pen
pen=turtle.Turtle()
pen.speed(0)
pen.color("White")
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A:0  Player B:0",align="center",font=("Courier",24,"normal"))

#move a paddle
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)    
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

#short keys to move paddle
sc.listen()
sc.onkeypress(paddle_a_up,"w")
sc.onkeypress(paddle_a_down,"s")
sc.onkeypress(paddle_b_up,"Up")
sc.onkeypress(paddle_b_down,"Down")

while True:
    sc.update()

#movement of ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

#collision of ball with four side    
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1   
    
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A :{}  Player B :{}".format(score_a,score_b) ,align="center",font=("Courier",24,"normal"))

    
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A:{} Player B:{}".format(score_a,score_b),align="center",font=("Courier",24,"normal"))

        
   
    #ball and paddle collision    
    if (ball.xcor() >  340 and ball.xcor() < 350)  and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
         ball.setx(340)
         ball.dx = -1
    if (ball.xcor() <  -340 and ball.xcor() > -350)  and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
         ball.setx(340)
         ball.dx = -1
