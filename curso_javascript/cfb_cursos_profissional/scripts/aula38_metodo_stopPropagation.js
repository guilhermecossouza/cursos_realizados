const caixa = document.querySelector("#caixa1");
const bc1 = document.querySelector("#c1");
const cursos = [...document.querySelectorAll(".curso")];

caixa.addEventListener("click", () => {
    console.log("clicou!");
});

// bc1.addEventListener("click", (event) => {
//     event.stopPropagation();   
// });



cursos.map((elemento) => {
    elemento.addEventListener("click", (event) => {
        event.stopPropagation();
    });
});

// for (const curso of cursos) {
//     curso.addEventListener("click", (event) => {
//         event.stopPropagation();
//     });
// }
