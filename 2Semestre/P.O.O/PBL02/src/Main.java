import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Digite o valor do primeiro termo da PA: ");
        int a1 = input.nextInt();
        System.out.println("Digite o valor da razão da PA: ");
        int r = input.nextInt();
        System.out.println("Digite a quantidade de termos da PA: ");
        int n = input.nextInt();
        double a_n = a1 + (n-1) * r;
        System.out.println("O último termo da PA é: " + a_n);
        double S_n = (a1 + a_n) * n / 2;
        System.out.println("A soma dos termos da PA é: " + S_n);
    }
}