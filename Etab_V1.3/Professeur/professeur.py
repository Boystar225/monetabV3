from models.personne import Personne
from Professeur.ICrudProfesseur import ICRUDProfesseur
from Professeur.IEducation import IEducation

class Professeur(Personne, IEducation, ICRUDProfesseur):
    """
    Classe représentant un professeur, héritant de Personne et implémentant des interfaces éducatives.
    """

    __professeurs = []
    
    def __init__(self, dateNaissance, ville, prenom, nom, telephone, vacant, matiereEnseigne, prochainCours, sujetProchaineReunion):
        super().__init__(dateNaissance, ville, prenom, nom, telephone)
        self.__vacant = vacant
        self.__matiereEnseigne = matiereEnseigne
        self.__prochainCours = prochainCours
        self.__sujetProchaineReunion = sujetProchaineReunion

    def __str__(self):
        statut_affiche = "Oui" if self.__vacant else "Non"
        return f"Professeur n° {self.get_id()} : {self.get_nom()} {self.get_prenom()}, né le {self.get_date_naissance()} à {self.get_ville()}, téléphone : {self.get_telephone()}, vacant: {statut_affiche}, enseigne {self.__matiereEnseigne}"

    @property 
    def vacant(self):
        return self.__vacant
    
    @property 
    def matiereEnseigne(self):
        return self.__matiereEnseigne

    @property 
    def prochainCours(self):
        return self.__prochainCours
    
    @property 
    def sujetProchaineReunion(self):
        return self.__sujetProchaineReunion

    def set_sujetProchaineReunion(self, sujetProchaineReunion):
        self.__sujetProchaineReunion = sujetProchaineReunion            

    def set_prochainCours(self, prochainCours):
        self.__prochainCours = prochainCours

    def set_matiereEnseigne(self, matiereEnseigne):
        self.__matiereEnseigne = matiereEnseigne            

    def set_vacant(self, vacant):
        self.__vacant = vacant    

    @staticmethod
    def ajouter(professeur):
        Professeur.__professeurs.append(professeur)

    @staticmethod
    def modifier(professeur):
        for index, prof_existe in enumerate(Professeur.__professeurs):
            if prof_existe.get_id() == professeur.get_id():
                Professeur.__professeurs[index] = professeur
                return True 
        return False

    @staticmethod
    def supprimer(identifiant):
        for index, prof in enumerate(Professeur.__professeurs):
            if prof.get_id() == identifiant:
                del Professeur.__professeurs[index]
                return True
        return False

    @staticmethod
    def obtenir_professeurs():
        return [str(prof) for prof in Professeur.__professeurs]

    @staticmethod
    def obtenir(identifiant):
        for prof in Professeur.__professeurs:
            if prof.get_id() == identifiant:
                return prof
        return None
