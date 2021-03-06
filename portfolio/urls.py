"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from core.views import home, acercade, contacto
from projects.views import lista_proyectos
from blog.views import lista_posts, posts_detalle

from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('acerca-de',  acercade, name="about"),
    path('contacto', contacto, name='contact'),
    # URLS PROJECTS
    path('proyectos', lista_proyectos, name='list_projects'),
    # URL BLOG
    path('blog', lista_posts, name='list_posts'),
    path('blog/<int:id>/', posts_detalle, name='post_detail'),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)