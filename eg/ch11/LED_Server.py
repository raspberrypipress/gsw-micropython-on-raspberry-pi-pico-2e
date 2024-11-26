from connect import wlan
import socket
import machine

led_onboard = machine.Pin("LED", machine.Pin.OUT)
led_onboard.value(0)
led_state = "LED is off"

html = """
<!DOCTYPE html>
<html>
    <head> <title>Raspberry Pi Pico W</title> </head>
    <body> <h1>Raspberry Pi Pico W</h1>
        <p>%s</p>
    </body>
</html>
"""

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
        request = client.recv(1024).decode("UTF-8")
        print(request)

        led_on = request.startswith("GET /led/on")
        led_off = request.startswith("GET /led/off")
        print("led_on = " + str(led_on))
        print("led_off = " + str(led_off))

        if led_on:
            print("Client requested to turn the LED on.")
            led_onboard.value(1)
            led_state = "LED is on"

        if led_off:
            print("Client requested to turn the LED off.")
            led_onboard.value(0)
            led_state = "LED is off"

        response = html % led_state

        client.send("HTTP/1.0 200 OK\r\n")
        client.send("Content-type: text/html\r\n\r\n")
        client.send(response)
        client.close()

    except OSError as e:
        client.close()
        print("Error, connection closed.")
