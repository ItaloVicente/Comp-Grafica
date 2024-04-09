import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import math
from PIL import Image

def save_image(filename, width, height):
    glPixelStorei(GL_PACK_ALIGNMENT, 1)
    data = glReadPixels(0, 0, width, height, GL_RGB, GL_UNSIGNED_BYTE)
    image = Image.frombytes("RGB", (width, height), data)
    image = image.transpose(Image.FLIP_TOP_BOTTOM)  # Inverter a imagem para o formato PIL
    image.save(filename)
def draw_circle(radius, center_x, center_y):
    glBegin(GL_LINE_LOOP)
    for i in range(360):
        angle = math.radians(i)
        x = radius * math.cos(angle) + center_x
        y = radius * math.sin(angle) + center_y
        glVertex2f(x, y)
    glEnd()
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
    window = glfw.create_window(width, height, "Espada", None, None)

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
        # Linhas laterais
        draw_line(570, 450, 570, 290)
        draw_line(590, 450, 590, 290)
        draw_line(580, 470, 580, 290)
        # Ponta
        draw_line(570, 450, 580, 470)
        draw_line(580, 470, 590, 450)
        # Base
        draw_line(540, 290, 620, 290)
        draw_line(540, 280, 620, 280)
        draw_line(540, 290, 540, 280)
        draw_line(620, 290, 620, 280)
        # Empunhadura
        draw_line(575, 280, 575, 235)
        draw_line(585, 280, 585, 235)
        draw_line(575, 235, 585, 235)
        draw_circle(5, 580, 230)

        save_image("Espada.png", width, height)
        glfw.swap_buffers(window)

    glfw.terminate()


if __name__ == "__main__":
    main()