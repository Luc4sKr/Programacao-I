import java.util.Scanner;
import java.util.ArrayList;
import java.util.List;

public class App {
    public static void main(String[] args) throws Exception {

        Scanner sc = new Scanner(System.in);
        List<Pessoa> pessoas = new ArrayList<>();
        
        while (true) {
            System.out.println("==================================");
            sc = new Scanner(System.in);
            System.out.print("Nome: ");
            String nome = sc.nextLine();

            if (nome.toUpperCase().equals("FIM")) {
                break;
            }

            System.out.print("Idade: ");
            Integer idade = sc.nextInt();

            sc = new Scanner(System.in);

            System.out.print("Cidade: ");
            String cidade = sc.nextLine();

            System.out.print("Bairro: ");
            String bairro = sc.nextLine();

            System.out.print("Rua: ");
            String rua = sc.nextLine();

            System.out.print("Número: ");
            Integer numero = sc.nextInt();

            Endereco endereco = new Endereco(cidade, bairro, rua, numero);
            Pessoa pessoa = new Pessoa(nome, idade, endereco);

            pessoas.add(pessoa);
            System.out.println("==================================");
        }

        Double mediaIdades = 0.0;
        for (Pessoa pessoa : pessoas) {
            mediaIdades += pessoa.idade;
            System.out.println("==================================");
            System.out.println(pessoa.exibeDados());
            System.out.println("==================================");
        }

        System.out.println("Média idades: " + mediaIdades / pessoas.size());


        System.out.println("Digite o nome de uma cidade: ");
        String cidade = sc.nextLine();

        int i = 0;
        for (Pessoa pessoa : pessoas) {
            if (pessoa.endereco.cidade.toUpperCase().equals(cidade.toUpperCase())) {
                i++;
            }
        }
        System.out.println("Quantidade de pessoas que moram na cidade " + cidade + ": " + i);
    }
}
