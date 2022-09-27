import os
import asyncio
from azure.iot.device import IoTHubDeviceClient


#async def main():
    # Fetch the connection string from an environment variable
conn_str = "HostName=iot-az220-training-asf081276.azure-devices.net;DeviceId=sensor-th-p-0002;SharedAccessKey=5gId9wHgi6DWWQGiLI/iwdGIAvu/FgS8fmW/UK60i4o="

# Create instance of the device client using the connection string
device_client = IoTHubDeviceClient.create_from_connection_string(conn_str)

# Connect the device client.
device_client.connect()

# Send a single message
print("Sending message...")
device_client.send_message("This is a message that is being sent")
print("Message successfully sent!")

# Finally, shut down the client
device_client.shutdown()


#if __name__ == "__main__":
#    asyncio.run(main())