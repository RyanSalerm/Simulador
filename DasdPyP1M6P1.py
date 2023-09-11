from random import choice, shuffle
import seaborn as sns
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings("ignore")


class Academia:
    def __init__(self):
        self.halter = [i for i in range(10, 36) if i % 2 == 0]
        self.posicao = {}
        self.reiniciar()

    def reiniciar(self):
        self.posicao = {i: i for i in self.halter}

    def listar_halteres(self):
        return [i for i in self.posicao.values() if i != 0]

    def listar_espacos(self):
        return [i for i, j in self.posicao.items() if j == 0]

    def pegar(self, peso):
        halter_pegar = list(self.posicao.values()).index(peso)
        posicao_pegar = list(self.posicao.keys())[halter_pegar]
        self.posicao[posicao_pegar] = 0
        return peso

    def devolver_halter(self, pos, peso):
        self.posicao[pos] = peso

    def calcular_caos(self):
        num_caos = [i for i, j in self.posicao.items() if i != j]
        return len(num_caos) / len(self.posicao)


class Usuario:
    def __init__(self, tipo, academia):
        self.tipo = tipo
        self.academia = academia
        self.peso = 0

    def iniciar_treino(self):
        lista_pesos = self.academia.listar_halteres()
        self.peso = choice(lista_pesos)
        self.academia.pegar(self.peso)

    def finalizar_treino(self):
        espacos = self.academia.listar_espacos()

        if self.tipo == 1:
            if self.peso in espacos:
                self.academia.devolver_halter(self.peso, self.peso)
            else:
                pos = choice(espacos)
                self.academia.devolver_halter(pos, self.peso)

        if self.tipo == 2:
            pos = choice(espacos)
            self.academia.devolver_halter(pos, self.peso)
        self.peso = 0


fitness = Academia()
usuarios = [Usuario(1, fitness) for c in range(10)]
usuarios += [Usuario(2, fitness) for d in range(1)]
shuffle(usuarios)

caos = []
for k in range(50):
    fitness.reiniciar()
    for c in range(10):
        shuffle(usuarios)
        for user in usuarios:
            user.iniciar_treino()
        for user in usuarios:
            user.finalizar_treino()
        caos += [fitness.calcular_caos()]

sns.displot(caos)
plt.show()
