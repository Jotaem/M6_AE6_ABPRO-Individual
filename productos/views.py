from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .models import Producto

class HomeView(LoginRequiredMixin, ListView):
    model = Producto
    template_name = 'productos/home.html'
    context_object_name = 'productos'

class ProductoListView(LoginRequiredMixin, ListView):
    model = Producto
    template_name = 'productos/lista_productos.html'
    context_object_name = 'productos'

class ProductoDetailView(LoginRequiredMixin, DetailView):
    model = Producto
    template_name = 'productos/detalle_producto.html'

class ProductoCreateView(LoginRequiredMixin, CreateView):
    model = Producto
    template_name = 'productos/form_producto.html'
    fields = ['nombre', 'descripcion', 'precio', 'stock', 'imagen']
    success_url = reverse_lazy('lista_productos')

class ProductoUpdateView(LoginRequiredMixin, UpdateView):
    model = Producto
    template_name = 'productos/form_producto.html'
    fields = ['nombre', 'descripcion', 'precio', 'stock', 'imagen']
    success_url = reverse_lazy('lista_productos')

class ProductoDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Producto
    template_name = 'productos/confirmar_eliminar.html'
    success_url = reverse_lazy('lista_productos')

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.groups.filter(name='Administradores').exists()

def acceso_denegado(request):
    return render(request, 'productos/acceso_denegado.html')

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/registro.html', {'form': form})

