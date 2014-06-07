from django.db import models

# Create your models here.

class settings(models.Model):

    '''def image_path(self, filename):
        ruta = "Setting/%s/%s" % (self.settings_name, str(filename))
        return ruta'''

    settings_name = models.CharField(max_length=200)
    my_name = models.CharField(max_length=200)
    my_job = models.CharField(max_length=200)
    my_description = models.TextField(max_length=500)
    status = models.BooleanField(default=False)

    class Met:
        verbose_name = "Configuracion de la Web"
        verbose_name_plural = "Configuraciones de la Web"
