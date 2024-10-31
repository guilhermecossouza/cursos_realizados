export {}

//++> Exemplo 01 - Satisfies Operator

type Cidade = NomeCidade | CidadeCoordenadas;

type NomeCidade = "São Paulo" | "Rio de Janeiro" | "Belo Horizonte";

type CidadeCoordenadas = {
    x: number;
    y: number;  
}

type Pessoa = {
    localNascimento: Cidade;
    residenciaAtual: Cidade;
}

const pessoa = {
    localNascimento: "Belo Horizonte",
    residenciaAtual: {x: 10, y: 20}
} satisfies Pessoa

console.log(pessoa.localNascimento.toUpperCase());

//exemplo 02 - Satisfies Operator

type Connection = {}

declare function createConnection(
    host: string,
    port: string,
    database: string,
    user: string,
    password: string,
    reconnect: boolean,
): Connection


type Configuration = {
    host: string;
    port: string | number;
    database: string;
    user: string;
    password: string;
    tryReconnect: boolean | (() => boolean);
}


const config = {
    host: "localhost",
    port: "5432",
    database: "postgres",
    user: "postgres",
    password: "123456",
    tryReconnect: () => true,
} satisfies Configuration

function connect() {
    let {host, port, database, user, password, tryReconnect} = config;
    // if(typeof port === "number") port = port.toString();
    // if(typeof tryReconnect !== "boolean") tryReconnect = tryReconnect();
    createConnection(host, `${port}`, database, user, password, tryReconnect());
}