import pygame
pygame.init()
ekraani_pind=pygame.display.set_mode((640,480))
ekraani_pind.fill((0,0,200))
pygame.display.set_captoin("Esimene aken")
#отступ слева, справа,
ristkülik=pygame.Rect(0,0,100,100)
pygame.draw.rect(ekraani_pind,(100,0,0),ristkülik)


pygame.display.flip()
while True:
    event=pygame.event.poll()
    if event.type==pygame.QUIT:
        break
pygame.quit()