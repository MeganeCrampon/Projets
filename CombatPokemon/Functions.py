from Class import Attaque, Pokemon, Starter, Dresseur, Objet
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

def apprendre_attaque(nouvelle_attaque):
    """if Pokemon.attaque >= 4:
    print(f"{Pokemon.nom_pk} connait déjà trop d'attaques. Voulez-vous lui faire en oublier une et apprendre {nouvelle_attaque} (O/N) ?")
    choix = input("> ")
    match choix :
        case "O" :
            pass
        case "N" :
            pass
    """
    pass

def combat(pk_sauvage, pk_dresseur):
    pass

def utiliser_soins(nom_obj, valeur_soin):
    print("Quel Pokémon souhaitez-vous soigner ?\n")
    pk_cible = input("Nom : ").capitalize().strip()
    if Yuki.sac.get(nom_obj, 0) > 0 :
        print(f"Vous utilisez un.e {nom_obj} sur {pk_cible} (+{valeur_soin} PV)")
        Yuki.sac[nom_obj] -= 1
    else :
        print(f"Vous n'avez plus de {nom_obj} !")

def utiliser_ether():
    print("Quelle attaque voulez-vous régérénérer ?")
    print(Pokemon.attaques)
    atq_cible = input(" ").title().strip()
    print(f"Vous utilisez un Ether sur {atq_cible} (+ 5pp)")

def utiliser_rappel():
    print("Quel Pokémon voulez-vous ramener à la vie ?")
    print(Yuki.equipe)
    pk_mort = input(" ").title().strip()
    print(f"Vous utilisez un Rappel sur {pk_mort}")

def lancer_pokeball(pk_sauvage):
    print(f"Vous lancez une Pokéball sur {pk_sauvage} !")
    reussite = 

def utiliser_objet():
    print(Yuki.sac)
    print("Quel objet souhaitez-vous utiliser ?\n")
    choix = input(" ").capitalize().strip()
    match choix :
        case "Potion":
            utiliser_soins("Potion", 20)
        case "Super-potion":
            utiliser_soins("Super-potion", 50)
        case "Ether":
            utiliser_ether()
        case "Rappel":
            utiliser_rappel()
        case "Pokéball":
            lancer_pokeball("Pokémon sauvage")
        case _:
            print("Objet non_présent dans le sac.")

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
            lancer_pokeball()
        case "3":
            utiliser_objet()
        case "4":
            print("Vous prenez la fuite !")