import pygame
import random
# Viiva
naytto = pygame.display.set_mode((640, 400))
pygame.display.set_caption("Piirtäminen")



#def main():
    #while True:
        #tapahtuma = pygame.event.poll()
        #if tapahtuma.type == pygame.QUIT:
            #break

        #naytto.fill((0, 0, 0))
        #pygame.draw.line(naytto, (0, 0, 255), (640, 400), (0, 0))
        #pygame.draw.line(naytto, (0, 255, 0), (0, 400), (640, 0))
        #pygame.display.flip()

#main()

# Kuvan piirtäminen


#naytto = pygame.display.set_mode((640, 400))
#pygame.display.set_caption("Piirtäminen")
#x = 0
#y = 0

#def main():
    #while True:
        #tapahtuma = pygame.event.poll()
        #if tapahtuma.type == pygame.QUIT:
            #break

        #naytto.fill((0, 0, 0))
        #kuva = pygame.image.load("cat.jpg").convert()
        #naytto.blit(kuva, (x, y))
        #pygame.display.flip()

#main()

kuva = pygame.image.load("cat.jpg").convert()
def piirraKuva(kuva):
    while True:
        tapahtuma = pygame.event.poll()
        if tapahtuma.type == pygame.QUIT:
            break

        naytto.fill((0, 0, 0))
        naytto.blit(kuva, (1, 1))
        pygame.display.flip()

#piirraKuva(kuva)

# Hahmo satunnainen

#kuva = pygame.image.load("cat.jpg").convert()
#def piirraKuva(kuva):
    #while True:
        #tapahtuma = pygame.event.poll()
        #if tapahtuma.type == pygame.QUIT:
            #break
        #x = random.randint(0, 640)
        #y = random.randint(0, 400)
        #naytto.fill((0, 0, 0))
        #naytto.blit(kuva, (x,y))
        #pygame.display.flip()

#piirraKuva(kuva)