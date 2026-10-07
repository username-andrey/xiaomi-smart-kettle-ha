# Xiaomi Smart Kettle 2 Pro for Home Assistant

Custom Home Assistant integration for **Xiaomi Smart Kettle 2 Pro** (`xiaomi.kettle.v20`) using local LAN communication via miIO/MIoT.

Current version: **0.1.0**  
Tested device firmware: **v2.2.7_0016**

## Features

- Current water temperature
- Kettle status and fault state
- Target temperature
- Keep-warm temperature and duration
- Keep-warm enable/disable
- Remember temperature after lifting
- Boiling reminder
- Keep-warm reminder
- Do Not Disturb
- Kettle-lifted sensor
- Stop action

Heating and boiling start actions are not exposed in v0.1.0 while their MIoT behavior is being validated.

## Installation with HACS

1. Open HACS in Home Assistant.
2. Add this repository as a custom repository of type **Integration**.
3. Install **Xiaomi Smart Kettle**.
4. Restart Home Assistant.
5. Open **Settings > Devices & services > Add integration**.
6. Search for **Xiaomi Smart Kettle**.
7. Enter the kettle's local IPv4 address and 32-character miIO token.

## Manual installation

Copy:

`custom_components/xiaomi_smart_kettle`

to:

`/config/custom_components/xiaomi_smart_kettle`

Restart Home Assistant and add the integration from **Settings > Devices & services**.

## Supported device

- Xiaomi Smart Kettle 2 Pro
- Model: `xiaomi.kettle.v20`

## Notes

This project is experimental. It communicates directly with the kettle on the local network and does not require Xiaomi Cloud for normal operation.
