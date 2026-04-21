from Class import Attaque, Pokemon, Starter, Dresseur, Objet
from Data import starters_dispo, Yuki, Thomas
import Sounds
import random
import pygame
import os
import time

pygame.mixer.init()

dossier_actuel = os.path.dirname(__file__)

# FONCTIONS
def jouer_son(nom_son):
    chemin = os.path.join(dossier_actuel, "sounds", nom_son)
    son = pygame.mixer.Sound(chemin)
    son.set_volume(0.6)
    son.play()

def jouer_musique(nom_musique):
    chemin = os.path.join(dossier_actuel, "sounds", nom_musique)
    son = pygame.mixer.music.load(chemin)
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(-1)

def entrer_herbes_hautes(pkmn_sauvage):
    jouer_son(Sounds.herbes)
    print("Vous entrez dans des herbes hautes...")
    time.sleep(1)
    print(f"Vous tombez sur un {pkmn_sauvage} !!")
    time.sleep(0.5)
    rencontre_pk()

def trouver_pkmn(nom, equipe):
    for pkmn in equipe :
        if pkmn.nom_pk == nom :
            return pkmn
    return None

def trouver_atq(nom, pkmn):
    for atq in pkmn:
        if atq.nom_atq == nom :
            return atq
    return None

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

def combat(pk_adverse, pk_dresseur):
    print("")

def utiliser_soins(nom_obj, valeur_soin):
    print("Quel Pokémon souhaitez-vous soigner ?\n")
    pk_cible = input("Nom : ").capitalize().strip()
    if Yuki.sac.get(nom_obj, 0) > 0 :
        print(f"Vous utilisez un.e {nom_obj} sur {pk_cible.nom_pk} (+{valeur_soin} PV)")
        Yuki.sac[nom_obj] -= 1
        mon_pk = trouver_pkmn(pk_cible, Yuki.equipe)
        if mon_pk:
            mon_pk.pv += valeur_soin
        else : 
            print("Pokémon non trouvé dans l'équipe !")
    else :
        print(f"Vous n'avez plus de {nom_obj} !")
        rencontre_pk()

def utiliser_ether(dresseur, pkmn_actif):
    if dresseur.sac.get("Ether", 0) > 0 :
        print("\nQuelle attaque voulez-vous recharger ?")
        for i, atq in enumerate(pkmn_actif.attaques, 1):
            print(f"{i}) {atq.nom} ({atq.pp}/{atq.pp_max}PP)")
        try :
            choix = int(input("Numéro de l'attaque : ")) - 1
            if 0 <= choix < len(pkmn_actif.attaques):
                atq_cible = pkmn_actif.attaques[choix]
                print(f"Vous utilisez un Ether sur {atq_cible.nom_atq} (+5pp)")
                atq_cible.pp = min(atq_cible.pp + 5, atq_cible.pp_max)
                dresseur.sac["Ether"] -= 1
                print(f"Succès ! L'attaque {atq_cible.nom_atq} récupère 5pp et a maintenant {atq_cible.pp}!")
            else : 
                print("Choix invalide, attaque non trouvée !")
        except ValueError:
            print("Veuillez entrer un chiffre.")
    else :
            print(f"Vous n'avez plus d'Ether !")
    rencontre_pk()

def utiliser_rappel(dresseur):
    if dresseur.sac.get("Rappel", 0) > 0:
        print("Quel Pokémon voulez-vous ramener à la vie ?")
        for i, pkmn in enumerate(dresseur.equipe):
            print(f"{i}) {pkmn.nom_pk} ({pkmn.pv}PV)")
        try :
            choix = int(input("Numéro du pokémon : ")) - 1
            if 0 <= choix < len(dresseur.equipe):
                pkmn_choisi = dresseur.equipe[choix]
                if pkmn_choisi.pv <= 0:
                    print(f"Vous utilisez un Rappel sur {pkmn_choisi.nom_pk}")
                    gain_pv = int(pkmn_choisi.pv_max * 0.20) 
                    pkmn_choisi.pv = gain_pv
                    dresseur.sac["Rappel"] -= 1
                    print(f"Succès ! {pkmn_choisi.nom_pk} a été ramené à la vie avec {gain_pv}PV!")
                else :
                    print("Ce Pokémon n'est pas mort.")
        except ValueError:
            print("Veuillez entrer un chiffre.")
    else :
        print("Vous n'avez plus de Rappel !")
    rencontre_pk()

def lancer_pokeball(pk_sauvage):
    print(f"Vous lancez une Pokéball sur {pk_sauvage} !")
    # reussite =
    rencontre_pk() 

def utiliser_objet(dresseur):
    sac_liste = list(dresseur.sac.keys())
    if not sac_liste:
        print("Votre sac est vide !")
        return
    print("\n--- SAC ---")
    for i, nom_obj in enumerate(sac_liste, 1):
            print(f"{i}) {nom_obj} (Quantité : {dresseur.sac[nom_obj]})")
    print("Quel objet souhaitez-vous utiliser ?\n")
    try : 
        choix = int(input("Numero de l'objet souhaité : ")) - 1
        if 0 <= choix < len(sac_liste):
            nom_choisi = sac_liste[choix]
            if nom_choisi == "Potion":
                utiliser_soins("Potion", 20)
            elif nom_choisi == "Super-potion":
                utiliser_soins("Super-potion", 50)
            elif nom_choisi == "Ether":
                utiliser_ether()
            elif nom_choisi == "Rappel":
                utiliser_rappel()
            elif nom_choisi == "Pokéball":
                lancer_pokeball("Pokémon sauvage")
    except ValueError:
        print("Objet non présent dans le sac.")

def rencontre_pk():
    jouer_musique(Sounds.m_combat)
    time.sleep(0.1)
    print("\nQue voulez-vous faire (1/2/3/4) ?")
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
            utiliser_objet(Yuki)
        case "4":
            print("Vous prenez la fuite !")