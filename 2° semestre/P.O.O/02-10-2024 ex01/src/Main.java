public class Main {

    static void assar (Pizza x) {
        System.out.println("Assando uma pizza do sabor: ");
        x.mostrarmensagem();
    }

    static void assar (Pao x) {
        System.out.println("Assando uma pão do tipo: ");
        x.mostrarmensagem();
    }

    static void assar (Carne x) {
        System.out.println("Assando uma carne do tipo: ");
        x.mostrarmensagem();
    }

    public static void main(String[] args) {

        Pizza pi = new Pizza("Peperoni");
        Carne c = new Carne("Picanha");
        Pao p = new Pao("Brioche");

        assar(pi);
        assar(c);
        assar(p);

    }
}

class Pizza {
    private String sabor;

    Pizza(String sabor) {
        this.sabor = sabor;
    }

    void mostrarmensagem () {
        System.out.println(sabor);
    }
}

class Carne {
    private String corte;
    Carne(String corte) {
        this.corte = corte;
    }

    void mostrarmensagem () {
        System.out.println(corte);
    }
}

class Pao {
    String tipo;
    Pao(String tipo) {
        this.tipo = tipo;
    }

    void mostrarmensagem () {
        System.out.println(tipo);
    }
}

