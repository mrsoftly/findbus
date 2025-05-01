from flask import Flask, render_template, request
import requests

url = 'https://api.xor.cl/red/bus-stop/'
respuesta = []
sinserv = []
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}




app = Flask(__name__)
@app.route("/")
def home():
    return render_template("home.html")
@app.route('/buscador', methods=['POST'])
def buscar():
    paradero = request.form.get("paradero")
    response = requests.get(url + f'{paradero}', headers=headers)
    if response.status_code !=200:
        return response.status_code
    datos = response.json()
    respuesta.clear()

    for serv in datos.get('services',{}):
        paradero = datos['name']
        id = serv['id']
        valid = serv['valid']
        status = serv['status_description']

        if valid == False:
            sinserv.append(({"micro":id,"valid":valid,"status":status}))
        for bus in serv.get('buses',{}):
            distancia = bus['meters_distance']
            tp_min = bus['min_arrival_time']
            tp_max = bus['max_arrival_time']
            respuesta.append(({"paradero":paradero,"micro": id,"estado":status,"status":valid,"distancia":distancia,"min":tp_min,"max":tp_max}))
    resp = list(zip(sinserv,respuesta))
    print(resp)
    return render_template('buscador.html',
                           respuesta = respuesta
                           )

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)