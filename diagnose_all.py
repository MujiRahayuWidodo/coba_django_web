#!/usr/bin/env python
# diagnose_all.py - Comprehensive Django project diagnostic
import os
import sys
import django
from pathlib import Path

def header(title):
    print(f"\n{'='*60}")
    print(f"🔍 {title}")
    print('='*60)

def check(condition, msg_ok, msg_err):
    if condition:
        print(f"✅ {msg_ok}")
        return True
    else:
        print(f"❌ {msg_err}")
        return False

# Setup
project_root = Path(__file__).parent
os.chdir(project_root)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

header("1. STRUCTURE CHECK")
checks = [
    ((project_root / 'manage.py').exists(), "manage.py exists"),
    ((project_root / 'config' / '__init__.py').exists(), "config/__init__.py exists"),
    ((project_root / 'config' / 'settings' / '__init__.py').exists(), "config/settings/__init__.py exists ⚠️"),
    ((project_root / 'diamond_web' / '__init__.py').exists(), "diamond_web/__init__.py exists"),
    ((project_root / 'templates' / 'base.html').exists(), "templates/base.html exists"),
]
for cond, msg in checks:
    check(cond, msg, f"Missing: {msg}")

header("2. DJANGO SETUP CHECK")
try:
    django.setup()
    check(True, "Django setup() successful", "Django setup() failed")
except Exception as e:
    check(False, "Django setup() successful", f"Django setup() error: {e}")
    sys.exit(1)

header("3. SETTINGS CHECK")
from django.conf import settings
check(settings.DEBUG, "DEBUG mode: ON", "DEBUG mode: OFF (production)")
check('diamond_web' in settings.INSTALLED_APPS, "diamond_web in INSTALLED_APPS", "diamond_web NOT in INSTALLED_APPS")
check(settings.TEMPLATES[0]['APP_DIRS'], "APP_DIRS: True", "APP_DIRS: False ⚠️")

header("4. DATABASE CHECK")
from django.db import connection
try:
    with connection.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) FROM django_migrations")
        count = cursor.fetchone()[0]
        check(True, f"Database connected | Migrations applied: {count}", "Database check failed")
except Exception as e:
    check(False, "Database connected", f"Database error: {e}")

header("5. AUTH USER CHECK")
from django.contrib.auth import get_user_model
User = get_user_model()
try:
    admin_count = User.objects.filter(is_superuser=True).count()
    check(True, f"Auth system works | Superusers: {admin_count}", "Auth system check failed")
except Exception as e:
    check(False, "Auth system works", f"Auth error: {e}")

header("6. URL CHECK")
from django.urls import get_resolver
try:
    resolver = get_resolver()
    check(len(resolver.url_patterns) > 0, f"URLs configured: {len(resolver.url_patterns)} patterns", "No URL patterns found")
except Exception as e:
    check(False, "URLs configured", f"URL error: {e}")

header("📋 DIAGNOSIS COMPLETE")
print("💡 Jika ada ❌, perbaiki sesuai pesan error di atas.")
print("🔄 Setelah perbaikan, jalankan: python manage.py check")
print("🚀 Lalu: python manage.py runserver")