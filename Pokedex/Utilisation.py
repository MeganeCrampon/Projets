from FonctionsEtDB import *

# MENU
print("--- POKEDEX ---")
print("\nMENU PRINCIPAL : " \
"\n1. Afficher le Pokédex" \
"\n2. Chercher un Pokémon par type" \
"\n3. Chercher un Pokémon par niveau" \
"\n4. Ajouter un Pokémon" \
"\n5. Supprimer un Pokémon" \
"\n6. Quitter")

while True :
    choix = input("\nQUE VOULEZ-VOUS FAIRE ? ")

    # CHOIX UTILISATEUR
    if choix == "1":
        afficher_pokedex()
    if choix == "2":
        trouver_type() 
    if choix == "3":
        trouver_niveau()
    if choix == "4":
        ajouter_pokemon()
    if choix == "5":
        supprimer_pokemon()
    if choix == "6":
        print("Au revoir !")
        break