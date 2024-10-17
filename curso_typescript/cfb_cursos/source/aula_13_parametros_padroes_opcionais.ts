function soma(n1:number=0, n2:number=0): number {
    return n1 + n2;
}

// console.log(soma(10,20));
// console.log(soma(10));
// console.log(soma());    

//parametros posicionais
function novoUsuario(username:string, email?:string):void {
    console.log(username);
    if(email !== undefined) {
        console.log(email);    
    }
}    

novoUsuario("Guilherme", "d2Gx8@example.com");
novoUsuario("Guilherme");