from turtle import *
import random

# 1. initial setup, option for animation on/off
tracer(0, 0)
setup(600, 600)
bgcolor('lightcoral')
speed(0)
penup()
title("Generative Heart Art")

# 2. the big red heart!
penup()
goto(0, -150)
pendown()
color('red')
begin_fill()
left(140)
forward(224)

# loop for the heart curves
for i in range(200):
    right(1)
    forward(2)
left(120)
for i in range(200):
    right(1)
    forward(2)
forward(224)
end_fill()

# small baby pink heart!
setheading(0)
penup()
goto(0, -100)
pendown()
color('pink')
begin_fill()
left(140)
forward(150)

# while loop for smaller heart curves
count = 0
while count < 200:
    right(1)
    forward(1.3)
    count += 1

left(120)

count = 0
while count < 200:
    right(1)
    forward(1.3)
    count += 1

forward(150)
end_fill()

# reset heading for the next part
setheading(0)

# 3. generative elements
# requirement: using random and list together
colors = ['yellow', 'gold', 'white', 'oldlace']

# while loop with 3 steps
count = 0
while count < 50:

    # requirement: randomness
    star_color = random.choice(colors)
    x = random.randint(-250, 250)
    y = random.randint(-250, 250)

    # requirement: conditional statement
    if abs(x) > 120 or abs(y) > 120:
        penup()
        goto(x, y)
        pendown()
        color(star_color)

        # requirement: nested loop
        for i in range(5):
            forward(15)
            right(144)

    count += 1  # 3. update

# 4. finalizing
update()
hideturtle()
done()