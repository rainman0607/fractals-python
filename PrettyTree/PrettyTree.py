import turtle

t = turtle.Turtle()
t.left(90)

def Tree(n):
    t.speed(n * 1.5)

    if n < 10:
        return
    else:
        t.forward(n)
        t.left(30)
        Tree(3*n / 4)
        t.right(60)
        Tree(3*n / 4)
        t.left(30)
        t.backward(n)



Tree(100)
turtle.done()


