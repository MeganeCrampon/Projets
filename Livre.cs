using System;

public class Livre
{
	public string Titre { get; set; }
	public string Auteur { get; set; }
	public string Genre { get; set; }
	public bool EstLu { get; set; } = false;

	public Livre(string titre, string auteur, string genre)
	{
		Titre = titre;
		Auteur = auteur;
		Genre = genre;
	}
}
