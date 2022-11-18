from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve

from controller.candidato_controller import ControladorCandidato
from controller.mesa_controller import ControladorMesa
from controller.partido_controller import ControladorPartido
from controller.resultado_controller import ControladorResultado

app = Flask(__name__)
cors = CORS(app)
candidato_controller = ControladorCandidato()
mesa_controller = ControladorMesa()
partido_controller = ControladorPartido()
resultado_controller = ControladorResultado()


def load_file_config():
    with open("config.json") as f:
        data = json.load(f)
    return data


@app.route("/partidos", methods=["GET"])
def listar_partidos():
    lista_partidos = partido_controller.index()
    return jsonify(lista_partidos)


@app.route("/partido", methods=["POST"])
def crear_partido():
    info_partido = request.get_json()
    partido_creado = partido_controller.create(info_partido)
    return jsonify(partido_creado)


@app.route("/partido/<string:id>", methods=["GET"])
def mostrar_partido(id):
    par = partido_controller.show(id)
    return jsonify(par)


@app.route("/partido/<string:id>", methods=["PUT"])
def actualizar_partido(id):
    info_partido = request.get_json()
    partido_actualizado = partido_controller.update(id, info_partido)
    return jsonify(partido_actualizado)


@app.route("/partido/<string:id>", methods=["DELETE"])
def eliminar_partido(id):
    resp = partido_controller.delete(id)
    return jsonify(resp)

@app.route("/candidatos", methods=["GET"])
def listar_candidatos():
    lista_candidatos = candidato_controller.index()
    return jsonify(lista_candidatos)


@app.route("/candidato", methods=["POST"])
def crear_candidato():
    info_candidato = request.get_json()
    candidato_creado = candidato_controller.create(info_candidato)
    return jsonify(candidato_creado)


@app.route("/candidato/<string:id>", methods=["GET"])
def mostrar_candidato(id):
    can = candidato_controller.show(id)
    return jsonify(can)


@app.route("/candidato/<string:id>", methods=["PUT"])
def actualizar_candidato(id):
    info_candidato = request.get_json()
    candidato_actualizado = candidato_controller.update(id, info_candidato)
    return jsonify(candidato_actualizado)


@app.route("/candidato/<string:id>", methods=["DELETE"])
def eliminar_candidato(id):
    resp = candidato_controller.delete(id)
    return jsonify(resp)

@app.route("/mesas", methods=["GET"])
def listar_mesas():
    lista_mesas = mesa_controller.index()
    return jsonify(lista_mesas)


@app.route("/mesa", methods=["POST"])
def crear_mesa():
    info_mesa = request.get_json()
    mesa_creada = mesa_controller.create(info_mesa)
    return jsonify(mesa_creada)


@app.route("/mesa/<string:id>", methods=["GET"])
def mostrar_mesa(id):
    mesa = mesa_controller.show(id)
    return jsonify(mesa)


@app.route("/mesa/<string:id>", methods=["PUT"])
def actualizar_mesa(id):
    info_mesa = request.get_json()
    mesa_actualizada = mesa_controller.update(id, info_mesa)
    return jsonify(mesa_actualizada)


@app.route("/mesa/<string:id>", methods=["DELETE"])
def eliminar_mesa(id):
    resp = mesa_controller.delete(id)
    return jsonify(resp)

@app.route("/resultados", methods=["GET"])
def listar_resultados():
    lista_resultados = resultado_controller.index()
    return jsonify(lista_resultados)


@app.route("/resultado", methods=["POST"])
def crear_resultado():
    info_resultado = request.get_json()
    resultado_creado = resultado_controller.create(info_resultado)
    return jsonify(resultado_creado)


@app.route("/resultado/<string:id>", methods=["GET"])
def mostrar_resultado(id):
    resul = resultado_controller.show(id)
    return jsonify(resul)


@app.route("/resultado/<string:id>", methods=["PUT"])
def actualizar_resultado(id):
    info_resultado = request.get_json()
    resultado_actualizado = resultado_controller.update(id, info_resultado)
    return jsonify(resultado_actualizado)


@app.route("/resultado/<string:id>", methods=["DELETE"])
def eliminar_resultado(id):
    resp = resultado_controller.delete(id)
    return jsonify(resp)

@app.route("/votos-candidatos", methods=["POST"])
def votos_candidatos():
    q = request.get_json()
    votos = resultado_controller.find_by_query(q)
    return jsonify(votos)



if __name__ == "__main__":
    data_config = load_file_config()
    print(f"Server running: http://{data_config['url-backend']}:{data_config['port']}")
    serve(app, host=data_config["url-backend"], port=data_config["port"])
