import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        Album skibiditoilet = new Album("Rock", "Skibidi", "2024", "SkibidiToilet");

        for (int i = 0; i < 5; i++){
            System.out.println("Escreva o nome da musica:");
            String nome = input.nextLine();
            System.out.println("Escreva o Duração: ");
            String ano = input.nextLine();
            Musica m = new Musica(nome, ano);
            skibiditoilet.musicas.add (m);
        }

        for (Musica m : Album.musicas ){
            System.out.printf("O titulo é: %s ", m.titulo());
            System.out.printf("A duração é: %s \n",m.duracao());
        }
    }
}

class Album {
    private String genero;
    private String nomeArtista;
    private String ano;
    private String nomeAlbum;
    static ArrayList <Musica> musicas = new ArrayList<Musica>();

    Album (String genero, String nomeArtista, String ano, String nomeAlbum){
        this.genero = genero;
        this.nomeArtista = nomeArtista;
        this.ano = ano;
        this.nomeAlbum = nomeAlbum;
    }
}

record Musica (String titulo, String duracao){
}