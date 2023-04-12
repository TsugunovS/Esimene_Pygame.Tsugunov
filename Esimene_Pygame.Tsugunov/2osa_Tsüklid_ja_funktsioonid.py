from lib2to3 import pygram
import pygame
import random
import sys

def Maja(x,y,laius,kõrgus,pind,värv):
    punktid=[(x,y- ((3/4.0)*kõrgus)), (x,y), (x+laius,y), (x+laius,y-(3/4.0) * kõrgus),
             (x,y-((3/4.0)*kõrgus)), (x + laius/2.0,-kõrgus), (x+laius,y-(3/4.0)*kõrgus)]
    suurus=random.randint(1,10)
    pygame.draw.lines(pind,värv,False,punktid,suurus)
    pygame.draw.lines(pind, värv, False, punktid, suurus)

def draw_house(x, y, width, height, surface, color):
    # Draw the house
    points = [(x, y - 0.75 * height), (x, y), (x + width, y), (x + width, y - 0.75 * height),
              (x, y - 0.75 * height), (x + width / 2, -height), (x + width, y - 0.75 * height)]
    thickness = random.randint(1, 10)
    pygame.draw.lines(surface, color, False, points, thickness)

r=random.randint(0,255)
g=random.randint(0,255)
b=random.randint(0,255)
varv=[r,g,b]
fon=[r,g,b]

r=random.randint(0,255)
g=random.randint(0,255)
b=random.randint(0,255)
majavarv=[r,g,b]

pind=pygame.display.set_mode([640,480])
pygame.display.set_caption("Juhuslikud objektid + majake")
pind.fill(fon)

Maja(100,400,300,400,pind,majavarv)
pygame.display.flip()

for i in range(10):
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    varv=[r,g,b]
    #suurus
    laius=random.randint(1,80)
    kõrgus=random.randint(1,80)
    #asukoht
    x=random.randint(0,640-laius)
    y=random.randint(0,480-kõrgus)
    pygame.draw.rect(pind,varv,[x,y,laius,kõrgus])

    pygame.display.flip()
while True:
    event=pygame.event.poll()
    if event.type==pygame.QUIT:
        sys.exit()
pygame.quit()