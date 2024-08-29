const todos_elementos = [...document.querySelectorAll(".curso")];
const botao = document.querySelector("#btn_copiar");

todos_elementos.map((el)=>{
    el.addEventListener("click", (event) => {
        event.target.classList.add("selecionado");
    });
});

botao.addEventListener("click",(event) => {
    const selecionados = [...document.querySelectorAll(".selecionado")];
    const caixa2 = document.querySelector("#caixa2");
    selecionados.map((el) => {
        caixa2.appendChild(el);
    });
});

