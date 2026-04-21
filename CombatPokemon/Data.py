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
    "rattata" : {
        "nom" : "Rattata", 
        "type" : "Normal",
        "niveau" : 2, 
        "pv" : 32,
        "cri" : "rattata.mp3", 
        "attaques" : [morsure]
    },
    "abo" : {
        "nom" : "Abo", 
        "type" : "Poison",
        "niveau" : 3, 
        "pv" : 35,
        "cri" : "abo.mp3", 
        "attaques" : [dard_venin]
    },
    "aspicot" : {
        "nom" : "Aspicot", 
        "type" : "Insecte",
        "niveau" : 2, 
        "pv" : 30,
        "cri" : "aspicot.mp3", 
        "attaques" : [dard_venin]
    },
    "roucool" : {
        "nom" : "Roucool", 
        "type" : "Vol",
        "niveau" : 3, 
        "pv" : 40,
        "cri" : "roucool.mp3", 
        "attaques" : [charge]
    },
}

ROUTE_02 = {
    "pikachu" : {
        "nom" : "Pikachu", 
        "type" : "Electrik",
        "niveau" : 5, 
        "pv" : 44,
        "cri" : "pikachu.mp3", 
        "attaques" : [eclair, charge]
    },
    "caninos" : {
        "nom" : "Caninos", 
        "type" : "Feu",
        "niveau" : 5, 
        "pv" : 53,
        "cri" : "caninos.mp3", 
        "attaques" : [flammeche, charge]
    },
}


# Objets
"""potion = Objet("Potion", 20, 20, "soin")
super_po = Objet("Super-potion", 100, 50, "soin")
rappel = Objet("Rappel", 100,  ,"soin")
ether = Objet("Ether", 80, 5, "soin") # +5pp à une attaque au choix 
pokeball = Objet("Pokéball", 20,  ,"capture")"""