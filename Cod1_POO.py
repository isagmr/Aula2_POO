class ClassCarro:
    def __init__(self):
        self.modelo = ""
        self.cor    = ""
        self.__velocidadeInstantanea = 0   # privado: dois underscores

    # Método público que recebe a taxa de aceleração como parâmetro
    def Faceleracao(self, a):
        self.__velocidadeInstantanea += a   # acumula no ATRIBUTO da classe
        print(f"\nVelocidade atual: {self.__velocidadeInstantanea} km/h")

    # Getter público para ler o atributo privado
    def getVelocidade(self):
        return self.__velocidadeInstantanea


# ---------- main ----------
carro = ClassCarro()
carro.modelo = "Astra"
carro.cor    = "Roxo"

print(f"Carro: {carro.modelo}\nCor: {carro.cor}")

# Tentativa de acesso direto ao atributo privado — gera AttributeError:
# print(carro.__velocidadeInstantanea)

aa = 5   # taxa configurável aqui na main

carro.Faceleracao(aa)
carro.Faceleracao(aa)
carro.Faceleracao(aa)

print(f"\nVelocidade final: {carro.getVelocidade()} km/h")
