import turtle
turtle.left(90)

UP = 0

direction = None

print(direction)

def up():
    global direction
    direction = UP
    print("you pressed the up key.")
    print(direction)
    on_move()

def right():
    turtle.right(10)


    
turtle.onkey(up,"Up")
turtle.listen()

def on_move():
    (x,y) = turtle.pos()
    if direction == UP:
        turtle.forward(5)
                       

turtle.mainloop()
