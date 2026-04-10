# CREATION DES CLASSES
class Pokemon :
    def __init__(self, nom_pk, type_pk, xp, niveau, attaques):
        self.nom = nom_pk
        self.type = type_pk
        self.xp = xp # besoin de 20 pour passer de 1 à 2, 30 pour passer de 2 à 3... 
        self.niveau = niveau   
        self.attaques = attaques # 4 maximum

class Starter(Pokemon):
    def __init__(self, nom_pk, type_pk, xp, niveau, attaques, affection):
        super().__init__(nom_pk, type_pk, xp, niveau, attaques)
        self.affection = affection # monte quand on termine un combat avec lui

class Dresseur :
    def __init__(self, nom_dr):
        self.nom = nom_dr
        self.equipe = []
        self.sac = [] # Potion, Super-Potion, Ether, Rappel
        self.badge = 0