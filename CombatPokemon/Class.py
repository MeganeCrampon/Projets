# CREATION DES CLASSES
class Attaque :
    def __init__(self, nom_atq, type_atq, puissance):
        self.nom = nom_atq
        self.type = type_atq
        self.puissance = puissance

class Pokemon :
    def __init__(self, nom_pk, type_pk, niveau):
        self.nom = nom_pk
        self.type = type_pk
        self.xp = 0 # besoin de 20 pour passer de 1 à 2, 30 pour passer de 2 à 3... 
        self.niveau = niveau   
        self.attaques = [] # 4 maximum
    def __str__(self):
        return f"{self.nom}"
    def __repr__(self):
        return f"Nom : {self.nom} | Type : {self.type} | Niveau : {self.niveau}"

class Starter(Pokemon):
    def __init__(self, nom_pk, type_pk, niveau, affection):
        super().__init__(nom_pk, type_pk, niveau)
        self.affection = affection # monte quand on termine un combat avec lui
    def __str__(self):
        return f"{self.nom}"
    def __repr__(self):
        return f"Nom : {self.nom} | Type : {self.type} | Niveau : {self.niveau}"

class Dresseur :
    def __init__(self, nom_dr):
        self.nom = nom_dr
        self.equipe = []
        self.sac = [] # Potion, Super-Potion, Ether, Rappel
        self.badge = 0
    def __str__(self):
        return f"{self.nom}"
    def __repr__(self):
        return f"Nom : {self.nom}"