public class Aluno {
    
    String nome;
    String cpf;
    Double nota1;
    Double nota2;
    Double nota3;

    public Aluno(String nome, String cpf) {

        this.nome = nome;
        this.cpf = cpf;
        this.nota1 = null;
        this.nota2 = null;
        this.nota3 = null;

    }

    public Double CalcuarMedia() {
        return (this.nota1 + this.nota2 + this.nota3) / 3;
    }

    private Double notaValida(Double nota) {
        if (nota > 10) {
            return 10.0;
        } else {
            if (nota < 0) {
                return 0.0;
            }
        }
        return nota;
    }


    // Getters and Setters

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }


    public String getCpf() {
        return cpf;
    }

    public void setCpf(String cpf) {
        this.cpf = cpf;
    }


    public Double getNota1() {
        return nota1;
    }

    public void setNota1(Double nota1) {
        this.nota1 = notaValida(nota1);
    }


    public Double getNota2() {
        return nota2;
    }

    public void setNota2(Double nota2) {
        this.nota2 = notaValida(nota2);
    }

    public Double getNota3() {
        return nota3;
    }

    public void setNota3(Double nota3) {
        this.nota3 = notaValida(nota3);
    }
    
}
