from django.contrib.auth.models import User

# Ver todos los usuarios
users = User.objects.all()
for user in users:
    print(f"Username: {user.username}, Email: {user.email}")

# Buscar un usuario específico
user = User.objects.filter(email="ejemplo@email.com").first()
if user:
    print(f"Usuario encontrado: {user.username}")
else:
    print("Usuario no encontrado")

