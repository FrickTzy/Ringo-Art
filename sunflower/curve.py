import turtle

# Create turtle object
t = turtle.Turtle()

# Set speed
t.speed(1)

# Draw a curved line
t.setheading(90)
for i in range(20):
    t.forward(10)
    t.left(1)

# Hide turtle and display the result
t.hideturtle()
turtle.done()
