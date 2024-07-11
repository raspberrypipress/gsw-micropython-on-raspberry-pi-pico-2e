import struct
import asyncio
import aioble
import bluetooth

ble_name = "picow_ble"
ble_service_uuid = bluetooth.UUID(0x181A)
ble_characteristic_uuid = bluetooth.UUID(0x2A6E)
ble_scan_length = 5000
ble_interval = 30000
ble_window = 30000

async def ble_scan():
    print("Scanning for BLE beacon named", ble_name, "...")
    async with aioble.scan(
    ble_scan_length,
    interval_us=ble_interval,
    window_us=ble_window,
    active=True) as scanner:
        async for result in scanner:
            if result.name() == ble_name and \
               ble_service_uuid in result.services():
                return result.device
    return None

def decode_temp(data):
    return struct.unpack("<h", data)[0] / 100

async def main():
    device = await ble_scan()
    if not device:
        print("BLE beacon not found.")
        return

    try:
        print("Connecting to", device)
        connection = await device.connect()
    except asyncio.TimeoutError:
        print("Connection timed out.")
        return

    async with connection:
        try:
            ble_service = await connection.service(ble_service_uuid)
            ble_characteristic = await \
              ble_service.characteristic(ble_characteristic_uuid)
        except (asyncio.TimeoutError, AttributeError):
            print("Timeout discovering services or characteristics.")
            return

        while True:
            temperature = decode_temp(await ble_characteristic.read())
            print("Temperature:", temperature)
            await asyncio.sleep_ms(2000)

asyncio.run(main())