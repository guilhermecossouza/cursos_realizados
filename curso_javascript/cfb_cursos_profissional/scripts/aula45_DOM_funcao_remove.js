const cursos = ["HTML", "CSS", "Javascript", "Python", "React", "MySQL", "ReactNative"]
const div_caixaCursos = document.querySelector("#caixaCursos");

const add_element = (ele, value) => {
    const nova_div = document.createElement("div");
    nova_div.setAttribute("id", "c"+value+"");
    nova_div.setAttribute("class", "curso c1");
    nova_div.innerHTML = ele;

    const novo_radio = document.createElement("input");
    novo_radio.setAttribute("type", "radio");
    novo_radio.setAttribute("name", "rb_curso")
    nova_div.appendChild(novo_radio);

    div_caixaCursos.appendChild(nova_div);
}

cursos.map((ele, ind) => {
    add_element(ele, ind);    
});

const btn_AdicionarNovoCurso = document.querySelector("#btnAdicionarNovoCurso");
btn_AdicionarNovoCurso.addEventListener("click", (event) => {
    let text_tag = document.querySelector("#nomeCurso").value.trim()
    if (text_tag !== "") {
        let elementos_container = document.querySelector("#caixaCursos");
        let amount_children = elementos_container.childElementCount     
        add_element(text_tag, amount_children);   
    }
});

const btnRemoverCurso = document.querySelector("#btnRemoverCurso");
btnRemoverCurso.addEventListener("click", (event) => {
    let elemets_radio = document.querySelector("input[type=radio]:checked");
    elemets_radio.parentNode.remove();    
});


const btn_CursoSelecionado = document.querySelector("#btnCursoSelecionado");
btn_CursoSelecionado.addEventListener("click", (event) => {
    let elemets_radio = document.querySelector("input[type=radio]:checked");
    if (elemets_radio) {
        alert("O curso selecionado foi: "+ elemets_radio.parentNode.textContent);
    }else {
        alert("Nenhum curso selecionado")
    }        
});








