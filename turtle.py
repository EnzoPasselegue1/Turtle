import turtle
screen = turtle.Screen()
screen.bgcolor("#87CEEB")
screen.title("Dessin d'une Tortue 🐢")
t = turtle.Turtle()
t.speed(3)
t.width(2)
def draw_circle(color, x, y, radius):
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    t.color("black", color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
draw_circle("#228B22", 0, -50, 50)
draw_circle("#32CD32", 0, 50, 25)
draw_circle("#32CD32", -50, -20, 15)
draw_circle("#32CD32", 50, -20, 15)
draw_circle("#228B22", -30, -80, 15)
draw_circle("#228B22", 30, -80, 15)
draw_circle("#228B22", 0, -100, 10)
draw_circle("white", -10, 75, 5)
draw_circle("white", 10, 75, 5)
draw_circle("black", -10, 77, 2)
draw_circle("black", 10, 77, 2)
t.hideturtle()
screen.mainloop()
