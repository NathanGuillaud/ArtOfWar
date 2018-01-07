# -----
# Manque classe lors de l'appel des fonctions
# Certains objets mal créés : e : newc = Carte.creerSoldat() au lieu de newc = Carte() puis newc.creerSoldat() 
# Inversions des paramètres d'appel dans les fonctions
# Nombre de paramètres erronné dana sle sappels de fonctions
# Objet passé au fonctions pas du bon type (e : <str> carte au lieu de <Carte> carte
# Gestion des joueurs (joueur courant vs adverse) => utilisation de variables globales
# A l'init, manque certaines créations d'instances d'objets (ex : Joueur, Picohe)
# Imports ?
#Manque de la position dans la récupération de la liste des cartes attaquables
#Récupération de la position des cartes sur le cbd avec la fonction getAttaquants
#Gestion des erreurs de saisie ?
# Manipulation de string au lieu de d'objets après saisie
# Visibilité joueur courant => afficher message lors des permutations de joueurs (pas seuelment en fin de tour)
# -----

#!/usr/bin/python
# -*- coding: utf-8 -*-

# Realise par:
# - ARNAUD Paul
# - RANARIMAHEFA Mitantsoa Michel

#### Importations :

from Joueur import *
from Main import *
from Pioche import *
from CDB import *
from Carte import *
from Reserve import *
from Royaume import *
from Cimetiere import *
from random import *
from xdg.Mime import MagicDB

##### Fonction Programme Principal :

# getJoueurCourant : -> Joueur
# description : retourne le joueur qui joue, la fonction change la variable joueurcourant
# postcondition : il n'y a que deux sorties possibles, soit joueur1, soit joueur2 et getJoueurCourant() != getJoueurAdverse
def getJoueurCourant():
    return joueurCourant

def getNomJoueurCourant():
    if joueurCourant == joueur1:
        return "joueur 1"
    else:
        return "joueur 2"

# getJoueurAdverse : -> Joueur
# description : retourne le joueur adverse, la fonction chnage la variable joueuradverse
# postcondition : il n'y a que deux sorties possibles, soit joueur1, soit joueur2 et getJoueurCourant() != getJoueurAdverse
def getJoueurAdverse():
    return joueurAdverse

# changeJoueurCourant :
# description : change le joueur courant en joueur adverse et inversement, change les variables joueurcourant et joueuradverse,
def changeJoueurCourant():
    global joueurCourant, joueurAdverse
    joueurCourant, joueurAdverse = joueurAdverse, joueurCourant
    print("Le joueur courant est {}".format(getNomJoueurCourant()))


# deployer : Joueur x Carte x int x CDB -> Partie
# description : deploye une carte sur le champ de bataille
# postcondition : - si la position est déjà occupée et que la carte provient de la main, la fonction renvoye l’ancienne carte à la réserve
#                 - 1 <= position <= 6
#                 - avance la carte au front si deployer à l'arriere et que le front est vide
def deployer(joueur, carte, position, cdb):
    if ((joueur == joueur1) and (position <= 6) and (position >= 1)) or (
            (joueur == joueur2) and (position <= 12) and (position >= 7)):  # Si les cases du cdb correspondent au donné

        zoneCarte = Carte.getZoneCarte(carte)
        
        if (CDB.estOccupee(cdb, str(position))):  # Si il y a une carte à la position voulue
            ancienne = CDB.getCarteCDB(cdb, position)  # On récupère le carte présente à la position
            reserve = Joueur.getReserve(joueur)  # On récupère la réserve du joueur
            Reserve.ajouterReserve(reserve, ancienne)  # On ajoute l'ancienne carte à la réserve du joueur

        if (position == 4) or (position == 5) or (position == 6) or (position == 10) or (position == 11) or (
            position == 12):  # Si la position est à l'arrière
            front = position - 3  # Position correspondant à l'avant

            if (CDB.estOccupee(cdb, front)):  # Si la position devant est occupée
                cdb.ajouterCDB(carte,position)  # Ajout de la carte à la position donnée sur le champ de bataille

            else:  # Si la position devant est vide
                cdb.ajouterCDB(carte,str(front)) # Ajout de la carte à la position sur le front

        else:
            cdb.ajouterCDB(carte,position)  # Ajout de la carte à la position donnée sur le champ de bataille

        if (zoneCarte == "reserve"):
            Reserve.supprimerReserve(Joueur.getReserve(joueur),carte)
        #else:
            #Main.supprimerMain(Joueur.getMain(joueur),carte)
    else:
        return 0


