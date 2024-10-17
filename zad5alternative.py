import sys
from glfw.GLFW import *
from OpenGL.GL import *
import random

# Vertices of the triangle
vertices = [(-100, -100), (100, -100), (0, 100)]

# Global variables to store random point's coordinates
current_x = 0.0
current_y = 0.0

# Global variables to store random RGB color
red = 0.0
green = 0.0
blue = 0.0

def startup():
    update_viewport(None, 400, 400)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glPointSize(2.0)  # Set point size for drawing

def shutdown():
    pass

# Method to generate random RGB color
def randomColor():
    global red, green, blue
    red = random.random()
    green = random.random()
    blue = random.random()
    glColor3f(red, green, blue)

# Method to find a random point according to Chaos game algorithm
def random_point():
    global current_x, current_y
    current_x, current_y = random.choice(vertices)

def renderSierpinskiChaos(num_points):
    global current_x, current_y

    glBegin(GL_POINTS)
    for i in range(num_points):
        target_vertex = random.choice(vertices)
        current_x = (current_x + target_vertex[0]) / 2
        current_y = (current_y + target_vertex[1]) / 2
        glVertex2f(current_x, current_y)
    glEnd()


def update_viewport(window, width, height):
    if height == 0:
        height = 1
    if width == 0:
        width = 1
    aspectRatio = width / height

    glMatrixMode(GL_PROJECTION)
    glViewport(0, 0, width, height)
    glLoadIdentity()

    if width <= height:
        glOrtho(-100.0, 100.0, -100.0 / aspectRatio, 100.0 / aspectRatio,
                1.0, -1.0)
    else:
        glOrtho(-100.0 * aspectRatio, 100.0 * aspectRatio, -100.0, 100.0,
                1.0, -1.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def main():
    if not glfwInit():
        sys.exit(-1)

    window = glfwCreateWindow(400, 400, __file__, None, None)
    if not window:
        glfwTerminate()
        sys.exit(-1)

    glfwMakeContextCurrent(window)
    glfwSetFramebufferSizeCallback(window, update_viewport)
    glfwSwapInterval(1)

    startup()
    randomColor()
    random_point()

    while not glfwWindowShouldClose(window):
        glClear(GL_COLOR_BUFFER_BIT)
        renderSierpinskiChaos(10000)
        glFlush()
        glfwSwapBuffers(window)
        glfwPollEvents()
    shutdown()

    glfwTerminate()


if __name__ == '__main__':
    main()