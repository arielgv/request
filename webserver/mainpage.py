from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI()

@app.get('/')
def listado():
    listado = list(range(10))
    return listado

@app.get('/contact')
def contacto():
    diccionario= { "Nombre": "Ariel Gustavo","Edad" : 37, "Direccion": "Santa Fe", "Numero": 391485935}
    return diccionario


@app.get('/webpage', response_class=HTMLResponse)
def pagina():
    return  """
    <html>
        <head>
            <title> Este es el titulo en la pagina HTML</title>
        </head>
        <body> <h1> Aqui poner codigo HTML! </h1>
        <iframe width="1068" height="601" src="https://www.youtube.com/embed/t6z6ORjEqfs" title="Best of Classic House 2000s (Roger Sanchez, Supermode, Fake Blood, Axwell, A. Gaudino, Daft Punk...)" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
        </body>
    </html>
    """