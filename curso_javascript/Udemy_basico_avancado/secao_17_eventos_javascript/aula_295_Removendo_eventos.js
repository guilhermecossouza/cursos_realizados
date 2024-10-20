const btn1 = document.getElementById("btn1");
const btn2 = document.getElementById("btn2");


const mensagem = () => {
    console.log("Clicou no botão 1");
}

btn1.addEventListener("click", mensagem);


btn2.addEventListener("click", () => {
    btn1.removeEventListener("click", mensagem);
});

