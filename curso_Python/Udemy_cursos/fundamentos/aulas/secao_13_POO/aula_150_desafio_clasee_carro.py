class Carro:
    def __init__(self, velocidade=0) -> None:
        self.velocidade_incial = 0
        self.velocidade_atual = 0
        self.velocidade_maxima = velocidade

    def acelerar(self, velocidade=0):
        self.velocidade_atual += velocidade
        return self.velocidade_atual if self.velocidade_atual <= self.velocidade_maxima else self.velocidade_maxima

    def frear(self, velocidade=0):
        self.velocidade_atual -= velocidade
        return self.velocidade_atual if self.velocidade_atual > 0 else 0


if __name__ == "__main__":
    palio = Carro(velocidade=180)

    for kilometros in range(8, 25, 8):
        palio.velocidade_atual = palio.acelerar(velocidade=20)
        print(f"{palio.velocidade_atual}km/h")

    for metros in range(10):
        velocidade_final = palio.frear(velocidade=20)
        if velocidade_final > 0:
            print(velocidade_final)
