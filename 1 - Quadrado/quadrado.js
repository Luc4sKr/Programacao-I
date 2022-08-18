var Quadrado = class {
    constructor(lado) {
        this.lado = lado;
    }

    calcular_area() {
        return this.lado * this.lado;
    }

    calcular_perimetro() {
        return this.lado * 4;
    }

    imprimir() {
        return `Lado: ${this.lado} \nArea: ${this.calcular_area()} \nPerímetro: ${this.calcular_perimetro()}`;
    }

}

module.exports = Quadrado;
