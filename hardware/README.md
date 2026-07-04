# Hardware Subsystem Overview

This directory contains the hardware design and simulation files for the **Office Monitoring System**. The hardware is implemented as a **representative room prototype** using an ESP32 development board in Wokwi.

## 1. Hardware Design Philosophy

The office consists of three rooms, each containing:

- 2 Fans
- 3 Lights

Instead of duplicating the hardware three times, a **single room** is implemented in Wokwi. This representative circuit demonstrates the control logic that can be replicated for the remaining rooms.

To simplify the simulation, LEDs are used to represent the office devices:

- **Yellow LEDs** → Fans
- **Blue LEDs** → Lights

Each LED is connected to an ESP32 GPIO pin through a 220Ω current-limiting resistor.

In a real-world deployment, these GPIO pins would drive relay modules that switch the corresponding 220V AC electrical loads.

---

# 2. Hardware Components

The representative hardware includes:

- ESP32-WROOM-32 Development Board
- 3 Blue LEDs (Lights)
- 2 Yellow LEDs (Fans)
- 5 × 220Ω Resistors
- Jumper Wires

---

# 3. System Workflow

The hardware follows a simple control flow:

```
Web Dashboard / Discord Bot
            │
            ▼
      Django Backend
            │
            ▼
    Device State Update
            │
            ▼
        ESP32 GPIO
            │
            ▼
      LED ON / OFF
```

Each GPIO pin controls one simulated office device independently.

- GPIO HIGH → Device ON
- GPIO LOW → Device OFF

---

# 4. Simulation Purpose

The Wokwi circuit demonstrates how an ESP32 can independently control multiple office devices.

Although LEDs are used in the simulation, they represent actual electrical appliances:

- Blue LED → Office Light
- Yellow LED → Office Fan

This approach provides a safe and simple demonstration of the hardware control logic.

---

# 5. Real-World Deployment

For deployment in a real office environment:

- LEDs would be replaced by relay modules.
- Each relay would control a 220V AC fan or light.
- Optional current sensors (such as ACS712) could be integrated for real-time power monitoring.
- The same circuit design would be replicated for every room.

---

# 6. Repository Contents

- **ESP32_Office_Schematic.png** — Wokwi circuit screenshot.
- **ESP32_Office_Schematic.pdf** — PDF version of the schematic.
- **Pin_Mapping.md** — ESP32 GPIO assignments.
- **Wokwi_Link.txt** — Public link to the Wokwi simulation.
- **README.md** — Hardware overview and design documentation.

---

# Notes

- This hardware implementation represents **one office room**.
- The complete office is formed by replicating this circuit for each room.
- The hardware simulation complements the Django-based software simulator used in the project and demonstrates the physical feasibility of the proposed system architecture.