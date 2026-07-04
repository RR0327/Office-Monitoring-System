import os
import sys
import time
import random
from pathlib import Path

# Setup system environment routing path variables
BASE_DIR = Path(__file__).resolve().parent.parent
BACKEND_DIR = BASE_DIR / "backend"
sys.path.append(str(BACKEND_DIR))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

import django
django.setup()

from devices.models import Device
from rooms.models import Room

def run_iot_simulator():
    print("=" * 60)
    print("🚀 CORE WORKSPACE SYSTEM DEVICE STATE SIMULATOR ACTIVE")
    print("   Target Engine Source: Local SQLite Node")
    print("   Frequency Pattern: Mutation Interval Toggled Every 4 Seconds")
    print("=" * 60)
    
    try:
        while True:
            # Fetch all registered tracking device entries
            devices = list(Device.objects.all())
            if not devices:
                print("⚠️ Error Context: No tracking device profiles found in the target database instance. Run seed data first.")
                time.sleep(5)
                continue
            
            # Select a random device to toggle state values
            target_device = random.choice(devices)
            old_status = target_device.status
            new_status = "OFF" if old_status == "ON" else "ON"
            
            # Save the new status (this triggers overridden save() model computation automatically)
            target_device.status = new_status
            target_device.save()
            
            print(f"📡 [SIM_EVENT] | Room: {target_device.room.name:<15} | Device: {target_device.name:<10} | Transition: {old_status} ──► {new_status} | Wattage: {target_device.current_power}W")
            
            # Wait 4 seconds before the next event loop run
            time.sleep(4)
            
    except KeyboardInterrupt:
        print("\n🛑 Simulation session terminated gracefully by user control break input.")

if __name__ == "__main__":
    run_iot_simulator()