import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gestion_contratacion.settings')
django.setup()

from accounts.models import User

username = 'juan'
email = 'juan@gmail.com'
password = '123456'

if not User.objects.filter(username=username).exists():
    User.objects.create_user(
        username=username,
        email=email,
        password=password,
        role='candidato'
    )
    print('Usuario candidato creado correctamente')
else:
    print('El usuario ya existe')