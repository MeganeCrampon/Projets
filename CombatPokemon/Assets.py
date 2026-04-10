from Class import Pokemon, Starter, Dresseur 

# FONCTIONS
def intro():
    texte_intro = ["Vous êtes Yuki, une jeune apprentie dresseuse en quête d'aventure.",
        "Avec votre ami et rival de toujours, Thomas, vous décidez de rendre visite au le Professeur Chêne, spécialiste des Pokémons.",
        "C'est ainsi que vous vous rendez à son laboratoire, pour obtenir votre tout premier Pokémon chacun."]
    it_intro = iter(texte_intro)
    print("--- BIENVENUE DANS LE MONDE DES POKEMONS ---")
    for phrase in it_intro:
        input(phrase)

def utiliser_objet():
    print("Que souhaitez vous utiliser ?")
    print(Dresseur.sac)
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
            pass
        case "2":
            pass
        case "3":
            pass
        case "4":
            print("Vous prenez la fuite !")