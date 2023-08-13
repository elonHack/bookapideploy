
from django.contrib import admin
from django.urls import path, include

app_name = 'bookstore'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls'))
]
