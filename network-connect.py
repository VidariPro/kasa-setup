import asyncio
import kasa

print("Ensure you are connected to the Kasa device's WiFi and press Enter to continue.")
input()

device = kasa. SmartDevice("192.168.0.1")

asyncio.run(device.update())

networks = asyncio.run(device.wifi_scan())

print("Below is a list of available networks for the dvice to join.")
print("")
for x in range(len(networks)):
    print(x + ": " + networks[x])
print("")

print("Enter value next to the network for the device to join.")
toJoin = input()
print("")

print("Enter the password.")
password = input()

asyncio.run(device.wifi_join(networks[toJoin], password))