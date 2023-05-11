from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.contrib import messages
from django import forms


# Create your views here.
def base(request):
    return render(request, 'WebJecApp/Base.html')

def home(request):

    return render(request, 'WebJecApp/Home.html')

def comunidad(request):

    return render(request, 'WebJecApp/Comunidad.html')

def mision(request):

    return render(request, 'WebJecApp/Mision.html')

def contacto(request):

    return render(request, 'WebJecApp/Contacto.html')

def mensaje(request):

    return render(request, 'WebJecApp/Mensaje.html')

def index(request):

    return render(request, 'WebJecApp/Index.html')


class ContactForm(forms.Form):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    phone_number = forms.IntegerField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)


from django.core.mail import EmailMessage
from django.shortcuts import render
from django.contrib import messages


def contact_view(request):
    if request.method == 'POST':
        # Obtener información del formulario
        name = request.POST.get('Name')
        email = request.POST.get('Email')
        phone_number = request.POST.get('Phone_Number')
        message = request.POST.get('Message')

        # Validar que todos los campos obligatorios se han completado
        if not (name and email and phone_number and message):
            messages.error(request, 'Debe completar todos los campos para enviar el mensaje.')
            return render(request, 'WebJecApp/Mensaje.html')

        # Validar que el campo Phone_Number solo contiene números
        if not phone_number.isdigit():
            messages.error(request, 'El campo "Número de teléfono" solo debe contener números.')
            return render(request, 'WebJecApp/Mensaje.html')

        # Construir el correo electrónico
        subject = f"Nuevo mensaje de {name}"
        body = f"Nombre: {name}\nEmail: {email}\nTeléfono: {phone_number}\nMensaje: {message}"
        from_email = 'lukasredfield01@gmail.com'
        to_email = ['lukasredfield@gmail.com']

        # Enviar el correo electrónico
        email = EmailMessage(subject, body, from_email, to_email)
        email.send()
        messages.success(request, '¡Mensaje enviado, nos contactaremos a la brevedad! "Pidan, y se les dará; busquen, y encontrarán; llamen, y se les abrirá. 8 Porque todo el que pide, recibe; el que busca, encuentra; y al que llama, se le abrirá.  (Mateo 7:7-8)"')
        return render(request, 'WebJecApp/Mensaje.html')
    else:
        return render(request, 'WebJecApp/Mensaje.html')


        


