public class Main {
    public static void main(String[] args) {
        // Criando objetos das classes e testando suas funções

        // Mamífero: Cachorro
        Cachorro cachorro = new Cachorro("Rex", 5, 4, "Marrom");
        cachorro.locomover();  // Rex andou
        cachorro.emitirSom();  // Rex Latiu
        cachorro.abanarrabo(); // Rex abanou o rabo
        cachorro.enterrarosso(); // Rex enterrou um osso
        cachorro.alimentar("ração"); // Rex comeu ração!

        // Mamífero: Canguru
        Canguru canguru = new Canguru("Jack", 3, 4, "Cinza");
        canguru.locomover();  // Jack pulou
        canguru.emitirSom();  // Jack fez sons de boxe
        canguru.usarbolsa();  // Jack usou a bolsa
        canguru.alimentar("grama"); // Jack comeu grama!

        // Réptil: Cobra
        Cobra cobra = new Cobra("Naja", 2, 0, "Verde");
        cobra.locomover();    // Naja rastejou
        cobra.emitirSom();    // Naja mexeu a linguinha
        cobra.morder();       // Naja mordeu
        cobra.alimentar("rato"); // Naja comeu rato!

        // Réptil: Tartaruga
        Tartaruga tartaruga = new Tartaruga("Leonardo", 100, 4, "Verde");
        tartaruga.locomover();  // Leonardo rastejou
        tartaruga.emitirSom();  // Leonardo não fez som
        tartaruga.alimentar("alface"); // Leonardo comeu alface!

        // Peixe: Peixe-palhaço
        Peixepalhaco nemo = new Peixepalhaco("Nemo", 1, 0, "Laranja");
        nemo.locomover();      // Nemo nadou
        nemo.emitirSom();      // Nemo não fez som
        nemo.soltarbolhas();   // Nemo soltou bolha
        nemo.alimentar("plâncton"); // Nemo comeu plâncton!

        // Peixe: Kynguyo
        Kynguyo kynguyo = new Kynguyo("Gold", 2, 0, "Dourada");
        kynguyo.locomover();   // Gold nadou
        kynguyo.emitirSom();   // Gold não fez som
        kynguyo.alimentar("algas"); // Gold comeu algas!

        // Ave: Galinha
        Galinha galinha = new Galinha("Pipoca", 1, 2, "Branca");
        galinha.locomover();   // Pipoca andou (a implementação está faltando)
        galinha.emitirSom();   // Pipoca cacarejou
        galinha.ciscar();      // Pipoca ciscou
        galinha.alimentar("milho"); // Pipoca comeu milho!

        // Ave: Arara
        Arara arara = new Arara("Azul", 5, 2, "Azul");
        arara.locomover();     // Azul andou (a implementação está faltando)
        arara.emitirSom();     // Azul fez piu-piu
        arara.serbonita();     // Azul é uma arara bonita
        arara.alimentar("frutas"); // Azul comeu frutas!
    }
}


abstract class Animal {
    protected String nome;
    protected int idade;
    protected int membros;

    Animal(String nome, int idade, int membros) {
        this.nome = nome;
        this.idade = idade;
        this.membros = membros;
    }

    abstract void locomover ();
    void alimentar(String alimento) {
        System.out.println(this.nome + " comeu " + alimento + "!");
    }
    abstract void emitirSom();
}

class Mamifero extends Animal {
    protected String corpelo;
    Mamifero(String nome, int idade, int membros, String corpelo) {
        super(nome, idade, membros);
        this.corpelo = corpelo;
    }

    void locomover() {
        System.out.println(this.nome + " andou");
    }
    void emitirSom() {}

}

class Reptil extends Animal {
    protected String corescama;
    Reptil(String nome, int idade, int membros, String corescama) {
        super(nome, idade, membros);
        this.corescama = corescama;
    }

    void locomover() {
        System.out.println(this.nome + " rastejou");
    }
    void emitirSom() {}
}

class Peixe extends Animal {
    protected String corescama;
    Peixe(String nome, int idade, int membros, String corescama) {
        super(nome, idade, membros);
        this.corescama = corescama;
    }
    void soltarbolhas() {
        System.out.println(this.nome + " soltou bolha");
    }

    void locomover() {
        System.out.println(this.nome + " nadou");
    }
    void emitirSom() {}
}

class Ave extends Animal {
    protected String corpena;
    Ave(String nome, int idade, int membros, String corpena) {
        super(nome, idade, membros);
        this.corpena = corpena;
    }

    void locomover() {}
    void emitirSom() {}
}

class Cachorro extends Mamifero {
    Cachorro(String nome, int idade, int membros, String corpelo) {
        super(nome, idade, membros, corpelo);
    }

    void enterrarosso() {
        System.out.println (this.nome + " enterrou um osso");
    }

    void abanarrabo() {
        System.out.println (this.nome + " abanou o rabo");
    }

    @Override
    void emitirSom () {
        System.out.println (this.nome + " Latiu");
    }
}

class Canguru extends Mamifero {
    Canguru(String nome, int idade, int membros, String corpelo) {
        super(nome, idade, membros, corpelo);
    }

    void usarbolsa () {
        System.out.println (this.nome + " usou a bolsa");
    }

    @Override
    void locomover (){
        System.out.println (this.nome + " pulou");
    }
    @Override
    void emitirSom () {
        System.out.println (this.nome + " fez sons de boxe");
    }
}

class Cobra extends Reptil {
    Cobra(String nome, int idade, int membros, String corescama) {
        super(nome, idade, membros, corescama);
    }

    void morder () {
        System.out.println (this.nome + " mordeu");
    }

    @Override
    void emitirSom () {
        System.out.println (this.nome + " mexeu a linguinha");
    }
}

class Tartaruga extends Reptil {
    Tartaruga(String nome, int idade, int membros, String corescama) {
        super(nome, idade, membros, corescama);
    }

    @Override
    void emitirSom () {
        System.out.println (this.nome + " não fez som");
    }

}

class Peixepalhaco extends Peixe {
    Peixepalhaco(String nome, int idade, int membros, String corescama) {
        super(nome, idade, membros, corescama);
    }

    }


class Kynguyo extends Peixe {
    Kynguyo(String nome, int idade, int membros, String corescama) {
        super(nome, idade, membros, corescama);
    }

    @Override
    void locomover () {
        System.out.println (this.nome + " nadou");
    }
}

class Galinha extends Ave {
    Galinha(String nome, int idade, int membros, String corpena) {
        super(nome, idade, membros, corpena);
    }

    void ciscar () {
        System.out.println (this.nome + " ciscou");
    }

    @Override
    void emitirSom () {
        System.out.println (this.nome + " Cacarejou");
    }
}

class Arara extends Ave {
    Arara(String nome, int idade, int membros, String corpena) {
        super(nome, idade, membros, corpena);
    }

    void serbonita () {
        System.out.println (this.nome + " é uma arara bonita");
    }

    @Override
    void emitirSom () {
        System.out.println (this.nome + " fez piu-piu");
    }
}