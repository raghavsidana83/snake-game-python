import turtle
import random
import time
delay=0.1
sc=0
hs=0
bodies=[]

#creating a screen
s1=turtle.Screen()
s1.title("Snake Game")
s1.bgcolor("light blue")
s1.setup(height=600,width=600)
s1.tracer(0)

#creating a head
h1=turtle.Turtle()
h1.shape("circle")
h1.color("red")
h1.fillcolor("blue")
h1.speed(0)
h1.penup()
h1.ht()
h1.goto(0,0)
h1.st()
h1.direction="stop"

#creating a food
f1=turtle.Turtle()
f1.shape("square")
f1.color("green")
f1.speed(0)
f1.penup()
f1.ht()
f1.goto(-280,200)
f1.st()
f1.direction="stop"


#creating a scoreboard
sb=turtle.Turtle()
sb.ht()
sb.penup()
sb.goto(-260,280)
sb.write("Scored:0 | Highest Score:0")

#game over message
gm=turtle.Turtle()
gm.ht()
gm.penup()
gm.color("red")
gm.goto(0,0)

def moveup():
    if h1.direction!="down":
        h1.direction="up"

def movedown():
    if h1.direction!="up":
        h1.direction="down"

def moveright():
    if h1.direction!="left":
        h1.direction="right"

def moveleft():
    if h1.direction!="right":
        h1.direction="left"

def movestop():
    h1.direction="stop"

def restart():
    global sc, delay

    h1.goto(0,0)
    h1.direction="stop"

    for b in bodies:
        b.ht()

    bodies.clear()
    sc=0
    delay=0.1

    gm.clear()
    sb.clear()
    sb.write(
        "Score: {} | High Score: {}".format(sc,hs),
        font=("Arial",14,"bold")
    )


def move():
    if h1.direction=="up":
        y=h1.ycor()
        h1.sety(y+20)
    if h1.direction=="down":
        y=h1.ycor()
        h1.sety(y-20)
    if h1.direction=="left":
        x=h1.xcor()
        h1.setx(x-20)
    if h1.direction=="right":
        x=h1.xcor()
        h1.setx(x+20)

#event handling
s1.listen()
s1.onkey(moveup,"Up")
s1.onkey(movedown,"Down")
s1.onkey(moveleft,"Left")
s1.onkey(moveright,"Right")
s1.onkey(movestop,"space")
s1.onkey(restart,"r")

while True:
    s1.update()
    #check collision with border
    if h1.xcor()>290:
        h1.setx(-300)
    if h1.xcor()<-290:
        h1.setx(300)
    if h1.ycor()>290:
        h1.sety(-300)
    if h1.ycor()<-290:
        h1.sety(300)
    #check collision with food
    if h1.distance(f1)<20:
        x=random.randrange(-280,281,20)
        y=random.randrange(-240,241,20)
        f1.goto(x,y)
        #increase the length of snake
        body=turtle.Turtle()
        body.speed(0)
        body.shape("square")
        body.penup()
        body.color("yellow")
        bodies.append(body)
        sc=sc+100
        if sc>hs:
            hs=sc
        sb.clear()
        sb.write( "Score: {} | High Score: {}".format(sc, hs),font=("Arial", 14, "bold"))
        delay=max(0.04,delay-0.001)
    #move snake body
    for i in range(len(bodies)-1,0,-1):
        x=bodies[i-1].xcor()
        y=bodies[i-1].ycor()
        bodies[i].goto(x,y)
    if len(bodies)>0:
        x=h1.xcor()
        y=h1.ycor()
        bodies[0].goto(x,y)
    move()
    #check collision with body
        #check collision with body
    for b in bodies:
        if b.distance(h1)<20:
            h1.direction="stop"
            gm.goto(0,0)
            gm.write(
                "GAME OVER\nPress R to Restart",
                align="center",
                font=("Arial",18,"bold")
            )
            break
    time.sleep(delay)
s1.mainloop()


