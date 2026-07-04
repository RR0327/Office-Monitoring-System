import os
import sys
from pathlib import Path

# Add backend directory to Python path
BASE_DIR = Path(__file__).resolve().parent.parent
BACKEND_DIR = BASE_DIR / "backend"

sys.path.append(str(BACKEND_DIR))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

import django
django.setup()

from rooms.models import Room
from devices.models import Device


def create_rooms():
    rooms = [
        {
            "name": "Drawing Room",
            "code": "DRAWING",
            "description": "Main drawing room"
        },
        {
            "name": "Work Room 1",
            "code": "WORK1",
            "description": "Office workspace 1"
        },
        {
            "name": "Work Room 2",
            "code": "WORK2",
            "description": "Office workspace 2"
        },
    ]

    created_rooms = []

    for room_data in rooms:
        room, created = Room.objects.get_or_create(
            code=room_data["code"],
            defaults=room_data
        )
        created_rooms.append(room)

    return created_rooms


def create_devices(rooms):

    for room in rooms:

        # Two Fans
        for i in range(1, 3):
            Device.objects.get_or_create(
                room=room,
                name=f"Fan {i}",
                defaults={
                    "device_type": "FAN",
                    "status": "OFF",
                    "power_rating": 75,
                }
            )

        # Three Lights
        for i in range(1, 4):
            Device.objects.get_or_create(
                room=room,
                name=f"Light {i}",
                defaults={
                    "device_type": "LIGHT",
                    "status": "OFF",
                    "power_rating": 15,
                }
            )


def main():
    rooms = create_rooms()
    create_devices(rooms)

    print("=" * 50)
    print("Database seeded successfully!")
    print("=" * 50)

    print(f"Rooms : {Room.objects.count()}")
    print(f"Devices : {Device.objects.count()}")


if __name__ == "__main__":
    main()