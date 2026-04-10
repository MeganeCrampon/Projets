from Class import Attaque, Pokemon, Starter, Dresseur
from Data import starters_dispo, Yuki, Thomas
import random

# FONCTIONS
def intro():
    texte_intro = ["Vous êtes Yuki, une jeune apprentie dresseuse en quête d'aventure.",
        "Avec votre ami et rival de toujours, Thomas, vous décidez de rendre visite au Professeur Chêne, spécialiste des Pokémons.",
        "C'est ainsi que vous vous rendez à son laboratoire, pour obtenir votre tout premier Pokémon chacun.",
        "...Vous vous retrouvez enfin face au grand Professeur Chêne.\n"]
    it_intro = iter(texte_intro)
    print("--- BIENVENUE DANS LE MONDE DES POKEMONS ---")
    for phrase in it_intro:
        input(phrase)

def dialogue_chêne():
    dial = ["Eh bien, bien le bonjour les enfants, qu'est ce qui vous ammène ?",
    "Oh mais oui, suis-je bête... Vous venez pour récupérer votre tout premier Pokémon : votre Starter !",
    "Dans ce cas, mhh... innovons ! Ce sera le Pokémon qui vous choisira !\n"]
    it_dial = iter(dial)
    for phrase in it_dial:
        input(phrase)

def attribution_starter():
    starter_Yuki = random.choice(starters_dispo)
    Yuki.equipe.append(starter_Yuki)
    starters_dispo.remove(starter_Yuki)
    print(f"Yuki a obtennu............{starter_Yuki} !!")
    starter_Thomas = random.choice(starters_dispo)
    Thomas.equipe.append(starter_Thomas)
    starters_dispo.remove(starter_Thomas)
    print(f"\nThomas a obtennu............{starter_Thomas} !!")

def combat(pk_sauvage, pk_dresseur):
    pass

def capture():
    pass

def utiliser_objet():
    print(Dresseur.sac)
    print("Que souhaitez vous utiliser ?")
    choix = input(" ").capitalize().strip()

def rencontre_pk(pk_sauvage):
    print(f"Vous tombez sur un...{pk_sauvage} !!")
    print("\nQue voulez-vous faire (1/2/3/4) ? ")
    choix = input("""
        "1) Attaquer" \
        "2) Capturer" \
        "3) Utiliser un objet" \
        "4) Fuir 
        > """)
    match choix :
        case "1":
            combat()
        case "2":
            pass
        case "3":
            pass
        case "4":
            print("Vous prenez la fuite !")