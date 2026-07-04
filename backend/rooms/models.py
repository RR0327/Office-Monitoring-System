from django.db import models


class Room(models.Model):
    ROOM_TYPES = [
        ("DRAWING", "Drawing Room"),
        ("WORK1", "Work Room 1"),
        ("WORK2", "Work Room 2"),
    ]

    name = models.CharField(max_length=50)
    code = models.CharField(max_length=20, unique=True, choices=ROOM_TYPES)
    description = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["id"]
        verbose_name = "Room"
        verbose_name_plural = "Rooms"

    def __str__(self):
        return self.name