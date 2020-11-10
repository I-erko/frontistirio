from flask import Flask, render_template
from flask_mysqldb import MySQL


app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'frontistirio'
mysql = MySQL(app)


#MAIN'S ROUTES

@app.route('/')
def index():
    return render_template('index.html')

#ADMIN'S ROUTES

@app.route('/listaEvento')
def listaEvento():
    return render_template('lista-evento.html')

@app.route('/crearEvento')
def crearEvento():
    return render_template('crear-evento.html')

@app.route('/listaCategoria')
def listaCategoria():
    return render_template('lista-categoria.html')

@app.route('/crearCategoria')
def crearCategoria():
    return render_template('crear-categoria.html')

@app.route('/listaInvitado')
def listaInvitado():
    return render_template('lista-invitado.html')

@app.route('/crearInvitado')
def crearInvitado():
    return render_template('crear-invitado.html')

@app.route('/listaAdmin')
def listaAdmin():
    return render_template('lista-admin.html')

@app.route('/crearAdmin')
def crearAdmin():
    return render_template('crear-admin.html')


if __name__ == '__main__':
    app.run(port = 3000, debug = True)

