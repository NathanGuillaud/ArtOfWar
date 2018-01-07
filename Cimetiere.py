#!/usr/bin/python
# -*- coding: utf-8 -*-

# Realise par:
# - ARNAUD Paul
# - RANARIMAHEFA Mitantsoa Michel

# classe Cimetiere

from Carte import *
class Cimetiere:
    # creerCimetiere : -> Cimetiere
    # description : creer un Cimetiere Vide
    def creerCimetiere(self):
        self.cimetiere = []
        return self.cimetiere

    # ajouterCimetiere : Cimetiere x carte -> Cimetiere
    # description : ajoute la carte au cimetiere
    def ajouterCimetiere(self,carte):
        self.cimetiere.append(carte)
        Carte.setZoneCarte(carte,"cimetiere")
        return self.cimetiere

    # supprimerCimetiere : Cimetiere x carte -> Cimetiere
    # description : enleve la carte du cimetiere
    def supprimerCimetiere(self,carte):
        self.self.remove(carte)
        Main.setZoneCarte(carte,"")
        return self.cimetiere
