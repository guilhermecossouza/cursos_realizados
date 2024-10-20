const btn1 = document.getElementById("btn1");
const tagP = document.querySelector("p");

btn1.addEventListener("click", (event) => {
    console.log("O botão 1 foi clicado");
    event.stopPropagation();
});

tagP.addEventListener("click", (event) => {
    console.log("clicou no parágrafo");
})