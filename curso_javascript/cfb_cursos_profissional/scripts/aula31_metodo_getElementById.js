console.log("Elemento c1'");
const dc1 = document.getElementById("c1");
console.log(dc1);
console.log(dc1.id);
console.log(dc1.innerHTML);
console.log(dc1.innerText);
dc1.innerHTML = "Guilherme"
dc1.style = "color: red"

console.log("");
console.log("");
console.log("Criando arrays com os elementos");
const arrElementos = [
    document.getElementById("c1"),
    document.getElementById("c2"),
    document.getElementById("c3"),
    document.getElementById("c4"),
    document.getElementById("c5"),
    document.getElementById("c6"),
] 

for(el of arrElementos) {
    switch (el.id) {
        case "c1":
            el.style = "color: red";
            break;
        case "c5":
            el.innerHTML = "zaca";
            el.style = "color: green";
            break;
        default:
            el.style = "color: yellow";
    }
}