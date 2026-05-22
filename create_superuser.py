import os
import django

# 🔥 Configurar settings
os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE',
    'gestion_contratacion.settings'
)

django.setup()

from accounts.models import User

# Crear superusuario si no existe
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser(
        username='admin',
        email='admin@gmail.com',
        password='123456',
        role='reclutador'
    )

    print("✅ Superusuario creado")
else:
    print("⚠️ El superusuario ya existe")