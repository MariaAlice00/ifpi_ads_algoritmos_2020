import math
import turtle

def d_torta(t, n, r):
    torta(t, n, r)
    t.pu()
    t.fd(r*2 + 10)
    t.pd()

def torta(t, n, r):
    ang = 360.0 / n
    for i in range(n):
        triangulo(t, r, ang/2)
        t.lt(ang)

def triangulo(t, r, ang):
    y = r * math.sin(ang * math.pi / 180)
    t.rt(ang)
    t.fd(r)
    t.lt(90+ang)
    t.fd(2*y)
    t.lt(90+ang)
    t.fd(r)
    t.lt(180-ang)

bob = turtle.Turtle()

bob.pu()
bob.bk(130)
bob.pd()

tam = 40
d_torta(bob, 5, tam)
d_torta(bob, 6, tam)
d_torta(bob, 7, tam)

bob.hideturtle()
turtle.mainloop()