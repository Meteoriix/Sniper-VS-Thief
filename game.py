# -*- coding: utf-8 -*-
#Pour plus d'informations, lisez le README.md sur notre page GitHub : https://github.com/Meteoriix/Sniper-VS-Thief
#JEU
import random
import pygame
import csv
from random import *
from pygame import *
from tkinter import *
from tkinter import messagebox

#Initialisations
x = 0
y = 0
tour = 0 #Tour = 0 = Tour voleur / Tour = 1 = Tour Sniper
Tk().wm_withdraw() 

#Fonction de création des index de chaque case
def indexfind(index):
    y = index // 13 * 99
    x = (index * 99) - (1287 * (y/99))
    return([x,y])

#Fonction de sauvegarde dans le CSV
def saveincsv():
    with open("gamedata.csv", "w") as output:
        character_writer = csv.DictWriter(output, fieldnames=["A","B"])
        character_writer.writerow({"A" : "A", "B" : "B"})
        character_writer.writerow({"A" : "current", "B" : voleurindex})
        character_writer.writerow({"A" : "old", "B" : oldindex})

#Initalisation de PyGame
pygame.init()

#Fenêtre PyGame (Dimensions : 1278x684)
fenetre = pygame.display.set_mode((1278, 684))
pygame.display.set_caption("Sniper VS Thief")
icon = pygame.image.load("assets/images/diamond.png")
pygame.display.set_icon(icon)

#Génération aléatoire du plateau
MAP = []
walls = [0,13,26,39,52,65,78,12,25,38,51,64,77,90]

for row in range (0,7): #nombre de lignes
    for columns in range(0,13): #nombre de colonnes
        #Génération aléatoire des obstacles
        if (row * 13 + columns) in walls:
            obstacle = pygame.image.load("assets/images/obstacle.png")
            fenetre.blit(obstacle, (x, y))
            MAP.append(1)
        else:
            casetype = randint(1,5)
            if (columns != 1 or row != 3):
                if (columns != 11 or row != 3):
                    if casetype == 1:
                        obstacle = pygame.image.load("assets/images/obstacle.png")
                        fenetre.blit(obstacle, (x, y))
                        MAP.append(1)
                    elif casetype !=1:
                        case = pygame.image.load("assets/images/case.png")
                        fenetre.blit(case, (x, y))
                        casepos = case.get_rect()
                        MAP.append(0)
                else:
                    case = pygame.image.load("assets/images/case.png")
                    fenetre.blit(case, (x, y))
                    casepos = case.get_rect()
                    MAP.append(0)
            else:
                case = pygame.image.load("assets/images/case.png")
                fenetre.blit(case, (x, y))
                casepos = case.get_rect()
                MAP.append(0)
        x += 99
    x = 0
    y += 99
y = 0
for i in range (13):
    MAP.append(1)

#Chargement des images
diamond = pygame.image.load("assets/images/diamond.png").convert_alpha()
valid = pygame.image.load("assets/images/valid.png")
maybe = pygame.image.load("assets/images/maybe.png")
voleur = pygame.image.load("assets/images/voleur.png").convert_alpha()
oldvoleur = pygame.image.load("assets/images/oldvoleur.png").convert_alpha()
voleurindex = 40
oldindex = voleurindex
saveincsv()

#Chargement du sélecteur
selector = pygame.image.load("assets/images/selecteur.png")
selindex = 40
selpos = selector.get_rect()
selpos = selpos.move(indexfind(40))

IndexMatrice = {0 : -1 ,1 : -13,2 : 1,3 : 13,4 : 0,}

#Actualisation de la fenêtre
pygame.display.flip()

