from django.shortcuts import render
from .models import Proyecto

def lista_proyectos(request):
    # SELECT * FROM projects_proyecto;
    proyectos = Proyecto.objects.all().order_by('fecha_creacion')
    # Es buena practica para optimizar las consultas
    # print(Proyecto.objects.count()) 
    # No se recomienda seguir este Ejemplo
    # print(len(proyectos))
    try:
        q = Proyecto.objects.get(titulo='Proyecto 3')    
    except Proyecto.DoesNotExist:
        q = None
    if q:
        print(q)
    else:
        print('No obtuvo resultado')
    return render(
        request, 'projects/lista_proyectos.html' , 
        {'proyectos': proyectos}
    )