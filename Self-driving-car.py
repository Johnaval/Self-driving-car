import pygame
import math
import numpy as np
import os

def rotate_point(x, y, cx, cy, angle):
    x = x - cx
    y = y - cy

    x1 = x * math.cos(math.radians(angle)) - y * math.sin(math.radians(angle))
    y1 = x * math.sin(math.radians(angle)) + y * math.cos(math.radians(angle))
    
    x1 = x1 + cx
    y1 = y1 + cy

    return [x1, y1]

clock = pygame.time.Clock()
pygame.init()

window_width = 2000
window_height = 1000
window = pygame.display.set_mode([window_width, window_height])
pygame.display.set_caption('Self driving car')

x = window_width/2
y = window_height/2
width = 40
height = 60

vel = 0
velx = 0
vely = 0
vel_max = 100
angle = 0

trackX = 100
trackY = 300

run = True
while run:
    acc = 5
    time = 60
    keypress = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        if vel > 0:
            angle -= 1
    if keys[pygame.K_d]:
        if vel > 0:
            angle += 1 
    if keys[pygame.K_w]:
        keypress = True
        if vel <= vel_max:
            vel = vel + acc * time/1000
        velx = vel * math.sin(math.radians(angle))
        vely = vel * math.cos(math.radians(angle))
        x = x + velx * time/1000
        y = y - vely * time/1000
    if keys[pygame.K_s]:
        acc = 3 * acc

    if keypress == False and vel > 0:
        vel = vel - acc * time/1000
        if vel < 0:
            vel = 0
        velx = vel * math.sin(math.radians(angle))
        vely = vel * math.cos(math.radians(angle))
        x = x + velx * time/1000
        y = y - vely * time/1000

    pointA = [x,y]
    pointB = [x + width, y]
    pointC = [x + width, y + height]
    pointD = [x, y + height]

    window.fill((0,0,0))   
    pygame.draw.rect(window, (255,255,255), (trackX, trackY,10,350))
    pygame.draw.rect(window, (255,255,255), (trackX + 300, trackY,10,350))
    pygame.draw.rect(window, (255,255,255), (window_width - trackX, trackY,10,350))
    pygame.draw.rect(window, (255,255,255), (window_width - trackX - 300, trackY,10,350))
    for i in range(1, 30):
        arc_endX = trackX + 10 * i + 10
        arc_endY = trackY - 10 * i - 10
        pygame.draw.rect(window, (255,255,255), (trackX + 10 * i, trackY - 10 * i, 10, 10))
        pygame.draw.rect(window, (255,255,255), (trackX + 10 * i, trackY + 340 + 10 * i, 10, 10))
        pygame.draw.rect(window, (255,255,255), (window_width - trackX - 10 * i, trackY - 10 * i, 10, 10))
        pygame.draw.rect(window, (255,255,255), (window_width - trackX - 10 * i, trackY + 340 + 10 * i, 10, 10))
    pygame.draw.rect(window, (255,255,255), (arc_endX, arc_endY, 1210, 10))
    pygame.draw.rect(window, (255,255,255), (arc_endX, arc_endY + 940, 1210, 10))
    for i in range(1,15):
        arc_endX = trackX + 300 + 10 * i + 10
        arc_endY = trackY + 10 * i + 10
        pygame.draw.rect(window, (255,255,255), (trackX + 300 + 10 * i, trackY - 10 * i, 10, 10))
        pygame.draw.rect(window, (255,255,255), (trackX + 300 + 10 * i, trackY + 340 + 10 * i, 10, 10))       
        pygame.draw.rect(window, (255,255,255), (window_width - trackX - 300 - 10 * i, trackY - 10 * i, 10, 10))
        pygame.draw.rect(window, (255,255,255), (window_width - trackX - 300 - 10 * i, trackY + 340 + 10 * i, 10, 10))
    pygame.draw.rect(window, (255,255,255), (arc_endX, arc_endY - 300, 910, 10))
    pygame.draw.rect(window, (255,255,255), (arc_endX, arc_endY + 340, 910, 10))
    pygame.draw.polygon(window, (255,0,0), (rotate_point(pointA[0], pointA[1], pointA[0] + width/2, pointA[1] + height/2, angle), \
                                            rotate_point(pointB[0], pointB[1], pointB[0] - width/2, pointB[1] + height/2, angle), \
                                            rotate_point(pointC[0], pointC[1], pointC[0] - width/2, pointC[1] - height/2, angle), \
                                            rotate_point(pointD[0], pointD[1], pointD[0] + width/2, pointD[1] - height/2, angle)))
    pygame.display.update()
    clock.tick(time)

pygame.quit()
