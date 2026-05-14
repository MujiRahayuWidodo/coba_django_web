# check_structure.py - Diagnostic script untuk struktur folder
import os
from pathlib import Path

def check_file(path, description):
    exists = Path(path).exists()
    status = "✅" if exists else "❌"
    print(f"{status} {description}: {path}")
    return exists

print("🔍 CHECK STRUKTUR FOLDER & PACKAGE MARKERS\n")
print("=" * 60)

# Root files
check_file('manage.py', 'Entry point Django')
check_file('config/__init__.py', 'Package marker: config/')
check_file('config/settings/__init__.py', 'Package marker: config/settings/ ⚠️ KRITIS')
check_file('config/settings/base.py', 'Base settings')
check_file('config/settings/dev.py', 'Development settings')

# App files
check_file('diamond_web/__init__.py', 'Package marker: diamond_web/')
check_file('diamond_web/apps.py', 'App config')
check_file('diamond_web/models/__init__.py', 'Package marker: models/')
check_file('diamond_web/views/__init__.py', 'Package marker: views/')

# Templates
check_file('templates/base.html', 'Global template: base.html')
check_file('templates/diamond_web/home.html', 'App template: home.html')

# Requirements
check_file('requirements/base.txt', 'Dependencies base')
check_file('requirements/dev.txt', 'Dependencies dev')

# Environment
check_file('.env', 'Environment variables')

print("\n" + "=" * 60)
print("💡 Jika ada ❌ pada file __init__.py, buat file kosong tersebut!")
print("   Contoh: type nul > config/settings/__init__.py")