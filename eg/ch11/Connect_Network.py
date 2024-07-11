import time
import network
import rp2
rp2.country("GB")

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("NetworkName", "Password")

while not wlan.isconnected() and wlan.status() >= 0:
    print("Waiting for Wi-Fi connection...")
    time.sleep(1)
print(wlan.ifconfig())
print(wlan.isconnected())
