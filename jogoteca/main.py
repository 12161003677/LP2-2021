from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = 'LP2'

class Jogo:
    def __init__(self, nome, categoria, console):
        self._nome = nome
        self._categoria = categoria
        self._console = console

jogo1 = Jogo('Tetrix', 'Puzzle', 'Super Nintendo')
jogo2 = Jogo('Super Mario', 'Aventura', 'Nintendo 64')
jogo3 = Jogo('Sonic', 'Aventura', 'Mega Drive')
jogo4 = Jogo('Sonic2', 'Aventura', 'Mega Drive')
jogo5 = Jogo('Sonic3', 'Aventura', 'Mega Drive')

jogos = [jogo1, jogo2, jogo3, jogo4, jogo5]

@app.route("/login")
def login():

    return render_template('login.html')

@app.route("/auth", methods=['POST'])
def auth():

    if 'mestra' == request.form['senha']:
        session['user_logged'] = request.form['usuario']
        flash(request.form['usuario'] + ' logou com sucesso!')
        return redirect('/')
    
    else:
        flash('Falha ao realizar login para ' + request.form['usuario'] + '!')
        return redirect('/login')

@app.route("/logout")
def logout():

    session['user_logged'] = None
    flash('Sessão finalizada!')
    
    return redirect('/login')

@app.route("/")
def index():
    
    titulo = "Lista de Jogos"

    return render_template('lista.html', titulo = titulo, jogos = jogos)

@app.route("/create")
def create():
    titulo = "Novo Jogo"
    return render_template('novo.html', titulo = titulo)


@app.route("/store", methods=['POST'])
def store():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']

    novoJogo = Jogo(nome, categoria, console)
    jogos.append(novoJogo)

    return redirect('/')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)