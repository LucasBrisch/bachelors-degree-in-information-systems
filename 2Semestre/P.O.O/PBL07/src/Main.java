public class Main {
    public static void main(String[] args) {
        Batman batman = new Batman(true, 0, 0, 0, 1);
        batman.correr(1, 1);
        batman.saltar(2);
        batman.atirar();
        batman.camufla(2);
        batman.morrer();

        JamesBond jamesBond = new JamesBond(true, 0, 0, 0, 2);
        jamesBond.correr(1, 1);
        jamesBond.saltar(2);
        jamesBond.atirar();
        jamesBond.morrer();

        GoldFinger goldFinger = new GoldFinger(true, 0, 0, 0, 3, batman);
        goldFinger.correr(1, 1);
        goldFinger.saltar(2);
        goldFinger.atirar();
        goldFinger.personifica(jamesBond);
        goldFinger.morrer();

        DrNo drNo = new DrNo(true, 0, 0, 0, 5);
        drNo.correr(1, 1);
        drNo.saltar(2);
        drNo.atirar();
        drNo.morrer();

        Coringa coringa = new Coringa(true, 0, 0, 0, 6);
        coringa.correr(1, 1);
        coringa.saltar(2);
        coringa.atirar();
        coringa.morrer();

        Penguin pinguim = new Penguin(true, 0, 0, 0, 7);
        pinguim.correr(1, 1);
        pinguim.saltar(2);
        pinguim.atirar();
        pinguim.morrer();
    }
}

abstract class Personagem {
    protected boolean vivo;
    protected float posicao_x;
    protected float posicao_y;
    protected float posicao_z;
    int cor;

    Personagem(boolean vivo, float posicao_x, float posicao_y, float posicao_z, int cor) {
        this.vivo = vivo;
        this.posicao_x = posicao_x;
        this.posicao_y = posicao_y;
        this.posicao_z = posicao_z;
        this.cor = cor;
    }

    abstract void correr(float x, float y);
    abstract void saltar(float z);
    abstract void atirar();
    abstract void morrer();
}

abstract class Heroi extends Personagem {
    Heroi(boolean vivo, float posicao_x, float posicao_y, float posicao_z, int cor) {
        super(vivo, posicao_x, posicao_y, posicao_z, cor);
    }

    @Override
    abstract void correr(float x, float y);

    @Override
    abstract void saltar(float z);

    @Override
    abstract void atirar();

    @Override
    void morrer() {
        this.vivo = false;
        System.out.println(this.getClass().getSimpleName() + " morreu.");
    }
}

abstract class Vilao extends Personagem {
    Vilao(boolean vivo, float posicao_x, float posicao_y, float posicao_z, int cor) {
        super(vivo, posicao_x, posicao_y, posicao_z, cor);
    }

    @Override
    abstract void correr(float x, float y);

    @Override
    abstract void atirar();

    @Override
    void morrer() {
        this.vivo = false;
        System.out.println(this.getClass().getSimpleName() + " morreu.");
    }
}

abstract class Ladrao extends Vilao {
    Ladrao(boolean vivo, float posicao_x, float posicao_y, float posicao_z, int cor) {
        super(vivo, posicao_x, posicao_y, posicao_z, cor);
    }

    @Override
    abstract void saltar(float z);
}

abstract class Terrorista extends Vilao {
    Terrorista(boolean vivo, float posicao_x, float posicao_y, float posicao_z, int cor) {
        super(vivo, posicao_x, posicao_y, posicao_z, cor);
    }

    @Override
    abstract void atirar();
}

interface Camuflagem {
    void camufla(int cor);
}

interface Personificacao extends Camuflagem {
    void personifica(Heroi h);
}

class Batman extends Heroi implements Camuflagem {
    Batman(boolean vivo, float posicao_x, float posicao_y, float posicao_z, int cor) {
        super(vivo, posicao_x, posicao_y, posicao_z, cor);
    }

    @Override
    void correr(float x, float y) {
        this.posicao_x = x;
        this.posicao_y = y;
        System.out.println("Batman correndo ...");
    }

