from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/executar", methods=["POST"])
def executar():
    dados = request.json
    x = float(dados["x"])
    y = float(dados["y"])

    resultado = x + y  # seu algoritmo aqui

    return jsonify({"resultado": resultado})

if __name__ == "__main__":
    app.run()
