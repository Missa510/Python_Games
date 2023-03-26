#Pagina web con Flask y Django en Pyhton
from flask import Flask, render_template

app = Flask(__name__) #Para verificar que Index sea el archivo principal

@app.route('/') #Que la primera página sea Idex
def home():
    return render_template('Home.html')

@app.route('/AboutMe') #Ir a la ruta "Sobre Nosotros"
def AboutMe():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug = True) #La página está en modo de prueba