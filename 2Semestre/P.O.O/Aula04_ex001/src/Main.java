import java.util.ArrayList;
public class Main {
    public static void main(String[] args) {
        filme f1 = new filme(2013, "Sharknado");
        filme f2 = new filme(2018, "Guerra infinita");
        filme f3 = new filme(2010, "Como treinar o seu dragão");
        filme f4 = new filme(2013, "Meu malvado favorito 2");
        filme f5 = new filme(2015, "Minions");

        ArrayList<filme> listafilmes = new ArrayList<>();

        listafilmes.add(f1);
        listafilmes.add(f2);
        listafilmes.add(f3);
        listafilmes.add(f4);
        listafilmes.add(f5);

        for (int i = 0; i < listafilmes.size(); i++) {
            System.out.println(listafilmes.get(i).Titulo);
            System.out.println(listafilmes.get(i).AnoLancamento);
        }

    }
}


class filme {
    int AnoLancamento;
    String Titulo;
    public filme(int AnoLancamento, String Titulo) {
        this.AnoLancamento = AnoLancamento;
        this.Titulo = Titulo;
    };

}