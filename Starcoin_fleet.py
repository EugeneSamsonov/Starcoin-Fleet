import turtle
import time
import random

# set up the screen
# настройка экран
wn = turtle.Screen()
wn.title("Starcoin Fleet")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

# decoration
# оформление
dec = turtle.Turtle()
dec.speed(0)
dec.hideturtle()
dec.penup()
dec.color('white')
dec.goto(300, 300)
dec.pendown()
dec.goto(-300, 300)
dec.goto(-300, -300)
dec.goto(300, -300)
dec.goto(300, 300)
for i in range(20):
    dec.penup()
    dec.goto(random.randint(-300, 300), random.randint(-300, 300))
    dec.pendown()
    dec.circle(1, 3)
dec.penup()
dec.goto(600, 600)


# main character
# "главный герой"
m_c = turtle.Turtle()
m_c.speed(0)
m_c.shape("arrow")
m_c.shapesize(1, 2, 0)
m_c.color("white")
m_c.penup()
m_c.goto(0, 0)
m_c.direction = "stop"

# pirates
# пираты
pir = turtle.Turtle()
pir.hideturtle()
pir.speed(1)
pir.shape("arrow")
pir.shapesize(3)
pir.color("red")
pir.penup()
pir.goto(610, 610)

# coin
# монета
coin = turtle.Turtle()
coin.speed(0)
coin.shape("circle")
coin.color("yellow")
coin.penup()
coin.goto(0, 100)


score, high_score, x, y = 0, 0, 0, 0
delay = 0.06

# score pen
# ручка для подсчета очков
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f"Счёт: {score} Рекорд: {high_score}",
          align="center", font=('Courier', 24, "normal"))


def move_up():
    m_c.direction = 'up'
    m_c.setheading(90)


def move_down():
    m_c.direction = 'down'
    m_c.setheading(270)


def move_left():
    m_c.direction = 'left'
    m_c.setheading(180)


def move_right():
    m_c.direction = 'right'
    m_c.setheading(0)


def m_chek():
    if m_c.direction == 'up':
        y = m_c.ycor()
        m_c.sety(y + 20)
    if m_c.direction == 'down':
        y = m_c.ycor()
        m_c.sety(y - 20)
    if m_c.direction == 'left':
        x = m_c.xcor()
        m_c.setx(x - 20)
    if m_c.direction == 'right':
        x = m_c.xcor()
        m_c.setx(x + 20)


wn.listen()
# keyboard bindings
# привязкa клавиатуры
wn.onkeypress(move_up, 'w')
wn.onkeypress(move_down, 's')
wn.onkeypress(move_left, 'a')
wn.onkeypress(move_right, 'd')

while True:
    wn.update()

    # Check for a collision with the border
    # Проверка нет ли столкновения с границей
    if m_c.xcor() > 300 or m_c.xcor() < -300 or m_c.ycor() > 300 or m_c.ycor() < -300:
        time.sleep(1)
        m_c.direction = 'stop'
        m_c.goto(0, 0)
        pir.goto(610, 610)

        # Reset the score
        # Сброс счета
        score = 0
        pen.clear()
        pen.write(f"Счёт: {score} Рекорд: {high_score}",
                  align="center", font=('Courier', 24, "normal"))

    m_chek()

    # Check for a collision with the coin
    # Проверrf нет ли столкновения с монетой
    if m_c.distance(coin) < 20:
        # Move the coin to a random spot
        # Переместить монету в случайное место
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        coin.goto(x, y)
        # Increase thу score
        # Увеличение счета
        score += 10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write(f"Счёт: {score} Рекорд: {high_score}",
                  align="center", font=('Courier', 24, "normal"))

    if score >= 50:
        pir.showturtle()
        pir.setheading(pir.towards(m_c.xcor(), m_c.ycor()))
        if score >= 50 and score < 100:
            pir.fd(5)
        elif score >= 100:
            pir.fd(10)

        if pir.distance(m_c) < 25:
            time.sleep(1)
            m_c.direction = 'stop'
            m_c.goto(0, 0)
            pir.goto(610, 610)

        # Reset the score
        # Сброс счета
            score = 0
            pen.clear()
            pen.write(f"Счёт: {score} Рекорд: {high_score}",
                      align="center", font=('Courier', 24, "normal"))

    time.sleep(delay)

wn.mainloop()
