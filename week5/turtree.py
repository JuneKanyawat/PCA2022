import turtle
ws = turtle.Screen()
t = turtle.Turtle()

def tree(size):
    if size < 10:
        return
    t.forward(size)
    t.left(30)
    tree(size * 0.5)
    t.right(60)
    tree(size * 0.5)
    t.left(30)
    t.backward(size)
 
tree(150)