# mourir : Joueur x Carte x CDB
# description : envoye une carte detruite du champ de bataille au cimetiere, la fonction peut vérifier que les PDV de la carte sont négatifs ou nuls, sinon renvoit un message d'erreur
def mourir(joueur, carte, cdb):
    i = 1  # Compteur
    trouve = False
    while (i < 13 and trouve == False):  # Tant qu'on est pas à la fin du Champ de bataille et que la carte n'a pas été supprimée
        c = CDB.getCarteCDB(cdb, i)  # On récupère la carte à une position

        if (c != ""):
            if (Carte.getPDV(c) < 0) and (c == carte):  # Si les points de vie de la carte sur cette position sont négatifs, et que c'est la carte donnée en paramètres
                CDB.supprimerCDB(cdb, carte, i)  # On supprime la carte du champ de bataille
                cimetiere = Joueur.getCimetiere(joueur)  # On récupère le cimetière du joueur
                Cimetiere.ajouterCimetiere(cimetiere, carte)  # On ajoute la carte au cimetière
                trouve = True
        i = i + 1  # Incrémentation du compteur


# capturer : CDB x Joueur x Carte
# description : envoye la carte du joueur adverse du champ de bataille au royaume du joueur courant
def capturer(cdb, joueur, carte):
    i = 1  # Compteur
    trouve = False
    while (i < 13 and trouve == False):  # Tant qu'on est pas à la fin du Champ de bataille et que la carte n'a pas été supprimée
        c = CDB.getCarteCDB(cdb, i)  # On récupère la carte à une position

        if (c != ""):
            if (Carte.getPDV(c) == 0) and (c == carte):  # Si les points de vie de la carte sur cette position sont nuls, et que c'est la carte donnée en paramètres
                CDB.supprimerCDB(cdb, carte, i)  # On supprime la carte du champ de bataille
                royaume = Joueur.getRoyaume(joueur)  # On récupère le royaume du joueur
                Royaume.ajouterRoyaume(royaume, carte)  # On ajoute la carte au royaume
                trouve = True
        i = i + 1  # Incrémentation du compteur


# redressement : Joueur x CDB
# description : place toute les unites du joueur sur le champ de bataille en position defensive et rétabli leurs points de vies max et leur état normal
def reinitilisation(joueur, cdb):
    if joueur == joueur1:
        for i in range(1, 7):
            if CDB.estOccupee(cdb, i):
                newc = Carte()
                c = CDB.getCarteCDB(cdb, i)
                if c == "roi":
                    newc.creerRoi1()
                    CDB.ajouterCDB(cdb, newc, i)

                elif c == "soldat":
                    newc.creerSoldat()
                    CDB.ajouterCDB(cdb, newc, i)

                elif c == "archer":
                    newc.creerArcher()
                    CDB.ajouterCDB(cdb, newc, i)

                elif c == "garde":
                    newc.creerGarde()
                    CDB.ajouterCDB(cdb, newc, i)
    else:
        for i in range(7, 12):
            if CDB.estOccupee(cdb, i):
                c = CDB.getCarteCDB(cdb, i)
                newc = Carte();
                if c == "roi":
                    newc.creerRoi1()
                    CDB.ajouterCDB(cdb, newc, i)

                elif c == "soldat":
                    newc.creerSoldat()
                    CDB.ajouterCDB(cdb, newc, i)

                elif c == "archer":
                    newc.creerArcher()
                    CDB.ajouterCDB(cdb, newc, i)

                elif c == "garde":
                    newc .creerGarde()
                    CDB.ajouterCDB(cdb, newc, i)

    return cdb


# CDBIsEmpty : Joueur x CDB -> boolean
# description : renvoie vrai si le joueur se retrouve sans armée sur le champ de bataille. Faux sinon
def CDBIsEmpty(joueur, cdb):
    res = True
    if joueur == joueur1:
        for i in range(1, 7):
            if CDB.estOccupee(cdb, i):
                res = False
    else:
        for i in range(7, 12):
            if CDB.estOccupee(cdb, i):
                res = False
    return res


# getAttaquants : Joueur x CDB -> List[Carte]
# description : renvoye la liste des cartes du joueur qui sont sur le champ de bataille
def getAttaquants(joueur, cdb):
    lstCarte = []
    lstPos = []
    if joueur == joueur1:
        for i in range(1, 7):
            if CDB.estOccupee(cdb, i):
                lstCarte.append(CDB.getCarteCDB(cdb, i))
                lstPos.append(i)
    else:
        for i in range(7, 12):
            if CDB.estOccupee(cdb, i):
                lstCarte.append(CDB.getCarteCDB(cdb, i))
                lstPos.append(i)
    return lstCarte,lstPos


