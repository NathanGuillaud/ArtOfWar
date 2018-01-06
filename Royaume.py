#!/usr/bin/python
# -*- coding: utf-8 -*-

# Realise par:
# - ARNAUD Paul
# - RANARIMAHEFA Mitantsoa Michel

# classe Royaume

from Carte import *

class Royaume:

    # creerRoyaume : -> Royaume
    # description : creer un Royaume vide
    # postcondition : - getTailleRoyaume(creerRoyaume()) == 0
    #                 - RoyaumeIsEmpty(creerRoyaume()) == True
    #                 - getNbSoldat(creerRoyaume()) == 0
    #                 - getNbArcher(creerRoyaume()) == 0
    #                 - getNbGarde(creerRoyaume()) == 0
    def creerRoyaume(self):
        self.royaume = dict()
        self.royaume["soldat"] = []
        self.royaume["archer"] = []
        self.royaume["garde"] = []
        return self.royaume

    # ajouterRoyaume : Royaume x Carte -> Royaume
    # description : ajoute la carte au Royaume
    #               - getTailleRoyaume(ajouterRoyaume(royaume,carte)) == getTailleRoyaume(royaume,carte) + 1
    #               - RoyaumeIsEmpty(ajouterRoyaume(reserve,carte)) == False
    def ajouterRoyaume(self, carte):
        if carte.carte["type"] == "roi":
            print("Le roi ne peut pas etre ajouté au Royaume !")
            return self.royaume
        else:
            self.royaume[carte.carte["type"]].append(carte.carte)
            Carte.setZoneCarte(carte,"royaume")
        return self.royaume

    #main.main.append(carte)
    #Carte.setZoneCarte(carte, "main")
    #return main.main

    # supprimerRoyaume : Royaume x Carte -> Royaume
    # description : enleve la carte du Royaume
    # precondition : on n'enleve pas la carte si le royaume est vide
    # postcondition : getTailleRoyaume(supprimerRoyaume(royaume,carte)) == getTailleRoyaume(royaume,carte) - 1
    def supprimerRoyaume(self,carte):
        if(not RoyaumeIsEmpty(royaume)):
            self.royaume[carte["type"]].remove(carte)
            Carte.setZoneCarte(carte,"")
        return self.royaume

    # getTailleRoyaume : Royaume -> int
    # description : renvoie le nombre de carte dans le royaume du joueur
    def getTailleRoyaume(self):
        return len(self.royaume["soldat"]) + len(self.royaume["archer"]) + len(self.royaume["garde"])

    # getNbSoldat : Royaume -> int
    # description : renvoie le nombre de soldats dans le royaume du joueur
    def getNbSoldat(self):
        return len(self.royaume["soldat"])

    # getNbArcher : Royaume -> int
    # description : renvoie le nombre d'archers dans le royaume du joueur
    def getNbArcher(self):
        return len(self.royaume["archer"])

    # getNbGarde : Royaume -> int
    # description : renvoie le nombre de garde dans le royaume du joueur
    def getNbGarde(self):
        return len(self.royaume["garde"])

    # RoyaumeIsEmpty : Royaume -> boolean
    # description : renvoie vrai si le Royaume est vide. Faux sinon
    def RoyaumeIsEmpty(self):
        return getTailleRoyaume(self.royaume) == 0

    # getElementsRoyaume : Royaume -> List[Carte]
    # description : renvoie la liste des cartes dans le royaume du joueur
    # postcondition : getElementsRoyaume(creerRoyaume()) == []
    def getElementsRoyaume(self):
        return 0

    # royaumeToString : Royaume -> Text
    # description : renvoie le nombre d'elements de chaque type de carte sous forme de texte
    #               exemple : "Royaume :  Archer = 2, Garde = 0, Soldat = 1"
    def royaumeToString(self):
        return "Royaume : Archer = " + str(getNbArcher(self.royaume)) + ", Garde = " + str(getNbGarde(self.royaume)) + ", Soldat = " + str(getNbSoldat(self.royaume))

    # getCarteRoyaume : Royaume x Text -> Carte
    # description : renvoie la carte dans le royaume correspondant au texte rentree, si plusieurs occurences renvoie la 1er occurence
    #               sinon renvoie une erreur
    # postcondition : Text est "soldat" ou "roi" ou "archer" ou "garde"
    def getCarteRoyaume(self,texte):
        if(self.royaume[texte] != 0):
            return self.royaume[texte][0]
        else:
            return "Pas de carte de ce type dans le Royaume"
