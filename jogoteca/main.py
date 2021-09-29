from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = 'LP2'

class Jogo:
    def __init__(self, nome, categoria, console):
        self._nome = nome
        self._categoria = categoria
        self._console = console

class Usuario:
    def __init__(self, username, nome, password):
        self._username = username
        self._nome = nome
        self._password = password

jogo1 = Jogo('Tetrix', 'Puzzle', 'Super Nintendo')
jogo2 = Jogo('Super Mario', 'Aventura', 'Nintendo 64')
jogo3 = Jogo('Sonic', 'Aventura', 'Mega Drive')
jogo4 = Jogo('Sonic2', 'Aventura', 'Mega Drive')
jogo5 = Jogo('Sonic3', 'Aventura', 'Mega Drive')

jogos = [jogo1, jogo2, jogo3, jogo4, jogo5]

usuario1 = Usuario('eli', 'Eliezer Alves', 'admin')
usuario2 = Usuario('admin', 'Administrador', 'admin')

usuarios = {
    usuario1._username: usuario1,
    usuario2._username: usuario2,
}

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

    if request.form['username'] in usuarios:
        if usuarios[request.form['username']]._password == request.form['password']:
            session['user_logged'] = request.form['username']
            flash(request.form['username'] + ' logou com sucesso!')
            next_page = request.form['callback_url']
            return redirect("/{}".format(next_page))
    
    flash('Falha ao realizar login para ' + request.form['username'] + '!')
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
    
    titulo = "Lista de Jogos"
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
    jogos.append(novoJogo)

    return redirect('/')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
    