# executions : joueur x joueur -> bool
# description : renvoye vrai si au moins un des rois a été capturé ou tué, sinon faux
def executions(joueur1, joueur2):
    cimetiere1 = Joueur.getCimetiere(joueur1)
    cimetiere2 = Joueur.getCimetiere(joueur2)
    for carte in cimetiere1.cimetiere: #Parcours des cartes du cimetière du joueur 1
        if Carte.getTypeCarte(carte) == "roi": #Retourne Vrai si une des cartes est un roi
            return True
    for carte in cimetiere2.cimetiere: #Parcours des cartes du cimetière du joueur 2
        if Carte.getTypeCarte(carte) == "roi": #Retourne Vrai si une des cartes est un roi
            return True
    return False


# getCarteAttaquable : Joueur x CDB x carte -> List[]
# description : renvoie la liste des cartes ennemies pouvant etre attaquées par le joueur
def getCarteAttaquable(joueur, cdb, carte, position):  # un entier qui représente la position de la carte sur le cdb

    # on calcule la porte pour le roi
    res = []
    if joueur == joueur1:
        if (Carte.getTypeCarte(carte) == "roi"):
            # la fonction en dessous calcule en fonction de la position du roi les emplacements qu'il peut atteindre
            if (position == 2):
                if CDB.estOccupee(cdb, position + 6 - 1):
                    res.append(CDB.getCarteCDB(cdb, (position - 1 + 6)))
                if CDB.estOccupee(cdb, position + 6):
                    res.append(CDB.getCarteCDB(cdb, (position + 6)))
                if CDB.estOccupee(cdb, position + 6 + 1):
                    res.append(CDB.getCarteCDB(cdb, (position + 6 + 1)))
                if CDB.estOccupee(cdb, position + 6 + 3):
                    res.append(CDB.getCarteCDB(cdb, (position + 6 + 3)))

            elif (position == 1):
                if CDB.estOccupee(cdb, position + 6):
                    res.append(CDB.getCarteCDB(cdb, (position + 6)))
                if CDB.estOccupee(cdb, position + 6 + 1):
                    res.append(CDB.getCarteCDB(cdb, (position + 6 + 1)))
                if CDB.estOccupee(cdb, position + 6 + 2):
                    res.append(CDB.getCarteCDB(cdb, (position + 6 + 2)))
                if CDB.estOccupee(cdb, position + 6 + 3):
                    res.append(CDB.getCarteCDB(cdb, (position + 6 + 3)))

            elif (position == 3):
                if CDB.estOccupee(cdb, position + 6 - 1):
                    res.append(CDB.getCarteCDB(cdb, (position - 1 + 6)))
                if CDB.estOccupee(cdb, position + 6):
                    res.append(CDB.getCarteCDB(cdb, (position + 6)))
                if CDB.estOccupee(cdb, position + 6 - 2):
                    res.append(CDB.getCarteCDB(cdb, (position - 2 + 6)))
                if CDB.estOccupee(cdb, position + 6 + 3):
                    res.append(CDB.getCarteCDB(cdb, (position + 3 + 6)))
            else:
                if CDB.estOccupee(cdb, position + 3):
                    res.append(CDB.getCarteCDB(cdb, (position + 3)))
        # on calcule les cartes a portée des gardes et des soldats
        elif (Carte.getTypeCarte(carte) == "soldat") or (Carte.getTypeCarte(carte) == "garde"):
            if position in (1, 2, 3):
                if CDB.estOccupee(cdb, position + 6):
                    res.append(CDB.getCarteCDB(cdb, (position + 6)))
        # on calcule les cartes a portée des arches, pour cela on fait tous les cas possibles
        else:
            if position == 1:
                if CDB.estOccupee(cdb, 11):
                    res.append(CDB.getCarteCDB(cdb, 11))
                if CDB.estOccupee(cdb, 9):
                    res.append(CDB.getCarteCDB(cdb, 9))

            elif position == 2:
                if CDB.estOccupee(cdb, 10):
                    res.append(CDB.getCarteCDB(cdb, 10))
                if CDB.estOccupee(CBD, 12):
                    res.append(CDB.getCarteCDB(cdb, 12))

            elif position == 3:
                if CDB.estOccupee(cdb, 7):
                    res.append(CDB.getCarteCDB(cdb, 7))
                if CDB.estOccupee(cdb, 11):
                    res.append(CDB.getCarteCDB(cdb, 11))

            elif position == 4 or position == 6:
                if CDB.estOccupee(cdb, 8):
                    res.append(CDB.getCarteCDB(cdb, 11))

            else:
                if CDB.estOccupee(cdb, 7):
                    res.append(CDB.getCarteCDB(cdb, 7))
                if CDB.estOccupee(cdb, 9):
                    res.append(CDB.getCarteCDB(cdb, 9))
    else:
        if (Carte.getTypeCarte(carte) == "roi"):
            # la fonction en dessous calcule en fonction de la position du roi les emplacements qu'il peut atteindre
            if (position == 8):
                if CDB.estOccupee(cdb, position - 6 - 1):
                    res.append(CDB.getCarteCDB(cdb, (position - 1 - 6)))
                if CDB.estOccupee(cdb, position - 6):
                    res.append(CDB.getCarteCDB(cdb, (position - 6)))
                if CDB.estOccupee(cdb, position - 6 + 1):
                    res.append(CDB.getCarteCDB(cdb, (position + 1 - 6)))

            elif (position == 7):
                if CDB.estOccupee(cdb, position - 6):
                    res.append(CDB.getCarteCDB(cdb, (position - 6)))
                if CDB.estOccupee(cdb, position - 6 + 1):
                    res.append(CDB.getCarteCDB(cdb, (position + 1 - 6)))
                if CDB.estOccupee(cdb, position - 6 + 2):
                    res.append(CDB.getCarteCDB(cdb, (position + 2 - 6)))

            elif (position == 9):
                if CDB.estOccupee(cdb, position - 6 - 1):
                    res.append(CDB.getCarteCDB(cdb, (position - 1 - 6)))
                if CDB.estOccupee(cdb, position - 6):
                    res.append(CDB.getCarteCDB(cdb, (position - 6)))
                if CDB.estOccupee(cdb, position - 6 - 2):
                    res.append(CDB.getCarteCDB(cdb, (position - 2 - 6)))


                    # on calcule les cartes a porte des gardes et des soldats
        elif (Carte.getTypeCarte(carte) == "soldat") or (Carte.getTypeCarte(carte) == "garde"):
            if position in (7, 8, 9):
                if CDB.estOccupee(cdb, position - 6):
                    res.append(CDB.getCarteCDB(cdb, (position - 6)))

        # on calcule les cartes a porte des arches, pour cela on fait tous les cas possibles
        else:
            if position == 9:
                if CDB.estOccupee(cdb, 5):
                    res.append(CDB.getCarteCDB(cdb, 5))
                if CDB.estOccupee(cdb, 1):
                    res.append(CDB.getCarteCDB(cdb, 1))

            elif position == 8:
                if CDB.estOccupee(cdb, 6):
                    res.append(CDB.getCarteCDB(cdb, 6))
                if CDB.estOccupee(CBD, 4):
                    res.append(CDB.getCarteCDB(cdb, 4))

            elif position == 7:
                if CDB.estOccupee(cdb, 5):
                    res.append(CDB.getCarteCDB(cdb, 5))
                if CDB.estOccupee(cdb, 3):
                    res.append(CDB.getCarteCDB(cdb, 3))

            elif position == 12 or position == 10:
                if CDB.estOccupee(cdb, 2):
                    res.append(CDB.getCarteCDB(cdb, 2))

            else:
                if CDB.estOccupee(cdb, 3):
                    res.append(CDB.getCarteCDB(cdb, 3))
                elif CDB.estOccupee(cdb, 1):
                    res.append(CDB.getCarteCDB(cdb, 1))

    return res


