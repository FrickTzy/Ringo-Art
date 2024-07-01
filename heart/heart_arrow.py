# import package
import turtle

# record a polygon
turtle.begin_poly()

# form a polygon
turtle.color("red", "pink")
turtle.begin_fill()
turtle.left(140)
turtle.forward(15)
turtle.circle(-7, 200)
turtle.left(120)
turtle.circle(-7, 200)
turtle.forward(15)
turtle.end_fill()
turtle.end_poly()

# get polygon
pairs = turtle.get_poly()
print(pairs)

# register shape with
# name : new_shape
# polygon : pairs
turtle.register_shape("new_shape", pairs)

# clear screen
turtle.clearscreen()

# use new shape and
# apply properties
turtle.shape("new_shape")
turtle.fillcolor("blue")

# do some motion
for i in range(50):
	turtle.forward(5+2*i)
	turtle.right(45)
