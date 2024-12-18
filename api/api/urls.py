
from django.contrib import admin
from django.urls import path, include

import apiApp

# Customize the admin panel
admin.site.site_header = "TileStore Administration"
admin.site.site_title = "TileStore Admin Panel"
admin.site.index_title = "Welcome to TileStore Admin"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apiApp.urls')),
]
