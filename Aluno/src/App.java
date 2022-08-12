import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        
        Scanner sc = new Scanner(System.in);
        List<Aluno> alunos = new  ArrayList<>();
        Double mediaTurma = 0.0;

        while (true) {
            System.out.println("Nome: ");
            String nome = sc.nextLine();

            if (nome.equals("FIM")) {
                sc.close();
                break;
            }

            System.out.print("CPF: ");
            String cpf = sc.nextLine();

            Aluno aluno = new Aluno(nome, cpf);

            System.out.print("Nota 1: ");
            aluno.nota1 = sc.nextDouble();
            System.out.print("Nota 2: ");
            aluno.nota2 = sc.nextDouble();
            System.out.print("Nota 3: ");
            aluno.nota3 = sc.nextDouble();

            System.out.printf("Nome: %s%n", nome);
            System.out.printf("CPF: %s%n", cpf);
            System.out.printf("Média: %f%n", aluno.CalcuarMedia());

            alunos.add(aluno);

        }

        for (Aluno aluno : alunos) {
            mediaTurma += aluno.CalcuarMedia();
        }

        System.out.printf("Média da turma: %f%n", mediaTurma);

    }
}
