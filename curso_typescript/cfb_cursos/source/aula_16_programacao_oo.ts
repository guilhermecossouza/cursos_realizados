class Computador {
    nome:string = "";
    ram:number = 0;
    cpu:number = 0;
    ligado:boolean = false;
}

let comp1 = new Computador();
comp1.nome = "Computador 1";
comp1.ram = 4;
comp1.cpu = 2.5;
comp1.ligado = true;

console.log(comp1)
