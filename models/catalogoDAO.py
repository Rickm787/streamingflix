class CatalogoDAO():
    def __init__(self, con):
        self.con = con

    # CRUD - Create, Retrieve, Update, Delete
    def inserir(self, catalogo):
        try:
            sql = "INSERT INTO Catalogo(nome, genero, " \
                  "sinopse, duracao, dt_lancamento) VALUES (%s, %s, %s, %s, %s)"

            cursor = self.con.cursor()
            cursor.execute(sql, (catalogo.nome, catalogo.genero,
                                 catalogo.sinopse, catalogo.duracao, catalogo.dt_lancamento))
            self.con.commit()
            codigo = cursor.lastrowid
            return codigo
        except:
            return 0

    def listar(self, codigo=None):
        try:
            cursor = self.con.cursor()
            if codigo != None:
                # pegar somente uma planta
                sql = "SELECT * FROM Catalogo WHERE codigo=%s"
                cursor.execute(sql, (codigo,))
                catalogo = cursor.fetchone()
                return catalogo
            else:
                # pegar todas as plantas
                sql = "SELECT * FROM Catalogo"
                cursor.execute(sql)
                catalogo = cursor.fetchall()
                return  catalogo

        except:
            return None