    @Override
    void saltar(float z) {
        this.posicao_z = z;
        System.out.println("Batman saltando ...");
    }

    @Override
    void atirar() {
        System.out.println("Batman atirando ...");
    }

    @Override
    public void camufla(int cor) {
        this.cor = cor;
        System.out.println("Batman camuflando ...");
    }
}

class JamesBond extends Heroi {
    JamesBond(boolean vivo, float posicao_x, float posicao_y, float posicao_z, int cor) {
        super(vivo, posicao_x, posicao_y, posicao_z, cor);
    }

    @Override
    void correr(float x, float y) {
        this.posicao_x = x;
        this.posicao_y = y;
        System.out.println("JamesBond correndo ...");
    }

    @Override
    void saltar(float z) {
        this.posicao_z = z;
        System.out.println("JamesBond saltando ...");
    }

    @Override
    void atirar() {
        System.out.println("JamesBond atirando ...");
    }
}

class GoldFinger extends Terrorista implements Personificacao {
    Heroi heroi;

    GoldFinger(boolean vivo, float posicao_x, float posicao_y, float posicao_z, int cor, Heroi heroi) {
        super(vivo, posicao_x, posicao_y, posicao_z, cor);
        this.heroi = heroi;
    }

    @Override
    void correr(float x, float y) {
        this.posicao_x = x;
        this.posicao_y = y;
        System.out.println("GoldFinger correndo ...");
    }

    @Override
    void saltar(float z) {
        this.posicao_z = z;
        System.out.println("GoldFinger saltando ...");
    }

    @Override
    void atirar() {
        System.out.println("GoldFinger atirando ...");
    }

    @Override
    void morrer() {
        this.vivo = false;
        System.out.println(this.getClass().getSimpleName() + " morreu.");
    }

    @Override
    public void camufla(int cor) {}

    @Override
    public void personifica(Heroi h) {
        this.heroi = h;
        System.out.println("Personificando");
    }
}

class DrNo extends Terrorista {
    DrNo(boolean vivo, float posicao_x, float posicao_y, float posicao_z, int cor) {
        super(vivo, posicao_x, posicao_y, posicao_z, cor);
    }

    @Override
    void correr(float x, float y) {
        this.posicao_x = x;
        this.posicao_y = y;
        System.out.println("DrNo correndo ...");
    }

    @Override
    void saltar(float z) {
        this.posicao_z = z;
        System.out.println("DrNo saltando ...");
    }

    @Override
    void atirar() {
        System.out.println("DrNo atirando ...");
    }

    @Override
    void morrer() {
        this.vivo = false;
        System.out.println(this.getClass().getSimpleName() + " morreu.");
    }
}

class Coringa extends Ladrao {
    Coringa(boolean vivo, float posicao_x, float posicao_y, float posicao_z, int cor) {
        super(vivo, posicao_x, posicao_y, posicao_z, cor);
    }

    @Override
    void correr(float x, float y) {
        this.posicao_x = x;
        this.posicao_y = y;
        System.out.println("Coringa correndo ...");
    }

    @Override
    void saltar(float z) {
        this.posicao_z = z;
        System.out.println("Coringa saltando ...");
    }

    @Override
    void atirar() {
        System.out.println("Coringa atirando ...");
    }

    @Override
    void morrer() {
        this.vivo = false;
        System.out.println(this.getClass().getSimpleName() + " morreu.");
    }
}

class Penguin extends Ladrao {
    Penguin(boolean vivo, float posicao_x, float posicao_y, float posicao_z, int cor) {
        super(vivo, posicao_x, posicao_y, posicao_z, cor);
    }

    @Override
    void correr(float x, float y) {
        this.posicao_x = x;
        this.posicao_y = y;
        System.out.println("Pinguim correndo ...");
    }

    @Override
    void saltar(float z) {
        this.posicao_z = z;
        System.out.println("Pinguim saltando ...");
    }

    @Override
    void atirar() {
        System.out.println("Pinguim atirando ...");
    }

    @Override
    void morrer() {
        this.vivo = false;
        System.out.println(this.getClass().getSimpleName() + " morreu.");
    }
}
