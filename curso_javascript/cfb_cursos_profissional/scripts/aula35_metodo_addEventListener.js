
// function msg() {
//     alert("clicou no c4");
// }

// const msg1 = () => {
//     alert("Olá Mundo")
// }

// const elemento_c4 = document.querySelector("#c4")
/**
 * addEventListener
 * Em tese é um escutador responsável por tratar os eventos
 * Esse método precisa de dois parâmetro:
 * o evento [ click, change e etc.. ] e a função
 */

//elemento_c4.addEventListener("click", msg1)
// elemento_c4.addEventListener("click", (event) => {
//     event.target.classList.add("destaque");
    
// });


const cursos = [...document.querySelectorAll(".curso")];
cursos.map((el) => {
    el.addEventListener("click", (event) => {
        event.target.classList.add("destaque");
    });
});




