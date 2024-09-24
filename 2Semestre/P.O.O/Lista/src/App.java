import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.Scanner;

public class App {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Informe o tamanho da lista: ");
        int tamanho = input.nextInt();

        List<Integer> lista = gerarListaAleatoria(tamanho);

        for (int numero : lista) {
            System.out.println("Número: " + numero);
            if (numero % 3 == 0) {
                System.out.println("É múltiplo de 3");
            }
            if (numero % 2 == 0) {
                System.out.println("É par");
            } else {
                System.out.println("É ímpar");
            }
        }
    }

    public static List<Integer> gerarListaAleatoria(int tamanho) {
        List<Integer> lista = new ArrayList<>();
        Random random = new Random();

        for (int i = 0; i < tamanho; i++) {
            lista.add(random.nextInt(100));
        }

        return lista;
    }
}