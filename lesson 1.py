from turtle import*


#we want to paint a house
#draw the square base
speed(10)
width(7)
color("purple")
begin_fill()
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
end_fill()
#end of house base 


#drawing a door


forward(70)
color("yellow")
begin_fill()
left(90)
forward(100)
right(90)
forward(60)
right(90)
forward(100)
end_fill()

#end of door drawing
penup()
goto(200,200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#end of roof drawing

penup()
goto(170,170)
pendown()

color("brown")
begin_fill()
left(30)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)

#end of right window drawing
penup()
goto(30,170)
pendown()

forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)

end_fill()

#end of left window drawing



exitonclick()




