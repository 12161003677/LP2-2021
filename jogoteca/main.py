from flask import Flask, render_template, request, redirect, session, flash

from dao import JogoDao, UsuarioDao
from flask_mysqldb import MySQL
from models import Jogo, Usuario

app = Flask(__name__)
app.secret_key = 'LP2'

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'admin'
app.config['MYSQL_DB'] = 'jogoteca'
app.config['MYSQL_PORT'] = 3306
db = MySQL(app)

jogoDao = JogoDao(db)
usuarioDao = UsuarioDao(db)


def session_valid():
    if 'user_logged' not in session or session['user_logged'] == None:
        return False
    return True

@app.route("/login")
def login():
    callback_url = request.args.get('callback_url') or ""

    return render_template('login.html', callback_url=callback_url)

@app.route("/auth", methods=['POST'])
def auth():
    usuario = usuarioDao.buscaPorId(request.form['username'])

    if usuario:
        if usuario._senha == request.form['senha']:
            session['user_logged'] = request.form['username']
            flash(request.form['username'] + ' logou com sucesso!')
            next_page = request.form['callback_url']
            return redirect("/{}".format(next_page))
    
    flash('Falha ao realizar login para: ' + request.form['username'] + '!')
    return redirect('/login')

@app.route("/logout")
def logout():

    session['user_logged'] = None
    flash('Sessão finalizada!')
    
    return redirect('/login')

@app.route("/")
def index():
    if not session_valid():
        return redirect('/login?callback_url=')
    
    titulo = "Index"
    return render_template('index.html', titulo = titulo)

@app.route("/game-list")
def gameList():
    if not session_valid():
        return redirect('/login?callback_url=')
    
    titulo = "Lista de Jogos"
    jogos = jogoDao.listar()
    return render_template('lista.html', titulo = titulo, jogos = jogos)

@app.route("/create")
def create():
    if not session_valid():
        return redirect('/login?callback_url=create')

    titulo = "Novo Jogo"
    return render_template('novo.html', titulo = titulo)


@app.route("/store", methods=['POST'])
def store():
    if not session_valid():
        return redirect('/login?callback_url=create')

    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']

    novoJogo = Jogo(nome, categoria, console)
    jogoDao.salvar(novoJogo)

    return redirect('/game-list')

@app.route("/edit/<int:id>")
def edit(id):
    if not session_valid():
        return redirect('/login?callback_url=create')

    titulo = "Editar Jogo"
    jogo = jogoDao.buscaPorId(id)
    return render_template('editar.html', titulo = titulo, jogo = jogo)

@app.route("/update", methods=['POST'])
def update():
    if not session_valid():
        return redirect('/login?callback_url=create')

    id = request.form['id']
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']

    jogo = Jogo(nome, categoria, console, id)
    jogoDao.editar(jogo)

    return redirect('/game-list')

@app.route("/delete/<int:id>")
def delete(id):
    if not session_valid():
        return redirect('/login?callback_url=create')

    jogoDao.deletar(id)

    return redirect('/game-list')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
    