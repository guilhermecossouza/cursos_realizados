const tagA = document.querySelector("a");

tagA.addEventListener("click", (event) => {
    event.preventDefault();
    console.log("Clicou no link");
})