 
"""
Module composé d'une classe  :
    Classe Chiffrer_Dechiffrer :
        Effectue les différentes étapes de chiffrage / déchiffrage d'un texte ou d'un fichier.      
    
    Les classes, fonctions et modules extérieurs utilisées :
    int, str, bytes; ord, chr.
"""


# Classe principale :

class Chiffrer_Dechiffrer(object):
    """
    Classe Qui permet de chiffrer / déchiffrer des paramètres :

    Méthode Chiffrer : Renvoie une chaine chiffrée à partir de l'attribut chaine_Chiffrer
    Méthode Dechiffrer : Renvoie une chaine déchiffrée à partir de l'attribut chaine_Dechiffrer

    Les valeurs des attributs donnés en argument sont modifiés via les méthodes mutateurs  (set)
    Leur valeur est obtenue via les méthodes accesseurs  (get)
    """

    def __init__(self, chaine_Chiffrer=str(), chaine_Dechiffrer=str()):
        """
        Paramètre chaine_Chiffrer : Attribut _chaine_C, chaine de caractère à chiffrer
        Paramètre chaine_Dechiffrer : Attribut _chaine_D, chaine de caractère à déchiffrer
        Paramètre _chaine_C : Chaine de caractères à chiffrer
        Paramètre _chaine_D : Chaine de caractères à déchiffrer
        """

        self._chaine_C = chaine_Chiffrer
        self._chaine_D = chaine_Dechiffrer


    #  Définition des accesseurs et mutateurs :

    def set_Chaine_A_Chiffrer(self, chaine):
        """Remplace la valeur de l'attribut _chaine_C par celle du paramètre chaine"""
        self._chaine_C = chaine

    def set_Chaine_A_Dechiffrer(self, chaine):
        """Remplace la valeur de l'attribut _chaine_D par celle du paramètre chaine"""
        self._chaine_D = chaine

    def get_Chaine_A_Chiffrer(self):
        """Renvoie la valeur de l'attribut _chaine_C"""
        return self._chaine_C

    def get_Chaine_A_Dechiffrer(self):
        """Renvoie la valeur de l'attribut _chaine_D"""
        return self._chaine_D


    # Méthodes d'accession au contenu du fichier texte :

    @staticmethod
    def _get_Contenu_Fichier(path):
        """
        Fonction qui permet de récupérer le contenu d'un fichier.
        Renvoie : contenu, une chaine de caractères.
        """

        with open(path, 'rb') as f:  # Le fichier est ouvert en mode lecture bytes
            contenu = f.read()  # contenu est un objet de type bytes

        return contenu.decode(encoding="charmap")  # On renvoie le contenu sous forme de chaine de caractères


    @staticmethod
    def _set_Contenu_Fichier(path, contenu):
        """
        Fonction qui permet de remplacer le contenu d'un fichier, et de le créer s'il n'existe pas.
        Paramètre : contenu, une chaine de caractères, remplace le contenu actuel du fichier.
        """

        with open(path, 'wb') as f:  # Le fichier est ouvert en mode écriture bytes
            f.write(contenu.encode(encoding="charmap"))  # contenu est traduit en bytes et écrit dans le fichier


    # Méthodes principales de chiffrage / déchiffrage :

    def Chiffrer(self):
        """
        Méthode qui va, étape par étape, chiffrer l'attribut _chaine_C, une chaine de caractères
        Renvoie : chaine_Chiffree, la chaine de caractères chiffrée
        """

        chaine = self.get_Chaine_A_Chiffrer()

        chaine_Bin = self._etape1_Convertire_Chaine_En_Bin(chaine)
        liste_Bin = self._etape2_Diviser_En_Quartiles(chaine_Bin)
        liste_Bin = self._etape3_Ajouter_01_10(liste_Bin)
        liste_Bin = self._etape4_Inverser_Quartiles(liste_Bin)
        chaine_Chiffree = self._etape5_chiffrer_Bin_ASCII(liste_Bin)

        return chaine_Chiffree


    def Dechiffrer(self):
        """
        Méthode qui va, étape par étape, déchiffrer l'attribut _chaine_D, une chaine de caractères
        Renvoie : chaine_Dechiffree, la chaine de caractères déchiffrée
        """

        chaine_Chiffree = self.get_Chaine_A_Dechiffrer()

        liste_Bin = self._REVERSE_etape5_dechiffrer_ASCII_Bin(chaine_Chiffree)
        liste_Bin = self._etape4_Inverser_Quartiles(liste_Bin)
        liste_Bin = self._REVERSE_etape3_Enlever_01_10(liste_Bin)
        liste_Bin = self._REVERSE_etape2_Rejoindre_Les_Quartiles(liste_Bin)
        chaine_Dechiffree = self._REVERSE_etape1_Convertire_Bin_En_Chaine(liste_Bin)

        return chaine_Dechiffree


    # Méthodes auxillaires :

    @staticmethod
    def _convertire_Decimal_Bin(entier_Dec):
        """
        Cette fonction permet de convertire un entier décimal en entier binaire, en utilisant la division euclidienne par deux.
        on récupère successivement le reste de la division euclidienne de l'entier décimal par deux.
        Paramètre entier_Dec : Entier décimal
        Renvoie : chaine_Bin une chaine de caractères qui représente un entier binaire
        """

        nb = entier_Dec

        chaine_Bin = str()
        while nb >= 1:
            chaine_Bin = str(nb % 2) + chaine_Bin
            nb = nb//2

        return chaine_Bin


    # Opérations de chiffrage :

    @staticmethod
    def _etape1_Convertire_Chaine_En_Bin(chaine):
        """
        Etape 1 : La chaine de caractères initiale est convertie en chaine binaire, caractère par caractère.
        Paramètre : chaine, une chaine de caractère
        Renvoie : chaine_Bin, l'argument chaine traduit en binaire
        """

        chaine_Bin = str()

        for char in chaine:
            mot_Bin = str(Chiffrer_Dechiffrer._convertire_Decimal_Bin(ord(char)))  # La lettre est d'abord convertie en entier base 10 relatif à la table ASCII, puis en binaire.
            while len(mot_Bin) < 8:  # Chaque lettre codée en binaire doit faire la taille d'un octet, pour les étapes suivantes
                mot_Bin = '0' + mot_Bin  # On ajoute donc des '0' en bit de poids fort (à gauche), pour atteindre la taille d'un octet (8 bits)
            chaine_Bin += mot_Bin  # Le caractère traduit est ajouté à la nouvelle chaine de caractères

        return chaine_Bin


    @staticmethod
    def _etape2_Diviser_En_Quartiles(chaine_Bin):
        """
        Etape 2 : La chaine binaire est divisée en parties de 4, une liste des parties est renvoyée; si la dernière partie
        a une taille inférieure à 4, on augmente sa taille.
        Paramètre : chaine_Bin, une chaine de caractères en binaire.
        Renvoie : liste_Bin, la liste contenant chaine_Bin divisée en parties de 4 bits.
        """

        liste_Bin = list()

        while chaine_Bin != "":
            chaine, chaine_Bin = chaine_Bin[0:4], chaine_Bin[4:]  # chaine_Bin perds ses 4 premiers caractères à chaque tour, jusqu'a être vide.
            liste_Bin += [chaine]  # Ces caractères sont ajoutés à liste_Bin
        if not liste_Bin == []:  # On vérifie ensuite que, si la liste n'est pas vide (si chaine_Bin == ""), le dernier quartile a bien une taille de 4
            while len(liste_Bin[-1]) < 4:  # On ajoute des '0' à gauche du dernier quartile, jusqu'à ce que sa taille soit 4.
                liste_Bin[-1] = '0' + liste_Bin[-1]  # indice -1 : dernier élément

        return liste_Bin


    @staticmethod
    def _etape3_Ajouter_01_10(liste_Bin):
        """
        Etape 3 : On ajoute '01' et '10' au début et à la fin de chaque élément de liste_Bin.
        Paramètre : liste_Bin, une liste de chaines de caractères représentant 4 bits chacune.
        Renvoie : liste_Bin, dont chaque élément fait maintenant 1 octet.
        """

        for i in range(len(liste_Bin)):
            liste_Bin[i] = '01' + liste_Bin[i] + '10'  # On ajoute '01' et '10' au début et à la fin de chaque élément de liste_Bin

        return liste_Bin


    @staticmethod
    def _etape4_Inverser_Quartiles(liste_Bin):
        """
        Etape 4 : Chaque élément de liste_Bin étant un octet; on inverse les quatre premiers bits de chaque octet avec les
                    quatre derniers.
        Paramètre : liste_Bin, une liste de chaines de caractères représentant un octet chacune.
        Renvoie : liste_Bin, dont chaque octet a été inversé.
        """

        for i in range(len(liste_Bin)):
            Q1, Q2 = liste_Bin[i][:4], liste_Bin[i][4:]  # Q1 contient les 4 premiers bits de l'élément, Q2 les 4 derniers.
            liste_Bin[i] = Q2 + Q1  # les 4 bits sont inversés pour chaque élément de liste_Bin

        return liste_Bin


    @staticmethod
    def _etape5_chiffrer_Bin_ASCII(liste_Bin):
        """
        Etape 5 : Chaque octet de liste_Bin est traduit en caractère chiffré selon la table ASCII, puis concaténé à une chaine de caractères.
        Paramètre : liste_Bin, une liste de chaines de caractères d'octets binaires non chiffrés.
        Renvoie : chaine_Chiffree, une chaine de caractères chiffrés
        """

        chaine_Chiffree = str()

        for i in range(len(liste_Bin)):
            liste_Bin[i] = chr(int(liste_Bin[i], 2))  # L'octet chaine de caractère binaire est transformé en entier base 2, puis en caractère ASCII.
            chaine_Chiffree += liste_Bin[i]  # La lettre chiffrée est ajoutée à la chaine.

        return chaine_Chiffree


    # Opérations de déchiffrage :

    @staticmethod
    def _REVERSE_etape5_dechiffrer_ASCII_Bin(chaine_Chiffree):
        """
        Etape 1 du déchiffrage : Chaque caractère de chaine_Chiffree est ajouté à liste_Bin et traduit en octet binaire.
        Paramètre : chaine_Chiffree, une chaine de caractères chiffrés
        Renvoie : liste_Bin, une liste de chaines de caractères d'octets binaires chiffrés.
        """

        liste_Bin = list(chaine_Chiffree)  # crée une liste dont les éléments sont les caractères de chaine_Chiffree

        for char in range(len(liste_Bin)):  # Chaque élément (chaine de caractères) est traduite en binaire.
            liste_Bin[char] = Chiffrer_Dechiffrer._convertire_Decimal_Bin(ord(liste_Bin[char]))
        for i in range(len(liste_Bin)):  # Puis leur taille est vérifiée, afin que ce soit des octets.
            while len(liste_Bin[i]) < 8:
                liste_Bin[i] = '0' + liste_Bin[i]

        return liste_Bin


    # 2e étape du déchiffrage : étape 4 : On réalise ici la même opération que dans _etape4_Inverser_Quartiles(liste_Bin)
    # (pas de fonction inverse)


    @staticmethod
    def _REVERSE_etape3_Enlever_01_10(liste_Bin):
        """
        Etape 3 du déchiffrage : On enlève les deux premiers '01' et derniers '10' de chaque élément de liste_Bin.
        Paramètre : liste_Bin, une liste de chaines de caractères représentant 1 octet chacune.
        Renvoie : liste_Bin, dont chaque élément est maintenant une chaine binaire de 4 bits.
        """

        for i in range(len(liste_Bin)):
            liste_Bin[i] = liste_Bin[i][2:-2]  # Pour chaque élément, seul les caractères entre les '01' et les '10' sont conservés.

        return liste_Bin

    @staticmethod
    def _REVERSE_etape2_Rejoindre_Les_Quartiles(liste_Bin):
        """
        Etape 4 du déchiffrement : Les chaines de 4 bits (chaque élément de liste_Bin) sont rejointes pour former des octet.
        On renvoie la liste de chaines de caractères, composée maintenant d'octets.
        Paramètre : liste_Bin, une liste de chaines de caractères en binaire de 4 bits.
        Renvoie : liste_Bin, la liste contenant des chaines d'octets.
        """

        for i in range(int(len(liste_Bin) / 2)):  # Regrouper les élément divise la taille de la liste par deux
            liste_Bin[i] = liste_Bin[i] + liste_Bin[i + 1]  # L'élément présent devient la concaténation de lui-même et du suivant
            del liste_Bin[i + 1]  # Puis l'élément suivant est supprimé, réduisant la taille de la liste

        return liste_Bin


    @staticmethod
    def _REVERSE_etape1_Convertire_Bin_En_Chaine(liste_Bin):
        """
        Etape 5 du déchiffrement : La liste de chaines de caractères de 8 bits est convertie en chaine de caractères non binaires, caractère par caractère.
        Paramètre : liste_Bin, la liste contenant des chaines d'octets.
        Renvoie : chaine_Dechiffree, la chaine de caractères finale.
        """

        chaine_Dechiffree = str()

        for elt in liste_Bin:
            chaine_Dechiffree += chr(int(elt, 2))  # Pour chaque élément de la liste : on traduit la chaine de 8 bits en entier binaire; puis on récupère le caractère correspondant dans la table ASCII.

        return chaine_Dechiffree


    # Méthodes d'affichage :

    def __str__(self):
        """
        Méthode qui affiche, lorsque l'objet est passé en argument dans print(), les résultats du chiffrage et du déchiffrage
        des attributs de la classe.
        Renvoie : chaine, une chaine de caractère des résultats.
        """

        chaine_Non_Chiffree = self.get_Chaine_A_Chiffrer()  # L'attribut _chaine_C
        chaine_Non_Dechiffree = self.get_Chaine_A_Dechiffrer()  # L'attribut _chaine_D
        resultat_Chiffrage = self.Chiffrer()  # L'attribut _chaine_C chiffré
        resultat_Dechiffrage = self.Dechiffrer()  # L'attribut _chaine_D déchiffré

        chaine = '"' + chaine_Non_Chiffree + '"' + " Chiffrée donne : " + resultat_Chiffrage + '\n' + '"' + chaine_Non_Dechiffree + '"' + " Déchiffrée donne : " + resultat_Dechiffrage
        # Exemple de résultat :
        # "NSI" Chiffré donne : %§eä%f
        # "%§eä%f" Déchiffré donne : NSI

        return chaine
