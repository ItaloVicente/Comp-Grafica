import glfw
from OpenGL.GL import *
from PIL import Image
def save_image(filename, width, height):
    glPixelStorei(GL_PACK_ALIGNMENT, 1)
    data = glReadPixels(0, 0, width, height, GL_RGB, GL_UNSIGNED_BYTE)
    image = Image.frombytes("RGB", (width, height), data)
    image = image.transpose(Image.FLIP_TOP_BOTTOM)  # Inverter a imagem para o formato PIL
    image.save(filename)
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
    window = glfw.create_window(width, height, "Cadeira", None, None)

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

        #Base
        draw_line(540, 290, 660, 290)
        draw_line(540, 280, 660, 280)
        draw_line(540, 290, 540, 280)
        draw_line(660, 290, 660, 280)

        #Liga base costas
        draw_line(550, 320, 550, 290)
        draw_line(560, 320, 560, 290)
        draw_line(640, 320, 640, 290)
        draw_line(650, 320, 650, 290)

        #Costas
        draw_line(540, 320, 660, 320)
        draw_line(540, 320, 540, 370)
        draw_line(660, 320, 660, 370)
        draw_line(540, 370, 660, 370)

        #Pernas
        draw_line(550, 240, 550, 280)
        draw_line(560, 240, 560, 280)
        draw_line(640, 240, 640, 280)
        draw_line(650, 240, 650, 280)
        draw_line(550, 240, 560, 240)
        draw_line(640, 240, 650, 240)
        save_image("Cadeira.png", width, height)
        glfw.swap_buffers(window)

if __name__ == "__main__":
    main()