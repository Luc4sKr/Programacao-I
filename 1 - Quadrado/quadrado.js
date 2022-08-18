export default class Quadrado {
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
        return `Lado: ${this.lado} <br>Area: ${this.calcular_area()} <br>Perímetro: ${this.calcular_perimetro()}`;
    }

}

