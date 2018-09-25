from django.shortcuts import render
from .models import Proyecto

def lista_proyectos(request):
    proyectos = Proyecto.objects.all()
    # SELECT * FROM projects_proyecto;
    print(proyectos)
    return render(
        request, 'projects/lista_proyectos.html' , 
        {'proyectos': proyectos}
    )