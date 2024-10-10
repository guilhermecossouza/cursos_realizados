function Cliente(rua, bairro, cidade, estado) {
    this.rua = rua;
    this.bairro= bairro;
    this.cidade = cidade;
    this.estado = estado;
}


Cliente.prototype.atualizarRua = function(novaRua) {
    this.rua = novaRua
}

Cliente.prototype.atualizarBairro = function(novoBairro) {
    this.bairro = novoBairro
}

Cliente.prototype.atualizarCidade = function(novaCidade) {
    this.cidade = novaCidade
}

Cliente.prototype.atualizarEstado = function(novoEstado) {
    this.estado = novoEstado
}

let cliente = new Cliente("Jataí", "Da Graça", "Belo Horizonte", "Minas Gerais");
console.log(cliente);
cliente.atualizarRua("Rua Divino Espírito Santo");
cliente.atualizarBairro("Ribeiro de Abreu");
cliente.atualizarCidade("teste");
cliente.atualizarEstado("teste");
console.log(cliente);
