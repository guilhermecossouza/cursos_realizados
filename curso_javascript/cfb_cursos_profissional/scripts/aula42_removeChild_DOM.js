const caixa = document.querySelector("#caixa1");
const text_div = ["HTML", "CSS", "Javascript", "PHP", "React", "MySQL"]
text_div.map((text, chave) => {
    const elemento = document.createElement("div");
    elemento.setAttribute("id", "c"+chave + 1+"");
    elemento.setAttribute("class", "curso c1");
    elemento.innerHTML = text;
    caixa.appendChild(elemento);
    elemento.addEventListener("click", (ele) => {
        caixa.removeChild(ele.target);
    });
});



