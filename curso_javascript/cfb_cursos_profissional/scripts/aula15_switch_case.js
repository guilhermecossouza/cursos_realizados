let convocacao = 10

switch(convocacao) {
    case 1:
        console.log("Primeiro lugar");
        break;
    case 2:
        console.log("Segundo lugar");
        break;
    case 3:
        console.log("terceiro lugar");
        break;
    default:
        console.log("Não tem mais premiação");
        break;    
}

console.log("");
//podendo ser feito assim
switch(convocacao) {
    case 1: case 2: case 3:
        console.log("Subir ao pódio e pegar premiação");
        break;
    case 4: case 5: case 6:
        console.log("Somente pegar a premiação");
        break
    default:
        console.log("Não há premiação");
        break
}