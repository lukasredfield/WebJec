from django.shortcuts import render

# Create your views here.
def base(request):
    return render(request, 'WebJecApp/Base.html')

def home(request):

    return render(request, 'WebJecApp/Home.html')

def nosotros(request):

    return render(request, 'WebJecApp/Nosotros.html')

def mision(request):

    return render(request, 'WebJecApp/Mision.html')

def contacto(request):

    return render(request, 'WebJecApp/Contacto.html')

def comunidad(request):

    return render(request, 'WebJecApp/Comunidad.html')

def index(request):

    return render(request, 'WebJecApp/Index.html')


#dfsdfdsdf
#sdsadsads
