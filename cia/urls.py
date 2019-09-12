from django.contrib import admin
from django.urls import path, re_path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', include('mobileapp.urls'))
    re_path('api/(?P<version>(v1|v2))/', include('mobileapp.urls'))
]