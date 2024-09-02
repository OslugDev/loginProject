# login_app/forms.py

from django import forms
class LoginForm(forms.Form):
    """
        Formulario para el inicio de sesión.

        Este formulario se utiliza para capturar el correo electrónico y la contraseña del usuario.
        Se asegura de que el correo electrónico tenga un formato válido y la contraseña se oculte
        en el campo de entrada.

        Attributes:
            email (forms.EmailField): Campo de entrada para el correo electrónico del usuario.
            password (forms.CharField): Campo de entrada para la contraseña del usuario.
        """
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    """
        Campo de entrada para el correo electrónico del usuario.

        - **label**: Etiqueta que se muestra junto al campo de entrada.
        - **widget**: Widget utilizado para representar el campo en el HTML.
          - **attrs**: Atributos HTML adicionales. En este caso, se aplica la clase 'form-control' para estilos CSS.
        """
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    """
        Campo de entrada para la contraseña del usuario.

        - **label**: Etiqueta que se muestra junto al campo de entrada.
        - **widget**: Widget utilizado para representar el campo en el HTML.
          - **attrs**: Atributos HTML adicionales. En este caso, se aplica la clase 'form-control' para estilos CSS.
          - **PasswordInput**: Se utiliza para ocultar la entrada del usuario, mostrando asteriscos en lugar de texto plano.
        """