# listToString : List[Carte] -> Text
# description : renvoie le type de chaque carte de la liste en paramètre en sous forme de texte
#               exemple : "soldat, soldat, archer, archer"
def listToString(liste):
    res = ""
    for i in range(0, len(liste)):
        carte = liste[i]
        res = res + getTypeCarte(carte)

    return res


# Avancer : joueur x cdb -> cdb
# description : avance toutes les cartes  du joueur sur le champ de bataille se trouvant à l'arrière et que le front devant eux est vide.
def Avancer(joueur, cdb):
    return 0
    
    
#### Programme Principal :

# Realise par:
# - ARNAUD Paul
# - RANARIMAHEFA Mitantsoa Michel

# Création des joueurs
print('Création des joueurs')

joueur1 = Joueur()
joueur1.creerJoueur()
joueur2 = Joueur()
joueur2.creerJoueur()

joueurCourant =joueur1
joueurAdverse = joueur2

# Création du champ de bataille
print('Création du champ de bataille')

cdb = CDB()
cdb.creerCDB()

#### Mise en place :

# On pioche 4 cartes
print('Mise en place')

pioche1 = Pioche()
pioche1.creerPioche()
Joueur.setPioche(joueur1,pioche1)

pioche2 = Pioche()
pioche2.creerPioche()
Joueur.setPioche(joueur2,pioche2)

