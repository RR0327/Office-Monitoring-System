from django.urls import path
from .views import system_overview, toggle_device

urlpatterns = [
    path('status/', system_overview, name='api-system-overview'),
    path('device/<int:device_id>/toggle/', toggle_device, name='api-toggle-device'),
]