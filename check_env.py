import os
import sys
import socket

print("🚀 Memulai Diagnostic Project Diamond-Web...")
print("=" * 50)

def print_result(label, success, msg):
    status = "✅ OK" if success else "❌ ERROR"
    print(f"{label}: {status}")
    if not success and msg:
        print(f"    Detail: {msg}")

# 1. Cek Lokasi & Struktur Folder
print("\n 1. Cek Struktur Folder")
try:
    if not os.path.exists('manage.py'):
        print_result("Root Project", False, "File manage.py tidak ditemukan. Jalankan dari folder yang salah.")
    else:
        print_result("Root Project", True, None)
    
    if not os.path.exists('diamond_web'):
        print_result("App Folder", False, "Folder 'diamond_web' tidak ada.")
    else:
        print_result("App Folder", True, None)

    if not os.path.exists('config/settings'):
        print_result("Config Folder", False, "Folder 'config/settings' tidak ada.")
    else:
        print_result("Config Folder", True, None)

    if os.path.exists('templates'):
        print_result("Templates Folder", True, None)
    else:
        print_result("Templates Folder", False, "Folder 'templates' tidak ada (mungkin typo 'tamplate'?)")

except Exception as e:
    print(f"   ❌ Error sistem: {e}")

# 2. Cek Python & Virtual Environment
print("\n🐍 2. Cek Python Environment")
print(f"   Python Path: {sys.executable}")
if ".venv" in sys.executable:
    print_result("Virtual Env", True, "Menggunakan virtual environment yang benar.")
else:
    print_result("Virtual Env", False, "Tidak menggunakan .venv! Jalankan '.venv\\Scripts\\activate' dulu.")

# 3. Cek Instalasi Django
print("\n📦 3. Cek Instalasi Django")
try:
    import django
    print_result("Django Import", True, f"Versi: {django.VERSION}")
except ImportError:
    print_result("Django Import", False, "Django belum terinstall di environment ini. Jalankan: pip install django")
    sys.exit(1) # Berhenti jika Django tidak ada

# 4. Cek Konfigurasi Settings (Kritis!)
print("\n⚙️ 4. Cek Settings Django")
try:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.dev')
    django.setup()
    print_result("Django Setup", True, "Berhasil load settings.")
except Exception as e:
    print_result("Django Setup", False, str(e))
    print("   💡 Saran: Cek file config/settings/dev.py dan base.py untuk typo atau modul yang hilang.")
    sys.exit(1)

# 5. Cek Model Database
print("\n🗄️ 5. Cek Model Database")
try:
    from diamond_web.models import DiamondItem
    print_result("Model Import", True, "Model DiamondItem ditemukan.")
except Exception as e:
    print_result("Model Import", False, str(e))

# 6. Cek URL Routing
print("\n🔗 6. Cek URL Routing")
try:
    from diamond_web import urls as app_urls
    if app_urls.urlpatterns:
        print_result("App URLs", True, f"Menemukan {len(app_urls.urlpatterns)} routes.")
    else:
        print_result("App URLs", False, "List urlpatterns kosong di diamond_web/urls.py")
        
    from config import urls as project_urls
    print_result("Project URLs", True, "Config urls.py valid.")
except Exception as e:
    print_result("URL Routing", False, str(e))

# 7. Cek Port Server
print("\n🌐 7. Cek Port Server (8000)")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
result = sock.connect_ex(('127.0.0.1', 8000))
if result == 0:
    print_result("Port 8000", False, "Port SEDANG DIGUNAKAN oleh aplikasi lain.")
else:
    print_result("Port 8000", True, "Port kosong, siap untuk runserver.")
sock.close()

print("\n" + "=" * 50)
print("🏁 Diagnostic Selesai!")