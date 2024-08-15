public class Main {
    public static void main(String[] args){
        Album Nevermind = new Album("Rock", 1991, "Nevermind", "Nirvana");

        Musica Smellliketeenspirit = new Musica("Smell Like Teen Spirit", 5.01);
        Musica Inbloom = new Musica("In Bloom", 4.15);
        Musica Commeasyouare = new Musica("Come As You Are", 3.39);
        Musica Breed = new Musica("Breed", 3.03);
        Musica Lithium = new Musica("Lithium", 4.17);

        Nevermind.musicas[0] = Smellliketeenspirit;
        Nevermind.musicas[1] = Inbloom;
        Nevermind.musicas[2] = Commeasyouare;
        Nevermind.musicas[3] = Breed;
        Nevermind.musicas[4] = Lithium;


        System.out.println("Album: " + Nevermind.nome + "\n" + "Ano: " + Nevermind.ano + "\n" + "Artista: " + Nevermind.artista + "\n" + "Genero: " + Nevermind.genero + "\n");
        for (Musica i : Nevermind.musicas) {
            System.out.println("Musica: " + i.titulo + "Duracao: " + i.duracao + "\n");
        }

        for (Musica i : Nevermind.musicas) {
            tocarMusica(i);

        }
    }

    static void tocarMusica(Musica musica) {
        System.out.println("Tocando: " + musica.titulo);
    }
}

class Album{
    String genero;
    int ano;
    String nome;
    Musica [] musicas = new Musica [5];
    String artista;

    Album (String genero, int ano, String nome, String artista) {
        this.genero = genero;
        this.ano = ano;
        this.nome = nome;
        this.artista = artista;
    }
}

class Musica {
    String titulo;
    Double duracao;

    Musica (String titulo, Double duracao) {
        this.titulo = titulo;
        this.duracao = duracao;
}
}