for i in range(4):
    carte = Carte()
    carte = Pioche.getFirstPioche(pioche1)
    joueur1.getMain().ajouterMain(carte)

    carte = Pioche.getFirstPioche(pioche2)
    joueur2.getMain().ajouterMain(carte)
    #carte = Pioche.getFirstPioche(pioche2)
    #Main.ajouterMain(Joueur.getMain(joueur2), carte)

# On demobilise une unité au hasard
# On recupere la liste des cartes dans la main et on en prend une au hasard avec la fonction random

hasard = randint(0, 3)
liste = Main.getElementsMain(Joueur.getMain(joueur1))
Joueur.demobiliser(joueur1,liste[hasard])

hasard = randint(0, 3)
liste = Main.getElementsMain(Joueur.getMain(joueur2))
Joueur.demobiliser(joueur2,liste[hasard])

# On cree et insère ensuite les rois dans la main pour eviter de le demobiliser
# le joueur 1 obtient le roi de type 1 et le jouieur 2 obtient le roi de type 2

roi1 = Carte()
roi1.creerRoi1()
roi2 = Carte()
roi2.creerRoi2()

Main.ajouterMain(Joueur.getMain(joueur1),roi1)
Main.ajouterMain(Joueur.getMain(joueur2),roi2)

# On affiche la main du joueur, puis on lui demande de choisir une des cartes qu'il possède dans sa main, on lui demande aussi une position. Finalement on deploie cette carte sur la position. Attention !!! la position doit être une position du front.

print('Joueur 1 quelle carte voulez-vous placer sur le champ de bataille ? et où voulez-vous la placer ?')
print(Main.mainToString(Joueur.getMain(joueur1)))
carte1 = input('Carte = ')
position1 = int(input('Position = '))
carteObj1 = Main.getCarteMain(Joueur.getMain(joueur1), carte1)
deployer(joueur1,carteObj1,position1,cdb)

print('Joueur 2 quelle carte voulez-vous placer sur le champ de bataille ? et où voulez-vous la placer ?')
print(Main.mainToString(Joueur.getMain(joueur2)))
carte2 = input('Carte = ')
position2 = int(input('Position = '))
carteObj2 = Main.getCarteMain(Joueur.getMain(joueur2), carte2)
deployer(joueur2,carteObj2,position2,cdb)

# On affiche la main du joueur, puis on lui demande de choisir une des cartes qu'il possède dans sa main. On met ensuite cette carte dans sa reserve

print('Joueur 1 quelle carte voulez vous mettre en réserve?')
print(Main.mainToString(Joueur.getMain(joueur1)))
carte11 = input('Carte =')
Joueur.mettreEnReserve(joueur1,Main.getCarteMain(Joueur.getMain(joueur1),carte11))

print('Joueur 2 quelle carte voulez vous mettre en réserve?')
print(Main.mainToString(Joueur.getMain(joueur2)))
carte22 = input('Carte =')
Joueur.mettreEnReserve(joueur2,Main.getCarteMain(Joueur.getMain(joueur2),carte22))

#### Debut du jeu :

print('Debut du jeu')

# conscription fait référence au fait que le joueur peut, au cas où il n'a plus d'unités sur le champ de bataille, prendre dans sa réserve ou son royaume. Dans le cas où c'est possible de le faire conscritpion est égal à "possible", "impossible" sinon.
conscription = "possible"

# finguerre fait référence au fait que le joueur ne peut plus piocher, dans ce cas là la partie est terminée.
finguerre = False

