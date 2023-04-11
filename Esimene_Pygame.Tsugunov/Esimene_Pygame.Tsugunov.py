import pygame
pygame.init()
ekraani_pind=pygame.display.set_mode((640,480))
ekraani_pind.fill((0,0,200))
pygame.display.set_caption("Esimene aken")

#отступ слева, справа
ristkülik=pygame.Rect(0,300,640,100)
pygame.draw.rect(ekraani_pind,(100,0,0),ristkülik)
jalg=pygame.Rect(310,200,30,200)
pygame.draw.rect(ekraani_pind,(236,0,0),jalg)
lill=pygame.Rect(100,200,150,150)
pygame.draw.ellipse(ekraani_pind,(236,255,0),lill)
lill=pygame.Rect(400,200,150,150)
pygame.draw.ellipse(ekraani_pind,(230,255,0),lill)
jalg=pygame.Rect(30,60,580,200)
pygame.draw.rect(ekraani_pind,(25,236,0),jalg)
ristkülik=pygame.Rect(0,30,200,100)
pygame.draw.rect(ekraani_pind,(0,0,200),ristkülik)

pilt=pygame.image.load("images.png")
ekraani_pind.blit(pilt,(300,60,))

font=pygame.font.SysFont("Times New Roman",48)
sõnad="Tere tulemast!"
värv=[0,0,0]
teksti_lisanime=font.render(sõnad,False,värv)
ekraani_pind.blit(teksti_lisanime,(150,30))

pygame.display.flip()
while True:
    event=pygame.event.poll()
    if event.type==pygame.QUIT:
        break
pygame.quit()
