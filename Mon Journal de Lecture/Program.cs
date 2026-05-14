using System;
using System.Collections.Generic;
using System.Globalization;
using Microsoft.Data.Sqlite;

class Program
{
    static void Main(string[] args)
    {
        Console.OutputEncoding = System.Text.Encoding.UTF8;
        Database db = new Database();
        db.InitDB();

        bool continuer = true;
        while (continuer)
        {
            AfficherMenu();
            string choix = Console.ReadLine();

            switch (choix)
            {
                case "1":
                    AfficherListeLivres(db);
                    break;
                case "2":
                    AjouterLivre(db);
                    break;
                case "3":
                    MarquerCommeLu(db);
                    break;
                case "4":
                    ChercherTitre(db);
                    break;
                case "5":
                    NoterLivre(db);
                    break;
                case "6":
                    SupprimerLivre(db);
                    break;
                case "7":
                    Console.WriteLine("Merci d'avoir utilisé votre bibliothèque personnelle ! Au revoir !");
                    continuer = false;
                    break;
                default:
                    Console.WriteLine("Choix invalide, veuillez réessayer.");
                    break;
            }
        }
    }

    static void AfficherMenu()
    {
        Console.WriteLine("\n=== Mon Journal de Lecture ===");
        Console.WriteLine("1. Afficher les livres");
        Console.WriteLine("2. Ajouter un livre");
        Console.WriteLine("3. Marquer un livre comme lu");
        Console.WriteLine("4. Chercher un livre par titre");
        Console.WriteLine("5. Noter un livre");
        Console.WriteLine("6. Supprimer un livre");
        Console.WriteLine("7. Quitter");
        Console.Write("Votre choix : ");
    }

    static string AfficherEtoiles(int? note)
    {
        if (note == null) return "Non noté";
        else if (note == 1) return "★☆☆☆☆";
        else if (note == 2) return "★★☆☆☆";
        else if (note == 3) return "★★★☆☆";
        else if (note == 4) return "★★★★☆";
        else if (note == 5) return "★★★★★";
        else return "Note invalide";
    }

    static void AfficherListeLivres(Database db)
    {
        var livres = db.ObtenirLivres();
        if (livres.Count > 0)
        {
            Console.WriteLine("=== Liste de vos Livres ===");
            for (int i = 0; i < livres.Count; i++)
            {
                string statut = livres[i].EstLu ? "Lu" : "Non Lu";
                Console.WriteLine($"[{i + 1}] {livres[i].Titre} - Auteur : {livres[i].Auteur} - Genre : {livres[i].Genre} - {statut} - Note : {AfficherEtoiles(livres[i].Note)}");
            }
        } 
        else 
        {
            Console.WriteLine("Aucun livre dans votre bibliothèque ! Voulez vous en ajouter un ? (O/N) : ");
            string validation = Console.ReadLine();
            switch (validation.ToUpper())
            {
                case "O":
                    AjouterLivre(db);
                    break;
                case "N":
                    Console.WriteLine("Retour au menu principal.");
                    break;
            }
        }
    }
    static void AjouterLivre(Database db)
    {
        Console.WriteLine("Titre du livre : ");
        string titre = Console.ReadLine();
        titre = CultureInfo.CurrentCulture.TextInfo.ToTitleCase(titre.ToLower());

        Console.WriteLine("Auteur du livre : ");
        string auteur = Console.ReadLine();
        auteur = CultureInfo.CurrentCulture.TextInfo.ToTitleCase(auteur.ToLower());

        Console.WriteLine("Genre du livre : ");
        string genre = Console.ReadLine();
        genre = CultureInfo.CurrentCulture.TextInfo.ToTitleCase(genre.ToLower());

        db.AjouterLivreDB(new Livre(titre, auteur, genre));
        Console.WriteLine("Livre ajouté avec succès !");
    }

    static void MarquerCommeLu(Database db)
    {
        var livres = db.ObtenirLivres();
        AfficherListeLivres(db);
        Console.WriteLine("Entrez le numéro du livre que vous avez lu : ");
        string saisie = Console.ReadLine();
        int numero = int.Parse(saisie);
        var livreLu = livres[numero - 1];
        if (livreLu.EstLu)
        {
            Console.WriteLine("Ce livre est déjà marqué comme Lu.");
        }
        else
        {
            db.ChangerStatutDB(livreLu.Id, !livreLu.EstLu);
            Console.WriteLine($"Le livre '{livreLu.Titre}' a été marqué comme Lu !");
        }
    }

    static void ChercherTitre(Database db)
    {
        var livres = db.ObtenirLivres();
        Console.WriteLine("Entrez le titre du livre que vous cherchez : ");
        string saisie = Console.ReadLine();
        var livresTrouves = livres.FirstOrDefault(l => l.Titre.Contains(saisie, StringComparison.OrdinalIgnoreCase));
        if (livresTrouves != null)
        {
            string statut = livresTrouves.EstLu ? "Lu" : "Non Lu";
            Console.WriteLine($"Livres trouvés : {livresTrouves.Titre} - Auteur : {livresTrouves.Auteur} - Genre : {livresTrouves.Genre} - {statut}");
        }
        else
        {
            Console.WriteLine("Aucun livre trouvé avec ce titre.");
            Console.WriteLine("Voulez-vous chercher un autre titre ? (O/N) : ");
            string validation = Console.ReadLine();

            switch (validation)
            {
                case "O":
                    ChercherTitre(db);
                    break;
                case "N":
                    Console.WriteLine("Retour au menu principal.");
                    break;
            }
        }
    }

    static void NoterLivre(Database db)
    {
        var livres = db.ObtenirLivres();
        AfficherListeLivres(db);
        Console.WriteLine("Entrez le numéro du livre que vous souhaitez noter : ");
        string saisie = Console.ReadLine();
        int numero = int.Parse(saisie);
        var livreANoter = livres[numero - 1];
        Console.WriteLine($"Entrez votre note pour '{livreANoter.Titre}' (1 à 5) : ");
        string noteSaisie = Console.ReadLine();
        int note = int.Parse(noteSaisie);
        db.NoterLivreDB(livreANoter.Id, note);
        Console.WriteLine("Livre noté avec succès !");
    }

    static void SupprimerLivre(Database db)
    {
        var livres = db.ObtenirLivres();
        AfficherListeLivres(db);
        Console.WriteLine("Entrez le numéro du livre que vous souhaitez supprimer : ");
        string saisie = Console.ReadLine();
        int numero = int.Parse(saisie);
        var LivreASupp = livres[numero - 1];
        Console.WriteLine($"Êtes-vous sûr de vouloir supprimer '{LivreASupp.Titre}' ? (O/N) : ");
        string validation = Console.ReadLine();
        switch (validation.ToUpper())
        {
            case "O":
                db.SupprimerLivreDB(LivreASupp.Id);
                Console.WriteLine("Livre supprimé avec succès !"); break;
            case "N":
                Console.WriteLine("Suppression annulée."); break;
        }
    }
}