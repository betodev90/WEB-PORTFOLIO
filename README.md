# Ejercicio práctico#1: Web Protfolio 

Proyecto web django que permite crear una web básica para llevar un portfolio.


## Sesión #4:

    1. Clonar el repositorio, ubicar en un directorio de su máquina local y ejecutar el comando:
        `git clone https://github.com/betodev90/WEB-PORTFOLIO.git`

    2. Crear y activar un virtualenv con pipenv:
        `pipenv shell`

    3. Instalar las dependencias del proyecto que se acaba de clonar:
        `pipenv install` 
    
    4. Revisar el entorno en el directorio `./vscode` modificar las configuraciones de su equipo local, es decir cambiar el "python.pythonPath": '' del settings.json.
        ej: En Windows
            `pipenv --venv` # para ver el path de donde se crea el virtual enviroment
             "python.pythonPath": "C:\\Users\\<nombre_usuario>\\...\\bin\\Scripts\\python.exe"
    
    5. Realizar los siguientes ajustes al proyecto:
        5.1. Llevar el HTML contact.html a el motor de templates de django y aplicar la reutilización del base.html.
        5.2. Crear la vista que permita renderizar el HTML contac.html.
        5.3. Agregar en el fichero urls.py la vista creada en el paso previo.

    6. Agregar un name representativo en urls.py correspondiente a una vista ejemplo:
        `...
            path('', home, name="home"),
        ...
        ` 
        Hacer lo mismo para las urls y vistas respectivamente.
    
    7. Crear una aplicación de django que solo se encargue de gestionar la administración de proyectos
    del sitio web.
        Recordar el comando: `django-admin.py startapp <name_application>`

    8. Crear el modelo `models.Proyecto` con los siguientes campos `titulo`, `descripcion`, `image`, `url`, `fecha_creacion` y `fecha_modificacion`
        6.1 Representar la clase del modelo Project con el campo `titulo`
        6.2 Ordenamiento predeterminado del modelo Proyecto `ordering = ['fecha_creacion']`    
        6.3 Agregar el modelo al admin.py de la aplicación

    9. Crear una vista que muestre los proyectos ingresados desde el admin.py.

    10. Agregue el template tag `{% url '<name_url>'}` para que la anavegación del proyecto web sea amigable. 
    
## Sesión #5:

    # Verificar el estado del proyecto según lo solicitado en la sesión anterior.

    1. Realizar un cambio en el campo imagen para que sea `null=True`, ejecutar las migracions.
        `python manage.py makemigrations projects`
        `python manage.py migrate projects`
    
    2. Crear un datamigrate con el comando:
        `python manage.py makemigrations projects --empty`
    
    3. En el fichero creado por el paso previo agregar la funcionalidad para que llene la base de datos con objetos proyectos, crear 10 proyectos.

    4. Una vez realizado la logica para crear los objetos ejecutar el comando migrate:
        `python manage.py migrate projects`

    5. Revisar en la vista que lista los proyectos o en el admin si se crearon los registros en la bd.

    6. Revisar los conceptos sobre la API Querysets de Django.

    7. Crear una aplicacion llamada 'blog'.

    8. Crear un `models.Blog` con los siguientes fields (titulo, autor, slug, fecha_creacion, fecha_modificacion, contenido, publicado este campo es un boolean), el campo slug tiene que ser unico.

    9. Ejecutar los comandos de migraciones.

    10. Crear un empty migrations para crear 10 posts.

    11. Agregar los modelos de la aplicacion blog en el admin site de django.

    12. Customizar las funcionalidades del BlogAdmin como busquedas por slug, author, filtro.

    13. Asignar una url para mostrar los posts.

    14. Crear la vista respectiva a `/posts`.

    15. Crear una vista para ver la informacion detallada de un post. (como referencia crear la url respectiva /posts/:id)
        `path('post/<int:pk>/', detalle_post, name='post_detail'),`

    16. Revisar capitulo de tests.
    