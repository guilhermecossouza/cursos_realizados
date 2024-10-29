export {}

interface DadosBancarios {
    conta: number;
    agencia: number;
    banco: string;  
}

interface Cliente {
    nome: string;
    sobrenome: string;
    idade: number;
    email: string;
}

interface DadosPessoaFisica {
    cpf: string;
}

interface DadosPessoaJuridica {
    cnpj: string;
}

//=> É obrigado a passar todas as informções das interfaces
type DadosClientePF = DadosBancarios & Cliente & DadosPessoaFisica;


const dadosCliente: DadosClientePF = {
    conta: 123,
    agencia: 123,
    banco: "Itau",
    nome: "Guilherme",
    sobrenome: "Costa",
    idade: 40,
    email: "teste@teste.com",
    cpf: "01447498508",
}

console.log(dadosCliente);


