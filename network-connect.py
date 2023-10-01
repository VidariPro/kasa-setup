import asyncio
import kasa

print("Ensure you are connected to the Kasa device's WiFi and press Enter to continue.")
input()

device = kasa. SmartDevice("192.168.0.1")

asyncio.run(device.update())

networks = asyncio.run(device.wifi_scan())

for x in range(len(networks)):
    check = str(networks[x])
    if check[0:18] == "WifiNetwork(ssid='":
        separate = check.split("'")
        networks[x] = separate[1]
    elif check[0:18] == 'WifiNetwork(ssid="':
        separate = check.split('"')
        networks[x] = separate[1]

print("Below is a list of available networks for the dvice to join.")
print("")
for x in range(len(networks)):
    print(str(x) + ": " + str(networks[x]))
print("")

print("Enter value next to the network for the device to join.")
toJoin = int(input())
print("")

print("Enter the password for " + networks[toJoin] + ".")
password = str(input())

asyncio.run(device.wifi_join(networks[toJoin], password))