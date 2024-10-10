const pessoa = {
    maos: 2,
    falar: function() {
        return "Bom dia"
    }
}

const novaPessoa = Object.create(pessoa)
console.log(novaPessoa.maos);
novaPessoa.pes = 2
console.log(novaPessoa.pes);
console.log(novaPessoa.falar());

