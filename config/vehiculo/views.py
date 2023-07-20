from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.views import LoginView
from .forms import VehiculoForm
from vehiculo.models import Vehiculo

# Create your views here.

def index(request):
    return render(request, 'index.html')

@login_required(login_url='/')
def listar(request):
    vehiculos = Vehiculo.objects.all()
    
    for vehiculo in vehiculos:
        if vehiculo.precio <= 10000:
            vehiculo.condicion_precio = 'Bajo'
        elif vehiculo.precio > 10000 and vehiculo.precio <= 30000:
            vehiculo.condicion_precio = 'Medio'
        else:
            vehiculo.condicion_precio = 'Alto'
            
    contexto = {'vehiculos': vehiculos}
    
    return render(request, 'listar.html', contexto)

@login_required(login_url='/')
def vehiculo_form(request):
    if request.method == "POST":
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vehiculo_form')
    
    else:
        form = VehiculoForm()
    
    return render(request, 'add.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'login.html'
    
    def get_success_url(self) -> str:
        return '/'