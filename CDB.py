#!/usr/bin/python
# -*- coding: utf-8 -*-

# Realise par:
# - ARNAUD Paul
# - RANARIMAHEFA Mitantsoa Michel

# classe Champ de bataille

from Carte import *
class CDB:
    # creerCDB : -> CDB
    # description : crée un champ de bataille vide
    #               1 à 3 correspond au front du 1er joueur de gauche à droite, 4 à 6 à les positions
    #               de l'arriere du champ de bataille avec 4 derrière le 1 et ainsi de suite.
    #               Meme chose pour le 2eme Joueur mais en commençant par 7 jusqu'a 12.
    def creerCDB(self):
        self.cdb = dict()
        for i in range(1, 13):
            self.cdb[str(i)] = ""
        return self.cdb

    # ajouterCDB : CDB x carte x int -> CDB
    # description : ajoute la carte au champ de bataille à la position donnée.
    #               1 à 3 correspond au front du 1er joueur de gauche à droite, 4 à 6 à les positions
    #               de l'arriere du champ de bataille avec 4 derrière le 1 et ainsi de suite.
    #               Meme chose pour le 2eme Joueur mais en commençant par 7 jusqu'a 12.
    # precondition : 1 <= position <= 12
    def ajouterCDB(self,carte,position):
        self.cdb[str(position)] = carte
        Carte.setZoneCarte(carte,"cdb")
        return self.cdb

    # supprimerCDB : CDB x carte x int -> CDB
    # description : enlever la carte à la position donnée du champ de bataille
    #               1 à 3 correspond au front du 1er joueur de gauche à droite, 4 à 6 à les positions
    #               de l'arriere du champ de bataille avec 4 derrière le 1 et ainsi de suite.
    #               Meme chose pour le 2eme Joueur mais en commençant par 7 jusqu'a 12.
    # precondition : 1 <= position < 12
    def supprimerCDB(self,carte,position):
        self.cdb[str(position)] = ""
        Carte.setZoneCarte(carte,"")
        return self.cdb

    # estOccupee : CDB x int -> boolean
    # description : renvoie faux si aucune carte n'est sur la positon donnée. Vrai sinon
    #               1 à 3 correspond au front du 1er joueur de gauche à droite, 4 à 6 à les positions
    #               de l'arriere du champ de bataille avec 4 derrière le 1 et ainsi de suite.
    #               Meme chose pour le 2eme Joueur mais en commençant par 7 jusqu'a 12.
    # precondition : 1 <= position < 12
    def estOccupee(self, position):
        return not self.cdb[str(position)] == ""

    # getCarteCDB : CDB x int -> carte
    # description : renvoie la carte à la position donnee, renvoie
    #               1 à 3 correspond au front du 1er joueur de gauche à droite, 4 à 6 à les positions
    #               de l'arriere du champ de bataille avec 4 derrière le 1 et ainsi de suite.
    #               Meme chose pour le 2eme Joueur mais en commençant par 7 jusqu'a 12.
    # precondition : 1 <= position < 12
    def getCarteCDB(self, position):
        return self.cdb[str(position)]

    # avancerCarte : CDB x carte -> CDB
    # description : avance la carte de la ligne arriere au front
    def avancerCarte(self,carte):
        if (self.cdb["4"] == carte):
            self.cdb["4"] = ""
            self.cdb["1"] = carte
        if (self.cdb["5"] == carte):
            self.cdb["5"] = ""
            self.cdb["2"] = carte
        if (self.cdb["6"] == carte):
            self.cdb["6"] = ""
            self.cdb["3"] = carte
        if (self.cdb["10"] == carte):
            self.cdb["10"] = ""
            self.cdb["7"] = carte
        if (self.cdb["11"] == carte):
            self.cdb["11"] = ""
            self.cdb["8"] = carte
        if (self.cdb["12"] == carte):
            self.cdb["12"] = ""
            self.cdb["9"] = carte
        return self.cdb
