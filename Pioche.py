#!/usr/bin/python
# -*- coding: utf-8 -*-

# Realise par:
# - ARNAUD Paul
# - RANARIMAHEFA Mitantsoa Michel

# classe Pioche
import random
from Carte import *
from Main import *
class Pioche:
    # creerPioche : -> Pioche
    # description : creer une pioche avec 9 soldat, 6 gardes et 5 archers répartie dans la pioche de manière aléatoire
    # poscondition : - getTaillePioche(creerPioche()) == 20
    #                - PiocheIsEmpty(creerPioche()) == False
    def creerPioche(self):
        self.pioche = list()

        archer = Carte()
        archer.creerArcher()

        for i in range(1,5):
            self.pioche.append(archer)

        garde = Carte()
        garde.creerGarde()

        for i in range(1, 7):
            self.pioche.append(garde)

        soldat = Carte()
        soldat.creerSoldat()

        for i in range(1, 10):
            self.pioche.append(soldat)
        
        random.shuffle(self.pioche)
                
        return self.pioche

    # getTaillePioche : Pioche -> Int
    # description : renvoie le nombre de carte dans la pioche du joueur
    def getTaillePioche(self):
        return len(self.pioche)

    # getFirstPioche : Pioche -> Carte
    # description : renvoie la 1er carte de la pioche du joueur
    # postcondition : getFirstPioche(ajouterPioche(creerPioche(),carte)) == carte
    def getFirstPioche(self):
        cartePioche = self.pioche[0]
        del self.pioche[0]
        return cartePioche

    # ajouterPioche : Pioche x Carte -> Pioche
    # description : ajoute la carte à la self.

    # postcondition : - place la carte au dessus de la pile
    #                 - getTaillePioche(ajouterPioche(pioche,carte)) == getTaillePioche(pioche,carte) + 1
    def ajouterPioche(self,carte):
        self.self.append(carte)
        setZoneCarte(carte,"pioche")
        return self.pioche

    # supprimerPioche : Pioche x Carte -> Pioche
    # description : enleve la 1er carte de la pioche
    # precondition : on n'enleve pas la carte si la pioche est vide
    # postcondition: - enleve la 1er carte de la pioche
    #                - getTaillePioche(supprimerPioche(pioche,carte)) == getTaillePioche(pioche,carte) - 1
    #def supprimerPioche(self,carte):
    def supprimerPioche(self, carte):
        del self.pioche[0]
        Carte.setZoneCarte(carte,"")
        return self.pioche
    
    # piocheIsEmpty : Pioche -> boolean
    # description : renvoie vrai si la pioche est vide. Faux sinon
    def piocheIsEmpty(self):
        return (len(self.pioche) == 0)
