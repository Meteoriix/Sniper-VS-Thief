# -*- coding: utf-8 -*-
#Pour plus d'informations, lisez le README.md sur notre page GitHub : https://github.com/Meteoriix/Sniper-VS-Thief
#MENU PRINCIPAL

#Importations
import pygame
from pygame import *

#Initialisation des variables
current_button = 0 #Bouton = 0 = Rejouer / Bouton = 1 = Quitter
black = [0,0,0]
orange_salmon = [239,166,130]
green = [85,255,0]

#Initalisation de PyGame
pygame.init()

#Fenêtre PyGame (Dimensions : 1278x684)
fenetre = pygame.display.set_mode((1278, 684))
pygame.display.set_caption("Sniper VS Thief")
icon = pygame.image.load("assets/images/diamond.png")
pygame.display.set_icon(icon)

#Remplissage du fond
fenetre.fill(orange_salmon)

#Chargement de l'image
logo = pygame.image.load("assets/images/diamond.png").convert_alpha()

#Initialisation des polices
karmatic_arcade = pygame.font.Font('assets/fonts/karmatic_arcade.ttf',36)
blackboard = pygame.font.Font('assets/fonts/blackboard.ttf',30)

#Initialisation des textes
game_name = karmatic_arcade.render('Sniper VS Thief', True, black, orange_salmon)
playbutton = blackboard.render('>>JOUER<<', True, green, orange_salmon)
leavebutton = blackboard.render('>>QUITTER<<', True, black, orange_salmon)
credits_txt = blackboard.render("Jeu fait avec PyGame avec amour par Nathan MULLER, Antoine JEAN et Vivien CROS", True, black, orange_salmon)

#Affichages des textes et du logo
fenetre.blit(logo, (595, 170))
fenetre.blit(game_name, (430, 70))
fenetre.blit(playbutton, (575, 340))
fenetre.blit(leavebutton, (565, 420))
fenetre.blit(credits_txt, (190, 500))

#Actualisation de la fenêtre
pygame.display.flip()

#BOUCLE PRINCIPALE
menuloop = 1 #Variable de la boucle du menu
while menuloop: #Lancement de la boucle du menu
    for event in pygame.event.get(): #Lancement des évènements
        #Fermeture améliorée de la fenêtre
        if event.type == QUIT: 
            menuloop = 0
            pygame.quit()

        #Changement des boutons 
        if event.type == KEYDOWN and event.key == K_UP:
            if current_button == 1:
                playbutton = blackboard.render('>>JOUER<<', True, green, orange_salmon)
                leavebutton = blackboard.render('>>QUITTER<<', True, black, orange_salmon)
                current_button = 0
        if event.type == KEYDOWN and event.key == K_DOWN:
            if current_button == 0:
                playbutton = blackboard.render('>>JOUER<<', True, black, orange_salmon)
                leavebutton = blackboard.render('>>QUITTER<<', True, green, orange_salmon)
                current_button = 1

        #Choix d'un bouton
        if event.type == KEYDOWN:
            if event.key == K_RETURN or event.key == K_KP_ENTER:
                if current_button == 0:
                    pygame.quit()
                    menuloop = 0
                    exec(open("game.py").read())
                elif current_button == 1:
                    pygame.quit()
                    menuloop = 0

    #Actualisation de tous les affichages
    fenetre.fill(orange_salmon)
    fenetre.blit(logo, (595, 170))
    fenetre.blit(game_name, (430, 70))
    fenetre.blit(playbutton, (575, 340))
    fenetre.blit(leavebutton, (565, 420))
    fenetre.blit(credits_txt, (190, 500))
    pygame.display.update()
    pygame.display.flip()