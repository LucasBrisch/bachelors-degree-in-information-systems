public class Main {
    public static void main(String[] args) {
        System.out.println(B.f(4,1));
    }
}
class B {
    static public int f(int a, int b) {
        int resultado = 0;

        if ( (a % 2 == 0) && (b % 2 == 1) ) {
            resultado = C.f(a, b);
        } else {
            resultado = C.f(b, a);
        }

        return resultado;
    }
}

class C {
    static public int f(int a, int b) {
        int resultado = 0;

        if (a < b) {
            resultado = b - a;
        } else {
            resultado = a * b;
        }

        return resultado;
    }
}
