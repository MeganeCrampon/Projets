from Class import Attaque, Pokemon, Starter, Dresseur

# ATTRIBUTION DES CLASSES
# Dresseurs
Yuki = Dresseur("Yuki")
Thomas = Dresseur("Thomas")

# Starters
bulbizarre = Pokemon("Bulbizarre", "Plante", 1)
salameche = Pokemon("Salamèche", "Feu", 1)
carapuce = Pokemon("Carapuce", "Eau", 1)
starters_dispo = [bulbizarre, salameche, carapuce]

# Pokémons
pikachu = Pokemon("Pikachu", "Electrique", 6)
rattata = Pokemon("Rattata", "Normal", 2)
abo = Pokemon("Abo", "Poison", 3)
caninos = Pokemon("Caninos", "Feu", 5)
aspicot = Pokemon("Aspicot", "Insecte", 4)
roucool = Pokemon("Roucool", "Vol", 4)

# Attaques
charge = Attaque("Charge", "Normal", 40)
pistolet_o = Attaque("Pistolet à O", "Eau", 40)
flammeche = Attaque("Flammeche", "Feu", 40)
morsure = Attaque("Morsure", "Ténébres", 30)
eclair = Attaque("Eclair", "Electrique", 40)
dard_venin = Attaque("Dard-Venin", "Poison", 20)

# Attributions attaques
bulbizarre.attaques.append(charge)
salameche.attaques.append(flammeche)
carapuce.attaques.append(pistolet_o)
pikachu.attaques.append(eclair)
rattata.attaques.append(morsure)
abo.attaques.append(dard_venin)
aspicot.attaques.append(dard_venin)
roucool.attaques.append(charge)