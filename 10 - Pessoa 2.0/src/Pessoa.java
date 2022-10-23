public class Pessoa {
    
    public String nome;
    public Integer idade;
    public Endereco endereco;

    public Pessoa(String nome, Integer idade, Endereco endereco) {

        this.nome = nome;
        this.idade = idade;
        this.endereco = endereco;
    }

    public String exibeDados() {
        return "Nome: " + this.nome + "\nIdade: " + this.idade+ "\n-- Endereço --\nCidade: " + this.endereco.cidade + "\nBairro: " + this.endereco.bairro + "\nRua: " + this.endereco.rua + "\nNúmero: " + this.endereco.numero;
    }
}
