from flask import Flask, jsonify #jsonify--> convertir datos en json
import xml.etree.ElementTree as ET #analizar xml
import requests #realizar solicitudes http

#crear aplicacion flask
app = Flask(__name__)

#definir ruta
@app.route('/informacion', methods=['GET'])
def obtener_informacion():
    # La URL del XML
    url = "https://www.aemet.es/xml/municipios/localidad_09408.xml"

    # Obtener el contenido del XML desde la URL
    response = requests.get(url)
    xml_data = response.text

    # Parsear el XML desde el contenido obtenido
    root = ET.fromstring(xml_data)

    # Lista para almacenar los datos
    datos = []

    # Obtener información del nodo principal
    nombre = root.find(".//nombre").text
    provincia = root.find(".//provincia").text
    elaborado = root.find(".//elaborado").text
    datos.append({"Nombre": nombre, "Provincia": provincia, "Elaborado": elaborado})

    # Obtener información de cada día
    for dia in root.findall(".//dia"):
        fecha = dia.get("fecha")
        maxima = dia.find(".//temperatura/maxima").text
        minima = dia.find(".//temperatura/minima").text
        estado_cielo = dia.find(".//estado_cielo").get("descripcion")
        viento_direccion = dia.find(".//viento/direccion").text
        viento_velocidad = dia.find(".//viento/velocidad").text

        datos_dia = {
            "Fecha": fecha,
            "Máxima": maxima,
            "Mínima": minima,
            "Estado Cielo": estado_cielo,
            "Viento": f"{viento_direccion} {viento_velocidad} km/h"
        }
        datos.append(datos_dia)

    return jsonify(datos)

if __name__ == '__main__':
    app.run(debug=True)
