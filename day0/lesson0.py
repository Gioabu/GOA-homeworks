from turtle import *

#we want to paint a house

#step 1: draw a square
speed(10)
width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door

forward(70)
color("yellow")
left(90)
forward(120)    #height of the door
right(90)
forward(60)
right(90)
forward(120)

penup()
goto(200, 200)
pendown()

#drawing the roof

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()


#left window
color("red")
left(30)
forward(60)
left(90)
forward(10)
color("lightblue")       
begin_fill()
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()


penup()
goto(200, 200)
pendown()


#right window
color("red")
forward(60)
right(90)
forward(10)
color("lightblue")
begin_fill()
forward(50)
right(90)                
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()

exitonclick()