import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gestion_contratacion.settings')
django.setup()

from accounts.models import User

username = 'juan2'

if not User.objects.filter(username=username).exists():

    user = User(
        username='juan2',
        email='juan@gmail.com',
        role='candidato'
    )

    user.set_password('123456')
    user.save()

    print('Usuario candidato creado correctamente')

else:
    print('El usuario ya existe')