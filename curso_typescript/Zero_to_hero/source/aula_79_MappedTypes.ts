export {}


// ==> Exemplo 01 - Mapped Types

type Usuario = {
    nome: string;
    endereco: string;
    telefone: string;
    idade: number;
}

type UsuarioMapped = {    
    [p in keyof Usuario]?: Usuario[p];
}


const usuario: UsuarioMapped = {
    nome: "Guilherme",
}
console.log(usuario.nome);


//=> exemplo 02 - Mapped Types

interface Livro {
    titulo: string;
    autor: string | null;
    preco: number;
    paginas: number;
}

type Artigo = Omit<Livro, "paginas">;
type LivroModelo = Readonly<Livro>


const artigo: Artigo = {
    titulo: "Artigo 1",
    autor: "Autor 1",
    preco: 100
}

const livroModelo: LivroModelo = {
    titulo: "Livro 1",
    autor: "Autor 1",
    preco: 100,
    paginas: 100
}

//livroModelo.autor = "Autor 2"; somente leitura
console.log(livroModelo.autor)


