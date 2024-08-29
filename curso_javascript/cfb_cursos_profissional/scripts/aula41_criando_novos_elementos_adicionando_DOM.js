const caixa = document.querySelector("#caixa1");

//criando um novo elemwnto
const elemento_novo = document.createElement("div");
elemento_novo.innerHTML = "ReactNative";

/**
 * setAttribute recebe dois parametro
 * 1° atributo que vao adicionar
 * 2° o que vai adicinar dentro do atributo
 */
elemento_novo.setAttribute("id", "c7");
elemento_novo.setAttribute("class", "curso c1");
//adicionando o novo elemento
caixa.appendChild(elemento_novo)

const novos_cursos = ["Python", "Django", "Serverless", "Docker"]

/// map pode ter dois parametro o value, key
// novos_cursos.map((value, key) => {    
//     const elem_novo = document.createElement("div");
//     elem_novo.setAttribute("id", "c"+key + 1+"");
//     elem_novo.setAttribute("class", "curso c1");
//     elem_novo.innerHTML = value
//     caixa.appendChild(elem_novo)
// });



let contador = caixa.children.length
for (const texto of novos_cursos) {
    const elem_novo = document.createElement("div");
    elem_novo.setAttribute("id", "c"+contador+"");
    elem_novo.setAttribute("class", "curso c1");
    elem_novo.innerHTML = texto
    caixa.appendChild(elem_novo)
    contador += 1
}