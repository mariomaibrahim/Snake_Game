import turtle
import time
import random
import math

delay = 0.15
score = 0
high_score = 0

window = turtle.Screen()
window.title("🐍 SNAKE GAME BY MARIAM IBRAHIM 🐍")
window.bgcolor("#0f0f23")
window.setup(width=600, height=600)
window.cv._rootwindow.resizable(False, False)
window.tracer(0)

border = turtle.Turtle()
border.speed(0)
border.shape("square")
border.color("#00ff88")
border.penup()
border.goto(-290, 290)
border.pendown()
border.pensize(4)
border.begin_fill()
for _ in range(4):
    border.forward(580)
    border.right(90)
border.end_fill()
border.penup()
border.goto(-285, 285)
border.pendown()
border.color("#0f0f23")
border.pensize(2)
border.begin_fill()
for _ in range(4):
    border.forward(570)
    border.right(90)
border.end_fill()
border.hideturtle()

grid_drawer = turtle.Turtle()
grid_drawer.speed(0)
grid_drawer.color("#1a1a3a")
grid_drawer.penup()
for x in range(-280, 300, 20):
    grid_drawer.goto(x, -270)
    grid_drawer.pendown()
    grid_drawer.goto(x, 270)
    grid_drawer.penup()
for y in range(-270, 290, 20):
    grid_drawer.goto(-280, y)
    grid_drawer.pendown()
    grid_drawer.goto(280, y)
    grid_drawer.penup()
grid_drawer.hideturtle()

head = turtle.Turtle()
head.shape("circle")
head.color("#ffffff")
head.penup()
head.speed(0)
head.goto(0, 0)
head.shapesize(1.2, 1.2)
head.direction = "stop"

food = turtle.Turtle()
food.shape("circle")
food.color("#ecc31d")
food.penup()
food.speed(0)
food.goto(0, 100)
food.shapesize(0.8, 0.8)

glow_food = turtle.Turtle()
glow_food.shape("circle")
glow_food.color("#ecc31d")
glow_food.penup()
glow_food.speed(0)
glow_food.goto(0, 100)
glow_food.shapesize(1.2, 1.2)

title_pen = turtle.Turtle()
title_pen.shape("square")
title_pen.color("#00ff88")
title_pen.penup()
title_pen.speed(0)
title_pen.goto(0, 250)
title_pen.hideturtle()
title_pen.write("🐍 SNAKE GAME 🐍", align="center", font=("Arial", 24, "bold"))

pen = turtle.Turtle()
pen.shape("square")
pen.color("#ffffff")
pen.penup()
pen.speed(0)
pen.goto(0, 220)
pen.hideturtle()
pen.write("Score: 0 ⭐ High Score: 0", align="center", font=("Courier", 16, "bold"))

segments = []
colors = ["#00ff88"]

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
        head.sety(y + 20)
    elif head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    elif head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    elif head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

def reset_game():
    global score, delay
    
    flash = turtle.Turtle()
    flash.speed(0)
    flash.shape("square")
    flash.color("#ff4757")
    flash.penup()
    flash.goto(0, 0)
    flash.shapesize(50, 50)
    time.sleep(0.1)
    flash.goto(1000, 1000)
    
    time.sleep(0.5)
    head.goto(0, 0)
    head.direction = "stop"
    
    for segment in segments:
        segment.goto(1000, 1000)
    segments.clear()
    
    score = 0
    delay = 0.15
    
    update_score()

def update_score():
    pen.clear()
    pen.write("Score: {} ⭐ High Score: {}".format(score, high_score), 
              align="center", font=("Courier", 16, "bold"))

def animate_food():
    current_size = glow_food.shapesize()[0]
    if current_size >= 1.4:
        glow_food.shapesize(1.0, 1.0)
    else:
        glow_food.shapesize(current_size + 0.1, current_size + 0.1)

window.listen()
window.onkeypress(go_up, "w")
window.onkeypress(go_up, "Up")
window.onkeypress(go_down, "s")
window.onkeypress(go_down, "Down")
window.onkeypress(go_left, "a")
window.onkeypress(go_left, "Left")
window.onkeypress(go_right, "d")
window.onkeypress(go_right, "Right")

animation_counter = 0

while True:
    window.update()
    
    animation_counter += 1
    if animation_counter % 3 == 0:
        animate_food()
    
    if (head.xcor() > 270 or head.xcor() < -270 or 
        head.ycor() > 260 or head.ycor() < -260):
        reset_game()
    
    if head.distance(food) < 20:
        x = random.randint(-260, 260)
        y = random.randint(-250, 250)
        x = (x // 20) * 20
        y = (y // 20) * 20
        food.goto(x, y)
        glow_food.goto(x, y)
        
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        segment_color = random.choice(colors)
        new_segment.color(segment_color)
        new_segment.penup()
        new_segment.shapesize(0.9, 0.9)
        segments.append(new_segment)
        
        if delay > 0.08:
            delay -= 0.002
        
        score += 10
        
        if score > high_score:
            high_score = score
        
        update_score()
        
        if score % 50 == 0 and score > 0:
            celebration = turtle.Turtle()
            celebration.speed(0)
            celebration.shape("circle")
            celebration.color("#ffd93d")
            celebration.penup()
            celebration.goto(0, 0)
            celebration.shapesize(3, 3)
            time.sleep(0.1)
            celebration.goto(1000, 1000)
    
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)
    
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    
    move()
    
    for segment in segments:
        if segment.distance(head) < 20:
            reset_game()
            break
    
    time.sleep(delay)

turtle.done()