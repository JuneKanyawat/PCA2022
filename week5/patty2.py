import turtle
ws = turtle.Screen()
t = turtle.Turtle()
def dott(n):
    for i in range(n):
        t.pendown()
        t.dot()
        t.penup()
        t.forward(10)
  

def down(n,s):
    t.penup()
    t.goto(0,(n*10)-(s+1)*10)
    dott(n)
    if n > 1:
        down(n-1,s)
    

def up(n,s):
    t.penup()
    t.goto(0,n*10-s*10)
    dott(s)
    if s < n:
        up(n,s+1)


def main(n):
    up(n,1)
    down(n,n)

main(7)