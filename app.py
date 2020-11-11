from flask import Flask, render_template
from flask_mysqldb import MySQL


app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'frontistirio'
mysql = MySQL(app)


#-------MAIN'S ROUTES----------

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registro')
def registro():
    return render_template('registro.html')

@app.route('/invitados')
def invitados():
    return render_template('invitados.html')

@app.route('/conferencia')
def conferencia():
    return render_template('conferencia.html')

@app.route('/calendario')
def calendario():
    return render_template('calendario.html')



#-----ADMIN'S ROUTES-------

#Login
@app.route('/login')
def login():
    return render_template('login.html')

#Evento
@app.route('/listaEvento')
def listaEvento():
    return render_template('lista-evento.html')

@app.route('/crearEvento')
def crearEvento():
    return render_template('crear-evento.html')

@app.route('/editarEvento')
def editarEvento():
    return render_template('editar-evento.html')

#Categoria
@app.route('/listaCategoria')
def listaCategoria():
    return render_template('lista-categoria.html')

@app.route('/crearCategoria')
def crearCategoria():
    return render_template('crear-categoria.html')

@app.route('/editarCategoria')
def editarCategoria():
    return render_template('editar-categoria.html')

#Invitado    
@app.route('/listaInvitado')
def listaInvitado():
    return render_template('lista-invitado.html')

@app.route('/crearInvitado')
def crearInvitado():
    return render_template('crear-invitado.html')

@app.route('/editarInvitado')
def editarInvitado():
    return render_template('editar-invitado.html')

#Admin
@app.route('/listaAdmin')
def listaAdmin():
    return render_template('lista-admin.html')

@app.route('/crearAdmin')
def crearAdmin():
    return render_template('crear-admin.html')

@app.route('/editarAdmin')
def editarAdmin():
    return render_template('editar-admin.html')


if __name__ == '__main__':
    app.run(port = 3000, debug = True)
