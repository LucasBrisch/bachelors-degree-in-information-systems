import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        // Criando uma turma
        Turma turma = new Turma();

        // Criando 5 alunos com diferentes notas
        double[] notasAluno1 = {8.0, 7.5, 9.0, 6.0};
        double[] notasAluno2 = {5.5, 6.0, 5.0, 7.0};
        double[] notasAluno3 = {9.0, 8.5, 8.0, 9.5};
        double[] notasAluno4 = {4.0, 3.5, 5.0, 6.0};
        double[] notasAluno5 = {7.5, 8.0, 7.0, 6.5};

        Aluno aluno1 = new Aluno("Maria", 101, notasAluno1);
        Aluno aluno2 = new Aluno("João", 102, notasAluno2);
        Aluno aluno3 = new Aluno("Pedro", 103, notasAluno3);
        Aluno aluno4 = new Aluno("Ana", 104, notasAluno4);
        Aluno aluno5 = new Aluno("Carlos", 105, notasAluno5);

        // Adicionando os alunos à turma
        turma.Alunos.add(aluno1);
        turma.Alunos.add(aluno2);
        turma.Alunos.add(aluno3);
        turma.Alunos.add(aluno4);
        turma.Alunos.add(aluno5);

        // Apresentando os alunos e suas médias
        turma.ApresentarAlunos();

        // Calculando e exibindo a média da turma
        System.out.println("Média da turma: " + turma.CalcularMediaTurma());
    }
}


class Aluno {
    String nome;
    int matricula;
    double[] notas = new double[4];

    Aluno(String nome, int matricula, double[] notas) {
        this.nome = nome;
        this.matricula = matricula;
        this.notas = notas;
    }

    double CalcularMedia (){
        double media = 0;
        for(int i = 0; i<notas.length; i++){
            media += notas[i];
        }
        media = media/notas.length;
        return media;
    }
    boolean VerificarMedia(double media){
        if (CalcularMedia() >= 7){
            return true;
        } else {
            return false;
        }

    }
    void ApresentarAluno(){
        System.out.println("Nome: " + nome);
        System.out.println("Matricula: " + matricula);
        System.out.println("Média: " + CalcularMedia());
    }
}

class Turma {
    int NumeroTurma;
    ArrayList<Aluno> Alunos = new ArrayList<>();

    void ApresentarAlunos(){
        for (Aluno aluno : Alunos) {
            System.out.printf ("Nome: %s \n", aluno.nome);
            System.out.printf("Matricula: %d \n", aluno.matricula);
            System.out.printf("Média: %f\n", aluno.CalcularMedia());
            if (aluno.VerificarMedia(aluno.CalcularMedia())){
                System.out.printf("Aluno aprovado!\n");
            } else {
                System.out.printf("Aluno reprovado!\n");
            }
            System.out.println("-----------------\n");
        }
    }

    double CalcularMediaTurma () {
        double media = 0;
        for (Aluno aluno : Alunos) {
            media += aluno.CalcularMedia();
        }
        media = media/Alunos.size();
        return media;
    }
}
