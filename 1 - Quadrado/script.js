import Quadrado from "./quadrado.js";

const q1 = new Quadrado(5);
const q2 = new Quadrado(10);
const q3 = new Quadrado(12.5);

console.log(q1.imprimir(), q2.imprimir(), q3.imprimir());

const square_container = document.querySelector(".square-container");

square_container.innerHTML = q1.imprimir();
