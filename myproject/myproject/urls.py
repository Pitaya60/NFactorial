from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('landing.urls')),
    path('results/<str:search_id>/', include('landing.urls')),  # Новый маршрут для результатов поиска
]
