from django.contrib import admin
from .models import Device


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "room",
        "device_type",
        "status",
        "current_power",
    )

    list_filter = (
        "room",
        "device_type",
        "status",
    )

    search_fields = (
        "name",
    )

    ordering = (
        "room",
        "name",
    )