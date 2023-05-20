from django.shortcuts import render
from django.core.mail import EmailMessage
from django.contrib import messages


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
            return render(request, 'WebJecApp/Mensaje.html', {'enviado': False})

        # Validar que el campo Phone_Number solo contiene números
        if not phone_number.isdigit():
            messages.error(request, 'El campo "Número de teléfono" solo debe contener números.')
            return render(request, 'WebJecApp/Mensaje.html', {'enviado': False})

        # Construir el correo electrónico
        subject = f"Nuevo mensaje de {name}"
        body = f"Nombre: {name}\nEmail: {email}\nTeléfono: {phone_number}\nMensaje: {message}"
        from_email = 'lukasredfield26@gmail.com'
        to_email = ['lukasredfield@gmail.com']

        try:
            # Enviar el correo electrónico
            email = EmailMessage(subject, body, from_email, to_email)
            email.send()
            messages.success(request, '¡Mensaje enviado! Nos contactaremos a la brevedad. "Pidan, y se les dará; busquen, y encontrarán; llamen, y se les abrirá. Porque todo el que pide, recibe; el que busca, encuentra; y al que llama, se le abrirá. (Mateo 7:7-8)"')
            return render(request, 'WebJecApp/Mensaje.html', {'enviado': True})
        except Exception as e:
            messages.error(request, 'No se ha podido enviar el mensaje. Te invitamos a que por el momento nos envíes un mensaje por medio de nuestras redes sociales. "Pidan, y se les dará; busquen, y encontrarán; llamen, y se les abrirá. Porque todo el que pide, recibe; el que busca, encuentra; y al que llama, se le abrirá. (Mateo 7:7-8)"')
            return render(request, 'WebJecApp/Mensaje.html', {'enviado': False})

    else:
        return render(request, 'WebJecApp/Mensaje.html', {'enviado': False})



        


