from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime
from rooms.models import Room
from devices.models import Device
from .serializers import RoomSerializer, DeviceSerializer

@api_view(['GET'])
def system_overview(request):
    """Returns a unified dashboard view with rooms, devices, power metrics, and alerts."""
    rooms = Room.objects.all()
    devices = Device.objects.all()
    
    # Calculate global power consumption metrics
    total_power = sum(d.current_power for d in devices)
    active_devices_count = devices.filter(status="ON").count()
    
    # Simple rule-based Alert Detection Engine for the hackathon
    # Checks if devices are left running after hours (Simulating after 6:00 PM rule)
    alerts = []
    current_hour = datetime.now().hour
    is_after_hours = current_hour >= 18 or current_hour < 6
    
    if is_after_hours and active_devices_count > 0:
        for room in rooms:
            active_room_devices = room.devices.filter(status="ON")
            if active_room_devices.exists():
                alerts.append({
                    "room_code": room.code,
                    "room_name": room.name,
                    "message": f"Security Notice: {active_room_devices.count()} appliances active during lockdown window.",
                    "severity": "CRITICAL"
                })

    return Response({
        "total_power_kw": round(total_power / 1000.0, 3),
        "total_power_w": total_power,
        "active_devices_count": active_devices_count,
        "total_devices_count": devices.count(),
        "rooms": RoomSerializer(rooms, many=True).data,
        "alerts": alerts
    })

@api_view(['POST'])
def toggle_device(request, device_id):
    """Allows control down-links from Dashboard or Discord to alter states."""
    try:
        device = Device.objects.get(id=device_id)
        new_status = request.data.get("status")
        if new_status in ["ON", "OFF"]:
            device.status = new_status
            device.save()
            return Response({"success": True, "device": DeviceSerializer(device).data})
        return Response({"success": False, "error": "Invalid status value"}, status=400)
    except Device.DoesNotExist:
        return Response({"success": False, "error": "Device not found"}, status=404)