from datetime import datetime

class Personne:
    """
    Classe représentant une personne avec des informations personnelles.
    """

    __idUnique = 0

    # Initialise une nouvelle personne avec ses informations personnelles.
    def __init__(self, dateNaissance, ville, prenom, nom, telephone):
        Personne.__idUnique += 1
        self.__id = Personne.__idUnique
        self.__dateNaissance = dateNaissance
        self.__ville = ville
        self.__prenom = prenom
        self.__nom = nom
        self.__telephone = telephone

    # Retourne une représentation sous forme de chaîne de la personne.
    def __str__(self):
        return (f"Personne n° {self.__id} : {self.__nom} {self.__prenom}, "
                f"née le {self.__dateNaissance} à {self.__ville}, numéro de téléphone : {self.__telephone}")

    # Calcule et retourne l'âge de la personne en années.
    def obtenir_age(self):
        date_present = datetime.today()
        date_naissance = datetime.strptime(self.__dateNaissance, '%Y-%m-%d')
        age = date_present.year - date_naissance.year - ((date_present.month, date_present.day) < (date_naissance.month, date_naissance.day))
        return age

    # Retourne l'identifiant unique de la personne
    @property
    def id(self):
        return self.__id

    # Retourne la date de naissance de la personne.
    @property
    def date_naissance(self):
        return self.__dateNaissance

    # Retourne la ville de résidence de la personne.
    @property
    def ville(self):
        return self.__ville

    # Retourne le prénom de la personne.
    @property
    def prenom(self):
        return self.__prenom

    # Retourne le nom de la personne.
    @property
    def nom(self):
        return self.__nom

    # Retourne le numéro de téléphone de la personne.
    @property
    def telephone(self):
        return self.__telephone

    def set_prenom(self, prenom):
        self.__prenom = prenom

    def set_nom(self, nom):
        self.__nom = nom

    def set_ville(self, ville):
        self.__ville = ville

    def set_date_naissance(self, date_naissance):
        self.__dateNaissance = date_naissance

    def set_telephone(self, telephone):
        self.__telephone = telephone
