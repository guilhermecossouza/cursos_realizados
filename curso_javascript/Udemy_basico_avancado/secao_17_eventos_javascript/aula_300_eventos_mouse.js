const btn2 = document.querySelector("#btn2");
// btn2.addEventListener("mousedown", (event) => {
//     console.log("Clicou no botão do mouse");
// });

// btn2.addEventListener("mouseup", (event) => {
//     console.log("Clicou no botão do mouse");
// });

// btn2.addEventListener("dblclick", (event) => {
//     console.log("Clicou duas vezes");
// });

btn2.addEventListener("contextmenu", (event) => {
    event.preventDefault();
    console.log("Clicou com o botão direito");
});

