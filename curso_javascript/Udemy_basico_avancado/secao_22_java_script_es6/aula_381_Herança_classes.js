class Car {
    constructor(ports, wheels) {
        this.ports = ports;
        this.wheels = wheels;
    }

    start() {
        console.log("Car started")
    }
}

class Accessories extends Car {
    constructor(ports, wheels, arCondicionado) {
        super(ports, wheels)
        this.arCondicionado = arCondicionado
    }
}

const uno = new Accessories(4, 4, false)


uno.start()