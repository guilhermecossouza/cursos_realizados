window.addEventListener("load", (event) => {
    console.log("A página foi carregada");
});


window.addEventListener("beforeunload", (event) => {
    event.returnValue = "Tem certeza que deseja sair?";
})