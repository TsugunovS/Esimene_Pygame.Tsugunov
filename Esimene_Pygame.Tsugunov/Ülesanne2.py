import pygame
pygame.init()
ekraani_pind=pygame.display.set_mode((620,380))
ekraani_pind.fill((195, 224, 223))

pygame.display.set_caption("Esimene aken")
pilt=pygame.image.load("planet.xcf")
ekraani_pind.blit(pilt,(0,0,))

pygame.display.flip()
while True:
    event=pygame.event.poll()
    if event.type==pygame.QUIT:
        break
pygame.quit()

