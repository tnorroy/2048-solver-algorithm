#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 14:37:57 2024

@author: tomnorroy
"""

"""
Le programme permet de simuler le jeu du 2048 dont le but est d'atteindre la case 2048 dans une grille de dimension 4 sur 4. Pour cela, on fusionne deux cases similaires pour créer une case de valeur deux fois suppérieures aux précédentes. Possibilité d'essayer le jeu rapidement au lien suivant: https://play2048.co
Afin de tester le programme, exécuter la fonction lancer_partieAI(profondeur, repetition) avec profondeur = 4 et récurrence = 10 (temps estimé d'une partie = 2 min)
"""
from random import randint
import random
import numpy as np
import copy


def lancer_partieAI(profondeur, repetition):
# Initialise la grille et lance l'algorithme de résolution
    matrice = [[0] * 4 for i in range(4)]
    for k in range(2):
        matrice = ajout(matrice)
    print(np.array(matrice))

    while True:

        matrice_avant = copy.deepcopy(matrice)
        matrice_test = copy.deepcopy(matrice)

        L = []
        h = 0
        b = 0
        d = 0
        g = 0

        for _ in range(repetition):
            matrice_test = copy.deepcopy(matrice)
            L.append(meilleur_mouvement(profondeur, matrice_test)[1])

        for i in range(len(L)):

            if L[i] == haut:
                h += 1
            if L[i] == bas:
                b += 1
            if L[i] == droite:
                d += 1
            if L[i] == gauche:
                g += 1
        if max(h, b, d, g) == h:
            mouv = haut
        if max(h, b, d, g) == b:
            mouv = bas
        if max(h, b, d, g) == d:
            mouv = droite
        if max(h, b, d, g) == g:
            mouv = gauche
        print((max(h, b, d, g) / repetition) * 100, "% de", mouv, "choisi")

        if mouv == haut:
            matrice = haut(matrice)
            e = etat_partie(matrice)
            print(e)
            if e == "PARTIE NON FINIE" and matrice != matrice_avant:

                matrice = ajout(matrice)
            elif e == "PARTIE NON FINIE" and matrice == matrice_avant:

                print("mouvement impossible")
            else:
                print(e)
                return score_grille(matrice)[0], meilleur_case(matrice)
                break

        if mouv == bas:
            matrice = bas(matrice)
            e = etat_partie(matrice)
            print(e)
            if e == "PARTIE NON FINIE" and matrice != matrice_avant:

                matrice = ajout(matrice)
            elif e == "PARTIE NON FINIE" and matrice == matrice_avant:

                print("mouvement impossible")
            else:
                print(e)
                return score_grille(matrice)[0], meilleur_case(matrice)
                break

        if mouv == gauche:
            matrice = gauche(matrice)
            e = etat_partie(matrice)
            print(e)
            if e == "PARTIE NON FINIE" and matrice != matrice_avant:

                matrice = ajout(matrice)
            elif e == "PARTIE NON FINIE" and matrice == matrice_avant:

                print("mouvement impossible")

            else:
                print(e)
                return score_grille(matrice)[0], meilleur_case(matrice)
                break

        if mouv == droite:
            matrice = droite(matrice)
            e = etat_partie(matrice)
            print(e)
            if e == "PARTIE NON FINIE" and matrice != matrice_avant:

                matrice = ajout(matrice)
            elif e == "PARTIE NON FINIE" and matrice == matrice_avant:

                print("mouvement impossible")
            else:
                print(e)
                return score_grille(matrice)[0], meilleur_case(matrice)
                break

        A = score_grille(matrice)[0]
        print(np.array(matrice), A)


def ajout(matrice):
# ajout d'un 2 ou d'un 4 dans une case vide aléatoire
    i = randint(0, 3)
    j = randint(0, 3)
    while matrice[i][j] != 0:
        i = randint(0, 3)
        j = randint(0, 3)
    r = random.random()
    if r <= 0.9:
        matrice[i][j] = 2
    else:
        matrice[i][j] = 4
    return matrice


def gauche(matrice,):
# Déplacement des cases vers la gauche et fusion des cases identiques adjacentes
    for i in range(4):
        new_mat = [x for x in matrice[i] if x != 0]
        for j in range(len(new_mat) - 1):
            if new_mat[j] == new_mat[j + 1]:
                new_mat[j] *= 2
                new_mat[j + 1] = 0

        new_mat = [x for i, x in enumerate(new_mat) if x != 0]
        new_mat += [0] * (4 - len(new_mat))
        matrice[i] = new_mat
    return matrice


def retourne(matrice):
# Symétrique par rapport à l'axe vertical de la grille
    new_mat = []
    for i in range(4):
        new_mat.append([])
        for j in range(4):

            new_mat[i].append(matrice[i][3 - j])
    return new_mat


def transpose(matrice):
# Transposée de la grille
    new_mat = []
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(matrice[j][i])
    return new_mat


def droite(matrice):
# Déplacement à droite et fusion des cases identiques
    matrice = retourne(matrice)
    matrice = gauche(matrice)
    matrice = retourne(matrice)
    return matrice


def haut(matrice):
# Déplacement en haut et fusion des cases identiques
    matrice = transpose(matrice)
    matrice = gauche(matrice)
    matrice = transpose(matrice)
    return matrice


def bas(matrice):
# Déplacement en bas et fusion des cases identiques
    matrice = transpose(matrice)
    matrice = droite(matrice)
    matrice = transpose(matrice)
    return matrice


def etat_partie(matrice):
# Vérifie si il est encore possile d'effectuer des mouvements

    for i in range(4):
        for j in range(4):
            if matrice[i][j] == 0:
                return "PARTIE NON FINIE"

    for i in range(3):
        for j in range(3):
            if matrice[i][j] == matrice[i + 1][j] or matrice[i][j] == matrice[i][j + 1]:
                return "PARTIE NON FINIE"

    for j in range(3):
        if matrice[3][j] == matrice[3][j + 1]:
            return "PARTIE NON FINIE"

    for i in range(3):
        if matrice[i][3] == matrice[i + 1][3]:
            return "PARTIE NON FINIE"

    return "PARTIE FINIE"


def score_grille(matrice):
# Calcul du score affecté à la grille en fonction des cases présentes et renvoie une matrice constituée des scores affectées à chaque case
    score = 0
    matrice_de_score = [[0] * 4 for i in range(4)]
    for i in range(4):
        for j in range(4):
            case = matrice[i][j]
            if case == 4:
                score += 3
                matrice_de_score[i][j] = 3
            elif case == 8:
                score += 15
                matrice_de_score[i][j] = 15
            elif case == 16:
                score += 46
                matrice_de_score[i][j] = 46
            elif case == 32:
                score += 124
                matrice_de_score[i][j] = 124
            elif case == 64:
                score += 313
                matrice_de_score[i][j] = 313
            elif case == 128:
                score += 748
                matrice_de_score[i][j] = 748
            elif case == 256:
                score += 1766
                matrice_de_score[i][j] = 1766
            elif case == 512:
                score += 4045
                matrice_de_score[i][j] = 4045
            elif case == 1024:
                score += 9113
                matrice_de_score[i][j] = 9113
            elif case == 2048:
                score += 20275
                matrice_de_score[i][j] = 20275
            elif case == 4096:
                score += 44646
                matrice_de_score[i][j] = 44646
            elif case == 8192:
                score += 97484
                matrice_de_score[i][j] = 97484

    return score, matrice_de_score

def meilleur_case(matrice):
# Renvoie la case à la valeur la plus grande
    case_max=0
    for i in range(4):
        for j in range(4):
            if case_max<matrice[i][j]:
              case_max=matrice[i][j]
    return case_max

def meilleur_mouvement(profondeur, matrice):
# Choix du meilleur mouvement par une fonction récursive

    meilleur_heuristique = 0
    meilleur_mvt = gauche

    if profondeur == 0 or etat_partie(matrice) == "PARTIE FINIE":
        return heuristique(matrice), None

    for mouvement in (droite, haut, bas, gauche):
        matrice_test2 = copy.deepcopy(matrice)
        matrice_test2 = mouvement(matrice_test2)

        if (
            etat_partie(matrice_test2) == "PARTIE NON FINIE"
            and matrice_test2 != matrice
        ):
            matrice_test2 = ajout(matrice_test2)
            heuristique_mat = meilleur_mouvement(profondeur - 1, matrice_test2)[0]

            if heuristique_mat > meilleur_heuristique:
                meilleur_heuristique = heuristique_mat
                meilleur_mvt = mouvement

    return meilleur_heuristique, meilleur_mvt


def heuristique(matrice):
# Pondère le score associé à la matrice selon l'emplacement des plus grosses cases, permet de guider la résolution vers des configurations favorables

    heuristique_grille = 0

    matrice_de_poids_haut_gauche = [
        [1, 0.8, 0.6, 0.4],
        [0.2, 0.2, 0.2, 0.2],
        [0.2, 0.2, 0.2, 0.2],
        [0.2, 0.2, 0.2, 0.2],
    ]
    matrice_de_poids_haut_droite = [
        [0.4, 0.6, 0.8, 1],
        [0.2, 0.2, 0.2, 0.2],
        [0.2, 0.2, 0.2, 0.2],
        [0.2, 0.2, 0.2, 0.2],
    ]
    matrice_de_poids_bas_gauche = [
        [0.2, 0.2, 0.2, 0.2],
        [0.2, 0.2, 0.2, 0.2],
        [0.2, 0.2, 0.2, 0.2],
        [1, 0.8, 0.6, 0.4],
    ]
    matrice_de_poids_bas_droite = [
        [0.2, 0.2, 0.2, 0.2],
        [0.2, 0.2, 0.2, 0.2],
        [0.2, 0.2, 0.2, 0.2],
        [0.4, 0.6, 0.8, 1],
    ]

    case_max = 0
    for i in range(4):
        for j in range(4):
            if case_max < matrice[i][j]:
                case_max = matrice[i][j]

            if matrice[0][0] == case_max:
                matrice_de_poids = matrice_de_poids_haut_gauche

            if matrice[0][3] == case_max:
                matrice_de_poids = matrice_de_poids_haut_droite

            if matrice[3][0] == case_max:
                matrice_de_poids = matrice_de_poids_bas_gauche

            if matrice[3][3] == case_max:
                matrice_de_poids = matrice_de_poids_bas_droite

# On calcule le score pondéré par la matrice de poids choisie et on renvoie ainsi l'heuristique de la grille.
    matrice_heuristique = np.array(score_grille(matrice)[1]) * matrice_de_poids
    for i in range(4):
        for j in range(4):
            heuristique_grille += matrice_heuristique[i][j]
    return heuristique_grille

### Programme principal ###

lancer_partieAI(4, 10)