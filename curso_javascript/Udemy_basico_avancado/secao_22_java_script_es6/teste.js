class Voo {
    constructor(codigoVoo, origem, destino, assentosDisponiveis) {
      this.codigoVoo = codigoVoo;             // Código único do voo
      this.origem = origem;                   // Cidade de origem
      this.destino = destino;                 // Cidade de destino
      this.assentosDisponiveis = assentosDisponiveis; // Número de assentos disponíveis
    }
  
    // Método para reservar um assento
    reservarAssento() {
      if (this.assentosDisponiveis > 0) {
        this.assentosDisponiveis--; // Decrementa o número de assentos
        console.log("Assento reservado com sucesso!");
      } else {
        throw new Error("Erro: Não há mais assentos disponíveis.");
      }
    }
  
    // Método para consultar a quantidade de assentos disponíveis
    consultarAssentosDisponiveis() {
      return this.assentosDisponiveis;
    }
  }
  
  // Exemplo de uso
  const voo1 = new Voo('ABC123', 'São Paulo', 'Rio de Janeiro', 1);
  
  console.log(`Assentos disponíveis: ${voo1.consultarAssentosDisponiveis()}`); // Saída: 1
  voo1.reservarAssento(); // Saída: Assento reservado com sucesso!
  console.log(`Assentos disponíveis: ${voo1.consultarAssentosDisponiveis()}`); // Saída: 0
  voo1.reservarAssento(); // Saída: Erro: Não há mais assentos disponíveis.
  