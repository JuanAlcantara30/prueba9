from flask import Flask, render_template, request, redirect, url_for, jsonify
import sqlite3
import os

app = Flask(__name__, template_folder='../templates', static_folder='../static')

def conectar_db():
    return sqlite3.connect("database.db")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/servicios")
def servicios():
    return render_template("servicios.html")

@app.route("/nosotros")
def nosotros():
    return render_template("nosotros.html")

@app.route("/membresias")
def membresias():
    return render_template("membresias.html")

@app.route("/blog")
def blog():
    return render_template("blog.html")

@app.route("/agenda", methods=["GET", "POST"])
def agenda():
    if request.method == "POST":
        nombre = request.form["nombre"]
        telefono = request.form["telefono"]
        servicio = request.form["servicio"]
        fecha = request.form["fecha"]
        hora = request.form["hora"]

        try:
            conn = conectar_db()
            cursor = conn.cursor()
            cursor.execute("""
            INSERT INTO citas (nombre, telefono, servicio, fecha, hora)
            VALUES (?, ?, ?, ?, ?)
            """, (nombre, telefono, servicio, fecha, hora))
            conn.commit()
            conn.close()
        except:
            pass # Vercel is read only

        return render_template("success.html", nombre=nombre, fecha=fecha, hora=hora)

    return render_template("agenda.html")

@app.route("/api/cita", methods=["POST"])
def crear_cita_api():
    data = request.get_json()
    nombre = data.get("nombre")
    telefono = data.get("telefono")
    servicio = data.get("servicio")
    fecha = data.get("fecha")
    hora = data.get("hora")

    if not all([nombre, telefono, servicio, fecha, hora]):
        return jsonify({"error": "Faltan datos obligatorios"}), 400

    try:
        conn = conectar_db()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO citas (nombre, telefono, servicio, fecha, hora)
            VALUES (?, ?, ?, ?, ?)
        """, (nombre, telefono, servicio, fecha, hora))
        conn.commit()
        conn.close()
    except:
        pass

    return jsonify({"status": "Cita registrada con éxito"}), 201

@app.route("/demo")
def demo():
    return render_template("demo.html")

@app.route("/contacto")
def contacto():
    return render_template("contacto.html")

if __name__ == "__main__":
    app.run(debug=True, port=5000)
