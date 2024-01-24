import pygame
pygame.init()

#Generer la fenetre du jeu
pygame.display.set_caption("EMLV best seller")
screen = pygame.display.set_mode((1080, 720))

## Importer l'arriere plan de notre jeu ici:

background = pygame.image.load('')

##

running = True

# Boucle tant que cette condition est vrai
while running:

    # appliquer l'arrière plan de notre jeu
    screen.blit(background, (0, 0))

    #Mettre à jour l'écran

    pygame.display.flip()

    # si le joueur ferme cette fenetre
    for event in pygame.event.get():
        #que l'evenement est fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("fermeture du jeu")