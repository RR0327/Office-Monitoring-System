from django.db import models
from rooms.models import Room


class Device(models.Model):
    DEVICE_TYPES = [
        ("FAN", "Fan"),
        ("LIGHT", "Light"),
    ]

    STATUS_CHOICES = [
        ("ON", "ON"),
        ("OFF", "OFF"),
    ]

    room = models.ForeignKey(
        Room,
        on_delete=models.CASCADE,
        related_name="devices"
    )

    name = models.CharField(max_length=100)

    device_type = models.CharField(
        max_length=10,
        choices=DEVICE_TYPES
    )

    status = models.CharField(
        max_length=5,
        choices=STATUS_CHOICES,
        default="OFF"
    )

    power_rating = models.FloatField(
        help_text="Power consumption in Watts"
    )

    current_power = models.FloatField(
        default=0
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["room", "device_type", "name"]

    def save(self, *args, **kwargs):
        """
        Automatically calculate current power.
        """
        if self.status == "ON":
            self.current_power = self.power_rating
        else:
            self.current_power = 0

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.room.name} - {self.name}"