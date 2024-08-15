public class Banco {
    public static void main(String[] args) {

        Cliente c1 = new Cliente("Jandira Silva", 2500.00);
        Cliente c2 = new Cliente("Sandra Rodrigues,", 1800.00);
        Cliente c3 = new Cliente("Luciana Teixeira,", 5000.00);


        System.out.println(c1.info());
        System.out.println(c2.info());
        System.out.println(c3.info());

        c1.retirada(1000);
        System.out.println (c1.info());

        c2.retirada (2000);
        c2.deposito (500);
        System.out.println(c2.info());

        c2.retirada(2000);
        System.out.println(c2.info());

        c3.deposito(1000);
        System.out.println(c3.info());



    }
}

class Cliente {
    String nome;
    double saldo;

    Cliente (String nome, Double saldo) {
        this.nome = nome;
        this.saldo = saldo;
    }

    void deposito (double quantidade) {
        saldo += quantidade;
    }

    void retirada (double saque) {
        saldo -= saque;
    }

    String info () {
        return ("Seu nome é: "+ nome + "\nSeu saldo é de: R$"+ saldo);
    }
}