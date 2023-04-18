import pygame
pygame.init()
ekraani_pind=pygame.display.set_mode((640,480))
ekraani_pind.fill((195, 224, 223))
pygame.display.set_caption("Esimene aken")

#отступ слева, справа,
ristkülik=pygame.Rect(0,300,640,100)
pygame.draw.rect(ekraani_pind,(0, 0, 0),ristkülik)
#jalg=pygame.Rect(310,200,30,200)
#pygame.draw.rect(ekraani_pind,(99, 112, 112),jalg)
lill=pygame.Rect(100,200,150,150)
pygame.draw.ellipse(ekraani_pind,(26, 48, 214),lill)
lill=pygame.Rect(400,200,150,150)
pygame.draw.ellipse(ekraani_pind,(26, 48, 214),lill)
jalg=pygame.Rect(30,60,580,200)
pygame.draw.rect(ekraani_pind,(99, 112, 112),jalg)
ristkülik=pygame.Rect(5,50,200,100)
pygame.draw.rect(ekraani_pind,(195, 224, 223),ristkülik)
ristkülik=pygame.Rect(500,50,200,100)
pygame.draw.rect(ekraani_pind,(195, 224, 223),ristkülik)

#фары
ristkülik=pygame.Rect(40,160,30,30)
pygame.draw.rect(ekraani_pind,(226, 230, 39),ristkülik)
ristkülik=pygame.Rect(570,160,30,30)
pygame.draw.rect(ekraani_pind,(196, 44, 33),ristkülik)

#дверные ручки
ristkülik=pygame.Rect(300,160,30,10)
pygame.draw.rect(ekraani_pind,(0, 0, 0),ristkülik)
ristkülik=pygame.Rect(430,160,30,10)
pygame.draw.rect(ekraani_pind,(0, 0, 0),ristkülik)

pilt=pygame.image.load("ooo.png")
ekraani_pind.blit(pilt,(250,50,))

font=pygame.font.SysFont("Times New Roman",48)
sõnad="Tere tulemast!"
värv=[0,0,0]
teksti_lisanime=font.render(sõnad,False,värv)
ekraani_pind.blit(teksti_lisanime,(180,10))

pygame.display.flip()
while True:
    event=pygame.event.poll()
    if event.type==pygame.QUIT:
        break
pygame.quit()
