import java.util.Scanner;
import java.util.ArrayList;

public class Main {
    static ArrayList<Pessoa> pessoas = new ArrayList<>();
    static Pessoa atual;

    static boolean encontrar(String pessoa) {
        for (Pessoa p : pessoas) {
            if (p.pegarnome().equals(pessoa)){
                atual = p;
                return true;
            }
        } return false;
    }

    public static void main(String[] args) {


        // Criação de alunos
        Aluno aluno1 = new Aluno("Pedro", 20, "pedro@gmail.com", "2023001", "Engenharia");
        Aluno aluno2 = new Aluno("Ana", 22, "ana@gmail.com", "2023002", "Medicina");

        // Criação de professores
        Professor professor1 = new Professor("Carlos", 45, "carlos@gmail.com", "Matemática", 5000.00);
        Professor professor2 = new Professor("Fernanda", 50, "fernanda@gmail.com", "História", 6000.00);

        // Criação de funcionários
        Funcionario funcionario1 = new Funcionario("Marcos", 40, "marcos@gmail.com", "Administração", 160, 30.00);
        Funcionario funcionario2 = new Funcionario("Julia", 35, "julia@gmail.com", "Manutenção", 150, 25.00);

        // Criação de monitores
        Monitor monitor1 = new Monitor("Lucas", 21, "lucas@gmail.com", "2023003", "Biologia", 10);
        Monitor monitor2 = new Monitor("Sara", 23, "sara@gmail.com", "2023004", "Química", 12);

        Scanner input = new Scanner(System.in);


        pessoas.add(aluno1);
        pessoas.add(aluno2);
        pessoas.add(professor1);
        pessoas.add(professor2);
        pessoas.add(monitor1);
        pessoas.add(monitor2);
        pessoas.add(funcionario1);
        pessoas.add(funcionario2);


        while (true) {
            System.out.println("Digite o nome da pessoa que você quer encontrar: ");
            String pessoa = input.nextLine();
            if (encontrar(pessoa)) {
                atual.apresentar();
            } else {
                System.out.println("Essa pessoa não existe!");
            }
        }
    }

}


class Pessoa {
     String nome;
     int idade;
     String email;


    Pessoa(String nome, int idade, String email) {
        this.nome = nome;
        this.idade = idade;
        this.email = email;

    }

    void apresentar () {
        System.out.println("Nome: " + nome);
        System.out.println("Idade: " + idade);
        System.out.println("E-mail: " + email);
    }

    String pegarnome () {
        return this.nome;
    }

    int pegaridade () {
        return this.idade;
    }

    String pegaremail () {
        return this.email;
    }


}


class Aluno extends Pessoa {
    String matricula;
    String curso;
    Aluno(String nome, int idade, String email, String matricula, String curso) {
        super(nome, idade, email);
        this.matricula = matricula;
        this.curso = curso;
    }

    void apresentar () {
        System.out.println("Nome: " + nome);
        System.out.println("Idade: " + idade);
        System.out.println("E-mail: " + email);
        System.out.println("Matricula: " + matricula);
        System.out.println("Curso: " + curso);
    }

}

class Professor extends Pessoa {
    String materia;
    double salario;
    Professor(String nome, int idade, String email, String matricula, double curso) {
        super(nome, idade, email);
        this.materia = matricula;
        this.salario = curso;
    }

    void apresentar () {
        System.out.println("Nome: " + nome);
        System.out.println("Idade: " + idade);
        System.out.println("E-mail: " + email);
        System.out.println("Matéria: " + materia);
        System.out.printf("Salário: %f", salario);
    }

    double calcularbonus (){
        double valor = this.salario * 1.1;
        return valor;
    }

}

class Funcionario extends Pessoa {
    private String departamento;
    int horas_trabalhadas;
    double salario_hora;

    Funcionario (String nome, int idade, String email, String depto, int horas, double sal_hora){
        super(nome, idade, email);
        this.departamento = depto;
        this.horas_trabalhadas = horas;
        this.salario_hora = sal_hora;
    }

    double calcular_pagamento (){
        double valor = this.salario_hora * horas_trabalhadas;
        return valor;
    }
    void apresentar () {
        System.out.println("Nome: " + nome);
        System.out.println("Idade: " + idade);
        System.out.println("E-mail: " + email);
        System.out.println("Departamento: " + departamento);
        System.out.printf("Salário: %f", salario_hora);
    }
}

class Monitor extends Aluno {
    int horas_monitorias;
    Monitor(String nome, int idade, String email, String matricula, String curso, int horas_monitorias) {
        super (nome, idade, email, matricula, curso);
        this.horas_monitorias = horas_monitorias;
    }

    void apresentar () {
        System.out.println("Nome: " + nome);
        System.out.println("Idade: " + idade);
        System.out.println("E-mail: " + email);
        System.out.println("Matricula: " + matricula);
        System.out.println("Curso: " + curso);
        System.out.println("Horas monitorias: " + horas_monitorias);
    }
}