from django.db import models

class Proveedores(models.Model):
    nombre = models.CharField(max_length=255)
    img = models.FileField(upload_to='image-svc')
    stock = models.IntegerField()
    noVenta = models.IntegerField()
    status = models.CharField(max_length=20)

    class Meta:
        db_table = 'principal_proveedores'

class Marcas(models.Model):
    nombre = models.CharField(max_length=255)
    img = models.FileField(upload_to='image-svc')
    stock = models.IntegerField()
    noVenta = models.IntegerField()
    status = models.CharField(max_length=20)
    proveedor = models.ForeignKey(Proveedores, on_delete=models.SET_NULL, null=True) #Tambien esta el Cascade

    class Meta:
        db_table = 'principal_marcas'