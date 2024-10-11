"use strict"

const isNumeric = (num) => {
    const number = Number(num);
    if (Number.isNaN(number)) {
        return true;        
    }else {
        return false;
    }
}

console.log(isNumeric('5'))
console.log(isNumeric(5))