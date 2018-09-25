from django.shortcuts import render

# Create your views here.
def home(request):
    m = 'Ingresando a la primera vista'
    return render(request, 'core/home.html', {'mensaje': m})

def acercade(request):
    return render(request, 'core/about.html')

def contacto(request):
    return render(request, 'core/contact.html')
