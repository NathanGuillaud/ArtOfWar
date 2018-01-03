#!/usr/bin/python
# -*- coding: utf-8 -*-

# Realise par:
# - ARNAUD Paul
# - RANARIMAHEFA Mitantsoa Michel

# classe Main
from Carte import *

class Main:
    # creerMain : -> Main
    # description : crée une main vide
    # postcondition : - getTailleMain(creerMain()) == 0
    #                 - mainIsEmpty(creerMain()) == True
    def creerMain(self):
        self.main = list()
        return self.main

    # ajouterMain : Main x Carte -> Main
    # description : ajoute la carte à la main
    # postcondition : getTailleMain(ajouterMain(main,carte)) == getTailleMain(main,carte) + 1
    def ajouterMain(self,carte):
        self.main.append(carte)
        Carte.setZoneCarte(carte,"main")
        return self.main

    # supprimerMain : Main x Carte -> Main
    # description : supprime la carte de la main
    # precondition : on n'enleve pas la carte si la main est vide
    # postcondition: getTailleMain(supprimerMain(main,carte)) == getTailleMain(main,carte) - 1
    def supprimerMain(self,carte):
       
        self.main.remove(carte)
        Carte.setZoneCarte(carte,"")
        return self.main
                                                                                                                                
    # getTailleMain : main -> int
    # description : renvoie le nombre de carte dans la main du joueur
    def getTailleMain(self):
        return len(self.main)

    # mainIsEmpty : Main -> boolean
    # description : renvoie vrai si la Main est vide. Faux sinon
    def mainIsEmpty(self):
        return (len(self.main)==0)

    # mainToString : Main -> Text
    # description : renvoie la main du joueur sous forme de texte
    #               exemple : "Main : Roi, Archer, Archer, Soldat"
    # postcondition : si mainIsEmpty(main) == True alors mainToString(main) = 'Main:vide'
    def mainToString(self):
        mainString = ""
        for i in range (0,len(self.main)):
            carte = self.main[i]
            mainString += carte.carte["type"] + " "
        return mainString

    # getElementsMain : Main -> List[Carte]
    # description : renvoie la liste des cartes dans la main du joueur
    # postcondition : renvoie une liste vide quand la main est vide
    def getElementsMain(self):
        self.cartesMain = []
        for i in range (0,len(self.main)):
            self.cartesMain.append(self.main[i])
        return self.cartesMain

    # getCarteMain : Main x Text -> Carte
    # description : renvoie la carte correspondant au texte rentree, si plusieurs occurences renvoie la 1er occurence
    #               sinon renvoie une erreur
    # postcondition : Text est "soldat" ou "roi" ou "archer" ou "garde"
    def getCarteMain(self,texte):
        trouver = False
        if texte == "soldat" or texte == "roi" or texte == "archer" or texte == "garde" :
            n=0
            while not(trouver) and (len(self.main) > n) :
                c = self.main[n]
                if (c.carte["type"] == texte):
                    trouver = True
                n = n + 1
            if trouver :
                return c
        else:
            print("erreur")
            return 0
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
