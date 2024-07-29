# tutorial en youtube de FASTAPI

https://www.youtube.com/watch?v=5gwCOje67Js&list=PLHftsZss8mw7pSRpCyd-TM4Mu43XdyB3R&index=5

# Create virtual environment

´´´
python -m venv venv
´´´

# Activar el entorno virtual

venv\Scripts\activate

# Instalar dependencias

pip install -r requirements.txt

# Arrancar la app

escribir en la terminal

```
    uvicorn app.main:app
```

# Arrancar la app con detección de cambios

escribir en la terminal:

```
    uvicorn app.main:app --host 0.0.0.0 --port 5000 --reload
```

# Arrancar la app con detección de cambios y visible en la red

escribir en la terminal: y dentro de la carpeta venv

```
uvicorn app.main:app --host 0.0.0.0 --port 5000 --reload

```

# Documentacion:

Swagger
http://localhost:5000/redoc

http://localhost:5000/doc
