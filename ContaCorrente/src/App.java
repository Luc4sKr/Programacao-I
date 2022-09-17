import java.util.Scanner;
import java.util.ArrayList;
import java.util.List;

public class App {
    public static void main(String[] args) throws Exception {

        Scanner sc = new Scanner(System.in);
        List<ContaCorrente> contas = new ArrayList<>();

        String numeroConta = "";
        Double saldoCliente;
        String nomeCliente, saldoClienteSTR = "", cpfCliente;


        while (true) {
            System.out.print("Número da conta: ");
            numeroConta = sc.nextLine();

            if (numeroConta.equals("0")) {
                break;
            }

            System.out.print("Saldo: ");
            saldoClienteSTR = sc.nextLine();
            saldoCliente = Double.valueOf(saldoClienteSTR).doubleValue();
            
            System.out.print("Nome: ");
            nomeCliente = sc.nextLine();

            System.out.print("CPF: ");
            cpfCliente = sc.nextLine();
            
            Cliente cliente = new Cliente(nomeCliente, cpfCliente);
            ContaCorrente contaCorrente = new ContaCorrente(numeroConta, saldoCliente, cliente);
        
            contas.add(contaCorrente);
        }

        System.out.println("\n--- Pesquisar conta ---\n");
        
        System.out.print("Número da conta: ");
        numeroConta = sc.nextLine();

        Double saldoTodasContas = 0.0;
        ContaCorrente maiorSaldo = contas.get(0);
        ContaCorrente menorSaldo = contas.get(0);
        boolean primeiraConta = true;

        System.out.println("--------------------------");
        boolean contaExiste = false;
        for (ContaCorrente conta : contas) {
            if (conta.getNumeroConta().equals(numeroConta)) {
                contaExiste = true;
            }

            saldoTodasContas += conta.getSaldo();

            if (primeiraConta) {
                maiorSaldo = conta;
                menorSaldo = conta;
                primeiraConta = false;
            } else {
                if (maiorSaldo.getSaldo() < conta.getSaldo()) {
                    maiorSaldo = conta;
                }
                if (menorSaldo.getSaldo() > conta.getSaldo()) {
                    menorSaldo = conta;
                }
            }
        }
    
        if (contaExiste) {
            for (ContaCorrente conta : contas) {
                if (conta.getNumeroConta().equals(numeroConta)) {
                    System.out.println(conta.exibirDados());
                    System.out.println("--------------------------");

                    System.out.println("1 - Sacar");
                    System.out.println("2 - Depositar");
                    
                    System.out.print("Operação: ");
                    String operacao = sc.nextLine();

                    switch (operacao) {
                        case "1":
                            System.out.print("Quanto deseja sacar: ");
                            Double valorSaque = sc.nextDouble();
                            if (conta.sacar(valorSaque)) {
                                System.out.println("Saque realizado com sucesso. Saldo atual: " + conta.getSaldo());
                            }
                            break;
                        case "2":
                            System.out.print("Quanto deseja depositar: ");
                            Double valorDeposito = sc.nextDouble();
                            if (conta.depositar(valorDeposito)) {
                                System.out.println("Deposito realizado com sucesso. Saldo atual: " + conta.getSaldo());
                            }
                        default:
                            break;
                    }
                }
            }
        } else {
            System.out.println("A conta não existe");
        }

        System.out.println("----- Informações -----");
        System.out.println("Saldo de todas as contas correntes: " + saldoTodasContas);
        System.out.println("Conta corrente com maior saldo: " + maiorSaldo.getSaldo());
        System.out.println("Conta corrente com menor saldo: " + menorSaldo.getSaldo());
        sc.close();
    }
}
