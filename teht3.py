import pygame

naytto = pygame.display.set_mode((640, 400))
pygame.display.set_caption("Piirtäminen")

örkkihahmo = pygame.image.load("hahmo.png").convert()
örkkihahmo2 = pygame.image.load("hahmo2.png").convert()
def piirraKuva(örkkihahmo, örkkihahmo2, x, y):
    naytto.blit("hahmo.png", x, y)
    naytto.blit("hahmo2.png", x, y)

def piirtaminen(naytto, hahmot):
    naytto.fill((0, 0, 0))
    for hahmo in hahmot:
        if hahmo[3] == True:
            kuva = pygame.image.load(hahmo[0]).convert()
            naytto.blit(kuva, (örkkihahmo[1], örkkihahmo[2]))
    pygame.display.flip()

def kontrolli(hahmot, tapahtuma):
    if tapahtuma.type == pygame.KEYDOWN:
        if tapahtuma.key == pygame.K_SPACE:
            hahmot[0][3] = True

def main():
    örkkihahmo = ["hahmo.png",  100, 100, False]
    örkkihahmo2 = ["hahmo2.png",  200, 200, False]
    hahmot = [örkkihahmo, örkkihahmo2]
    while True:
        tapahtuma = pygame.event.poll()
        if tapahtuma.type == pygame.QUIT:
            break
        kontrolli(hahmot, tapahtuma)
        piirtaminen(naytto, hahmot)


main()