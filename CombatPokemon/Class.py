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

# ATTRIBUTION DES CLASSES
# Dresseurs
Yuki = Dresseur("Yuki")
Thomas = Dresseur("Thomas")
# Starters
Bulbizarre = Pokemon("Bulbizarre", "Plante", 1)
Salamèche = Pokemon("Salamèche", "Feu", 1)
Carapuce = Pokemon("Carapuce", "Eau", 1)
# Pokémons
Pikachu = Pokemon("Pikachu", "Electrique", 6)
Rattata = Pokemon("Rattata", "Normal", 2)
Abo = Pokemon("Abo", "Poison", 3)
Caninos = Pokemon("Caninos", "Feu", 5)
Aspicot = Pokemon("Aspicot", "Insecte", 4)
Roucool = Pokemon("Roucool", "Vol", 4)