import turtle
import random

def fractal_tree(t, branch_len, branch_factor, angle, angle_factor):
    if branch_len > 5:
        t.forward(branch_len)
        t.right(angle)
        fractal_tree(t, branch_len * branch_factor, branch_factor, angle + angle_factor, angle_factor)
        t.left(2 * angle)
        fractal_tree(t, branch_len * branch_factor, branch_factor, angle + angle_factor, angle_factor)
        t.right(angle)
        t.backward(branch_len)

def generate_tree():
    t = turtle.Turtle()
    t.speed(0)
    t.left(90)
    t.up()
    t.backward(150)
    t.down()

    # Generate random parameters for the fractal tree
    branch_len = random.randint(50, 100)
    branch_factor = random.uniform(0.5, 0.8)
    angle = random.randint(15, 45)
    angle_factor = random.uniform(1, 2)

    fractal_tree(t, branch_len, branch_factor, angle, angle_factor)
    turtle.done()

generate_tree()
