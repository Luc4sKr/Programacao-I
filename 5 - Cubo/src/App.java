import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {

        Scanner sc = new Scanner(System.in);
        List<Cubo> cubos = new  ArrayList<>();

        System.out.printf("Quantos cubos quer criar? %n-> ");
        int nDeCubos = sc.nextInt();

        for (int i=0; i<nDeCubos; i++) {
            System.out.println("==============================");
            System.out.printf("Cubo %d%n", i+1);
            System.out.print("Altura: ");
            int altura = sc.nextInt();

            System.out.print("Largura: ");
            int largura = sc.nextInt();

            System.out.print("Profundidade: ");
            int profundidade = sc.nextInt();

            Cubo cubo = new Cubo(altura, largura, profundidade);
            cubos.add(cubo);
            System.out.println("Cubo adicionado");
            System.out.println("==============================");
        }

        int i = 1;
        System.out.println("==============================");
        for (Cubo cubo : cubos) {
            System.out.printf("%d - Cubo%n", i);
            System.out.printf("Altura: %d%n", cubo.getAltura());
            System.out.printf("Largura: %d%n", cubo.getLargura());
            System.out.printf("Profundidade: %d%n", cubo.getProfundidade());
            System.out.println("==============================");
            i++;
        }

        while (true) {
            System.out.print("Selecionar cubo ['0' para sair]: ");
            int cuboIndex = sc.nextInt();

            if (cuboIndex == 0) {
                break;
            }

            while (cuboIndex < 0 || cuboIndex > cubos.size()) {
                System.out.print("Valor inválido, digite novamente: ");
                cuboIndex = sc.nextInt();
            }

            Cubo cubo = cubos.get(cuboIndex-1);

            while (true) {
                System.out.printf("Cubo %d%n", cuboIndex);

                System.out.println("1 - Calcular área");
                System.out.println("2 - Calcular volume");
                System.out.println("3 - Sair");

                int resp = sc.nextInt();

                if (resp == 1) {
                    System.out.println("==============================");
                    System.out.printf("Área: %d%n", cubo.calcularArea());
                    System.out.println("==============================");
                } else {
                    if (resp == 2) {
                        System.out.println("==============================");
                        System.out.printf("Voume: %d%n", cubo.calcularVolume());
                        System.out.println("==============================");
                    } else {
                        if (resp == 3) {
                            break;
                        } else {
                            System.out.println("==============================");
                            System.out.println("Valor inválido");
                            System.out.println("==============================");
                        }
                    }
                }
            }
        }

        sc.close();

    }
}
