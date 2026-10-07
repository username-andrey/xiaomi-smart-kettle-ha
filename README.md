# Xiaomi Smart Kettle 2 Pro for Home Assistant

Local Home Assistant integration for `xiaomi.kettle.v20`.

## v0.2.0
- Local polling over miIO/MIoT
- Water temperature, status, fault and warming time
- Target temperature, keep-warm temperature and duration
- Keep warm, lift memory, reminders and DND
- **Heat** button: starts heating using the configured Target temperature
- **Boil** button: starts boiling to 99 °C
- **Stop** button

The Heat and Boil commands also use the current keep-warm settings when building the kettle's `heat-mode` / `boil-mode`.

## HACS
Add this repository as a custom HACS integration, install it, restart Home Assistant, then add **Xiaomi Smart Kettle** from Settings > Devices & services.

## Supported device
- Xiaomi Smart Kettle 2 Pro
- Model: `xiaomi.kettle.v20`
- Tested protocol mapping with firmware `v2.2.7_0016`

> This is an experimental custom integration. Start commands are based on the public MIoT specification for `xiaomi.kettle.v20` and should be tested cautiously.
