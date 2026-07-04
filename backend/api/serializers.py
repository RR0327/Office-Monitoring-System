from rest_framework import serializers
from rooms.models import Room
from devices.models import Device

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ['id', 'name', 'device_type', 'status', 'power_rating', 'current_power', 'updated_at']

class RoomSerializer(serializers.ModelSerializer):
    devices = DeviceSerializer(many=True, read_only=True)
    total_power = serializers.SerializerMethodField()

    class Meta:
        model = Room
        fields = ['id', 'name', 'code', 'description', 'devices', 'total_power']

    def get_total_power(self, obj):
        return sum(device.current_power for device in obj.devices.all() if device.status == 'ON')