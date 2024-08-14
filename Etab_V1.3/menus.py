from datetime import datetime
import time

# Constantes pour les couleurs
# Constantes pour les couleurs
bleu = '\033[0;94m'      # Bleu
blanc = '\033[0;97m'     # Blanc
gris = '\033[0;90m'      # Gris
violet = '\033[0;95m'    # Violet
turquoise = '\033[0;36m' # Turquoise
reset = '\033[0m'        # Réinitialisation

def accueil(contenu):
    print(f"{bleu}******************************************************\n")
    print(f'\t{contenu}\n')
    print('******************************************************\033[0m')

def afficher_menu():
    print(f"{blanc}\n\tMENU")
    print("1: Gestion des élèves")
    print("2: Gestion des professeurs")
    print("3: Gestion des utilisateurs") 
    print("0: Quitter()\n" + reset)
    print(f"Date et Heure Système : {gris}{datetime.now().strftime('%d/%m/%Y  %H:%M')} \n{reset}")

def afficherSousMenuElev():
    print(f"{violet}\n\tMENU")
    print("1: Ajouter un élève")
    print("2: Supprimer un élève")
    print("3: Modifier les informations de l'élève")
    print("4: Lister les élèves")
    print("5: Retour")
    print("0: Accueil")

def afficherSousMenuProf():
    print(f"{violet}\n\tMENU")
    print("1: Ajouter un professeur")
    print("2: Supprimer un professeur")
    print("3: Modifier les informations du professeur")
    print("4: Lister les professeurs")
    print("5: Retour")    
    print("0: Accueil")

def afficherSousMenuUtil():
    print(f"{violet}\n\tMENU")
    print("1: Ajouter un utilisateur")
    print("2: Supprimer un utilisateur")
    print("3: Modifier les informations d'un utilisateur")
    print("4: Lister les utilisateurs")
    print("5: Retour")    
    print("0: Accueil")

def quitter(debut):
    fin = time.time()
    dure = fin - debut
    minutes, seconds = divmod(dure, 60)
    print(f"{turquoise}Merci d'avoir utilisé l'application ! À bientôt.")
    print(f"Durée de la session : {int(minutes)} minutes et {int(seconds)} secondes.{reset}")
