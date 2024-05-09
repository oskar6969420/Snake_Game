import turtle
import time
import random

delay = 0.05

window = turtle.Screen()
window.bgcolor("green")
window.title("Snake game by Oskar")
window.setup(width=600, height=600)

snake = turtle.Turtle()
snake.shape("square")
snake.color("blue")
snake.speed(0)
snake.penup()
snake.goto(0,0)
snake.direction = "stop"

food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.speed(0)
food.penup()
food.goto(0,100)
food.direction = "stop"

bodys = []

def moving():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)
    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)
    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 20)
    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 20)

def up():
    if snake.direction != "down":
        snake.direction = "up"
def down():
    if snake.direction != "up":
        snake.direction = "down"
def right():
    if snake.direction != "left":
        snake.direction = "right"
def left():
    if snake.direction != "right":
        snake.direction = "left"

turtle.onkeypress(up, "w")
turtle.onkeypress(down, "s")
turtle.onkeypress(right, "d")
turtle.onkeypress(left, "a")
turtle.listen()

while True:
    window.update()

    if snake.ycor() > 290 or snake.ycor() < -290 or snake.xcor() > 290 or snake.xcor() < -290:
        snake.direction = "stop"
        snake.goto(0,0)
        time.sleep(1)


    if snake.distance(food) < 20:
        y = random.randint(-290, 290)
        x = random.randint(-290, 290)
        food.goto(x, y)

        new_body = turtle.Turtle()
        new_body.color("grey")
        new_body.speed(0)
        new_body.shape("square")
        new_body.penup()
        bodys.append(new_body)

    for index in range(len(bodys)-1, 0, -1):
        x = bodys[index-1].xcor()
        y = bodys[index-1].ycor()
        bodys[index].goto(x,y)

    if len(bodys) > 0:
        x = snake.xcor()
        y = snake.ycor()
        bodys[0].goto(x,y)

    moving()

    for body in bodys:
        if body.distance(snake) < 20:
            time.sleep(1)
            snake.goto(0,0)
            snake.direction = "stop"
            
            for body in bodys:
                body.goto(1000,1000)
            bodys.clear()


    time.sleep(delay)
