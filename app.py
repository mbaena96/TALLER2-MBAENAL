from flask import Flask, render_template, jsonify
from models.perro import Perro
from models.gato import Gato
from models.huron import Huron
from models.boa_constrictor import Boa_Constrictor

app = Flask(__name__, template_folder='views')

perro1 = Perro('Rocky', 2, 5.0)
gato1 = Gato('Armin', 3, 5.0)
huron1 = Huron('Juancho', 4, 2.0, 'USA', 10.0)
boa1 = Boa_Constrictor('Cecilia', 2, 7.0, 'Brasil', 15.0)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/perro')
def perro():
    return jsonify({'data': perro1.hacer_sonido()})

@app.route('/gato')
def gato():
    return jsonify({'data': gato1.hacer_sonido()})

@app.route('/huron')
def huron():
    return jsonify({'data': huron1.hacer_sonido()})

@app.route('/boa')
def boa():
    return jsonify({'data': boa1.hacer_sonido()})

if __name__ == '__main__':
    app.run(debug=True)