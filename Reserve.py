#!/usr/bin/python
# -*- coding: utf-8 -*-

# Realise par:
# - ARNAUD Paul
# - RANARIMAHEFA Mitantsoa Michel

# classe Reserve

from Carte import *
class Reserve:

    # creerReserve : -> Reserve
    # description : cree une reserve vide
    # postcondition : - getTailleReserve(creerReserve()) == 0
    #                 - ReserveIsEmpty(creerReserve()) == True
    def creerReserve(self):
        self.reserve = []
        return self.reserve

    # ajouterReserve : Reserve x carte -> Reserve
    # description : ajoute la carte à la reserve
    # postcondition: - Ajoute la carte en fin de file
    #                - getTailleReserve(ajouterReserve(reserve,carte)) == getTailleReserve(reserve,carte) +1
    #                - ReserveIsEmpty(ajouterReserve(reserve,carte)) == False
    def ajouterReserve(self,carte):
        self.reserve.append(carte)
        Carte.setZoneCarte(carte,"reserve")
        return self.reserve

    # supprimerReserve : Reserve x carte -> Reserve
    # description : supprime la carte de la reserve
    # precondition : on n'enleve pas la carte si la reserve est vide
    # postcondition: - enleve la 1er carte de la reserve
    #                - getTailleReserve(supprimerReserve(reserve,carte)) == getTailleReserve(reserve,carte) - 1
    def supprimerReserve(self,carte):
        self.reserve.remove(carte)
        Carte.setZoneCarte(carte,"")
        return self.reserve

    # getFirstReserve : Reserve -> Carte
    # description : renvoie la 1er carte de la reserve du joueur
    def getFirstReserve(self):
        return self.reserve[0]

    # getTailleReserve : reserve -> int
    # description : renvoie le nombre de carte dans la reserve du joueur
    def getTailleReserve(self):
        return len(self.reserve)

    # ReserveIsEmpty : Reserve -> boolean
    # description : renvoie vrai si la Reserve est vide. Faux sinon
    def ReserveIsEmpty(self):
        return self.getTailleReserve() == 0
