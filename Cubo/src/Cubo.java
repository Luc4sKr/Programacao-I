public class Cubo {

    private Integer altura;
    private Integer largura;
    private Integer profundidade;

    public Cubo(Integer altura, Integer largura, Integer profundidade) {
        this.altura = altura;
        this.largura = largura;
        this.profundidade = profundidade;
    }

    public Integer calcularArea() {
        return this.altura * this.largura;
    }

    public Integer calcularVolume() {
        return this.altura * this.largura * this.profundidade;
    }


    public Integer getAltura() {
        return this.altura;
    }

    public void setAltura(Integer altura) {
        this.altura = altura;
    }

    public Integer getLargura() {
        return this.largura;
    }

    public void setLargura(Integer largura) {
        this.largura = largura;
    }

    public Integer getProfundidade() {
        return this.profundidade;
    }

    public void setProfundidade(Integer profundidade) {
        this.profundidade = profundidade;
    }

}