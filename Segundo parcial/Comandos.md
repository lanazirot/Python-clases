# COMANDOS

## Inicializar entorno
    py -3 -m venv .venv

## Activar
    .venv\scripts\activate

## Instalar django
    pip install django

## Crear app
    django-admin startproject <Nombre>

## Correr servidor
    python manage.py runserver

## Crear app desde servidpr
    python manage.py startapp <Nombre>

## Agregar pagina
    Se agrega a los setting, urls.py....

## Registrar modelos 
    En admin.py => admin.site.register()

## Mostrar listado migraciones
[] No ejecutadas ..
    python manage.py showmigrations

## Ejecutar migraciones
    python manage.py migrate

## Cuando creas un modelo, agregarlo a las apps de mainapp y despues
    python manage.py makemigrations
## y despues ejecuta el de python manage.py migrate

## Crear superusuario
    python manage.py createsuperuser


## FLASK

## Correr codigo = flask db init = crear carpetas proyecto
## Empezar migraciones = flask db migrate = crear tabla default
## Hacer migraciones = flask db upgrade = actualizar

# flas-wft: forms en flask