from django import forms


class EdificioFormulario(forms.Form):
    nombre_fantasia = forms.CharField()
    direccion = forms.CharField()
    numero = forms.IntegerField()
    mail_contacto = forms.CharField()


class EquipoFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    edad = forms.IntegerField()
    num_contacto = forms.IntegerField()
    mail_contacto = forms.CharField()


class EncargadoFormulario(forms.Form):
    nombre = forms.CharField()
    edad = forms.IntegerField()
    num_contacto = forms.IntegerField()
    mail_contacto = forms.CharField()
