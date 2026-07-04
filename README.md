# Office Monitoring System

A centralized IoT-based Office Monitoring System that provides real-time monitoring of office electrical devices through a Web Dashboard and Discord Bot using a shared Django backend.

---

# Introduction

The Office Monitoring System is a simulated IoT solution developed for the **Techathon Nationals & Rover Summit 2026 – Preliminary Round**.

The project demonstrates how an office environment can be monitored and managed through a centralized backend. The backend serves both a web dashboard and a Discord bot, ensuring synchronized device information across multiple platforms.

The office setup consists of three rooms:

- Drawing Room
- Work Room 1
- Work Room 2

Each room contains:

- 2 Fans
- 3 Lights

Total Devices:

- 15 Devices

The system simulates device behavior, power consumption, and alert generation without requiring physical hardware.

---

# Features

## Web Dashboard

- Real-time device monitoring
- Room-wise device status
- Office layout visualization
- Power consumption monitoring
- Alert panel
- Responsive user interface

## Backend

- Django REST API
- Shared database
- Device simulator
- Power consumption calculator
- Alert generation engine
- WebSocket support for real-time updates

## Discord Bot

- View device status
- Check room information
- Monitor power usage
- Receive alert notifications

---

# Tech Stack

## Backend

- Python
- Django
- Django REST Framework
- Django Channels
- SQLite

## Frontend

- HTML
- CSS
- JavaScript
- Bootstrap

## Discord Bot

- discord.py

## Hardware Simulation

- ESP32
- Wokwi

---

# Installation

## Clone the Repository

```bash
git clone https://github.com/RR0327/Office-Monitoring-System.git
```

## Create a Virtual Environment

```bash
python -m venv venv
```

## Activate the Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux/macOS

```bash
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# How to Run

## Run the Backend

```bash
cd backend

python manage.py migrate

python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

## Run the Discord Bot

```bash
cd discord_bot

python bot.py
```

---

# Folder Structure

```text
office-monitoring-system/
│
├── backend/
│   ├── config/
│   ├── rooms/
│   ├── devices/
│   ├── simulator/
│   ├── alerts/
│   ├── websocket/
│   ├── dashboard/
│   ├── api/
│   ├── templates/
│   ├── static/
│   └── media/
│
├── discord_bot/
├── docs/
├── hardware/
├── scripts/
├── tests/
│
├── README.md
├── LICENSE
├── requirements.txt
├── .gitignore
└── .env.example
```

---

# Screenshots

Screenshots of the dashboard and system interface are available in:

```text
docs/Dashboard_Screenshots/
```

_(Screenshots will be added as the project progresses.)_

---

# System Diagram

The overall system architecture is shown below.

```text
              |---------------------|
              |  Simulated Devices  |
              |---------------------|
                        │
                        ▼
        |-------------------------------------|
        |           Django Backend            |
        |    (REST API + WebSocket Layer)     |
        |-------------------------------------|
                        │
            ┌───────────┴───────────┐
            ▼                       ▼
   |----------------|      |--------------|
   | Web Dashboard  |      |  Discord Bot |
   |----------------|      |--------------|
```

> The complete project documentation including API documentation, system architecture, data flow diagram, database ER diagram, and demo script is available inside the `docs/` directory.

---

# Hardware Diagram

The hardware simulation is designed using ESP32 and Wokwi.

Hardware files are located in:

```text
hardware/
```

Contents include:

- ESP32 Office Schematic
- Pin Mapping
- Wokwi Project Link
- Hardware Documentation

---

# Discord Commands

| Command             | Description                        |
| ------------------- | ---------------------------------- |
| `!help`             | Display all available commands     |
| `!status`           | Show the status of all devices     |
| `!room <room_name>` | Display devices in a specific room |
| `!usage`            | Show current power consumption     |
| `!alerts`           | Display active alerts              |

---

# Contributors

**Team Name:** Tech_Innovators

| Name                    | Role                            |
| ----------------------- | ------------------------------- |
| Md Rakibul Hassan       | Backend Developer & Team Leader |
| Md. Tahsin Azad Shaikat | Hardware Developer              |
| Md. Saif Hasan Shafe    | Frontend & UI Developer         |

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---