while not(executions(joueur1,joueur2)) and conscription == "possible" and not(finguerre) :
    # les condtions d'arrêts sont :
    # _ Si un des joueurs tue ou capture le roi adverse (execution)
    # _ Si la conscription n'est pas possible pour un des joueurs (conscription)
    # _ Si les joueurs ne peuvent plus piocher (finguerre)

    print('C est au ',getNomJoueurCourant(),'de jouer')
    
    print('Initialisation phase 1:')
    # on réinitialise les points de vie des unités sur le champ de bataille, et on remet les cartes en position défensive (seulement pour le joueur courant)
    reinitilisation(getJoueurCourant(),cdb)

    if  not Pioche.piocheIsEmpty(Joueur.getPioche(getJoueurCourant())):
        # si le joueur peut piocher
        Joueur.piocher(getJoueurCourant())

        print('Initialisation phase 2')

        print('Que voulez-vous faire ? \n Pour ne rien faire taper 1, \n pour mettre en réserve taper 2, \n pour déployer une unité taper 3, \n pour attaquer taper 4')
        ordre = int(input('Réponse ='))

        if ordre == 1:
            # le joueur ne veut rien faire
            print('ok')

        elif ordre == 2:
            # le joueur veut mettre une carte en réserve
            print('Choississez une carte de votre main que vous voulez mettre en réserve')
            # on affiche la main du joueur pour qu'il puisse choisir
            print(Main.mainToString(Joueur.getMain(getJoueurCourant())))
            entree = input('Carte =')
            carte = Main.getCarteMain(Joueur.getMain(getJoueurCourant()),entree)
            Joueur.mettreEnReserve(getJoueurCourant(),carte)

        elif ordre == 3:
            # le joueur veut déployer une unité
            if not(Reserve.ReserveIsEmpty(Joueur.getReserve(getJoueurCourant()))) :
                # si la réserve n'est pas vide alors on déploie la première unité de la réserve
                carte = Reserve.getFirstReserve(Joueur.getReserve(getJoueurCourant()))
                print('Ou voulez-vous mettre ',Carte.carteToString(carte),'?')
                position = int(input('Position ='))
                deployer(getJoueurCourant(),carte,position,cdb)

            else :
                # sinon on lui demande de choisir une des cartes de sa main
                print('Choisissez une carte de votre main que vous voulez déployer')
                # on affiche la main du joueur pour qu'il puisse choisir
                print(Main.mainToString(Joueur.getMain(getJoueurCourant())))
                entree = input('Carte =')
                carte = Main.getCarteMain(Joueur.getMain(getJoueurCourant()),entree)
                position = int(input('Position ='))
                deployer(getJoueurCourant(),carte,position,cdb)

        elif ordre == 4:
            # le joueur veut attaquer
            print('Mode combat activé')
            # on récupère la liste des unités que possède le joueur sur le champ de bataille
            listeCarte,listePos = getAttaquants(getJoueurCourant(),cdb)
            pos = 0

            for i in listeCarte:
                if not(executions(joueur1,joueur2)):
                    # si aucun roi n'est mort
                
                    # pour toutes les cartes dans la liste des attaquants, on demande au joueur s'il veut attaquer avec
                    print('Voici les unités que peut atteindre votre unité')
                    for carteList in getCarteAttaquable(getJoueurCourant(),cdb,i, listePos[pos]):
                        print(Carte.carteToString(carteList))
                    attaquable = getCarteAttaquable(getJoueurCourant(),cdb,i, listePos[pos])
                    print("Voulez vous attaquer avec ",Carte.carteToString(i),"? pour oui taper 1 pour non taper 0")
                    pos = pos + 1

                    reponse = int(input('Réponse ='))
                    carteactif = None;
                    if reponse == 1:
                    # lorsque le joueur veut attaquer avec la carte i
                        for j in attaquable:
                            # on va lui demander pour chaque carte qu'il peut attaquer avec l'unité choisie s'il veut attaquer
                            attaqueDone = False
                            
                            if attaqueDone == False:
                                
                                print("Voulez vous attaquer ",Carte.carteToString(j)," avec ",Carte.carteToString(i)," ? pour oui taper 1 pour non taper 0")
                                
                                reponse2 = int(input('Réponse ='))

                                # on change le boolean pour dire qu'on attaquer
                                if reponse2 == 1:
                                    
                                    carteactif= i
                                    cartepassif = j
                                    attaqueDone = True

                                    # si la carte est un soldat son attaque est egale au nombre de carte dans la main du joueur
                                    if Carte.getTypeCarte(carteactif) == "soldat":
                                        
                                        Carte.setForceAttaque(carteactif,Main.getTailleMain(Joueur.getMain(getJoueurCourant())))
                                    # si la valeur de l'attaque est égale à la valeur de la défense et que la carte attaquée n'a pas déjà subi de dégats, alors le joueur capture la carte.
                                    if Carte.getForceAttaque(carteactif) == Carte.getForceDefense(cartepassif) and Carte.getEtatCarte(cartepassif) != "affaiblie" :
                                        
                                        capturer(cdb,getJoueurCourant(),cartepassif)
                                        
                                    else :
                                        # sinon on retire les dégats des points de vie de la carte attaquée
                                        Carte.setPDV(cartepassif,Carte.getPDV(cartepassif) - Carte.getForceAttaque(carteactif))
                                        # si les points de vie de la carte attaquée sont à 0 ou moins, la carte meurt(déplacement vers le cimetière)
                                        if Carte.getPDV(cartepassif) <= 0 :
                                            
                                            mourir(getJoueurAdverse(),cartepassif,cdb)
                                else:
                                    print("ERREUR car pas d'autres cartes a attaquer")
                                    
                if (carteactif is not None):
                    # on modifie l'état de la carte qui vient d'attaquer, qui passe de l'état défensif à l'état offensif
                    Carte.setPosCarte(carteactif,"offensive")
                        
                    #au cas où une unité vient d'être tuée, on avance les cartes du joueur adverse
                    Avancer(getJoueurAdverse(),cdb)
                        
                    if CDBIsEmpty(getJoueurAdverse(),cdb) and not(executions(joueur1,joueur2)) :
                        # si le champ de bataille est vide alors il doit conscrire , pour cela on change de joueur courant juste pour que le joueur qui n'a plus d'unité sur son champ de bataille puisse déployer
                        print("on change de joueur")
                        changeJoueurCourant()
                        # on regarde si le champ de bataille du joueur courant est vide pour savoir s'il doit recruter ou non des unités
                        if Reserve.getTailleReserve(Joueur.getReserve(getJoueurCourant())) >= 2:
                        # on regarde si le joueur possède plus de deux cartes dans sa réserve, si oui, les deux cartes de la conscription proviennent de sa réserve
                            eltreserve = Reserve.getFirstReserve(getReserve(Joueur.getJoueurCourant()))
    
                            print('Ou voulez-vous mettre ',Carte.carteToString(eltreserve),'?')
                            position1 = int(input('Position ='))
                            deployer(getJoueurCourant(),eltreserve,position1,cdb)
    
                            eltreserve = Reserve.getFirstReserve(Joueur.getReserve(getJoueurCourant()))
    
                            print('Ou voulez-vous mettre ',Carte.carteToString(eltreserve),'?')
                            position2 = int(input('Position ='))
    
                            while position2 == position1 :
                            # le joueur ne doit pas mettre 2 fois la même position sinon il n'y aura qu'une seule carte sur le champ de bataille
                                print('Une carte est déjà présente sur cette position veuillez choisir une nouvelle position !')
    
                                print('Ou voulez-vous mettre ',Carte.carteToString(eltreserve),'?')
                                position2 = int(input('Position ='))
    
                                deployer(getJoueurCourant(),eltreserve,position2,cdb)
    
                        elif Reserve.getTailleReserve(Joueur.getReserve(getJoueurCourant())) == 1 and not Royaume.RoyaumeIsEmpty(Joueur.getRoyaume(getJoueurCourant())):
                        # si le joueur ne possède plus qu'une seule carte dans sa réserve et que son royaume contient au moins 1 carte
                            eltreserve = Reserve.getFirstReserve(Joueur.getReserve(getJoueurCourant()))
    
                            print('Ou voulez-vous mettre ',Carte.carteToString(eltreserve),'?')
                            position1 = int(input('Position ='))
    
                            deployer(getJoueurCourant(),eltreserve,position1,cdb)
    
    
                            print('Quelle carte voulez-vous mettre sur le champ de bataille et où ?')
                            print(Royaume.royaumeToString(Joueur.getRoyaume(getJoueurCourant())))
                            entree = input('Carte =')
                            carte = Royaume.getCarteRoyaume(Joueur.getRoyaume(getJoueurCourant()),entree)
                            position2 = int(input('Position ='))
    
                            while position2 == position1:
                            # le joueur ne doit pas mettre 2 fois la même position sinon il n'y aura qu'une seule carte sur le champ de bataille
                                print('Une carte est déjà présente sur cette position veuillez choisir une nouvelle position !')
    
                                print('Ou voulez-vous mettre ',Carte.carteToString(carte),'?')
                                position2 = int(input('Position ='))
    
                            deployer(getJoueurCourant(),carte,position2,cdb)
    
    
                        elif Royaume.getTailleRoyaume(Joueur.getRoyaume(getJoueurCourant())) >= 2:
                        # si le joueur ne possède plus de carte dans sa réserve et que son royaume possède au moins 2 cartes
                            print('Quelle carte voulez-vous mettre sur le champ de bataille et où ?')
                            print(Royaume.royaumeToString(Joueur.getRoyaume(getJoueurCourant())))
                            entree = input('Carte =')
                            #TODO la carte n'est pas un obket carte !!!!! donc deployer KO
                            carte = Royaume.getCarteRoyaume(Joueur.getRoyaume(getJoueurCourant()),entree)
                            position1 = int(input('Position ='))
                            deployer(getJoueurCourant(),carte,position1,cdb)
                            print('Quelle carte voulez-vous mettre sur le champ de bataille et où ?')
                            print(Royaume.royaumeToString(Joueur.getRoyaume(getJoueurCourant())))
                            entree = input('Carte =')
                            carte = Royaume.getCarteRoyaume(Joueur.getRoyaume(getJoueurCourant()),entree)
                            position2 = int(input('Position ='))
    
                            while position2 == position1:
                            # le joueur ne doit pas mettre 2 fois la même position sinon il n'y aura qu'une seule carte sur le champ de bataille
                                print('Ou voulez-vous mettre ',Carte.carteToString(carte),'?')
                                position2 = int(input('Position ='))
    
                            deployer(getJoueurCourant(),carte,position2,cdb)
    
                        else :
                            # le joueur n'a plus assez de cartes pour en mettre 2 sur le champ de bataille
                            print("Conscription impossible")
                            conscription = 'impossible'
                        
                        # on rechange de joueur pour que le joueur qui jouait initialement finisse son tour
                        print("on change de joueur")
                        changeJoueurCourant()
        else:
            # si le joueur n'a pas mis 1,2,3 ou 4, il passe son tour ( il n'écoute pas c'est de sa faute)
            print('erreur, vous n avez pas suivi les consignes, vous passez votre tour')

        print('Initialisation phase 3')
        
        if conscription == 'possible' and not(executions(joueur1,joueur2)): 
                if Main.getTailleMain(Joueur.getMain(getJoueurCourant())) >= 6 :
                    # si le joueur au moins 6 cartes dans sa main, il est obligé de démobiliser.
                    print('Quelle carte voulez-vous démobiliser ?')
                    # on lui affiche les cartes qu'il possède dans sa main
                    print(Main.mainToString(Joueur.getMain(getJoueurCourant())))
                    carte = input('Carte =')
                    # TODO ??? Retrouver l'objet carte ???
                    Joueur.demobiliser(getJoueurCourant(), Main.getCarteMain(Joueur.getMain(getJoueurCourant()),carte))

                print('Voulez-vous démobilisez ? 1 pour oui, 0 pour non')
                reponse = int(input('Réponse ='))
                
                if reponse == 0:
                    print('ok')

                elif reponse == 1:
                # si le joueur veut démobiliser
                    print('Quelle carte voulez-vous démobiliser ?')
                    # on lui affiche les cartes qu'il possède dans sa main
                    print(Main.mainToString(Joueur.getMain(getJoueurCourant())))
                    carte = input('Carte =')
                    # TODO ??? Retrouver l'objet carte ???
                    #Joueur.demobiliser(joueur1,carte)
                    Joueur.demobiliser(getJoueurCourant(), Main.getCarteMain(Joueur.getMain(getJoueurCourant()),carte))
                    
                else :
                    print('erreur, c est dommage !')

    else :
        # si le joueur ne peut plus piocher
        finguerre = True

    print('Fin du tour du ',getNomJoueurCourant())
    # on change de joueur
    changeJoueurCourant()

