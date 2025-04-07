from flask import Flask, request, jsonify
from consulta_orden_argumentos import consultar_orden

app = Flask(__name__)

@app.route("/consulta", methods=["POST"])
def consulta():
    data = request.get_json()  # usa get_json() en lugar de request.json
    orden = data.get("orden", "")
    if not orden:
        return jsonify({"error": "Falta el número de orden"}), 400

    resultado = consultar_orden(orden)
    return jsonify(resultado), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
