# create_admin.py - versi simpel
import os
import django
import sys

# Gunakan settings default (bukan dev)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

django.setup()

from django.contrib.auth import get_user_model
User = get_user_model()

if not User.objects.filter(username='admin').exists():
    user = User.objects.create_superuser(
        username='admin',
        email='admin@example.com',
        password='Admin123!'
    )
    print(f'✅ Superuser "{user.username}" berhasil dibuat!')
else:
    print('⚠️ User "admin" sudah ada.')