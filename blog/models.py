from django.db import models

# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=150)
    slug = models.SlugField(max_length=100, unique=True)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    publicado = models.BooleanField(default=True)
    contenido = models.TextField(default='')
    fecha_creacion = models.DateTimeField(auto_now=True)
    fecha_modificacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
    

