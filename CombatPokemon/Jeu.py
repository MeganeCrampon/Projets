import Functions
from Data import starters_dispo, Yuki, Thomas
from Class import Attaque, Pokemon, Starter, Dresseur, Objet
import Script
import Sounds
import pygame
import time

"""if __name__ == "__Jeu__":
    try:
        Functions.debut_aventure()
    except KeyboardInterrupt:
        print("\nPartie interrompue. À bientôt !")
    finally:
        pygame.quit()"""

Script.intro()
Script.dialogue_chêne()
time.sleep(1)
Script.attribution_starter()
time.sleep(1)
Functions.jouer_musique(Sounds.m_base)
Script.suite_aventure()

print("\n--- EN ROUTE VERS LA ROUTE 01 !! ---\n")
Script.route_01()
