export {}
// ==> Exemplo 01 - Optional Parameter
function informar_dados_pessoas(id:number, nome:string, email?:string):string {
    if(email === undefined) email = "Não informado";
    return `ID: ${id}, Nome: ${nome}, Email: ${email}`;
}
console.log(informar_dados_pessoas(1, "Guilherme"));
console.log(informar_dados_pessoas(1, "Guilherme", "guilhermecossouza@gmail.com"));

// ==> Exemplo 02
function mensagem_log(mensagem: string, usuarioId?: number): string {
    let dataHoraLog = new Date().toLocaleTimeString();
    return `Data: ${dataHoraLog}, mensagem: ${mensagem}, idUsuario: ${usuarioId || "Usuário não logado"}`;
}
console.log(mensagem_log("Atualizar página"))
console.log(mensagem_log("Atualizar página", 1))

// ==> Exemplo 03
type Pessoa = {
    IdFuncionario: number,
    nome: string,
    idade?: number,
    email?: string,
}

let pessoa: Pessoa = {
    IdFuncionario: 1,
    nome: "Guilherme",
}

console.log(pessoa);

let pessoa2: Pessoa = { 
    IdFuncionario: 2,
    nome: "Guilherme",
    idade: 40,
    email: "guilhermecossouza@gmail.com"
}

console.log(pessoa2);


