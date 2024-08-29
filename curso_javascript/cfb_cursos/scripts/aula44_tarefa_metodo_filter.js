"use strict"

/**
 * Código refatorado 
 */

document.querySelector("#btnAdicionarNovoCurso").addEventListener("click", (event) => {
    const elemento_erro = document.querySelector("#mensagemErro");
    const nomeCursoInput = document.querySelector("#nomeCurso");
    const input_text = nomeCursoInput.value;
    if(input_text.trim() !== "") {
        const cursoContainer = document.querySelector("#caixaCursos");
        const quantidate_cursos = cursoContainer.querySelectorAll(".curso").length;

        const nova_div = document.createElement("div");
        nova_div.setAttribute("id", "c"+quantidate_cursos+"");
		nova_div.setAttribute("class", "curso c1");
		nova_div.innerHTML = input_text;

        const novo_input  = document.createElement("input");
        novo_input.setAttribute("type", "radio");
        novo_input.setAttribute("name", "rb_curso");

        nova_div.appendChild(novo_input);
        cursoContainer.appendChild(nova_div);
        nomeCursoInput.value = "";
        elemento_erro.textContent = "";
        elemento_erro.style.display = "none";
    }else {        
        elemento_erro.textContent = "Informe um curso.";
        elemento_erro.style.display = "block";
    }
});

document.querySelector("#btnRemoverCurso").addEventListener("click", (event) => {
    const elemento_erro = document.querySelector("#mensagemErro");
    const dic_caixaCursos = document.querySelector("#caixaCursos");
    const input_radio = document.querySelector("input[type=radio]:checked");
    if (input_radio) {
        dic_caixaCursos.removeChild(input_radio.parentNode)
        elemento_erro.textContent = "";
        elemento_erro.style.display = "none";     
    }else {
        elemento_erro.textContent = "Selecione um curso";
        elemento_erro.style.display = "block";
    } 
});

document.querySelector("#btnCursoSelecionado").addEventListener("click", (event) => {
    const elemento_erro = document.querySelector("#mensagemErro");
    const input_radio = document.querySelector("input[type=radio]:checked"); 
    if (input_radio) {
        alert(input_radio.parentNode.firstChild.textContent);
        elemento_erro.textContent = "";
        elemento_erro.style.display = "none";  
    }else {
        elemento_erro.textContent = "Selecione um curso";
        elemento_erro.style.display = "block";
    }           
});


/**
 * Código não refatorado
 * 
 */

// document.querySelector("#btnAdicionarNovoCurso").addEventListener("click", (event) => {
//     const elemento_erro = document.querySelector("#mensagemErro");
//     const nomeCursoInput = document.querySelector("#nomeCurso");
//     const input_text = nomeCursoInput.value;
//     if(input_text.trim() !== "") {
//         const div_caixaCursos = document.querySelector("#caixaCursos");
//         const quantidate_cursos = div_caixaCursos.querySelectorAll(".curso").length;
//         const fragmento = document.createDocumentFragment();

//         const nova_div = document.createElement("div");
//         nova_div.setAttribute("id", "c"+quantidate_cursos+"");
// 		nova_div.setAttribute("class", "curso c1");
// 		nova_div.innerHTML = input_text;

//         const novo_imput = document.createElement("input");
//         novo_imput.setAttribute("type", "radio");
//         novo_imput.setAttribute("name", "rb_curso");

//         nova_div.appendChild(novo_imput);
//         fragmento.appendChild(nova_div);
//         div_caixaCursos.appendChild(fragmento);
//         nomeCursoInput.value = "";
//         elemento_erro.textContent = "";
//         elemento_erro.style.display = "none";
//     }else {        
//         elemento_erro.textContent = "Informe um curso.";
//         elemento_erro.style.display = "block";
//     }
// });

// document.querySelector("#btnRemoverCurso").addEventListener("click", (event) => {
//     const elemento_erro = document.querySelector("#mensagemErro");
//     const dic_caixaCursos = document.querySelector("#caixaCursos");
//     const input_rado = document.querySelectorAll("input[type=radio]"); 
//     if (input_rado.length > 0) {
//         input_rado.forEach((element) => {
//             if (element.checked) {
//                 dic_caixaCursos.removeChild(element.parentNode)    
//             }            
//         });
//         elemento_erro.textContent = "";
//         elemento_erro.style.display = "none";
//     }else{
//         elemento_erro.textContent = "Adicione o curso.";
//         elemento_erro.style.display = "block";
//     }
// });

// document.querySelector("#btnCursoSelecionado").addEventListener("click", (event) => {
//     const elemento_erro = document.querySelector("#mensagemErro");
//     const input_rado = document.querySelectorAll("input[type=radio]"); 
//     if (input_rado.length > 0) {
//         input_rado.forEach((element) => {
//             if (element.checked) {
//                 alert("O curso selecionado foi: "+ element.parentNode.firstChild.textContent);                
//             }
//         });
//         elemento_erro.textContent = "";
//         elemento_erro.style.display = "none";
//     }else {
//         elemento_erro.textContent = "Adicione o curso.";
//         elemento_erro.style.display = "block";
//     }           
// });

