from connect import wlan
import socket
from machine import ADC

address = socket.getaddrinfo("0.0.0.0", 80)[0][-1]
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
s.bind(address)
s.listen(1)
print("Listening for connections on", wlan.ifconfig()[0])

while True:
    try:
        client, address = s.accept()
        print("Connection accepted from", address)
        client_file = client.makefile("rwb", 0)
        while True:
            line = client_file.readline()
            if not line or line == b"\r\n":
                break
        client.send("HTTP/1.0 200 OK\r\n")
        client.send("Content-type: text/plain\r\n\r\n")
        client.send("Hello from Raspberry Pi Pico W!\r\n")
        client.close()
        print("Response sent, connection closed.")
    except OSError as e:
        client.close()
        print("Error, connection closed.")
