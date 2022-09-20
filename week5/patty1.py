import turtle
ws = turtle.Screen()
t = turtle.Turtle()

def dott(n):
    for i in range(n):
        t.pendown()
        t.dot()
        t.penup()
        t.forward(10)
  

def down(n):
    t.penup()
    t.goto(0,n*10)
    print(n*10)
    dott(n)
    if n > 1:
        down(n-1)
    

def up(n,s):
    t.goto(0,10-(s*10))
    print(10-(s*10))
    dott(s)
    if s < n:
        up(n,s+1)


def main(n):
    down(n)
    up(n,1)

main(4)