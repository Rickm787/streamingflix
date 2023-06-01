from flask import Flask, g, render_template, \
    request, redirect, url_for, flash, session

import mysql.connector

from models.usuario import Usuario
from models.usuarioDAO import UsuarioDAO
from models.catalogo import Catalogo
from models.catalogoDAO import CatalogoDAO
from models.plano import Plano
from models.planoDAO import PlanoDAO

app = Flask(__name__)
app.secret_key = "senha123"

DB_HOST = "127.0.0.1"
DB_USER = "root"
DB_PASS = ""
DB_NAME = "mydb"

app.auth = {
    # acao: { perfil:permissao }
    'painel': {0: 1, 1: 1},
    'logout': {0: 1, 1: 1},
    'cadastrar_usuario': {0: 1, 1: 1},
    'listar_usuario': {0: 1, 1: 1},
    'cadastrar_saida': {0: 1, 1: 1}
}


@app.before_request
def autorizacao():
    acao = request.path[1:]
    acao = acao.split('/')
    if len(acao) >= 1:
        acao = acao[0]

    acoes = app.auth.keys()
    if acao in list(acoes):
        if session.get('logado') is None:
            return redirect(url_for('login'))
        else:
            tipo = session['logado']['tipo']
            if app.auth[acao][tipo] == 0:
                return redirect(url_for('painel'))


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASS,
            database=DB_NAME
        )
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    if request.method == "POST":
        # valor = request.form['campoHTML']
        nome = request.form['nome']
        bairro = request.form['bairro']
        cep = request.form['cep']
        rua = request.form['rua']
        cidade = request.form['cidade']
        email = request.form['email']
        senha = request.form['senha']

        usuario = Usuario(nome, bairro, cep, rua, cidade, email, senha)

        dao = UsuarioDAO(get_db())
        codigo = dao.inserir(usuario)

        if codigo > 0:
            flash("Cadastrado com sucesso! Código %d" % codigo, "success")
        else:
            flash("Erro ao cadastrar!", "danger")

    vartitulo = "Cadastro"
    return render_template("cadastro.html", titulo=vartitulo)

@app.route('/listar_usuario', methods=['GET', ])
def listar_usuario():
    dao = UsuarioDAO(get_db())
    usuario_db = dao.listar()
    return render_template("listar_usuario.html", usuario=usuario_db)


@app.route('/cadastro_catalogo', methods=['GET', 'POST'])
def cadastro_catalogo():
    if request.method == "POST":
        nome = request.form['nome']
        genero = request.form['genero']
        sinopse = request.form['sinopse']
        duracao = request.form['duracao']
        dt_lancamento = request.form['dt_lancamento']

        catalogo = Catalogo(nome, genero, sinopse,
                duracao, dt_lancamento);

        dao = CatalogoDAO(get_db())
        codigo = dao.inserir(catalogo)

        if codigo > 0:
            flash("Cadastrado com sucesso! Código %d" % codigo, "success")
        else:
            flash("Erro ao cadastrar!", "danger")

    vartitulo = "Cadastro de Catalogo"
    return render_template("cadastro_catalogo.html", titulo=vartitulo)


@app.route('/listar_catalogo', methods=['GET', ])
def listar_Catalogo():
    dao = CatalogoDAO(get_db())
    catalogo_db = dao.listar()
    return render_template("listar_catalogo.html", catalogo=catalogo_db)


@app.route('/cadastrar_plano', methods=['GET', 'POST'])
def cadastrar_Plano():
    if request.method == "POST":
        valor = request.form['valor']
        categoria = request.form['categoria']

        plano = Plano(valor, categoria)

        dao = PlanoDAO(get_db())
        codigo = dao.inserir(plano)

        if codigo > 0:
            flash("Cadastrado com sucesso! Código %d" % codigo, "success")
        else:
            flash("Erro ao cadastrar!", "danger")

    vartitulo = "Cadastro de Plano"
    return render_template("plano-cadastrar.html", titulo=vartitulo)


@app.route('/listar_plano', methods=['GET', ])
def listar_Plano():
    dao = PlanoDAO(get_db())
    plano_db = dao.listar()
    return render_template("listar_plano.html", plano=plano_db)


# @app.route('/cadastrar_saida', methods=['GET', 'POST'])
# def cadastrar_saida():
#    daoUsuario = UsuarioDAO(get_db())
#    daoPlanta = PlantaDAO(get_db())
#
#    if request.method == "POST":
#
#        dtsaida = request.form['dtsaida']
#        usuario = request.form['usuario']
#        planta = request.form['planta']
#        saida = Saida(usuario, planta, dtsaida)
#
#        daoSaida = SaidaDAO(get_db())
#        codigo = daoSaida.inserir(saida)
#        if codigo > 0:
#            flash("Saída cadastrada com sucesso! Código %d" % codigo, "success")
#        else:
#            flash("Erro ao registrar saída!", "danger")


#    usuarios_db = daoUsuario.listar()
#    plantas_db = daoPlanta.listar()
#    return render_template("saida-cadastrar.html",
#                           usuarios=usuarios_db, plantas=plantas_db)


# @app.route('/listar_saidas', methods=['GET',])
# def listar_saidas():
#    dao = SaidaDAO(get_db())
#    saidas_db = dao.listar()
#    return render_template("saida-listar.html", saidas=saidas_db)

# @app.route('/excluir_saida/<codigo>', methods=['GET',])
# def excluir_saida(codigo):
#    dao = SaidaDAO(get_db())
#    ret = dao.exlcuir(codigo)
#    if ret == 1:
#        flash(f"Saída {codigo} excluída com sucesso!", "success")
#    else:
#        flash(f"Erro ao excluir saída {codigo}", "danger")
#    return redirect(url_for('listar_saidas'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        email = request.form['email']
        senha = request.form['senha']

        # Verificar dados
        dao = UsuarioDAO(get_db())
        usuario = dao.autenticar(email, senha)

        if usuario is not None:
            session['logado'] = {
                'codigo': usuario[0],
                'email': usuario[1],
                'senha': usuario[9],
            }
            return redirect(url_for('/painel'))
        else:
            flash("Erro ao efetuar login!", "danger")

    return render_template("login.html", titulo="Login")


@app.route('/logout')
def logout():
    session['logado'] = None
    session.clear()
    return redirect(url_for('index'))


@app.route('/cadastro')
def cadastro():
    return render_template("cadastro.html", titulo="Cadastro")


@app.route('/service')
def service():
    return render_template("login.html", titulo="Service")


@app.route('/painel')
def painel():
    return render_template("painel.html", titulo="Painel")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)
