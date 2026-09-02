from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

gastos = []


@app.route("/")
def inicio():
    total = sum(gasto["monto"] for gasto in gastos)
    return render_template("index.html", gastos=gastos, total=total)


@app.route("/registrar", methods=["POST"])
def registrar_gasto():
    descripcion = request.form["descripcion"]
    monto = float(request.form["monto"])

    gastos.append({
        "descripcion": descripcion,
        "monto": monto
    })

    return redirect(url_for("inicio"))


@app.route("/eliminar/<int:indice>")
def eliminar_gasto(indice):
    if 0 <= indice < len(gastos):
        gastos.pop(indice)

    return redirect(url_for("inicio"))


@app.route("/salir")
def salir():
    gastos.clear()
    return render_template("index.html", gastos=[], total=0, mensaje="La sesión fue cerrada y los gastos fueron eliminados.")


if __name__ == "__main__":
    app.run(debug=True)
