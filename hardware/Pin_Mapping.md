# Hardware Interface & Pin Mapping Report

**Project:** Office Monitoring System
**Target Architecture:** ESP32-WROOM-32E MCU  
**Scope:** Representative Room Configuration (**Drawing Room Module**)

## 1. Overview

For closing the difference between the low-voltage digital logic of control and high-voltage AC commercial devices (Fans & Lights), the hardware design includes an optically coupled electromagnetic Relay Module. Furthermore, an analog Hall effect current sensor is employed for sensing the total electrical values, proving that there is a need for physical feasibility.

## 2. Quantitative Pin Configuration Matrix

| Microcontroller Pin    | Peripheral Component      | Target Load Monitored   | Rated Wattage (Active) | Electrical Signaling Profile |
| :--------------------- | :------------------------ | :---------------------- | :--------------------- | :--------------------------- |
| **GPIO 13**            | Relay Channel 1 IN        | Drawing Room - Fan 1    | 60W                    | Digital Output (Active HIGH) |
| **GPIO 12**            | Relay Channel 2 IN        | Drawing Room - Fan 2    | 60W                    | Digital Output (Active HIGH) |
| **GPIO 14**            | Relay Channel 3 IN        | Drawing Room - Light 1  | 15W                    | Digital Output (Active HIGH) |
| **GPIO 27**            | Relay Channel 4 IN        | Drawing Room - Light 2  | 15W                    | Digital Output (Active HIGH) |
| **GPIO 26**            | Relay Channel 5 IN        | Drawing Room - Light 3  | 15W                    | Digital Output (Active HIGH) |
| **GPIO 34 (ADC1_CH6)** | ACS712 Current Sensor OUT | Room Main Line          | Cumulative Load        | Analog Input (0V - 3.3V)     |
| **3V3 Rail**           | VCC Bus                   | Logic Power             | N/A                    | DC Power Distribution        |
| **GND Rail**           | GND Bus                   | Common Ground Reference | N/A                    | Galvanic Ground Loop         |

## 3. Sensor Transfer Function & Telemetry Model

The analog interface on `GPIO 34` monitors the step voltage changes from the ACS712 sensor. The calculation pipeline implemented within the system follows standard power dynamics:

$$P_{\text{calc}} = V_{\text{RMS}} \times I_{\text{RMS}}$$

Where line voltage $V_{\text{RMS}} = 220\text{V}$ AC (Bangladesh Grid Standard), and $I_{\text{RMS}}$ is linearly derived from the ADC voltage shifts centered around an operational VCC/2 ($1.65\text{V}$) reference baseline.
