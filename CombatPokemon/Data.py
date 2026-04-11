from Class import Attaque, Pokemon, Starter, Dresseur, Objet

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
charge = Attaque("Charge", "Normal", 40, 15)
pistolet_o = Attaque("Pistolet à O", "Eau", 40, 12)
flammeche = Attaque("Flammeche", "Feu", 40, 12)
morsure = Attaque("Morsure", "Ténébres", 30, 14)
eclair = Attaque("Eclair", "Electrique", 40, 12)
dard_venin = Attaque("Dard-Venin", "Poison", 20, 12)

# Attributions attaques
bulbizarre.attaques.append(charge)
salameche.attaques.append(flammeche)
carapuce.attaques.append(pistolet_o)
pikachu.attaques.append(eclair)
rattata.attaques.append(morsure)
abo.attaques.append(dard_venin)
aspicot.attaques.append(dard_venin)
roucool.attaques.append(charge)

# Objets
potion = Objet("Potion", 20, 20)
super_po = Objet("Super-potion", 100, 50)
rappel = Objet("Rappel", 100, )
ether = Objet("Ether", 80, 5) # +5pp à une attaque au choix 
pokeball = Objet("Pokéball", 20, )