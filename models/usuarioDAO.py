class UsuarioDAO():
    def __init__(self, con):
        self.con = con

    # CRUD - Create, Retrieve, Update, Delete
    def inserir(self, usuario):
        try:
            sql = "INSERT INTO Usuario(nome, email, " \
                  "rua,bairro, cep, cidade,senha) VALUES (%s, %s, %s, %s, %s,%s, %s)"

            cursor = self.con.cursor()
            cursor.execute(sql, (usuario.nome, usuario.email,
                                 usuario.rua, usuario.bairro, usuario.cep, usuario.cidade, usuario.senha))
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
                sql = "SELECT * FROM Usuario WHERE codigo=%s"
                cursor.execute(sql, (codigo,))
                usuario = cursor.fetchone()
                return usuario
            else:
                # pegar todas as plantas
                sql = "SELECT * FROM Usuario"
                cursor.execute(sql)
                usuario = cursor.fetchall()
                return usuario
        except:
            return None

    def autenticar(self, email, senha):
        pass

