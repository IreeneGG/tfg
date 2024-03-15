from fastapi import FastAPI #para crear api web
import requests #realizar solicitud
from bs4 import BeautifulSoup #analizar html
from lxml import etree #xpath

app = FastAPI()

@app.get("/obtener_valor_celda")
def obtener_valor_celda():
    # URL de la página web
    url = "http://www.saihebro.com/saihebro/index.php?url=/datos/ficha/estacion:P006"

    # Hacer la solicitud HTTP y obtener el contenido HTML
    response = requests.get(url)
    html = response.text

    # Crear un objeto BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')
    dom = etree.HTML(str(soup))

    # Obtener valores de la celda
    celda_valor1 = dom.xpath('//*[@id="capa1"]/div/div/table[3]/tbody/tr[2]/td[7]')[0].text
    celda_valor2 = dom.xpath('//*[@id="capa1"]/div/div/table[4]/tbody/tr[2]/td[7]')[0].text
    celda_valor3 = dom.xpath('//*[@id="capa1"]/div/div/table[5]/tbody/tr[2]/td[7]')[0].text


    return {"celda_valor1 (Mes anterior): ": celda_valor1, " celda_valor2 (Mes en curso): ": celda_valor2, " celda_valor3 (año anterior):": celda_valor3}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
