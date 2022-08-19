var Eleitor = class {

    #nome;
    #idade;

    constructor(nome, idade) {
        this.#nome = nome;
        this.#idade = idade;
    }

    verificar() {
        if (this.#idade < 16) {
            return `${this.#nome} ainda não pode votar. Tem apenas ${this.#idade} anos.`;
        } else {
            if (this.#idade >= 16 && this.#idade < 18 || this.#idade > 65) {
                return `${this.#nome} - ${this.#idade}. Voto facultativo`;
            } else {
                return `${this.#nome} - ${this.#idade}. Deve Votar.`;
            }
        }
    }
}

module.exports = Eleitor;
