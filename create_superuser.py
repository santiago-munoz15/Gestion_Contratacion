import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gestion_contratacion.settings')
django.setup()

from accounts.models import User

username = 'admin'
email = 'admin@gmail.com'
password = 'Admin12345'

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(
        username=username,
        email=email,
        password=password,
        role='reclutador'
    )
    print('Superusuario creado correctamente')
else:
    print('El superusuario ya existe')