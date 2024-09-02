from django.apps import AppConfig
"""
    Configuración de la aplicación 'login_app'.

    Esta clase configura los ajustes específicos para la aplicación Django 'login_app'.
    Permite personalizar el comportamiento de la aplicación y establecer configuraciones adicionales.

    Attributes:
        default_auto_field (str): Tipo de campo por defecto para los campos auto-generados. 
                                  En este caso, se utiliza 'BigAutoField', que es adecuado para IDs grandes.
        name (str): Nombre de la aplicación. Este es el nombre que Django utilizará para referirse a la aplicación.
    """
class LoginAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'login_app'
