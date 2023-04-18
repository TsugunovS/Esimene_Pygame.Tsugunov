from lib2to3 import pygram
import pygame
import random
import sys

def Maja(x,y,laius,kõrgus,pind,värv,suurus):
    punktid=[(x,y-((3/4.0)*kõrgus)), (x,y), (x+laius,y), (x+laius,y-(3/4.0)*(kõrgus)),(x,y-((3/4.0)*kõrgus)), (x+laius/2.0,y-kõrgus),(x+laius,y-(3/4.0)*kõrgus)]
    pygame.draw.lines(pind,värv,False,punktid,suurus)

def Uks(x,y,laius,kõrgus,pind,värv,suurus):
    punktid=[(x,y),(x,y-(1/2)*kõrgus),(x+(1/3)*laius,y-(1/2)*kõrgus),(x+(1/3)*laius,y),(x,y)]
#    punktid=[(x,y-((3/4.0)*kõrgus)), (x,y), (x+laius,y), (x+laius,y-(3/4.0)*(kõrgus)),(x,y-((3/4.0)*kõrgus)), ]
    pygame.draw.lines(pind,värv,True,punktid,suurus)

def Aken(x,y,laius,kõrgus,pind,värv,suurus):
    punktid=[(x,y),(x,y-(1/2)*kõrgus),(x+(1/3)*laius,y-(1/2)*kõrgus),(x+(1/3)*laius,y),(x,y)]
    pygame.draw.lines(pind,värv,True,punktid,suurus)


r=random.randint(0,255)
g=random.randint(0,255)
b=random.randint(0,255)
varv=[r,g,b]
fon=[r,g,b]

r=random.randint(0,255)
g=random.randint(0,255)
b=random.randint(0,255)
majavarv=[r,g,b]
suurus=random.randint(1,10)

pind=pygame.display.set_mode([640,480])
pygame.display.set_caption("Juhuslikud objektid + majake")
pind.fill(fon)

Maja(100,400,500,400,pind,majavarv,suurus)
Uks(100,400,500,400,pind,majavarv,suurus)
Aken(100,400,500,400,pind,majavarv,suurus)
pygame.display.flip()

#ristkülik=pygame.Rect(0,0,0,0)                            
#pygame.draw.rect(pind,(200,0,0),ristkülik)

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