export {}


// ==> Exemplo 01 - Conditional Types

type Pessoa = {
    nome: string
    idade: number
    endereco: string
}

type Empresa = {
    nome: string
    cnpj: number
}

type EnderecoPessoa  = {
    enderecoSecundario: string;
    cidade: string;
    pais: string;
}

type EnderecoEmpresa = {
    localizacao: "rua" | "avenida" | "praça";
}


type EnderecoFinal<T> = T extends {endereco: string} ? EnderecoPessoa : EnderecoEmpresa;

const enderecoPessoa: EnderecoFinal<Pessoa> = {
    enderecoSecundario: "rua",
    cidade: "são Paulo",
    pais: "Brasil"
}

const enderecoEmpresa: EnderecoFinal<Empresa> = {
    localizacao: "rua"
}


// ==> Exemplo 02 - Conditional Types

type FormatoArquivos = "png" | "jpg" | "gif" | "svg" | "mp4" | "mp3";
type FiltarArquivosAudios<T> = T extends "mp4" | "mp3" ? T : never
type FiltrarArquivoImagem<T> = T extends "png" | "jpg" | "gif" | "svg" ? T : never

type ArquivoAudio = FiltarArquivosAudios<FormatoArquivos>;
type ArquivoImagem = FiltrarArquivoImagem<FormatoArquivos>
 

// => const arquivoAudio: ArquivoAudio = "jpg" => Erro arquivo não é audio
const arquivoAudio: ArquivoAudio = "mp4"
const ArquivoAudio: ArquivoAudio = "mp3"

const arquivoImagem: ArquivoImagem = "jpg"
//const ArquivoImagem: ArquivoImagem = "mp4" => Erro arquivo não é audio  