#Détermination du gagnant:
print('Détermination du gagnant')

if executions(joueur1,joueur2) :
    # si l'un des rois a été tué ou capturé
    if getZoneCarte(roi1) == cimetiere or getZoneCarte(roi1) == royaume :
        # on regarde si il est dans le cimetière ou dans le royaume, dans ce cas là le joueur 2 gagné
        print('Le joueur 2 a gagné')
    else :
        # sinon c'est le joueur 1 qui a gagné
        print('Le joueur 1 a gagné')

if conscription == "impossible" :
    # si la conscription n'est plus possible cela veut dire que le joueur qui a joué avant n'a pas pu conscrire donc il a perdu
    print(getJoueurAdverse(),'a gagné car le ',getJoueurCourant(),' ne peut plus conscrire')

if finguerre :
    # dans le cas de la fin de la guerre, les deux joueurs ne peuvent plus piocher, celui qui a un plus grand royaume a gagné
    if getTailleRoyaume(getRoyaume(getJoueurCourant())) > getTailleRoyaume(getRoyaume(getJoueurAdverse())) :
        print(getJoueurCourant(),'a gagné car il a un plus grand royaume')

    elif getTailleRoyaume(getRoyaume(getJoueurCourant())) < getTailleRoyaume(getRoyaume(getJoueurAdverse())) :
        print(getJoueurAdverse(),'a gagné car il a un plus grand royaume')

    else :
        print('Egalité')