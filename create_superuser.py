import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gestion_contratacion.settings')
django.setup()

from accounts.models import User

username = 'juan3'

if not User.objects.filter(username=username).exists():

    user = User.objects.create(
        username='juan3',
        email='juan3@gmail.com',
        role='candidato',
        is_active=True
    )

    user.set_password('123456')
    user.save()

    print('Usuario creado correctamente')

else:
    user = User.objects.get(username=username)

    user.set_password('123456')
    user.is_active = True
    user.save()

    print('Usuario actualizado correctamente')