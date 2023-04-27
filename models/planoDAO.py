class PlanoDAO():
    def __init__(self, con, categoria, valor):
        self.con = con
        self.categoria = categoria
        self.valor = valor

    # CRUD - Create, Retrieve, Update, Delete
    def inserir(self, plano):
        try:
            sql = "INSERT INTO Plano(categoria, valor)" "VALUES (%s, %s)"

            cursor = self.con.cursor()
            cursor.execute(sql, (plano.categoria, plano.valor))
            self.con.commit()
            codigo = cursor.lastrowid
            return codigo
        except:
            return 0

    def listar(self, codigo=None):
        try:
            cursor = self.con.cursor()
            if codigo is not None:
                # pegar somente uma planta
                sql = "SELECT * FROM Plano WHERE codigo=%s"
                cursor.execute(sql, (codigo,))
                plano = cursor.fetchone()
                return plano
            else:
                # pegar todas as plantas
                sql = "SELECT * FROM Plano"
                cursor.execute(sql)
                plano = cursor.fetchall()
                return plano

        except:
            return None
