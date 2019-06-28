import turtle
import time
import random

delay = 0.2

# Score
score = 0
high_score = 0


# Make a Window object
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0)

# Creating the head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"

segment = []

# Score Display

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score : 0  HighScore: 0", align="center",
          font=("Arial", 24, "normal"))


# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)


# Now lets update the screen
# Few functions


def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)


# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, 'Up')
wn.onkeypress(go_down, 'Down')
wn.onkeypress(go_left, 'Left')
wn.onkeypress(go_right, 'Right')


# Main game loop
while True:
    wn.update()

    # Collisions with window
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
        for s in segment:
            s.goto(10000, 10000)
        segment.clear()

        # Reset delay
        delay = 0.2
        # Reset the score
        score = 0
        pen.clear()
        pen.write("Score : {}  HighScore: {}".format(score, high_score), align="center",
                  font=("Courier", 24, "normal"))

    # If snake eats food move food to a random location
    if head.distance(food) < 20:
        # move to random location
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # decrease the delay
        delay -= 0.001

        # Update Score
        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score : {}  HighScore: {}".format(score, high_score), align="center",
                  font=("Courier", 24, "normal"))

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segment.append(new_segment)
    # move the last segement to the last but one segement and so on...
    for index in range(len(segment)-1, 0, -1):
        x = segment[index-1].xcor()
        y = segment[index-1].ycor()
        segment[index].goto(x, y)
    # move segment 0 to where the head is
    if len(segment) > 0:
        x = head.xcor()
        y = head.ycor()
        segment[0].goto(x, y)

    # Collision with itself
    move()
    for s in segment:
        if head.distance(s) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            for s in segment:
                s.goto(10000, 10000)
            segment.clear()

            # Reset the score
            score = 0
            pen.clear()
            pen.write("Score : {}  HighScore: {}".format(score, high_score), align="center",
                      font=("Courier", 24, "normal"))
            # Reset dealy
            delay = 0.2
    time.sleep(delay)


wn.mainloop()
