class Catalogo():
    def __init__(self, nome, genero, sinopse,
                 duracao, dt_lancamento):
        self.id = 0
        self.nome = nome
        self.genero = genero
        self.sinopse = sinopse
        self.duracao = duracao
        self.dt_lancamento = dt_lancamento

        def getNome(self):
            return self.nome

        def setnome(self, nome):
            self.nome = nome

        def getgenero(self):
            return self.genero

        def setgenero(self, genero):
            self.genero = genero

