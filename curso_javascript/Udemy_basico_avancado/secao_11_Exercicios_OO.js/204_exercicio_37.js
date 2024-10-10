class Carrinho  {
    constructor() {
        this.itens = [];
        this.quantidadeTotal = 0;
        this.valorTotal = 0;
    }

    addItem(itens, quantidadeTotal, valorTotal) {

        if (this.itens.length === 0) {
            this.itens.push(itens);
            this.quantidadeTotal += quantidadeTotal
            this.valorTotal += valorTotal
            return;    
        }

        let adicionaItem = true

        this.itens.forEach((item) => {
            if(item.id === itens.id) {
                item.quantidadeTotal += 1
                item.valorTotal += itens.valorTotal  
                adicionaItem = false              
            }            
        });  

        this.quantidadeTotal += quantidadeTotal
        this.valorTotal += valorTotal
        
        if (adicionaItem) {
            this.itens.push(itens);    
        }
    }

    removeItem(itens, quantidadeTotal, valorTotal) {
        this.itens.forEach((item) => {
            if(item.id === itens.id) {
                let obj = item
                let index = this.itens.findIndex((obj) => {return obj.id === item.id})
                this.itens.splice(index, 0)
            }    
        });

        this.quantidadeTotal -= quantidadeTotal
        this.valorTotal -= valorTotal
    }
}

let carrinho = new Carrinho()

carrinho.addItem({id: 1,nome: "caminsa",quantidadeTotal: 1,valorTotal: 50}, 1, 50);
carrinho.addItem({id: 2,nome: "bermuda",quantidadeTotal: 1,valorTotal: 50}, 1, 50);
carrinho.addItem({id: 1,nome: "caminsa",quantidadeTotal: 1,valorTotal: 50}, 1, 50);
carrinho.addItem({id: 2,nome: "bermuda",quantidadeTotal: 1,valorTotal: 50}, 1, 50)
carrinho.addItem({id: 3,nome: "coeca",quantidadeTotal: 2,valorTotal: 20}, 2, 20);
carrinho.removeItem({id: 3,nome: "coeca",quantidadeTotal: 2,valorTotal: 20}, 2, 20);
console.log(carrinho)




