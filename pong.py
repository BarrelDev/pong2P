#Pong in Python
import turtle
import math
import winsound

#Move Player1
def move_down1():
    y = player1.ycor()
    y -= player1speed
    if y < -280:
        y = -280
    player1.sety(y)

def move_up1():
    y = player1.ycor()
    y += player1speed
    if y > 280:
        y = 280
    player1.sety(y)

#Move Player2
def move_down2():
    y = player2.ycor()
    y -= player2speed
    if y < -280:
        y = -280
    player2.sety(y)


def move_up2():
    y = player2.ycor()
    y += player2speed
    if y > 280:
        y = 280
    player2.sety(y)

#Check For Collisions
def inCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 25:
        return True
    else:
        return False

#Write the Score
def drawScore():
    global score1
    global score2
    #Set the score
    score_pen.setposition(-290, 280)
    scorestring1 = "Score: %s" % score1
    score_pen.write(scorestring1, False, align="left", font=("Arial", "14", "normal"))
    score_pen.setposition(290, 280)
    scorestring2 = "Score: %s" % score2
    score_pen.write(scorestring2, False, align="right", font=("Arial", "14", "normal"))
    score_pen.hideturtle()

#Start Up Command
start = input("Welcome to Pong! Press enter to begin.")

#Setting up Screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Pong")

#set score to 0
score1 = 0
score2 = 0

#Draw the score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring1 = "Score: %s" %score1
score_pen.write(scorestring1, False, align="left", font=("Arial", "14", "normal"))
score_pen.setposition(290, 280)
scorestring2 = "Score: %s" %score2
score_pen.write(scorestring2, False, align="right", font=("Arial", "14", "normal"))
score_pen.hideturtle()

#Register Shapes
turtle.register_shape("pongrect.gif")

#Draw a Border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
   border_pen.fd(600)
   border_pen.lt(90)
border_pen.penup()
border_pen.pensize(6)
border_pen.setposition(0, 300)
border_pen.pendown()
border_pen.setheading(270)
border_pen.fd(600)
border_pen.hideturtle()

#Create Player Turtle1
player1 = turtle.Turtle()
player1.color("white")
player1.shape("pongrect.gif")
player1.penup()
player1.speed(0)
player1.setposition(250, 0)
player1.setheading(90)
player1speed = 15

#Create Player Turtle2
player2 = turtle.Turtle()
player2.color("white")
player2.shape("pongrect.gif")
player2.penup()
player2.speed(0)
player2.setposition(-250, 0)
player2.setheading(90)
player2speed = 15

#Create the player ball
ball = turtle.Turtle()
ball.color("white")
ball.shape("circle")
ball.penup()
ball.speed(0)
ball.setheading(90)
ball.shapesize(0.5, 0.5)
ball.dx = 2
ball.dy = 0
gravity = 0.06

#Create Keyboard Bindings
turtle.listen()
turtle.onkey(move_down1, "Down")
turtle.onkey(move_up1, "Up")
turtle.onkey(move_down2, "s")
turtle.onkey(move_up2, "w")

#Main Game Loop
while True:

    #Set the score
    drawScore()

    #Move the ball
    ball.dy -= gravity
    ball.sety(ball.ycor()+ball.dy)
    ball.setx(ball.xcor()+ball.dx)
    if inCollision(player1, ball):
        winsound.PlaySound("ballbump.wav", winsound.SND_ASYNC)
        ball.dx += 1
        ball.dx *= -1
        ball.sety(ball.ycor() + gravity)
    if inCollision(player2, ball):
        winsound.PlaySound("ballbump.wav", winsound.SND_ASYNC)
        ball.dx += 1
        ball.dx *= -1
        ball.sety(ball.ycor() + gravity)
    if ball.ycor() < -280:
        ball.dy *= -1
    if ball.ycor() > 280:
        ball.dy *= -1
    if ball.xcor() > 280:
        score_pen.clear()
        score1 += 1
        ball.setposition(0, 0)
    if ball.xcor() < -280:
        score2 += 1
        ball.setposition(0, 0)
        score_pen.clear()

turtle.mainloop()