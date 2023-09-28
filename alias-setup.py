import asyncio
import kasa

print("Ensure you are connected to the Kasa device's WiFi and press Enter to continue.")
input()

device = kasa. SmartDevice("192.168.0.1")

asyncio.run(device.update())

print("Input new device alias.")
newAlias = input()

asyncio.run(device.set_alias(newAlias))

print("Alias updated. Please run dev-check.py to check the alais reported by the device.")