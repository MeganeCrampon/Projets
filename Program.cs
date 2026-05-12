using System;
using System.Collections.Generic;
using System.Globalization;

class Program
{
    static void Main(string[] args)
    {
        List<Livre> livres = new List<Livre>();
        bool continuer = true;
        while (continuer)
        {
            AfficherMenu();
            string choix = Console.ReadLine();

            switch (choix)
            {
                case "1":
                    AfficherLivre(livres);
                    break;
                case "2":
                    AjouterLivre(livres);
                    break;
                case "3":
                    MarquerCommeLu(livres);
                    break;
                case "4":
                    SupprimerLivre(livres);
                    break;
                case "5":
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
        Console.WriteLine("4. Supprimer un livre");
        Console.WriteLine("5. Quitter");
        Console.Write("Votre choix : ");
    }

    static void AfficherLivre(List<Livre> livres)
    {
        Console.WriteLine("=== Liste de vos Livres ===");
        if (livres != null)
        {
            for (int i = 0; i < livres.Count; i++)
            {
                string statut = livres[i].EstLu ? "Lu" : "Non Lu";
                Console.WriteLine($"[{i + 1}] {livres[i].Titre} - {livres[i].Auteur} - {livres[i].Genre} - {statut}");
            }
        } 
        else 
        {
            Console.WriteLine("Aucun livre dans votre bibliothèque ! Voulez vous en ajouter un ? (O/N) : ");
            string validation = Console.ReadLine();
            switch (validation.ToUpper())
            {
                case "O":
                    AjouterLivre(livres);
                    break;
                case "N":
                    Console.WriteLine("Retour au menu principal.");
                    break;
            }
        }
    }
    static void AjouterLivre(List<Livre> livres)
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

        livres.Add(new Livre(titre, auteur, genre));
        Console.WriteLine("Livre ajouté avec succès !");
    }

    static void MarquerCommeLu(List<Livre> livres)
    {
        AfficherLivre(livres);
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
            livreLu.EstLu = true;
            Console.WriteLine($"Le livre '{livreLu.Titre}' a été marqué comme Lu !");
        }
    }

    static void SupprimerLivre(List<Livre> livres)
    {
        AfficherLivre(livres);
        Console.WriteLine("Entrez le numéro du livre que vous souhaitez supprimer : ");
        string saisie = Console.ReadLine();
        int numero = int.Parse(saisie);
        var LivreASupp = livres[numero - 1];
        Console.WriteLine($"Êtes-vous sûr de vouloir supprimer '{LivreASupp.Titre}' ? (O/N) : ");
        string validation = Console.ReadLine();
        switch (validation.ToUpper())
        {
            case "O":
                livres.Remove(LivreASupp);
                Console.WriteLine("Livre supprimé avec succès !"); break;
            case "N":
                Console.WriteLine("Suppression annulée."); break;
            }
    }
}