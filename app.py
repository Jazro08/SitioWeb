from flask import Flask, render_template, request, jsonify
import re
from datetime import datetime
#Libreria necesaria para graficar
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io
import base64
import pandas as pd
import webbrowser

app = Flask(__name__)


@app.route("/") #ruta raiz donde lo busca del directorio de acceso web
def home():
    return render_template("base.html")


@app.route('/proyecto/')
def proyecto():
    return render_template("base.html", datos=[])



@app.route("/impresoras-multifuncionales")
def impresoras_multi():
    return render_template("imp_multifuncion.html")

@app.route("/clientes_data")
def clientes_data():
    labels = ["P1", "P2", "P3", "P4"] #Del 1 al 10
    usuarios_a = [9.5, 8.0, 7.5, 10.0]
    usuarios_b = [10.0, 6.5, 8.0, 8.0]
    usuarios_c = [6.5, 9.5, 7.5, 9.0]
    usuarios_d = [9.0, 5.5, 8.5, 9.5]
    usuarios_e = [8.5, 6.5, 7.5, 10.0]
    return jsonify(labels=labels, usuarios_a=usuarios_a, usuarios_b=usuarios_b, usuarios_c=usuarios_c, usuarios_d=usuarios_d, usuarios_e=usuarios_e)

@app.route("/clientes")
def opinion_clientes():
    valoracion = ["atencion", "calidad", "satisfaccion", "confianza"]
    puntuacion = [10, 8, 8.5, 9.5]

    plt.figure(figsize=(100, 60))
    plt.plot(valoracion, puntuacion, marker='o', linestyle='--', color='green')
    plt.title("Valoracion de nuestros productos y servicio")
    plt.xlabel("Valoracion")
    plt.ylabel("Puntuacion")
    # Guardar grafico en un buffer
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    plt.close()
    buf.seek(0)
    # Codificar imagen en base64
    imagen = base64.b64encode(buf.getvalue()).decode('utf8')
    labels = ["P1", "P2", "P3", "P4"] #Del 1 al 10
    usuarios_a = [9.5, 8.0, 7.5, 10.0]
    usuarios_b = [10.0, 6.5, 8.0, 8.0]
    usuarios_c = [6.5, 9.5, 7.5, 9.0]
    usuarios_d = [9.0, 5.5, 8.5, 9.5]
    usuarios_e = [8.5, 6.5, 7.5, 10.0]
    return render_template('grafico.html', labels=labels, usuarios_a=usuarios_a, usuarios_b=usuarios_b, usuarios_c=usuarios_c, usuarios_d=usuarios_d, usuarios_e=usuarios_e, imagen=imagen)

@app.route('/grafico_ventas_productos/')
def grafico_ventas_productos():
    df = pd.read_csv('data/ventas_anuales.csv')
    #Agrupar por producto y sumar ventas
    resumen = df.groupby('Nombre Producto')['Ventas Totales'].sum().sort_values(ascending=False)

    plt.figure(figsize=(6, 3.5))
    resumen.plot(kind='bar', color='orange')
    plt.title('Ventas Totales por Producto')
    plt.xlabel('Producto')
    plt.ylabel('Ventas Totales')
    plt.tight_layout()
    #Convertir a imagen base64
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    imagen = base64.b64encode(buf.getvalue()).decode('utf8')
    plt.close()
    return render_template('index1.html', imagen=imagen)


#Ejemplo de otra ruta con paso de valor
@app.route("/hello/<name>")
def hello_there(name):
   now = datetime.now()
   formatted_now = now.strftime("%A, %d %B, %Y at %X")
   return f"Hola {name}! la fecha y hora actual es: {formatted_now}"

@app.route("/producto/<int:id>")
def mostrar_producto(id):
    return f"Mostrando producto con ID {id}"

@app.route("/temperatura/<float:grados>")
def mostrar_temperatura(grados):
    return f"La temperatura es {grados}°C"

@app.route("/sumar/<int:a>/<int:b>")
def sumar(a, b):
    resultado = a + b
    return f"La suma de {a} y {b} es {resultado}°C"

@app.route("/bienvenida/<nombre>")
def bienvenida(nombre):
    return render_template("index.html", nombre=nombre)

@app.route("/servicios") 
def servicios(): 
    lista_servicios = ["Consulta", "Odontología", "Laboratorio", "Urgencias"] 
    return render_template("index.html", servicios=lista_servicios)


@app.route("/fecha") 
def mostrar_fecha(): 
   ahora = datetime.now().strftime("%d/%m/%Y %H:%M") 
   return render_template("index.html", ahora=ahora)

if __name__ == "__main__":
    app.run(debug=True)

"""@app.route("/paciente") 
def paciente(): 
    datos_paciente = { 
        "nombre": "Carlos Gómez", 
        "servicio": "Consulta General", 
        "fecha": "28/04/2025",
        "edad": 35
    } 
    return render_template("index.html", paciente=datos_paciente)  


@app.route("/pacientes/")
def lista_pacientes():
   pacientes = [
      {"nombre":"Ana Ruiz", "edad":30, "servicio":"Odontologia"},
      {"nombre":"Luis Martinez", "edad":45, "servicio":"Pediatria"},
      {"nombre":"Laura Gomez", "edad":28, "servicio":"Laboratorio"}
   ]
   return render_template("index.html", pacientes=pacientes)






matplotlib.use('Agg')  # Evita errores con backends GUI en Flask

@app.route ('/grafico_ventas_productos/')
def grafico_ventas_productos():

# cargar archivo csv
  df = pd.read_csv('data/Ventas_anuales_actualizado1.csv')

# agrupar por producto y sumar ventas
  resumen = df.groupby('Nombre Producto')['Ventas Totales'].sum().sort_values(ascending=False)

#crear grafico
  plt.figure(figsize=(6, 3.5))
  resumen.plot(kind='bar', color='orange')
  plt.title('Ventas Totales por Producto')
  plt.xlabel('Producto')
  plt.ylabel('Ventas Totales')
  plt.xticks(rotation=4"""