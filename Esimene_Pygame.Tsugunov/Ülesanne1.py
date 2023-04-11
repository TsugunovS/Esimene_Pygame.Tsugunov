import pygame
pygame.init()
ekraani_pind=pygame.display.set_mode((300,300))
ekraani_pind.fill((27,100,255))
pygame.display.set_caption("Ülesanne 1")
screen = pygame.display.set_mode((300, 300))

jalg=pygame.Rect(95,20,90,250)
pygame.draw.rect(ekraani_pind,(0,0,0),jalg)
lill=pygame.Rect(106,30,70,70)
pygame.draw.ellipse(ekraani_pind,(219, 13, 23),lill)
lill=pygame.Rect(106,110,70,70)
pygame.draw.ellipse(ekraani_pind,(219, 206, 18),lill)
lill=pygame.Rect(106,190,70,70)
pygame.draw.ellipse(ekraani_pind,(39, 194, 25),lill)


pygame.init()
ekraani_pind=pygame.display.set_mode((300,300))
ekraani_pind.fill((100,100,255))
pygame.display.set_caption("Ülesanne 1")


lill=pygame.Rect(118,55,60,60)
pygame.draw.ellipse(ekraani_pind,(250, 255, 255),lill)
lill=pygame.Rect(114,112,70,70)
pygame.draw.ellipse(ekraani_pind,(250, 255, 255),lill)
lill=pygame.Rect(106,180,90,90)
pygame.draw.ellipse(ekraani_pind,(250, 255, 255),lill)


polygon=pygame.Rect(128,35,40,30)
pygame.draw.rect(ekraani_pind,(164, 189, 186),polygon)
jalg=pygame.Rect(142,84,10,10)
pygame.draw.rect(ekraani_pind,(219, 132, 18),jalg)
lill=pygame.Rect(135,70,10,10)
pygame.draw.ellipse(ekraani_pind,(0, 0, 0),lill)
lill=pygame.Rect(150,70,10,10)
pygame.draw.ellipse(ekraani_pind,(0, 0, 0),lill)
lill=pygame.Rect(145,130,10,10)
pygame.draw.ellipse(ekraani_pind,(0, 0, 0),lill)
lill=pygame.Rect(145,150,10,10)
pygame.draw.ellipse(ekraani_pind,(0, 0, 0),lill)
lill=pygame.Rect(145,210,10,10)
pygame.draw.ellipse(ekraani_pind,(0, 0, 0),lill)
lill=pygame.Rect(145,230,10,10)
pygame.draw.ellipse(ekraani_pind,(0, 0, 0),lill)


#polygon=pygame.Rect(128,35,40,30)
#pygame.draw.rect(ekraani_pind,(164, 189, 186),polygon)
jalg=pygame.Rect(45,140,70,10)
pygame.draw.rect(ekraani_pind,(0,0,0),jalg)
jalg=pygame.Rect(184,140,70,10)
pygame.draw.rect(ekraani_pind,(0,0,0),jalg)
jalg=pygame.Rect(60,125,10,40)
pygame.draw.rect(ekraani_pind,(0,0,0),jalg)
jalg=pygame.Rect(230,125,10,40)
pygame.draw.rect(ekraani_pind,(0,0,0),jalg)
#polygon=pygame.Rect(135,70,100,100)
#pygame.draw.rect(ekraani_pind,(0, 0, 0),polygon)

pygame.display.flip()

while True:
    event=pygame.event.poll()
    if event.type==pygame.QUIT:
        break
pygame.quit()



