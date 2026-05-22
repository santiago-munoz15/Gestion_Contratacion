import os
import django

# Configurar Django
os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE',
    'gestion_contratacion.settings'
)

django.setup()

from accounts.models import User


def crear_usuario(username, password, email, role, superuser=False):

    if not User.objects.filter(username=username).exists():

        if superuser:
            User.objects.create_superuser(
                username=username,
                email=email,
                password=password,
                role=role
            )
            print(f"✅ Superusuario {username} creado")

        else:
            User.objects.create_user(
                username=username,
                email=email,
                password=password,
                role=role
            )
            print(f"✅ Usuario {username} creado ({role})")

    else:
        print(f"⚠️ {username} ya existe")


# SUPERADMIN
crear_usuario(
    username='admin',
    password='123456',
    email='admin@gmail.com',
    role='reclutador',
    superuser=True
)

# RECLUTADOR
crear_usuario(
    username='juan',
    password='123456',
    email='juan@gmail.com',
    role='reclutador'
)

# CANDIDATO
crear_usuario(
    username='laura',
    password='123456',
    email='laura@gmail.com',
    role='candidato'
)

print("✅ Usuarios iniciales verificados")