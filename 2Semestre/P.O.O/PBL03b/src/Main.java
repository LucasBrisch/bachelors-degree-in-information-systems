public class Main {
    public static void main(String[] args) {

        Funcionario jessica = new Funcionario(1, "Jessica", 25, "Senior");
        Funcionario cristiano = new Funcionario(2, "Cristiano Ronaldo", 19, "Junior");
        Funcionario humberto = new Funcionario(3, "Humberto", 22, "Pleno");

        System.out.println(jessica.info());
        System.out.println(cristiano.info());
        System.out.println(humberto.info());
    }
}

class Funcionario {
    private int id;
    private String nome;
    private int idade;
    private String cargo;
    private double salario;

    Funcionario(int id, String nome, int idade, String cargo) {
        this.id = id;
        this.nome = nome;
        this.idade = idade;
        this.cargo = cargo;
        if (cargo.equals("Junior")) {
            this.salario = 50000;
        } else if (cargo.equals("Senior")) {
            this.salario = 100000;
        } else if (cargo.equals("Pleno")) { // pode ser o == tb
            this.salario = 75000;
        } else {
            this.salario = 0;
        }
    }

    String info() {
        return String.format("Nome: %s\nID: %d\nIdade: %d\nCargo: %s\nSalário: %.2f\n\n", nome, id, idade, cargo, salario);
    }
}