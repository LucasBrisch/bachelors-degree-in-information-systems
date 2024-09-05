import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        ContaCorrente cr1 = new ContaCorrente("Roberto", "123-321", 20000, "20-10-2005");
        ContaPoupanca cp1 = new ContaPoupanca("Silvia", "456-124", 16000, "10-01-2010");

        Banco santander = new Banco("Santander");

        santander.contas.add(cr1);
        santander.contas.add(cp1);




    }
}

class Banco {
    String nome;
    ArrayList <Conta> contas = new ArrayList();
    public Banco(String nome) {
        this.nome = nome;
    }
}

class Conta {
    String nome;
    String cumeroConta;
    double saldo;
    String Dataabertura;

    Conta (String nome, String cumeroConta, double saldo, String Dataabertura) {
        this.nome = nome;
        this.cumeroConta = cumeroConta;
        this.saldo = saldo;
        this.Dataabertura = Dataabertura;
    }

    void sacar (double saque) {
        saldo -= saque;

    }



}

class ContaPoupanca extends Conta {
    double taxa = 0.1;
    ContaPoupanca (String nome, String cumeroConta, double saldo, String Dataabertura) {
        super(nome, cumeroConta, saldo, Dataabertura);
    }

    void rendimento () {
        this.saldo += this.taxa * this.saldo;
    }

    void debitarRendimento (double valor) {
        if(valor <= this.saldo) {
            super.sacar(valor);
        } else {
            System.out.println("saldo insuficiente");
        }
    }
}

class ContaCorrente extends Conta {
    double taxaManutencao = 0.01;

    ContaCorrente (String nome, String cumeroConta, double saldo, String Dataabertura) {
        super(nome, cumeroConta, saldo, Dataabertura);
    }

    void debitotaxa () {
        this.saldo -= this.saldo * this.taxaManutencao;
    }

    void debitarCorrente (double valor) {
        if(valor <= this.saldo) {
            super.sacar(valor);
        } else {
            System.out.println("saldo insuficiente");
        }
    }
}