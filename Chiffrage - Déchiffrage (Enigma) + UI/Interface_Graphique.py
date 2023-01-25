
"""
Module composé d'une classe :
    Classe Main :
        Défini l'état initial du programme grapique et le fait tourner.

    Un objet de la classe Main est créé au lancement du module.

    Les classe et modules extérieurs utilisées :
    Chiffrer_Dechiffrer; tkinter.
"""


# Imports

from tkinter import *
from tkinter import filedialog
import Chiffrage_Dechiffrage as CD


# Classe principale :

class Main(CD.Chiffrer_Dechiffrer):
    """
    Classe Qui permet d'initialiser, d'éxecuter et de faire tourner l'interface graphique de Chiffrage / Déchiffrage :

    __init__ et création de l'objet : L'interface graphique est lancée dans son état initial lorsque l'objet est créé
    L'interface est divisée en deux cadres : celui des commandes (boutons) et celui des résultats.

    la classe Chiffrer_Dechiffree est utilisée pour le calcul du chiffrage / déchiffrage du texte ou des fichiers texte.
    """

    def __init__(self):
        """
        Défini l'état initial de la fenêtre quand l'application est lancée
        L'application se lance à la création de l'objet.
        """

        # Définition de la fenêtre principale

        self.root = Tk()  # Initialisation de la fenêtre
        self.root.title("Application Enigma")  # Le titre de la fenêtre
        self.root.iconbitmap('IconeEnigmaChiffrage.ico')  # L'icone de la fenêtre.
        (self.window_Width, self.window_Height) = (self.root.winfo_screenwidth(), self.root.winfo_screenheight())  # Pour obtenir la hauteur / largeur de l'écran.
        self.root.geometry(str(int(self.window_Width/1.5))+"x"+str(int(self.window_Height/1.5)))  # Définit la taille de la fenêtre (une fraction de la taille de l'écran).
        self.root.state("zoomed")  # La fenêtre est lancée en mode plein écran


        # Définition des frames :

        self.frame_Boutons = LabelFrame(self.root, text="Panneau de contrôle", padx=80, pady=70)
        self.frame_Resultats = LabelFrame(self.root, text="Affichage des résultats", padx=30, pady=30)

        self.frame_Boutons.pack(padx=20, pady=10, fill="x")
        self.frame_Resultats.pack(padx=20, pady=10, expand=True, fill="both")


        # Définition des widgets initiaux :

        self.text_Resultats = Text(self.frame_Resultats, padx=30, pady=30)
        self.entry = Entry(self.frame_Boutons, width=50, borderwidth=2)

        self.text_Resultats.pack(fill="x")
        self.entry.pack(anchor="w")

        self.text_Resultats.insert(0.0, "Pas de résultats")
        self.entry.insert(0, "Entrez un texte à chiffrer ici")


        # Définition des boutons :

        self.bouton_Chiffrer_Texte = Button(self.frame_Boutons, text="Chiffrer", command=self._commande_Chiffrer)
        self.bouton_Dechiffrer_Texte = Button(self.frame_Boutons, text="Déchiffrer", command=self._commande_Dechiffrer)
        self.bouton_Nettoyer = Button(self.frame_Boutons, text="Tout nettoyer", command=self._commande_Nettoyer)
        self.bouton_Chiffrer_Fichier = Button(self.frame_Boutons, text="Chiffrer un fichier...", command=self._commande_Chiffrer_Fichier)
        self.bouton_Dechiffrer_Fichier = Button(self.frame_Boutons, text="Déchiffrer un fichier...", command=self._commande_Dechiffrer_Fichier)

        self.bouton_Plein_Ecran = Button(self.frame_Boutons, text="")
        self.bouton_Ecran_Normal = Button(self.frame_Boutons)
        self.bouton_Quitter = Button(self.frame_Boutons, text="Quitter", command=self.root.destroy)

        self.bouton_Chiffrer_Texte.pack(anchor="w")
        self.bouton_Dechiffrer_Texte.pack(anchor="w")
        self.bouton_Nettoyer.pack(anchor="w")
        self.bouton_Chiffrer_Fichier.pack(anchor="w")
        self.bouton_Dechiffrer_Fichier.pack(anchor="w")
        self.bouton_Quitter.pack(anchor="w")

        self.root.mainloop()


    # Définition des méthodes et fonctions de commandes de boutons :

    def _commande_Chiffrer(self):
        """
        Méthode qui permet d'afficher dans la zone de texte des résultats le texte donné chiffré
        """

        self.text_Resultats.pack_forget()  # La zone de texte sera redéfinie.

        texte = self.entry.get()  # Le texte à chiffrer est récupéré.
        self.set_Chaine_A_Chiffrer(chaine=texte)  # Puis entré en argument de la classe Chiffrer_Dechiffrer

        chaine_Chiffree = self.Chiffrer()  # Et chiffré

        self.text_Resultats = Text(self.frame_Resultats, padx=30, pady=30)  # La zone de texte est redéfinie
        self.text_Resultats.insert(0.0, '"' + texte + '"' + " chiffré donne : " + chaine_Chiffree)  # Insertion du résultat dans la zone de texte.
        self.text_Resultats.pack(fill="x")  # Le widget est mis à l'écran.


    def _commande_Dechiffrer(self):
        """
        Méthode qui permet d'afficher dans la zone de texte des résultats le texte donné déchiffré
        """

        self.text_Resultats.pack_forget()  # La zone de texte sera redéfinie.

        texte = self.entry.get()  # Le texte à déchiffrer est récupéré.
        self.set_Chaine_A_Dechiffrer(chaine=texte)  # Puis entré en argument de la classe Chiffrer_Dechiffrer

        chaine_Dechiffree = self.Dechiffrer()  # Et déchiffré

        self.text_Resultats = Text(self.frame_Resultats, padx=30, pady=30)  # La zone de texte est redéfinie
        self.text_Resultats.insert(0.0, '"' + texte + '"' + " déchiffré donne : " + chaine_Dechiffree)  # Insertion du résultat dans la zone de texte.
        self.text_Resultats.pack(fill="x")  # Le widget est mis à l'écran.


    def _commande_Nettoyer(self):
        """
        Méthode qui réinitialise les widgets de zone d'entrée de texte et la zone de résultats.
        """

        self.entry.delete(0, "end")  # La zone d'entrée est vidée
        self.text_Resultats.pack_forget()  # La zone de texte est enlevée

        self.text_Resultats = Text(self.frame_Resultats, padx=30, pady=30)  # Puis réinitialisée.
        self.text_Resultats.insert(0.0, "Pas de résultats")
        self.text_Resultats.pack(fill="x")


    def _commande_Chiffrer_Fichier(self):
        """
        Cette méthode gère le chiffrage du contenu d'un fichier.
        Le contenu est d'abord récupéré, puis chiffré par l'intermédiaire de la classe Chiffrer_Dechiffrer
        Le résultat est écrit dans le fichier.
        """

        self.root.filename = filedialog.askopenfilename(initialdir="../Chiffrage - Déchiffrage", title="Choisissez un fichier", filetypes=(("tous les fichiers", "*.*"), ("fichiers txt", "*.txt")))  # On demande le chemin du fichier à l'utilisateur.  (On se place dans le fichier Chiffrer - Déchiffrer)

        self.text_Resultats.pack_forget()

        if not self.root.filename == '':  # Si un chemin est spécifié
            chaine = self._get_Contenu_Fichier(self.root.filename)  # Le contenu du fichier est récupéré

            self.set_Chaine_A_Chiffrer(chaine=chaine)
            chaine_Chiffree = self.Chiffrer()  # L'attribut est chiffré

            self._set_Contenu_Fichier(self.root.filename, chaine_Chiffree)  # Le résultat est écrit dans le fichier

            self.text_Resultats = Text(self.frame_Resultats, padx=30, pady=30)
            self.text_Resultats.insert(0.0, "Fichier " + self.root.filename + " chiffré !")  # La zone de résultats est mise à jour.
            self.text_Resultats.pack(fill="x")
        else:  # Un chemin n'est pas spécifié lorsque la fenêtre est fermée
            self.text_Resultats = Text(self.frame_Resultats, padx=30, pady=30)
            self.text_Resultats.insert(0.0, "Chemin spécifié non valide.")  # La zone de résultats est mise à jour.
            self.text_Resultats.pack(fill="x")


    def _commande_Dechiffrer_Fichier(self):
        """
        Cette méthode gère le déchiffrage du contenu d'un fichier.
        Le contenu est d'abord récupéré, puis déchiffré par l'intermédiaire de la classe Chiffrer_Dechiffrer
        Le résultat est écrit dans le fichier.
        """

        self.root.filename = filedialog.askopenfilename(initialdir="../Chiffrage - Déchiffrage", title="Choisissez un fichier", filetypes=(("tous les fichiers", "*.*"), ("fichiers txt", "*.txt")))  # On demande le chemin du fichier à l'utilisateur.  (On se place dans le fichier Chiffrer - Déchiffrer)

        self.text_Resultats.pack_forget()

        if not self.root.filename == '':  # Si un chemin est spécifié
            chaine = self._get_Contenu_Fichier(self.root.filename)  # Le contenu du fichier est récupéré

            self.set_Chaine_A_Dechiffrer(chaine=chaine)
            chaine_Chiffree = self.Dechiffrer()  # L'attribut est déchiffré

            self._set_Contenu_Fichier(self.root.filename, chaine_Chiffree)  # Le résultat est écrit dans le fichier

            self.text_Resultats = Text(self.frame_Resultats, padx=30, pady=30)
            self.text_Resultats.insert(0.0, "Fichier " + self.root.filename + " déchiffré !")  # La zone de résultats est mise à jour.
            self.text_Resultats.pack(fill="x")
        else:  # Un chemin n'est pas spécifié lorsque la fenêtre est fermée
            self.text_Resultats = Text(self.frame_Resultats, padx=30, pady=30)
            self.text_Resultats.insert(0.0, "Chemin spécifié non valide.")  # La zone de résultats est mise à jour.
            self.text_Resultats.pack(fill="x")



Enigma = Main()
