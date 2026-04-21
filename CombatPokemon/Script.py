from Class import Attaque, Pokemon, Starter, Dresseur, Objet
from Data import starters_dispo, Yuki, Thomas
import Data
import Functions
import Sounds
import random
import pygame
import os
import time

pygame.mixer.init()

dossier_actuel = os.path.dirname(__file__)

def intro():
    texte_intro = ["Vous êtes Yuki, une jeune apprentie dresseuse en quête d'aventure.",
        "Avec votre ami et rival de toujours, Thomas, vous décidez de rendre visite au Professeur Chêne, spécialiste des Pokémons.",
        "C'est ainsi que vous vous rendez à son laboratoire, pour obtenir votre tout premier Pokémon chacun.",
        "\n...Vous vous retrouvez enfin face au grand Professeur Chêne.\n"]
    it_intro = iter(texte_intro)
    Functions.jouer_musique(Sounds.m_base)
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
    pygame.mixer.music.fadeout(600)

def attribution_starter():
    print("Alors, par quel Pokémon sera choisie Yuki ?")
    print("...")
    time.sleep(1.5)
    starter_Yuki = random.choice(starters_dispo)
    Yuki.equipe.append(starter_Yuki)
    starters_dispo.remove(starter_Yuki)
    Functions.jouer_son(Sounds.recup_objet)
    print(f"Yuki a été choisie par............{starter_Yuki} !! Il rejoint son équipe !")
    time.sleep(2.5)
    print("\nEt maintenant, qui choisia Thomas ?")
    print("...")
    time.sleep(1.5)
    starter_Thomas = random.choice(starters_dispo)
    Thomas.equipe.append(starter_Thomas)
    starters_dispo.remove(starter_Thomas)
    Functions.jouer_son(Sounds.recup_objet)
    print(f"Thomas a été choisi par............{starter_Thomas} !! Il rejoint son équipe !\n")
    time.sleep(1.5)

def suite_aventure():
    dial = ["Hahaha, dites-donc jeunes gens ! Vos nouveaux Pokémon ont déjà l'air de beaucoup vous apprécier !",
    "Ils n'ont même pas hésité en vous choisissant !",
    "Bon...maintenant que vous avez un Pokémon, vous êtes quasiment prêts pour partir à l'aventure et découvrir le merveilleux monde des Pokémons !",
    "Pour se faire il ne vous manque plus qu'une petite chose... Vous savez de quoi il s'agit ?",
    "..."
    "... Non ?? Mais allons... Je parles des pokéballs voyons !",
    "Comment comptez-vous capturer des Pokémons sans pokéballs ? Hahaha, toujours tête en l'air cette jeunesse !",
    "Bref, tenez, voilà 5 pokéballs chacun pour commenecer à vous former une petite équipe ! Vous pourrez en trouver dans la nature ou en acheter dans une Boutique Pokémon.",
    "Bon, eh bien... On dirait qu'il est l'heure pour vous de voler de vos propres ailes, haha !!",
    "..."
    "...OH ! ATTENDEZ !!",
    "J'ai failli oublier, prenez ceci, c'est un Pokédex ! Il vous permettra de receuiller des informations sur chaque nouveau Pokémon que vous renconntrerez ! 'Tip-top' non !?",
    "..."
    "... Hm, bon...bref !!",
    "Je vous souhaite de vivre de belles aventures les enfants, à bientôt !!\n"]
    it_dial = iter(dial)
    for phrase in it_dial:
        input(phrase)
    time.sleep(0.5)
    Yuki.ajouter_obj("Pokéball", 5)
    Thomas.ajouter_obj("Pokéball", 5)
    Functions.jouer_son(Sounds.pop)
    time.sleep(2)
    input("\nVous décidez de partir tout de suite pour la première étape de votre aventure : la Route 01 !!")

def route_01():
    input("Vous vous dirigez vers la Route 01." \
    "Vous appercevez des hautes herbes sur le chemin, et vous n'avez pas d'autre choix si vous vouler continuer votre route, que de les traverser.")
    time.sleep(1)
    pygame.mixer.music.fadeout(600)
    pkmn_sauvage = Functions.generer_pkmn(Data.ROUTE_01)
    Functions.entrer_herbes_hautes(pkmn_sauvage)