import struct
import asyncio
import aioble
import bluetooth

sensor_temp = machine.ADC(4)
conversion_factor = 3.3 / (65535)

ble_name = "picow_ble"
ble_service_uuid = bluetooth.UUID(0x181A)
ble_characteristic_uuid = bluetooth.UUID(0x2A6E)
ble_appearance = 0x0300
ble_advertising_interval = 2000

ble_service = aioble.Service(ble_service_uuid)
ble_characteristic = aioble.Characteristic(
    ble_service,
    ble_characteristic_uuid,
    read=True,
    notify=True)
aioble.register_services(ble_service)

async def ble_task():
    while True:
        async with await aioble.advertise(
            ble_advertising_interval,
            name=ble_name,
            services=[ble_service_uuid],
            appearance=ble_appearance) as connection:
            print("Connection from", connection.device)
            await connection.disconnected()

def encode_temp(temperature):
    return struct.pack("<h", int(temperature * 100))

async def sensor_task():
    while True:
        reading = sensor_temp.read_u16() * conversion_factor
        temperature = 27 - (reading - 0.706) / 0.001721
        print("Temperature:", temperature)
        ble_characteristic.write(encode_temp(temperature))
        await asyncio.sleep_ms(2000)

async def main():
    task1 = asyncio.create_task(ble_task())
    task2 = asyncio.create_task(sensor_task())
    await asyncio.gather(task1, task2)

print("Launching Raspberry Pi Pico W BLE temperature sensor...")
asyncio.run(main())
