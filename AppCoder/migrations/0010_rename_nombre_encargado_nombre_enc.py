# Generated by Django 4.1.3 on 2022-12-23 02:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0009_edificio_mail_contacto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='encargado',
            old_name='nombre',
            new_name='nombre_enc',
        ),
    ]
