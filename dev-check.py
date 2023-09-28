import asyncio
import kasa

print("Ensure you are connected to the Kasa device's WiFi and press Enter to continue.")
input()

device = kasa. SmartDevice("192.168.0.1")

asyncio.run(device.update())

alias = asyncio.run(device.alias)

print("The devices current alias is: " + alias)
print("")
print("Please run alias-setup.py to change the device's alias.")