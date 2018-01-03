#!/usr/bin/python
# -*- coding: utf-8 -*-

# Realise par:
# - ARNAUD Paul
# - RANARIMAHEFA Mitantsoa Michel

# classe Carte

class Carte:

    # creerCarte : -> Carte
    # description : creer une carte Vide
    def creerCarte(self):
        self.carte = dict()
        self.carte["type"] = ""
        self.carte["etat"] = ""
        self.carte["position"] = ""
        self.carte["attaque"] = ""
        self.carte["defense"] = ""
        self.carte["pdv"] = ""
        self.carte["zone"] = ""
        return self.carte

    # creerArcher : -> Carte
    # postcondition : - getTypeCarte(creerArcher()) == "archer"
    #                 - getEtatCarte(creerArcher()) == "normal"
    #                 - getPosCarte(creerArcher()) == "offensive"
    #                 - getForceAttaque(creerArcher()) == 1
    #                 - getForceDefense(creerArcher()) == 1
    #                 - getPDV(creerArcher()) == 1
    def creerArcher(self):
        self.carte = dict()
        self.carte["type"] = "archer"
        self.carte["etat"] = "normal"
        self.carte["position"] = "defensive"
        self.carte["attaque"] = "1"
        self.carte["defense"] = "1"
        self.carte["pdv"] = "1"
        self.carte["zone"] = "pioche"
        return self.carte

    # creerSoldat : -> Carte
    # description : cree une carte de type soldat, par default elle est en position offensive et a 1 point en force d'attaque
    # postcondition : - getTypeCarte(creerSoldat()) == "soldat"
    #                 - getEtatCarte(creerSoldat()) == "normal"
    #                 - getPosCarte(creerSoldat()) == "offensive"
    #                 - getForceAttaque(creerSoldat()) == 1
    #                 - getForceDefense(creerSoldat()) == 1
    #                 - getPDV(creerSoldatr()) == 1
    def creerSoldat(self):
        self.carte = dict()
        self.carte["type"] = "soldat"
        self.carte["etat"] = "normal"
        self.carte["position"] = "defensive"
        self.carte["attaque"] = "1"
        self.carte["defense"] = "1"
        self.carte["pdv"] = "1"
        self.carte["zone"] = "pioche"
        return self.carte

    # creerGarde : -> Carte
    # description : cree une carte de type garde
    # postcondition : - getTypeCarte(creerGarde()) == "garde"
    #                 - getEtatCarte(creerGarde()) == "normal"
    #                 - getPosCarte(creerGarde()) == "offensive"
    #                 - getForceAttaque(creerGarde()) == 1
    #                 - getForceDefense(creerGarde()) == 2
    #                 - getPDV(creerGarde()) == 2
    def creerGarde(self):
        self.carte = dict()
        self.carte["type"] = "garde"
        self.carte["etat"] = "normal"
        self.carte["position"] = "defensive"
        self.carte["attaque"] = "1"
        self.carte["defense"] = "2"
        self.carte["pdv"] = "2"
        self.carte["zone"] = "pioche"
        return self.carte

    # creerRoi1 :  -> Carte
    # description : cree le roi de type 1
    # postcondition : - getTypeCarte(creerRoi1()) == "roi"
    #                 - getEtatCarte(creerRoi1()) == "normal"
    #                 - getPosCarte(creerRoi1()) == "offensive"
    #                 - getForceAttaque(creerRoi1()) == 1
    #                 - getForceDefense(creerRoi1()) == 4
    #                 - getPDV(creerRoi1()) == 4
    def creerRoi1(self):
        self.carte = dict()
        self.carte["type"] = "roi"
        self.carte["etat"] = "normal"
        self.carte["position"] = "defensive"
        self.carte["attaque"] = "1"
        self.carte["defense"] = "4"
        self.carte["pdv"] = "4"
        self.carte["zone"] = "pioche"
        return self.carte

    # creerRoi2 :  -> Carte
    # description : cree le roi de type 2
    # postcondition : - getTypeCarte(creerRoi2()) == "roi"
    #                 - getEtatCarte(creerRoi2()) == "normal"
    #                 - getPosCarte(creerRoi2()) == "offensive"
    #                 - getForceAttaque(creerRoi2()) == 1
    #                 - getForceDefense(creerRoi2()) == 4
    #                 - getPDV(creerRoi2()) == 4
    def creerRoi2(self):
        self.carte = dict()
        self.carte["type"] = "roi"
        self.carte["etat"] = "normal"
        self.carte["position"] = "defensive"
        self.carte["attaque"] = "1"
        self.carte["defense"] = "4"
        self.carte["pdv"] = "4"
        self.carte["zone"] = "pioche"
        return self.carte

    # getTypeCarte : Carte -> Text
    # description : renvoie le type de la carte
    # post: Text est "soldat" ou "roi" ou "archer" ou "garde"
    def getTypeCarte(self):
        return self.carte["type"]

    # getEtatCarte : Carte -> Text
    # description : renvoie l'etat de la carte
    # post : Text est "normal" ou "affaiblie" (à subit une attaque mais pas détruite)
    def getEtatCarte(self):
        return self.carte["etat"]

    # getPosCarte : Carte -> Text
    # description : renvoie la position de la carte, position offensive ou defensive
    # post : Text est "offensive" ou "defensive"
    def getPosCarte(self):
        return self.carte["position"]

    # getForceAttaque: Carte -> int
    # description : renvoie la valeur de la force d'attaque de la carte
    def getForceAttaque(self):
        return self.carte["attaque"]

    # getZoneCarte: Carte -> Text
    # description : renvoie la zone ou se trouve la carte
    # post : Text est "Main" ou "Royaume" ou "Reserve" ou "Cimetiere" ou "CDB" ou "Pioche"
    def getZoneCarte(self):
        return self.carte["zone"]

    # getForceDefense: carte -> int
    # description : renvoie la valeur de la force de defense de la carte
    def getForceDefense(self):
        return self.carte["defense"]

    # getPDV : carte -> int
    # description : renvoie la valeur des points de vie de la carte
    def getPDV(self):
        return self.carte["pdv"]

    # setTypeCarte : Carte x Text -> Carte
    # description : modifie le type de la carte
    # post: Text est "soldat" ou "roi" ou "archer" ou "garde"
    def setTypeCarte(self,texte):
        self.carte["type"] = texte
        return self.carte

    # setEtatCarte :  Carte x Text -> Carte
    # description : modifie l'etat de la carte
    # post : Text est "normal" ou "affaiblie" (à subit une attaque mais pas détruite) ou "detruite" (?) ou "capture" (?)
    def setEtatCarte(self,texte):
        self.carte["etat"] = texte
        return self.carte

    # setZoneCarte: Carte x Text -> Carte
    # description : renvoie la zone ou se trouve la carte
    # pre : Text est "Main" ou "Royaume" ou "Reserve" ou "Cimetiere" ou "CDB" ou "Pioche"
    def setZoneCarte(self, texte):
        self.carte["zone"] = texte
        return self

    # setPosCarte : Carte x Text -> Carte
    # description : modifie  la position de la carte, position offensive ou defensive
    # post : Text est "offensive" ou "defensive"
    def setPosCarte(self,texte):
        self.carte["position"] = texte
        return self.carte

    # setForceAttaque: Carte x Int -> Carte
    # description : modifie la valeur de la force d'attaque de la carte
    def setForceAttaque(self,int):
        self.carte["attaque"] = int
        return self.carte

    # setForceDefense: Carte x Int -> Carte
    # description : modifie la valeur de la force de defense de la carte
    def setForceDefense(self,valeur):
        self.carte["defense"] = valeur
        return self.carte

    # setPDV : Carte x Int -> Carte
    # description : modifie la valeur des points de vie de la carte
    def setPDV(self,valeur):
        self.carte["pdv"] = valeur
        return self.carte

    # carteToString : Carte -> Text
    # description : renvoye le type de carte sous forme de texte
    # postcondition : Text est "soldat" ou "roi" ou "archer" ou "garde"
    def carteToString(self):
        return self.carte["type"]
