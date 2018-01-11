import pygame

RES = (500,500)
SIZE = 16
WHITE = (255,255,255)
BLACK = (0,0,0)

cDim = int(RES[0]/SIZE)
rDim = int(RES[1]/SIZE)

pygame.init()
gd = pygame.display.set_mode(RES)
gd.fill(BLACK)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    [pygame.draw.rect(gd, WHITE, [c,r,cDim,rDim]) for r in range(0,RES[1], rDim * 2) for c in range(0,RES[0], cDim * 2)]
    [pygame.draw.rect(gd, WHITE, [c+cDim,r+rDim,cDim,rDim]) for r in range(0,RES[1], rDim * 2) for c in range(0,RES[0], cDim * 2)]
##    [pygame.draw.rect(gd, WHITE, [c,0,cDim,rDim]) for c in range(0,RES[0], cDim * 2)]
##    [pygame.draw.rect(gd, WHITE, [c+cDim,25,cDim,rDim]) for c in range(0,RES[0], cDim * 2)]
    
    pygame.display.update()
