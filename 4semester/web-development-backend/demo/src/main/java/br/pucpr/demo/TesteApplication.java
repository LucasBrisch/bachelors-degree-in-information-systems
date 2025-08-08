package br.pucpr.demo;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class TesteApplication {

	public static void main(String[] args) {
		SpringApplication.run(TesteApplication.class, args);
		contador.contador = 1;
		System.out.println("Contador: " + contador.contador);

		contador contadorA = new contador();
		contadorA.contador = 1;

		contador contadorB = new contador();
		contadorB.contador++;
		System.out.println("Contador: " + contador.contador);
	}

}

class contador {
	public static int contador;

	public int contadorObjeto;
}
