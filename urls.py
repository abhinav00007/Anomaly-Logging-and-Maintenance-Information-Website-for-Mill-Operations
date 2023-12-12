# anomaly_project/urls.py

from django.contrib import admin
from django.urls import path, include
from anomaly_app.views import home  # Update the import statement

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('anomaly_app.urls')),
    path('', home, name='home'),  # Add this line for the home view
]
