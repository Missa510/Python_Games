#Pagina web con Flask y Django en Pyhton
#Ahora con MySQL :3
from flask import *
from flask_mysqldb import MySQL

app = Flask(__name__) #Para verificar que Index sea el archivo principal

app.config['MySQL_HOST'] = 'localhost'
app.config['MySQL_USER'] = 'root'
app.config['MySQL_PASSWORD'] = ''
app.config['MySQL_DB'] = 'bd_flaskuwu'

mysql = MySQL(app)

@app.route('/') #Que la primera página sea Idex
def home():
    return render_template('Home.html')

@app.route('/AboutMe') #Ir a la ruta "Sobre Nosotros"
def AboutMe():
    return render_template('about.html')

@app.route('/Login')
def Login():
    return render_template('form.html')

@app.route('/AddUser', methods=['POST']) #Para agregar usuarios 
def AddUser():
    if request.method == 'POST':
        mail = request.form['mail']
        name = request.form['name']
        tel = request.form['tel']

        cur = mysql.connection.cursor()
        cur.execute('INSTER INTO contactos(fullname_con, telefono_con, email_con) VALUES(%s, %s, %s)',
                    (mail, name, tel))
        mysql.connection.commit()

        print("Email del usuario: "+mail + '\nNombre de registro: ' + name + '\nTeléfono: ' + tel)
        return '<h1 class="display-1 text-center">Recivido :3</h1>'
    

@app.route('/EditUser')
def EditUser():
    return render_template('form.html')

@app.route('/DeleteUser')
def DeleteUser():
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug = True) #La página está en modo de prueba