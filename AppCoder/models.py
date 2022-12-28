from django.db import models

# Create your models here.


class Edificio(models.Model):
    nombre_fantasia = models.CharField(max_length=40)
    direccion = models.CharField(max_length=40)
    numero = models.IntegerField()
    mail_contacto = models.CharField(max_length=50)


class Encargado(models.Model):
    nombre_enc = models.CharField(max_length=40)
    edad = models.IntegerField()
    num_contacto = models.IntegerField()
    mail_contacto = models.CharField(max_length=50)


class Equipo(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField()
    num_contacto = models.IntegerField()
    mail_contacto = models.CharField(max_length=50)
