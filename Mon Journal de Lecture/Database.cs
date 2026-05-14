using System;
using System.Collections.Generic;
using Microsoft.Data.Sqlite;

public class Database
{
    private static readonly string Connection = "Data Source=C:\\Users\\megan\\Desktop\\Code\\PROJETS\\Mon Journal de Lecture\\livres.db";
    public void InitDB()
    {
        Console.WriteLine($"Chemin DB : {Connection}");
        using var connexion = new SqliteConnection(Connection);
        connexion.Open();

        string request = @"CREATE TABLE IF NOT EXISTS Livres (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            TITRE TEXT NOT NULL,
            AUTEUR TEXT NOT NULL,
            GENRE TEXT NOT NULL,
            EST_LU INTEGER NOT NULL DEFAULT 0,
            NOTE INTEGER NULL DEFAULT NULL
        )";

        var commande = connexion.CreateCommand();
        commande.CommandText = request;
        commande.ExecuteNonQuery();
    }

    public List<Livre> ObtenirLivres()
    {
        using var connexion = new SqliteConnection(Connection);
        connexion.Open();

        string request = "SELECT * FROM Livres";

        var commande = connexion.CreateCommand();
        commande.CommandText = request;

        var livres = new List<Livre>();

        using var cursor = commande.ExecuteReader();
        while (cursor.Read())
        {
            livres.Add(new Livre(
                cursor["TITRE"].ToString(),
                cursor["AUTEUR"].ToString(),
                cursor["GENRE"].ToString()
            )
            {
                Id = Convert.ToInt32(cursor["ID"]),
                EstLu = Convert.ToInt32(cursor["EST_LU"]) == 1,
                Note = cursor["NOTE"] == DBNull.Value? (int?)null : Convert.ToInt32(cursor["NOTE"])
            });
        }
        return livres;
    }

    public void AjouterLivreDB(Livre livre)
    {
        using var connexion = new SqliteConnection(Connection);
        connexion.Open();

        string request = "INSERT INTO Livres (TITRE, AUTEUR, GENRE, EST_LU, NOTE) VALUES (@titre, @auteur, @genre, @estLu, @note)";

        var commande = connexion.CreateCommand();
        commande.CommandText = request;

        commande.Parameters.AddWithValue("@titre", livre.Titre);
        commande.Parameters.AddWithValue("@auteur", livre.Auteur);
        commande.Parameters.AddWithValue("@genre", livre.Genre);
        commande.Parameters.AddWithValue("@estLu", livre.EstLu ? 1 : 0);
        commande.Parameters.AddWithValue("@note", livre.Note.HasValue ? (object)livre.Note.Value : DBNull.Value);

        commande.ExecuteNonQuery();
    }

    public void ChangerStatutDB(int id, bool estLu)
    {
        using var connexion = new SqliteConnection(Connection);
        connexion.Open();

        string request = "UPDATE Livres SET EST_LU = @estLu WHERE ID = @id";

        var commande = connexion.CreateCommand();
        commande.CommandText = request;

        commande.Parameters.AddWithValue("@estLu", estLu ? 1 : 0);
        commande.Parameters.AddWithValue("@id", id);

        commande.ExecuteNonQuery();
    }

    public void NoterLivreDB(int id, int note)
    {
        using var connexion = new SqliteConnection(Connection);
        connexion.Open();

        string request = "UPDATE Livres SET NOTE = @note WHERE ID = @id";

        var commande = connexion.CreateCommand();
        commande.CommandText = request;

        commande.Parameters.AddWithValue("@note", note);
        commande.Parameters.AddWithValue("@id", id);

        commande.ExecuteNonQuery();
    }

    public void SupprimerLivreDB(int id)
    {
        using var connexion = new SqliteConnection(Connection);
        connexion.Open();

        string request = "DELETE FROM Livres WHERE ID = @id";

        var commande = connexion.CreateCommand();
        commande.CommandText = request;

        commande.Parameters.AddWithValue("@id", id);

        commande.ExecuteNonQuery();
    }
}