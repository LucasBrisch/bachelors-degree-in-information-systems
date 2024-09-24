public class Main {
    public static void main(String[] args) {
        Imovelnovo casa = new Imovelnovo("Rua toilet", 900000.00);
        ImovelVelho apartamento = new ImovelVelho("Rua skibidi", 300000.00);

        casa.preco = casa.acrescimo();
        apartamento.preco = apartamento.decrescimo();

        System.out.printf("a casa da %s está custando %f ", casa.endereco, casa.preco);
        System.out.printf("o apartamento da %s está custando %f ", apartamento.endereco, apartamento.preco);
    }
}

class Imovel{
    String endereco;
    double preco;

    Imovel (String endereco, double preco){
        this.endereco = endereco;
        this.preco = preco;
    }

    Imovel () {
        this.endereco = "";
        this.preco = 0;
    }
}

class Imovelnovo extends Imovel {

    Imovelnovo (String endereco, double preco){
        super(endereco, preco);
    }

    double acrescimo (){
     double valor = super.preco * 1.10;
     return valor;
    }
}

class ImovelVelho extends Imovel{

    ImovelVelho (String endereco, double preco){
        super(endereco, preco);
    }

    double decrescimo () {
        double valor = super.preco * 0.9;
        return valor;
    }
}