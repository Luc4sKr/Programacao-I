public class ContaCorrente {

    private String numeroConta;
    private Double saldo;
    private Cliente cliente;

    public ContaCorrente(String numeroConta, Double saldo, Cliente cliente) {
        this.numeroConta = numeroConta;
        this.saldo = saldo;
        this.cliente = cliente;

    }

    public boolean sacar(Double valor) {
        if ((this.saldo - valor) > 0) {
            this.saldo -= valor;
            return true;
        } else {
            return false;
        }
    }

    public boolean depositar(Double valor) {
        if (valor > 0) {
            this.saldo += valor;
            return true;
        } else {
            return false;
        }
    }

    public String exibirDados() {
        return "Nome: " + cliente.nomeCliente +
               "\nCPF: " + cliente.cpfCliente + 
               "\nNúmero da conta: " + this.numeroConta +
               "\nSaldo: " + this.saldo;
    }


    public String getNumeroConta() {
        return numeroConta;
    }

    public void setNumeroConta(String numeroConta) {
        this.numeroConta = numeroConta;
    }

    public Double getSaldo() {
        return saldo;
    }

    public void setSaldo(Double saldo) {
        this.saldo = saldo;
    }

    public Cliente getCliente() {
        return cliente;
    }
    
    public void setCliente(Cliente cliente) {
        this.cliente = cliente;
    }
}
