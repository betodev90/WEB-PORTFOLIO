from django.db import models

# Create your models here.

class Proyecto(models.Model):    
    titulo = models.CharField(verbose_name="Title", max_length=120, 
    help_text='Este campo es referente al titulo del proyecto')
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='proyecto/', null=True, blank=True)
    url = models.URLField()
    fecha_creacion = models.DateTimeField(auto_now=True)
    fecha_modificacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"
        ordering = ['-fecha_creacion']

    


    