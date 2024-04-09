import math
from PIL import Image
import glfw
from OpenGL.GL import *
from OpenGL.raw.GLU import gluOrtho2D

def save_image(filename, width, height):
    glPixelStorei(GL_PACK_ALIGNMENT, 1)
    data = glReadPixels(0, 0, width, height, GL_RGB, GL_UNSIGNED_BYTE)
    image = Image.frombytes("RGB", (width, height), data)
    image = image.transpose(Image.FLIP_TOP_BOTTOM)  # Inverter a imagem para o formato PIL
    image.save(filename)
# Função de desenho OpenGL
def draw_circle(radius, center_x, center_y):
    glBegin(GL_LINE_LOOP)
    for i in range(360):
        angle = math.radians(i)
        x = radius * math.cos(angle) + center_x
        y = radius * math.sin(angle) + center_y
        glVertex2f(x, y)
    glEnd()
def draw(control_points):
    glColor3f(1.0, 1.0, 1.0)
    # Desenha os pontos de controle
    glPointSize(5.0)
    glBegin(GL_POINTS)
    glEnd()

    # Habilita a curva de Bezier
    glEnable(GL_MAP1_VERTEX_3)
    glMap1f(GL_MAP1_VERTEX_3, 0.0, 1.0, control_points)

    # Desenha a curva de Bezier
    glBegin(GL_LINE_STRIP)
    for i in range(101):
        glEvalCoord1f(i / 100.0)
    glEnd()

    glFlush()


def draw_line(start1, end1, start2, end2):
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_LINE_STRIP)
    glVertex2f(start1, end1)
    glVertex2f(start2, end2)
    glEnd()

def main():
    if not glfw.init():
        raise Exception("glfw can not be initialized")

    width, height = 1280, 720
    window = glfw.create_window(width, height, "Peixe", None, None)

    if not window:
        glfw.terminate()
        raise Exception("glfw window can not be created")

    glfw.set_window_pos(window, 400, 200)

    glfw.make_context_current(window)

    glClearColor(0, 0.1, 0.1, 1)
    glOrtho(0, width, 0, height, -1, 1)
    while not glfw.window_should_close(window):
        glfw.poll_events()

        glClear(GL_COLOR_BUFFER_BIT)

        glfw.poll_events()
        #Espinha
        control_points = [
            [475, 375, 0],
            [525, 425, 0],
            [575, 425, 0],
            [675, 375, 0]
        ]
        draw(control_points)

        # Calda
        draw_line(700, 400, 700, 350)
        draw_line(700, 400, 675, 375)
        draw_line(700, 350, 675, 375)

        #Parte de baixo
        control_points = [
            [475, 375, 0],
            [525, 325, 0],
            [575, 325, 0],
            [675, 375, 0]
        ]
        draw(control_points)
        draw_circle(2,490,380)
        save_image("Peixe.png", width, height)
        glfw.swap_buffers(window)

if __name__ == "__main__":
    main()