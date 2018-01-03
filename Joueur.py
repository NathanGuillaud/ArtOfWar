#!/usr/bin/python
# -*- coding: utf-8 -*-

# Realise par:
# - ARNAUD Paul
# - RANARIMAHEFA Mitantsoa Michel

# classe Reserve

from Pioche import *
from Royaume import *
from Reserve import *
from Cimetiere import *
from Main import *
from Carte import *

class Joueur:

    # creerJoueur : -> Joueur
    # description : creer un Joueur avec une main vide, une royaume vide, une pioche pleine de 20 cartes,
    #               un cimetiere vide, une reserve vide
    def creerJoueur(self):
        self.joueur = dict()
        pioche = Pioche()
        pioche.creerPioche()
        main = Main()
        main.creerMain()
        royaume = Royaume()
        royaume.creerRoyaume()
        cimetiere = Cimetiere()
        cimetiere.creerCimetiere()
        reserve = Reserve()
        reserve.creerReserve()
        self.joueur["main"] = main
        self.joueur["pioche"] = pioche
        self.joueur["royaume"] = royaume
        self.joueur["cimetiere"] = cimetiere
        self.joueur["reserve"] = reserve
        return self.joueur

    # getMain : Joueur -> main
    # description : retourne la main du joueur
    def getMain(self):
        return self.joueur["main"]

    # getRoyaume : Joueur -> Royaume
    # description : retourne le royaume du joueur
    def getRoyaume(self):
        return self.joueur["royaume"]

    # getPioche : Joueur -> Pioche
    # description : retourne la pioche du joueur
    #def __getitem__(self, key):
     #   return getattr(self, key)

    def getPioche(self):
        return self.joueur["pioche"]

    # getCimetiere : Joueur -> Cimetiere
    # description : retourne le cimetiere du joueur
    def getCimetiere(self):
        return self.joueur["cimetiere"]

    # getReserve : Joueur -> Reserve
    # description : retourne la reserve du joueur
    def getReserve(self):
        return self.joueur["reserve"]

    # setMain : Joueur x Main -> Joueur
    # description : attribue la main passée en paramètre comme la main du joueur
    def setMain(self,main):
        self.joueur["main"] = main
        return self.joueur

    # setRoyaume : Joueur x Royaume ->  Joueur
    # description : attribue le royaume passée en paramètre comme le royaume du joueur
    def setRoyaume(self,royaume):
        self.joueur["royaume"]=royaume
        return self.joueur

    # setPioche : Joueur x Pioche ->  Joueur
    # description : attribue la pioche passée en paramètre comme la pioche du joueur
    def setPioche(self,pioche):
        self.joueur['pioche']=pioche
        return self.joueur

    # setCimetiere : Joueur x Cimetiere ->  Joueur
    # description : attribue le cimetiere passée en paramètre comme le cimetiere du joueur
    def setCimetiere(self,cimetiere):
        self.joueur["cimetiere"]=cimetiere
        return self.joueur

    # setReserve : Joueur x Reserve ->  Joueur
    # description : attribue la reserve passée en paramètre comme la reserve du joueur
    def setReserve(self,reserve):
        self.joueur["reserve"]=reserve
        return self.joueur

    # piocher : Joueur  -> joueur
    # description : pioche une carte, envoie la carte de la pioche à la main
    # precondition : on ne peut pas piocher si la pioche est vide
    # postcondition : - getTailleMain(getMain(piocher(joueur))) == getTailleMain(getMain(joueur))) + 1
    #                 - getTaillePioche(getPioche(piocher(joueur))) == getTaillePioche(getPioche(joueur))) - 1
    def piocher(self):
        if (not Pioche.piocheIsEmpty(self.joueur["pioche"])):
            carte = Pioche.getFirstPioche(self.joueur["pioche"])
            Pioche.supprimerPioche(self.joueur["pioche"],carte)
            Main.ajouterMain(self.joueur["main"],carte)
            Carte.setZoneCarte(carte,"main")
        return self.joueur

    # mettreEnReserve : Joueur x Carte -> joueur
    # description : envoie la carte de la main à la reserve
    # postcondition : - getTailleReserve(getReserve(mettreEnReserve(joueur,carte))) == getTailleReserve(getReserve(joueur))) + 1
    #                 - getTailleMain(getMain(mettreEnReserve(joueur,carte))) == getTailleMain(getMain(joueur)))  - 1
    def mettreEnReserve(self,carte):
        Reserve.ajouterReserve(self.joueur["reserve"],carte)
        Main.supprimerMain(self.joueur["main"],carte)
        Carte.setZoneCarte(carte,"reserve")
        return self.joueur

    # demobiliser : Joueur x Carte -> Joueur
    # description : Envoye la carte de la main au royaume
    # postcondition : - getTailleRoyaume(getRoyaume(demobiliser(joueur,carte))) == getTailleRoyaume(getRoyaume(joueur))) + 1
    #                 - getTailleMain(getMain(demobiliser(joueur,carte))) == getTailleMain(getMain(joueur)))  - 1
    def demobiliser(self,carte):
        Royaume.ajouterRoyaume(self.joueur["royaume"],carte)
        Main.supprimerMain(self.joueur["main"],carte)
        Carte.setZoneCarte(carte,"royaume")
        return self.joueur
