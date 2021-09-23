from flask import Flask, render_template

app = Flask(__name__)

class Jogo:
    def __init__(self, nome, categoria, console):
        self._nome = nome
        self._categoria = categoria
        self._console = console

@app.route("/")

def index():
    
    titulo = "Lista de Jogos"
    jogo1 = Jogo('Tetrix', 'Puzzle', 'Super Nintendo')
    jogo2 = Jogo('Super Mario', 'Aventura', 'Nintendo 64')
    jogo3 = Jogo('Sonic', 'Aventura', 'Mega Drive')
    jogo4 = Jogo('Sonic2', 'Aventura', 'Mega Drive')
    jogo5 = Jogo('Sonic3', 'Aventura', 'Mega Drive')

    jogos = [jogo1, jogo2, jogo3, jogo4, jogo5]

    return render_template('lista.html', titulo = titulo, jogos = jogos)
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)