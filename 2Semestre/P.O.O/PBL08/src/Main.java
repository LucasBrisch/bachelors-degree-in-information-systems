import java.time.LocalDateTime;

public class Main {

    static void tentarsaque(Banco b, ContaCorrente c, int numero, String senha, double valor) {
        try {
            b.sacar(c, numero, senha, valor);
        } catch (SaldoInsuficiente e) {
            System.out.println(e.toString());
        } catch (SenhaInvalida e) {
            System.out.println(e.toString());
        } catch (ContaInvalida e) {
            System.out.println(e.toString());
        } catch (HorarioInvalido e) {
            System.out.println(e.toString());
        }
    }

    public static void main(String[] args) throws SaldoInsuficiente, SenhaInvalida, ContaInvalida, HorarioInvalido {
        Banco bradesco = new Banco("Bradesco");
        ContaCorrente c1 = bradesco.criarconta(1, "conta1", 100.00);
        ContaCorrente c2 = bradesco.criarconta(2, "conta2", 200.00);
        ContaCorrente c3 = bradesco.criarconta(3, "conta3", 300.00);
        ContaCorrente c4 = bradesco.criarconta(4, "conta4", 400.00);
        ContaCorrente c5 = bradesco.criarconta(5, "conta5", 500.00);

        // 10 operações de saque:
        tentarsaque(bradesco, c1, 1, "conta1", 90.00);  // Sucesso
        tentarsaque(bradesco, c1, 1, "conta1", 20.00);  // Saldo insuficiente
        tentarsaque(bradesco, c2, 2, "conta2", 100.00); // Sucesso
        tentarsaque(bradesco, c2, 2, "conta2", 150.00); // Sucesso
        tentarsaque(bradesco, c3, 3, "conta3", 500.00); // Saldo insuficiente
        tentarsaque(bradesco, c3, 3, "contaerrada", 50.00); // Senha inválida
        tentarsaque(bradesco, c4, 99, "conta4", 100.00); // Conta inválida
        tentarsaque(bradesco, c4, 4, "conta4", 200.00); // Sucesso
        tentarsaque(bradesco, c5, 5, "conta5", 400.00); // Sucesso
        tentarsaque(bradesco, c5, 5, "contaerrada", 100.00); // Senha inválida

        // Imprimindo os saldos finais das contas
        System.out.println("\nSaldos finais das contas:");
        System.out.println("Conta 1: R$ " + c1.getSaldo());
        System.out.println("Conta 2: R$ " + c2.getSaldo());
        System.out.println("Conta 3: R$ " + c3.getSaldo());
        System.out.println("Conta 4: R$ " + c4.getSaldo());
        System.out.println("Conta 5: R$ " + c5.getSaldo());
    }
}

class SaldoInsuficiente extends Exception {
    private double valor;

    public SaldoInsuficiente(double valor) {
        super();
        this.valor = valor;
    }

    public String toString() {
        return "não é possível sacar o valor de R$" + valor;
    }
}

abstract class Seguranca extends Exception {}

abstract class Autenticacao extends Seguranca {}

class SenhaInvalida extends Autenticacao {
    public String toString() {
        return "Senha inválida, o saque não foi concluído";
    }
}

class ContaInvalida extends Autenticacao {
    private int numeroConta;

    public ContaInvalida(int numeroConta) {
        this.numeroConta = numeroConta;
    }

    @Override
    public String toString() {
        return "A conta " + numeroConta + " não existe. Verifique o número da conta e tente novamente.";
    }
}

class HorarioInvalido extends Seguranca {
    private LocalDateTime horarioTentativa;

    public HorarioInvalido(LocalDateTime horarioTentativa) {
        this.horarioTentativa = horarioTentativa;
    }

    @Override
    public String toString() {
        return "No horário " + horarioTentativa.getHour() + ":" + horarioTentativa.getMinute() +
                " não é permitido realizar transações. O horário de atendimento é das 8h às 22h.";
    }
}

class Banco {
    private String nome;

    Banco(String nome) {
        this.nome = nome;
    }

    ContaCorrente criarconta(int numero, String senha, double saldo) {
        ContaCorrente x = new ContaCorrente(numero, senha, saldo);
        return x;
    }

    void sacar(ContaCorrente c, int numero, String senha, double valor) throws SaldoInsuficiente, SenhaInvalida, ContaInvalida, HorarioInvalido {
        LocalDateTime agora = LocalDateTime.now();

        if (numero != c.getNumero()) {
            throw new ContaInvalida(numero); // Passando o número da conta inválida
        }

        if (agora.getHour() < 8 || agora.getHour() > 22) {
            throw new HorarioInvalido(agora); // Passando o horário da tentativa
        }

        c.retirar(valor, senha);
    }

}

class ContaCorrente {
    private int numero;
    private String senha;
    private double saldo;

    ContaCorrente(int numero, String senha, double saldo) {
        this.numero = numero;
        this.senha = senha;
        this.saldo = saldo;
    }

    void retirar(double valor, String senha) throws SaldoInsuficiente, SenhaInvalida {
        if (valor > this.saldo) {
            throw new SaldoInsuficiente(valor);
        }
        if (!senha.equals(this.senha)) {
            throw new SenhaInvalida();
        }
        this.saldo -= valor;
        System.out.println("Saque na conta " + this.numero + " realizado com sucesso!");
    }

    public int getNumero() {
        return numero;
    }

    public double getSaldo() {
        return saldo;
    }
}

