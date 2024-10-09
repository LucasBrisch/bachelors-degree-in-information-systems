import java.lang.reflect.Array;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        System.out.println("Hello world!");
    }
}

class Disco {
    private ArrayList<Pasta> pastas;
}

class Pasta {
    protected ArrayList<Arquivo> arquivos;
}

abstract class Arquivo {
}

class Compactado extends Arquivo {
    ArrayList<Compactado> compactados;
}

abstract class Documento extends Arquivo {

}

class Texto extends Documento {}

class Imagem extends Documento {}

class Som extends Documento {}

class Video extends Documento {}

class Planilha extends Documento {}

class Apresentacao extends Documento {}
