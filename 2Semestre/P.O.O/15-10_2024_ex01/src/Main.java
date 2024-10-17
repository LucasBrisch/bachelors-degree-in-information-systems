public class Main {
    public static void main(String[] args) {
        int[] numeros = {4, 5, 8, 9, 20, 3, 4, 5};
        int[] div = {2, 4, 0, 8, 3, 0};
        int i;

        for (i = 0; i < numeros.length; i++) {
            try {
                System.out.println(numeros[i] + " / " + div[i] + " = " + (numeros[i] / div[i]));
            }
            catch (ArithmeticException e) {
                System.out.println("o divisor é um 0");
            }
            catch (ArrayIndexOutOfBoundsException e) {
                System.out.println("não existe um divisor");
            }
        }
    }
}
