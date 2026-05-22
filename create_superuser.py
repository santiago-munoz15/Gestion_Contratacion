from accounts.models import User

if not User.objects.filter(username='juan').exists():
    User.objects.create_user(
        username='juan',
        password='123456',
        role='candidato'
    )
    print("Usuario creado")
else:
    print("Ya existe")