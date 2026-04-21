from Class import Attaque, Pokemon, Starter, Dresseur, Objet

# ATTRIBUTION DES CLASSES
# Dresseurs
Yuki = Dresseur("Yuki")
Thomas = Dresseur("Thomas")

# Attaques
charge = Attaque("Charge", "Normal", 40, 15)
pistolet_o = Attaque("Pistolet à O", "Eau", 40, 12)
flammeche = Attaque("Flammeche", "Feu", 40, 12)
morsure = Attaque("Morsure", "Ténébres", 30, 14)
eclair = Attaque("Eclair", "Electrik", 40, 12)
dard_venin = Attaque("Dard-Venin", "Poison", 20, 12)

# POKEDEX
STARTERS = {
    "bulbizarre" : {
        "nom" : "Bulbizarre", 
        "type" : "Plante", 
        "niveau" : 1, 
        "pv" : 45, 
        "cri" : "",
        "attaques" : [charge]
    },
    "salameche" : {
        "nom" : "Salamèche", 
        "type" : "Feu",
        "niveau" : 1, 
        "pv" : 40,
        "cri" : "", 
        "attaques" : [flammeche]
    },
    "carapuce" : {
        "nom" : "Carapuce", 
        "type" : "Eau",
        "niveau" : 1, 
        "pv" : 45,
        "cri" : "", 
        "attaques" : [pistolet_o]
    },
}
starters_dispo = ["bulbizarre", "salameche", "carapuce"]

ROUTE_01 = {
"rattata" : {"Rattata", "Normal", 2, 32, "rattata.mp3"},
"abo" : {"Abo", "Poison", 3, 36},
"aspicot" : {"Aspicot", "Insecte", 2, 30},
"roucool" : {"Roucool", "Vol", 3, 42}
}

ROUTE_02 = {
"pikachu" : {"Pikachu", "Electrik", 6, 40},
"caninos" : {"Caninos", "Feu", 5, 58},
}





# Attributions attaques
"""pikachu.attaques.append(eclair)
rattata.attaques.append(morsure)
abo.attaques.append(dard_venin)
aspicot.attaques.append(dard_venin)
roucool.attaques.append(charge)"""

# Objets
"""potion = Objet("Potion", 20, 20, "soin")
super_po = Objet("Super-potion", 100, 50, "soin")
rappel = Objet("Rappel", 100,  ,"soin")
ether = Objet("Ether", 80, 5, "soin") # +5pp à une attaque au choix 
pokeball = Objet("Pokéball", 20,  ,"capture")"""