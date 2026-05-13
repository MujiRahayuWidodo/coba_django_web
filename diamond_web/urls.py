from django.urls import path 
from . import views 

app_name = 'diamond_web'  # 🔑 WAJIB ADA! Ini yang diminta error tersebut

urlpatterns = [
    path('', views.home, name='home'), 
]

# from django.contrib import admin
# from django.urls import path, include 
# from django.conf import settings 
# from django.conf.urls.static import static 

# urlpatterns = [
#     path('admin/', admin.site.urls), 
#     path('', include('diamond_web.urls')), 
# ]

# if settings.DEBUG:
#     import debug_toolbar 
#     urlpatterns += [
#         path('__debug__/', include(debug_toolbar.urls)), 
#         path('schema/', include('schema_graph.urls')), 
#     ]
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 