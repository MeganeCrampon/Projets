import sqlite3

conn = sqlite3.connect("SQL/Exo 3/pokemon.db")
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS Pokemons (
    id INTEGER PRIMARY KEY,
    nom TEXT UNIQUE,
    type TEXT,
    niveau INTEGER
)           
''')

cur.execute("SELECT COUNT(*) FROM Pokemons")
nombre_pokemons = cur.fetchone()[0]
if nombre_pokemons == 0:
    cur.execute("INSERT OR REPLACE INTO Pokemons (nom, type, niveau) VALUES ('Pikachu', 'Electrique', 15)")
    cur.execute("INSERT OR REPLACE INTO Pokemons (nom, type, niveau) VALUES ('Caninos', 'Feu', 12)")
    cur.execute("INSERT OR REPLACE INTO Pokemons (nom, type, niveau) VALUES ('Kaiminus', 'Eau', 16)")
    conn.commit()

def affichage_recherche(liste_pokemons):
    if not liste_pokemons:
        print("[!] Aucun Pokemon trouvé !")
        return
    print("\n" + "="*55)
    print(f"{'Nom' :<15} | {'Type' :<19} | {'Niveau'}")
    print("-"*55)
    for pokemon in liste_pokemons:
        print(f"{pokemon[1]:<15} | Type : {pokemon[2] :<12} | Niveau : {pokemon[3]}")      
    print("="*55)

def ajouter_pokemon():
    nom = input("Quel est le nom du pokémon voulez vous rajouter ? ").strip().capitalize()
    type = input("Son type : ").strip().capitalize()
    niveau = input("Son niveau : ")
    commande = "INSERT OR REPLACE INTO Pokemons (nom, type, niveau) VALUES (?, ?, ?)"
    cur.execute(commande, (nom, type, niveau,))
    conn.commit()

def trouver_type ():
    type_choisi = input("Quel est le type de Pokémon que vous cherchez ? ").strip().capitalize()
    cur.execute("SELECT * FROM Pokemons WHERE type = ?", (type_choisi,))
    resultat_type = cur.fetchall()
    print(f"--- POKEMONS DE TYPE {type_choisi} : ---")
    affichage_recherche(resultat_type)

def trouver_niveau():
    choix = input("Quel est le niveau minimum de Pokémon que vous cherchez ? ")
    niveau_choisi = int(choix)
    cur.execute("SELECT * FROM Pokemons WHERE niveau >= ?", (niveau_choisi,))
    resultat_niveau = cur.fetchall()
    print(f"--- POKEMONS DE NIVEAU ({niveau_choisi}+) : ---")
    affichage_recherche(resultat_niveau)