#BOUCLE PRINCIPALE
gameloop = 1 #Variable de la boucle de jeu
while gameloop: #Lancement de la boucle de jeu
    for event in pygame.event.get(): #Lancement des évènements
        #Fermeture améliorée de la fenêtre
        if event.type == QUIT: 
            gameloop = 0
            pygame.quit()

        if event.type == KEYDOWN and event.key == K_LEFT: #Déplacement du selecteur vers la gauche
            if selpos.x != 0: #Vérification de la présence d'une bordure
                if MAP[selindex+ IndexMatrice.get(0)] == 0:
                    fenetre.blit(case, indexfind(selindex))
                    selpos = selpos.move(-99, 0)
                    selindex = selindex + IndexMatrice.get(0)

        if event.type == KEYDOWN and event.key == K_RIGHT: #Déplacement du sélecteur vers la droite
            if selpos.x < 1179: #Vérification de la présence d'une bordure
                if MAP[selindex+ IndexMatrice.get(2)] == 0:
                    fenetre.blit(case, indexfind(selindex))
                    selpos = selpos.move(99, 0)
                    selindex = selindex + IndexMatrice.get(2)

        if event.type == KEYDOWN and event.key == K_DOWN: #Déplacement du sélecteur vers le bas
            if selpos.y < 585: #Vérification de la présence d'une bordure
                if MAP[selindex+ IndexMatrice.get(3)] == 0:
                    fenetre.blit(case, indexfind(selindex))
                    selpos = selpos.move(0, 99)
                    selindex = selindex + IndexMatrice.get(3)

        if event.type == KEYDOWN and event.key == K_UP: #Déplacement du sélecteur vers le haut
            if selpos.y != 0: #Vérification de la présence d'une bordure
                if MAP[selindex+ IndexMatrice.get(1)] == 0:
                    fenetre.blit(case, indexfind(selindex))
                    selpos = selpos.move(0, -99)
                    selindex = selindex + IndexMatrice.get(1)

        if event.type == KEYDOWN and event.key == pygame.K_RETURN: #Validation du tour
            if tour == 0: #Validation du tour du Voleur
                if(selindex == 50): #Victoire du Voleur
                    messagebox.showinfo('Fin de partie','Le voleur a gagné')
                    gameloop = 0
                    pygame.quit()
                    exec(open("menu_end.py").read())
                else: #Passage au tour du Sniper
                    tour = 1
                    messagebox.showinfo('Tour suivant', "C'est au tour du Sniper")
                    if selindex in validcases:
                        input_file = csv.DictReader(open("gamedata.csv"))
                        for row in input_file:
                            old_type = row["A"]
                            csvindex = row["B"]
                            if old_type == "current":
                                oldindex = int(csvindex)
                        voleurindex = selindex
                        saveincsv()
                        selpos.x = 0
                        selpos.y = 0
                        selpos = selpos.move(indexfind(oldindex))
                        selindex = oldindex
                        for a in validcases:
                            fenetre.blit(case, indexfind(a))

            elif tour == 1: #Validation du tour du Sniper
                if selindex == voleurindex: #Victoire du Sniper
                    messagebox.showinfo('Fin de partie','Le sniper a gagné')
                    gameloop = 0
                    pygame.quit()
                    exec(open("menu_end.py").read())
                else: #Passage au tour du Voleur
                    if selindex in validcases:
                        tour = 0
                        selpos.x = 0
                        selpos.y = 0
                        selpos = selpos.move(indexfind(oldindex))
                        selindex = oldindex
                        messagebox.showinfo('Tour suivant', "C'est au tour du Voleur")
                        for a in validcases:
                            fenetre.blit(case, indexfind(a))

    validcases = []

    if tour == 0: #Affichage des cases possibles pour le voleur
        for u in range(0,5):
            if voleurindex + IndexMatrice.get(u) < -1 :
                validcases.append(voleurindex+ IndexMatrice.get(u))
            elif MAP[voleurindex+ IndexMatrice.get(u)] == 0:
                fenetre.blit(valid,indexfind(voleurindex+ IndexMatrice.get(u)))
                validcases.append(voleurindex+ IndexMatrice.get(u))
        fenetre.blit(diamond, indexfind(50))
        fenetre.blit(selector, indexfind(selindex))
        fenetre.blit(voleur, indexfind(voleurindex))

    if tour == 1: #Affichage des cases possibles pour le sniper
        for u in range(0,5):
            if oldindex + IndexMatrice.get(u) < -1 :
                validcases.append(oldindex+ IndexMatrice.get(u))
            elif MAP[oldindex+ IndexMatrice.get(u)] == 0:
                fenetre.blit(maybe,indexfind(oldindex+ IndexMatrice.get(u)))
                validcases.append(oldindex+ IndexMatrice.get(u))
        fenetre.blit(diamond, indexfind(50))
        fenetre.blit(selector, indexfind(selindex))
        fenetre.blit(oldvoleur, indexfind(oldindex))

    pygame.display.update()
    pygame.display.flip()


