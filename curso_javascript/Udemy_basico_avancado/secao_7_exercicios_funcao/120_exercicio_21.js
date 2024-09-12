function tipoParametro(n) {
    switch (typeof(n)) {
        case "string":            
            console.log(`O valor ${n} informado é uma tipo string`);
            break; 
        case "number":
            console.log(`O valor ${n} informado é uma tipo number`);
            break;
        case "boolean":
            console.log(`O valor ${n} informado é uma tipo boolean`);
            break;
        default:
            console.log(`O valor ${n} informado é uma tipo ${typeof(n)}`); 
    }
}
tipoParametro("123")