from django.db import models

class Proveedores(models.Model):
    nombre = models.CharField(max_length=255)
    img = models.FileField(upload_to='image-svc')
    stock = models.IntegerField()
    noVenta = models.IntegerField()
    status = models.CharField(max_length=20)