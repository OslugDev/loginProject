# login_app/views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import LoginForm

def login_view(request):
    """
        Maneja la vista de inicio de sesión.

        Si el método de la solicitud es POST, procesa el formulario con los datos enviados.
        Si el formulario es válido, muestra un mensaje de éxito y redirige a la vista de éxito.
        Si el método de la solicitud es GET, muestra el formulario vacío.

        Args:
            request (HttpRequest): La solicitud HTTP que llega al servidor.

        Returns:
            HttpResponse: Renderiza la plantilla 'login.html' con el formulario si el método
                          es GET, o redirige a 'success' si el formulario es válido.
        """
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Has ingresado correctamente')
            return redirect('success')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def success_view(request):
    """
        Maneja la vista de éxito después de un inicio de sesión exitoso.

        Args:
            request (HttpRequest): La solicitud HTTP que llega al servidor.

        Returns:
            HttpResponse: Renderiza la plantilla 'success.html'.
        """
    return render(request, 'success.html')


