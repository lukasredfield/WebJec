from django.shortcuts import render
from django.core.mail import EmailMessage
from django.contrib import messages



# Create your views here.
def base(request):
    return render(request, 'WebJecApp/Base.html')

def home(request):

    return render(request, 'WebJecApp/Home.html')

def ministerios(request):

    return render(request, 'WebJecApp/Ministerios.html')

def mision(request):

    return render(request, 'WebJecApp/Mision.html')

def contacto(request):

    return render(request, 'WebJecApp/Contacto.html')

def comunidad(request):

    return render(request, 'WebJecApp/Comunidad.html')

def index(request):

    return render(request, 'WebJecApp/Index.html')



def contact_view(request):
    if request.method == 'POST':
        # Obtener información del formulario
        name = request.POST.get('Name')
        email = request.POST.get('Email')
        phone_number = request.POST.get('Phone_Number')
        message = request.POST.get('Message')

        # Construir el correo electrónico
        subject = f"Nuevo mensaje de {name}"
        body = f"Nombre: {name}\nEmail: {email}\nTeléfono: {phone_number}\nMensaje: {message}"
        from_email = 'tu_email@gmail.com'
        to_email = ['lukasredfield@gmail.com']

        # Enviar el correo electrónico
        email = EmailMessage(subject, body, from_email, to_email)
        email.send()
        messages.success(request, '¡Mensaje enviado, nos contactaremos a la brevedad! "Pidan, y se les dará; busquen, y encontrarán; llamen, y se les abrirá. 8 Porque todo el que pide, recibe; el que busca, encuentra; y al que llama, se le abre.  (Mateo 7:7-8)"')

        

    # Renderizar la plantilla del formulario de contacto
    return render(request, 'WebJecApp/Home.html')


