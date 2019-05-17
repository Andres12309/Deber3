import turtle
import os
t=turtle.Pen()


ven=turtle.Screen()
t.color('red')
ven.bgcolor('lightblue')

#J
t.up()
t.right(180)
t.forward(400)
t.right(90)
t.forward(250)
t.right(-90)
t.down()
t.right(180)
t.forward(200)
t.up()
t.right(180)
t.forward(100)
t.down()
t.right(-90)
t.forward(300)
t.right(90)
t.forward(100)

#u

t.up()
t.right(90)
t.forward(300)
t.right(90)
t.forward(225)
t.down()
t.right(90)
t.forward(300)
t.right(-90)
t.forward(150)
t.right(-90)
t.forward(300)

#A
t.up()
t.right(90)
t.forward(25)
t.right(90)
t.forward(300)
t.down()
t.right(-90)
t.left(75)
t.forward(300)
t.right(75)
t.forward(80)
t.right(76)
t.forward(150)
t.right(105)
t.forward(150)
t.left(180)
t.forward(150)
t.right(76)
t.forward(150)

#N
t.up()
t.right(-76)
t.forward(25)
t.down()
t.right(-90)
t.forward(300)
t.right(150)
t.forward(325)
t.right(-150)
t.forward(300)


turtle.getscreen()._root.mainloop()