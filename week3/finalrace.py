import random, turtle
myscreen= turtle.Screen()
myscreen.bgcolor('gray')
myscreen.setup(1.0,1.0)
myscreen.title('Turtle Race Game')
pen=turtle.Turtle()
pen.speed(7)
pen.penup()
pen.goto(-240,200)
pen.write("START")
pen.goto(-200,200) 
pen.pendown()
pen.setheading(-90)
pen.forward(250)  
pen.back(250) 
pen.penup()
pen.setheading(0)
pen.forward(455)
pen.write("       FINISH")
pen.down()
pen.pendown()
pen.setheading(-90)
pen.forward(250)  
pen.back(250) 
pen.penup()
pen.setheading(0)
pen.penup()

pen.goto(-260,250)
pen.down()
pen.forward(580)
pen.right(90)
pen.forward(330)
pen.right(90)
pen.down()
pen.forward(580)
pen.right(90)
pen.forward(330)
pen.penup()



class TurtleFPO(turtle.Turtle):
    def __init__(self, shape, undobuffersize, visible,energy):
        super().__init__(shape, undobuffersize, visible)
        self.energy = energy
        
def createTurtlePlayer(color, startx, starty,energy): 
    player=TurtleFPO("turtle",0,True,energy)
    player.color(color) 
    player.penup() 
    player.goto(startx, starty)
    player.pendown() 
    return player

p1=createTurtlePlayer('light blue',-210,150,500) 
p2=createTurtlePlayer('light green',-210,100,500) 
p3=createTurtlePlayer('light yellow',-210,50,500) 
p4=createTurtlePlayer('pink',-210,0,250) 
finishLine=240

pen.goto(-240,280)
pen.down()
pen.forward(50)
pen.right(120)
pen.forward(25)
pen.right(120)
pen.forward(25)
pen.penup()
pen.hideturtle()

while True:
    if p1.energy > 0:
        distance1=random.randint(10,50)
        p1.forward(distance1)
        p1.energy-=distance1
        if p1.pos()[0]>=finishLine:
            p1.write('        WINNER!!')
            break
    else:
       p1.write('      TRIED!!')

    if p2.energy > 0:
        distance2=random.randint(10,50)
        p2.forward(distance2)
        p2.energy-=distance2
        if p2.pos()[0]>=finishLine:
            p2.write('        WINNER!!')
            break
    else:
       p2.write('      TRIED!!')

    if p3.energy > 0:     
        distance3 = random.randint(10,50)
        p3.forward(distance3)
        p3.energy-=distance3
        if p3.pos()[0]>=finishLine:
            p3.write('        WINNER!!')
            break
    else:
       p3.write('      TRIED!!')

    if p4.energy > 0:
        distance4 = random.randint(10,50)
        p4.forward(distance3)
        p4.energy-=distance3
        if p4.pos()[0]>=finishLine:
            p4.write('        WINNER!!')
            break
    else:
       p4.write('      TRIED!!') 
    
pen.forward(900)
turtle.exitonclick()

