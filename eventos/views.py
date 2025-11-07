from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView,
)
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Evento
from django.contrib.auth.models import Group
 
# Vista para la página de inicio
class HomeView(TemplateView):
    template_name = 'eventos/home.html'

# Vista para listar todos los eventos (accesible para todos los usuarios autenticados)
class ListaEventosView(LoginRequiredMixin, ListView):
    model = Evento
    template_name = 'eventos/lista_eventos.html'
    context_object_name = 'eventos'

    def get_queryset(self):
        user = self.request.user
        # Administradores y Organizadores ven todos los eventos
        if user.is_staff or user.groups.filter(name='Organizadores de eventos').exists():
            return Evento.objects.all()
        # Asistentes ven solo los eventos a los que están inscritos
        return user.eventos_asistidos.all()

# Vista para el registro de nuevos usuarios
class RegistroView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/registro.html'

# Vista para ver el detalle de un evento
class DetalleEventoView(LoginRequiredMixin, DetailView):
    model = Evento
    template_name = 'eventos/detalle_evento.html'

# Vista para crear un evento (solo Organizadores y Administradores)
class CrearEventoView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Evento
    fields = ['nombre', 'descripcion', 'fecha']
    template_name = 'eventos/form_evento.html'
    success_url = reverse_lazy('lista_eventos')
    permission_required = 'eventos.add_evento'
    permission_denied_message = "No tienes permiso para crear eventos."
    raise_exception = False
    login_url = reverse_lazy('acceso_denegado')

    def form_valid(self, form):
        form.instance.organizador = self.request.user
        messages.success(self.request, "¡Evento creado con éxito!")
        return super().form_valid(form)

# Vista para editar un evento (solo el organizador o un Administrador)
class EditarEventoView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Evento
    fields = ['nombre', 'descripcion', 'fecha']
    template_name = 'eventos/form_evento.html'
    success_url = reverse_lazy('lista_eventos')

    def test_func(self):
        evento = self.get_object()
        # Permite si el usuario es el organizador O si tiene el permiso para cambiar cualquier evento (admin)
        return self.request.user == evento.organizador or self.request.user.has_perm('eventos.change_evento')

    def handle_no_permission(self):
        messages.error(self.request, "No puedes editar un evento que no organizas.")
        return redirect("acceso_denegado")

# Vista para eliminar un evento (solo Administradores)
class EliminarEventoView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Evento
    template_name = 'eventos/confirmar_eliminar.html'
    success_url = reverse_lazy('lista_eventos')
    permission_required = 'eventos.delete_evento'
    
    def handle_no_permission(self):
        messages.error(self.request, "Solo los administradores pueden eliminar eventos.")
        return redirect("acceso_denegado")

# Vista para acceso denegado
class AccesoDenegadoView(TemplateView):
    template_name = 'eventos/acceso_denegado.html'
