from models import Jogo, Usuario

SQL_DELETA_JOGO = 'delete from jogo where id=%s'
SQL_CRIA_JOGO = 'insert into jogo(nome,categoria,console) values(%s,%s,%s)'
SQL_ATUALIZA_JOGO = 'update jogo set nome=%s,categoria=%s,console=%s where id=%s'
SQL_BUSCA_JOGOS = 'select id, nome, categoria, console from jogo'
SQL_BUSCA_USUARIO_POR_ID = 'select id, nome, senha from usuario where id=%s'
class JogoDao:
    def __init__(self, db):
        self.__db = db

    def salvar(self, jogo):
        cursor = self.__db.connection.cursor()

        if(jogo._id):
            cursor.execute(SQL_ATUALIZA_JOGO, (jogo._nome, jogo._categoria, jogo._console, jogo._id))
        else:
            cursor.execute(SQL_CRIA_JOGO, (jogo._nome, jogo._categoria, jogo._console))
            cursor._id = cursor.lastrowid
        
        self.__db.connection.commit()
        return jogo
    
    def listar(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_JOGOS)
        jogos = traduzJogos(cursor.fetchall())
        return jogos

def traduzJogos(jogos):
    def criaJogoComTupla(tupla):
        return Jogo(tupla[1], tupla[2], tupla[3], id=tupla[0])
    
    return list(map(criaJogoComTupla, jogos))


class UsuarioDao:
    def __init__(self, db):
        self.__db = db

    def buscaPorId(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_USUARIO_POR_ID, (id,))
        dados = cursor.fetchone()
        usuario = traduzUsuario(dados) if dados else None
        return usuario

def traduzUsuario(tupla):
    
    return Usuario(tupla[1], tupla[2], tupla[0])