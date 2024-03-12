from django.contrib import admin
from django.urls import path, include
from .views import home_page
from api1 import urls as api1_urls  # Importing urls from api1 app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home_page),
    path('api1/v1/', include(api1_urls)),  # Including urls from api1 app
]
