console.log(document.body);
console.log(document.body.childNodes);
console.log(document.body.childNodes[1]);
console.log(document.body.childNodes[1].childNodes);
console.log(document.body.childNodes[1].childNodes[1]);
console.log(document.body.childNodes[1].childNodes[1].innerText);
document.body.childNodes[1].childNodes[1].textContent = "Guilherme"
console.log(document.body.childNodes[1].childNodes[1].innerText);