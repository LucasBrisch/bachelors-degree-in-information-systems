import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        ArrayList<String> cores = new ArrayList<String>();
        cores.add("Azul");
        cores.add("Verde");
        cores.add("Amarelo");
        cores.add("Marrom");
        cores.add("Branco");
        System.out.println("Menu: \n[1] Ordenado\n[2] Fora de ordem\n[9] Sair\nEscolha: ");
        int escolha = input.nextInt();

        if (escolha == 1) {
            Collections.sort(cores);
            for (int i = 0; i < cores.size(); i++) {
                System.out.println(cores.get(i));
            }
        } else if (escolha == 2) {
            for (int i = 0; i < cores.size(); i++) {
                System.out.println(cores.get(i));
            }
        } else if (escolha == 9) {
            System.out.println("Saindo...");
            System.exit(0);
        }
    }
}