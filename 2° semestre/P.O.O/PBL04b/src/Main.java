
import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String devolvealuga = "aluga";
        ArrayList<livro> livros_alugados = new ArrayList<>();

        Prateleira p1_1 = new Prateleira(1, 1);
        Prateleira p2_1 = new Prateleira(2, 1);
        Prateleira p1_2 = new Prateleira(1, 2);
        Prateleira p2_2 = new Prateleira(2, 2);

        Biblioteca b1 = new Biblioteca();
        Biblioteca b2 = new Biblioteca();

        livro l1 = new livro(1, "titulo1", "editora1", "autor1", 60, false);
        livro l2 = new livro(2, "titulo2", "editora2", "autor2", 70, false);
        livro l3 = new livro(3, "titulo3", "editora3", "autor3", 80, false);
        livro l4 = new livro(4, "titulo4", "editora4", "autor4", 90, false);
        livro l5 = new livro(5, "titulo5", "editora5", "autor5", 100, false);
        livro l6 = new livro(6, "titulo6", "editora6", "autor6", 110, false);
        livro l7 = new livro(7, "titulo7", "editora7", "autor7", 120, false);
        livro l8 = new livro(8, "titulo8", "editora8", "autor8", 130, false);
        livro l9 = new livro(9, "titulo9", "editora9", "autor9", 140, false);
        livro l10 = new livro(10, "titulo10", "editora10", "autor10", 150, false);
        livro l11 = new livro(11, "titulo11", "editora11", "autor11", 160, false);
        livro l12 = new livro(12, "titulo12", "editora12", "autor12", 170, false);

        p1_1.livros.add(l1);
        p1_1.livros.add(l2);
        p1_1.livros.add(l3);
        p1_2.livros.add(l4);
        p1_2.livros.add(l5);
        p1_2.livros.add(l6);
        p2_1.livros.add(l7);
        p2_1.livros.add(l8);
        p2_1.livros.add(l9);
        p2_2.livros.add(l10);
        p2_2.livros.add(l11);
        p2_2.livros.add(l12);
        b1.prateleiras.add(p1_1);
        b1.prateleiras.add(p2_1);
        b1.prateleiras.add(p1_2);
        b1.prateleiras.add(p2_2);

        while (true) {
            System.out.println("você vai alugar ou devolver um livro?\nAlugar [1]\nDevolver [2]\nAcessar informações dos livros alugados [3]\n");
            int opcao = input.nextInt();
            if (opcao == 1) {
                devolvealuga = "aluga";
            } else if (opcao == 2) {
                devolvealuga = "devolve";
            } else if (opcao == 3) {
                devolvealuga = "ver";
            }
            if (devolvealuga == "aluga") {
                System.out.println("Para qual biblioteca vc vai?");
                int bibliotecas = input.nextInt();
                if (bibliotecas == 1) {
                    System.out.println("Qual prateleira você quer acessar?");
                    System.out.printf("Prateleira 1: %s, %s, %s \n", p1_1.livros.get(0).titulo, p1_1.livros.get(1).titulo, p1_1.livros.get(2).titulo);
                    System.out.printf("Prateleira 2: %s, %s, %s \n", p2_1.livros.get(0).titulo, p2_1.livros.get(1).titulo, p2_1.livros.get(2).titulo);
                    int prateleira = input.nextInt();
                    if (prateleira == 1) {
                        System.out.println("Qual livro você quer alugar?");
                        System.out.println(p1_1.livros.get(0).titulo);
                        System.out.println(p1_1.livros.get(1).titulo);
                        System.out.println(p1_1.livros.get(2).titulo);
                        int livro = input.nextInt();
                        if (livro == 1) {
                            if (p1_1.livros.get(0).alugado == true) {
                                System.out.println("O livro ja está alugado");
                            } else {
                                System.out.println("Livro alugado com sucesso");
                                p1_1.livros.get(0).alugado = true;
                                livros_alugados.add(p1_1.livros.get(0));
                            }

                        } else if (livro == 2) {
                            if (p1_1.livros.get(1).alugado == true) {
                                System.out.println("O livro ja está alugado");
                            } else {
                                System.out.println("Livro alugado com sucesso");
                                p1_1.livros.get(1).alugado = true;
                                livros_alugados.add(p1_1.livros.get(1));
                            }

                        } else if (livro == 3) {
                            if (p1_1.livros.get(2).alugado == true) {
                                System.out.println("O livro ja está alugado");
                            } else {
                                System.out.println("Livro alugado com sucesso");
                                p1_1.livros.get(2).alugado = true;
                                livros_alugados.add(p1_1.livros.get(2));
                            }
                        }

                    } else if (prateleira == 2) {
                        System.out.println("Qual livro você quer alugar?");
                        System.out.println(p2_1.livros.get(0).titulo);
                        System.out.println(p2_1.livros.get(1).titulo);
                        System.out.println(p2_1.livros.get(2).titulo);
                        int livro = input.nextInt();
                        if (livro == 1) {
                            if (p2_1.livros.get(0).alugado == true) {
                                System.out.println("O livro ja  está alugado");
                            } else {
                                System.out.println("Livro alugado com sucesso");
                                p2_1.livros.get(0).alugado = true;
                                livros_alugados.add(p2_1.livros.get(0));
                            }
                        } else if (livro == 2) {
                            if (p2_1.livros.get(1).alugado == true) {
                                System.out.println("O livro ja  está alugado");
                            } else {
                                System.out.println("Livro alugado com sucesso");
                                p2_1.livros.get(1).alugado = true;
                                livros_alugados.add(p2_1.livros.get(1));
                            }
                        } else if (livro == 3) {
                            if (p2_1.livros.get(2).alugado == true) {
                                System.out.println("O livro ja  está alugado");
                            } else {
                                System.out.println("Livro alugado com sucesso");
                                p2_1.livros.get(2).alugado = true;
                                livros_alugados.add(p2_1.livros.get(2));
                            }
                        }

                    }
                } else if (bibliotecas == 2) {

                    System.out.println("Qual prateleira você quer acessar?");
                    System.out.printf("Prateleira 1: %s, %s, %s \n", p1_2.livros.get(0).titulo, p1_2.livros.get(1).titulo, p1_2.livros.get(2).titulo);
                    System.out.printf("Prateleira 2: %s, %s, %s \n", p2_2.livros.get(0).titulo, p2_2.livros.get(1).titulo, p2_2.livros.get(2).titulo);
                    int prateleira = input.nextInt();
                    if (prateleira == 1) {
                        System.out.println("Qual livro você quer alugar?");
                        System.out.println(p1_2.livros.get(0).titulo);
                        System.out.println(p1_2.livros.get(1).titulo);
                        System.out.println(p1_2.livros.get(2).titulo);
                        int livro = input.nextInt();
                        if (livro == 1) {
                            if (p1_2.livros.get(0).alugado == true) {
                                System.out.println("O livro ja está alugado");
                            } else {
                                System.out.println("Livro alugado com sucesso");
                                p1_2.livros.get(0).alugado = true;
                                livros_alugados.add(p1_2.livros.get(0));
                            }

                        } else if (livro == 2) {
                            if (p1_2.livros.get(1).alugado == true) {
                                System.out.println("O livro ja está alugado");
                            } else {
                                System.out.println("Livro alugado com sucesso");
                                p1_2.livros.get(1).alugado = true;
                                livros_alugados.add(p1_2.livros.get(1));
                            }

                        } else if (livro == 3) {
                            if (p1_2.livros.get(1).alugado == true) {
                                System.out.println("O livro ja está alugado");
                            } else {
                                System.out.println("Livro alugado com sucesso");
                                p1_2.livros.get(2).alugado = true;
                                livros_alugados.add(p1_2.livros.get(2));
                            }
                        }
                    } else {
                        System.out.println("Qual livro você quer alugar?");
                        System.out.println(p2_2.livros.get(0).titulo);
                        System.out.println(p2_2.livros.get(1).titulo);
                        System.out.println(p2_2.livros.get(2).titulo);
                        int livro = input.nextInt();
                        if (livro == 1) {
                            if (p2_2.livros.get(0).alugado == true) {
                                System.out.println("O livro ja  está alugado");
                            } else {
                                System.out.println("Livro alugado com sucesso");
                                p2_2.livros.get(0).alugado = true;
                                livros_alugados.add(p2_2.livros.get(0));
                            }
                        } else if (livro == 2) {
                            if (p2_2.livros.get(1).alugado == true) {
                                System.out.println("O livro ja  está alugado");
                            } else {
                                System.out.println("Livro alugado com sucesso");
                                p2_2.livros.get(1).alugado = true;
                                livros_alugados.add(p2_2.livros.get(1));
                            }
                        } else if (livro == 3) {
                            if (p2_2.livros.get(2).alugado == true) {
                                System.out.println("O livro ja  está alugado");
                            } else {
                                System.out.println("Livro alugado com sucesso");
                                p2_2.livros.get(1).alugado = true;
                                livros_alugados.add(p2_2.livros.get(1));
                            }
                        }

                    }

                }
            } else if (devolvealuga == "devolve") {

                if (livros_alugados.size() == 0) {
                    System.out.println("Você não tem nenhum livro alugado");
                } else {
                    System.out.println("Qual livro você quer devolver? \n ");
                    for (int i = 0; i < livros_alugados.size(); i++) {
                        System.out.printf("%s [%x] \n", livros_alugados.get(i).titulo, i + 1);
                    }
                    System.out.println();
                    int livro_devolvido = input.nextInt();
                    if (livro_devolvido < livros_alugados.size() + 1) {
                        livros_alugados.get(livro_devolvido - 1).alugado = false;
                        livros_alugados.remove(livro_devolvido - 1);
                        System.out.println("Livro devolvido com sucesso!");
                    } else {
                        System.out.println("Opção invalida, tente novamente");
                    }
                }

            } else if (devolvealuga == "ver") {

                if (livros_alugados.size() == 0) {
                    System.out.println("Você não tem nenhum livro alugado");
                } else {
                    System.out.println("Você quer ver as informações de qual livro?\n");
                    for (int i = 0; i < livros_alugados.size(); i++) {
                        System.out.printf("%s [%x] \n", livros_alugados.get(i).titulo, i + 1);
                    }
                    System.out.println();
                    int livro_ver = input.nextInt();
                    if (livro_ver < livros_alugados.size() + 1) {
                        livros_alugados.get(livro_ver - 1).getinfo(livros_alugados.get(livro_ver - 1));
                    } else {
                        System.out.println("Opção invalida, tente novamente");
                    }
                }

            }
        }
    }
}

class livro {

    int id;
    String titulo;
    String editora;
    String autor;
    int pgs;
    boolean alugado;

    livro(int id, String titulo, String editora, String autor, int pgs, boolean alugado) {
        this.id = id;
        this.titulo = titulo;
        this.editora = editora;
        this.autor = autor;
        this.pgs = pgs;
        this.alugado = alugado;
    }

    void getinfo(livro l) {

        System.out.printf("Id: %x\nTitulo: %s\nAutor: %S\nPáginas:%x \n", l.id, l.titulo, l.autor, l.pgs);

    }
}

class Prateleira {

    ArrayList<livro> livros = new ArrayList<>();
    private int numero;
    private int biblioteca;

    Prateleira(int numero, int biblioteca) {
        this.numero = numero;
        this.biblioteca = biblioteca;
    }
}

class Biblioteca {

    ArrayList prateleiras = new ArrayList<>();
}
