public class Main {
    public static void main(String[] args) {
        Cachorro c1 = new Cachorro("totó");
        Gato g1 = new Gato("Garfield");
        c1.latir();
        g1.miar();
    }
}

class Animal {
    private String nome;
    private String raca;

    public Animal() {
        this.nome = "rex";
        this.raca = raca;
    }


    public Animal(String nome) {
        this.nome = nome;
        this.raca = raca;
    }

    public String getNome() {
        return nome;
    }

    public void caminhar (){
        System.out.printf("%s andou\n", this.nome);
    }
}

class Cachorro extends Animal{
     public Cachorro(String nome) {
         super(nome);
         super.caminhar();
     }

     public void latir () {
         System.out.printf("%s Latiu\n", super.getNome());
     }
}

class Gato extends Animal {
    public Gato(String nome) {
        super(nome);
    }

    public void miar () {
        System.out.printf("%s Miou\n", super.getNome());
    }
}

