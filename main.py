import pygame
from simulation_object_class import blue_object
import math
import tkinter


def screen_return(first_object, second_object, x, y):
    if first_object.mass > second_object.mass:
        heavier = first_object
        lesser = second_object
    else:
        heavier = second_object
        lesser = first_object
    if heavier.x > x:

        lesser.x = lesser.x - (heavier.x - x/2)
        heavier.x = x/2
    elif heavier.y > y:
        lesser.y = lesser.y - (heavier.y - y / 2)
        heavier.y = y / 2
    elif heavier.x < 0:

        lesser.x = (lesser.x + abs(heavier.x - x / 2))
        heavier.x = x / 2

    elif heavier.y < 0:
        lesser.y = (lesser.y + abs(heavier.y - y / 2))
        heavier.y = y / 2


def update_ui(first_object, second_object, screen):
    font = pygame.font.Font(None, 20)
    first_object_text = "First Object: Mass: {}, X: {}, Y: {}, VX: {}, VY: {}".format(
        first_object.mass, round(first_object.x,2), round(first_object.y,2), round(first_object.vx,2), round(first_object.vy,2))
    second_object_text = "Second Object: Mass: {}, X: {}, Y: {}, VX: {}, VY: {}".format(
        second_object.mass, round(second_object.x,2), round(second_object.y,2), round(second_object.vx,2), round(second_object.vy,2))
    first_object_text_render = font.render(first_object_text, True, (255, 255, 255))
    second_object_text_render = font.render(second_object_text, True, (255, 255, 255))
    screen.blit(first_object_text_render, (0, 50))
    screen.blit(second_object_text_render, (0, 100))


def gravity_change(first_object, second_object):
    ###
    iterator = math.pow(10,8)
    ###
    G = 6.67259 * math.pow(10, -11)
    dx = first_object.x - second_object.x
    dy = first_object.y - second_object.y
    r = math.sqrt(dx**2 + dy**2)
    F = G * first_object.mass * second_object.mass / (r**2)
    Fx = F * dx / r
    Fy = F * dy / r
    radius1 = math.log2(first_object.mass/math.pi)
    radius2 = math.log2(second_object.mass/math.pi)
    if (second_object.x != first_object.x or second_object.y != first_object.y):
        second_object.vx += Fx / second_object.mass * iterator
        second_object.vy += Fy / second_object.mass * iterator
        first_object.vx += -Fx / first_object.mass * iterator
        first_object.vy += -Fy / first_object.mass * iterator
    if (r < radius1 + radius2):
        if first_object.mass > second_object.mass:
            first_object.mass += second_object.mass
            second_object.mass = 1
        else:
            second_object.mass += first_object.mass
            first_object.mass = 1




pygame.init()

win = tkinter.Tk()

x = win.winfo_screenwidth()
y = win.winfo_screenheight()



screen = pygame.display.set_mode((x, y-50), pygame.RESIZABLE)


pygame.display.set_caption("Gravity Simulator")


#                               OBJECTS SETTINGS
#
#                             MASS         X    Y     VX  VY    RGB
first_object  = blue_object(2 * pow(10,3),x/2 ,y/5 ,-7, 0, (52,66,119))
second_object = blue_object(2 * pow(10,5),x/2,y/2,0, 0,(249,215,28))


running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            running = False

    screen_return(first_object,second_object,x,y)
    screen.fill((0, 0, 0))
    gravity_change(first_object,second_object)

    first_object.update()
    second_object.update()

    update_ui(first_object,second_object,screen)

    first_object.draw(screen)
    second_object.draw(screen)



    pygame.display.update()


pygame.quit()

