from conexion import get_estudiante, insertar_estudiante, update_nombre_estudiante,delete_estudiante
from flask import Flask,request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/insertar_estudiante", methods=['POST'])
def ins_est():
    content = request.get_json(silent=True)
    nombre = content['nombre']
    carne = content['carne']
    carrera = content['carrera']
    return (insertar_estudiante(nombre,carne,carrera))

@app.route("/get_estudiante/<int:carne>", methods=['GET'])
def get_est(carne):
    return (get_estudiante(carne))

@app.route("/update_nombre", methods=['PUT'])
def upd_est():
    content = request.get_json(silent=True)
    id_est = content['id']
    nombre = content['nombre']
    return (update_nombre_estudiante(id_est,nombre))

@app.route("/eliminar_estudiante/<int:id_est>", methods=['DELETE'])
def del_est(id_est):
    return (delete_estudiante(id_est))
if __name__ == "__main__":
    app.run()