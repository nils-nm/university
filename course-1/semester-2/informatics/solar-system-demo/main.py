"""
Showcase of planets/satellites (small boxes) orbiting around a star.

Uses a custom velocity function to manually calculate the gravity, assuming
the star is in the middle and is massive enough that the satellites does not
affect it.

This is a port of the Planet demo included in Chipmunk.
"""

import math
import random

random.seed(5)  # Feel free to adjust, this is just to make each run equal

import pygame
import pygame_widgets
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox

import pymunk
import pymunk.pygame_util

gravityStrength = 5.0e6


class Planet():
    def __init__(self, mass, radius):

        self.mass = mass
        self.radius = radius

    def add_box(self, space, x, y):
        self.body = pymunk.Body()
        self.body.position = pymunk.Vec2d(x, y)
        self.body.velocity_func = planetGravity

        r = self.body.position.get_distance((300, 300))
        v = math.sqrt(gravityStrength / r) / r
        self.body.velocity = (self.body.position - pymunk.Vec2d(300, 300)).perpendicular() * -v

        self.body.angular_velocity = v
        self.body.angle = math.atan2(self.body.position.y, self.body.position.x)

        self.box = pymunk.Poly.create_box(self.body, radius=self.radius)
        self.box.mass = self.mass
        self.box.friction = 0.7
        self.box.elasticity = 0
        self.box.color = pygame.Color("white")
        space.add(self.body, self.box)

    def update(self):
        self.box.mass = self.mass
        self.box.unsafe_set_radius(self.radius)
        #self.box = pymunk.Poly(self.body, radius=(self.radius, self.radius))



def planetGravity(body, gravity, damping, dt):

    sq_dist = body.position.get_dist_sqrd((300, 300))
    g = (
        (body.position - pymunk.Vec2d(300, 300))
        * -gravityStrength
        / (sq_dist * math.sqrt(sq_dist))
    )
    pymunk.Body.update_velocity(body, g, damping, dt)




pygame.init()
screen = pygame.display.set_mode((900, 900))
clock = pygame.time.Clock()

space = pymunk.Space()
draw_options = pymunk.pygame_util.DrawOptions(screen)

planets = []


slider_mass = Slider(screen, 100, 700, 400, 40, min=1, max=99, step=1, initial=1)
output_mass = TextBox(screen, 575, 700, 300, 50, fontSize=30)
slider_radius = Slider(screen, 100, 800, 400, 40, min=1, max=99, step=1, initial=20)
output_radius = TextBox(screen, 575, 800, 300, 50, fontSize=30)

output_mass.disable()
output_radius.disable()

#for x in range(10):
#    p = Planet(slider_mass.getValue(), slider_radius.getValue())
#    p.add_box(space)
#    planets.append(p)


while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
            if (0 < pos[0] < 600) and (0 < pos[1] < 600):
                p = Planet(slider_mass.getValue(), slider_radius.getValue())
                p.add_box(space, pos[0], pos[1])
                planets.append(p)

        if (event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            exit()

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            pygame.image.save(screen, "planet.png")

    screen.fill(pygame.Color("black"))

    space.debug_draw(draw_options)

    # 'Star' in the center of system
    pygame.draw.circle(screen, pygame.Color("yellow"), (300, 300), 10)

    space.step(1 / 60)


    output_mass.setText(f'mass of planet is: {slider_mass.getValue()}')
    output_radius.setText(f'radius of planet is: {slider_radius.getValue()}')

    for i in planets:
        i.mass = slider_mass.getValue()
        i.radius = slider_radius.getValue()
        i.update()


    pygame_widgets.update(events)

    pygame.display.flip()
    clock.tick(60)
    pygame.display.set_caption("fps: " + str(clock.get_fps()))
