var Eleitor = require("./eleitor");

const e1 = new Eleitor("Lucas", 16);
const e2 = new Eleitor("Maria", 16);
const e3 = new Eleitor("Josefino", 32);
const e4 = new Eleitor("Calrlos", 70);

console.log("E1 =============================");
console.log(e1.verificar());
console.log("E2 =============================");
console.log(e2.verificar());
console.log("E3 =============================");
console.log(e3.verificar());
console.log("E3 =============================");
console.log(e4.verificar());
console.log("E4 =============================");
