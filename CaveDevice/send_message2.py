import os
import time
import uuid
from azure.iot.device import IoTHubDeviceClient, Message

# The connection string for a device should never be stored in code. For the sake of simplicity we're using an environment variable here.
conn_str = "HostName=iot-az220-training-asf081276.azure-devices.net;DeviceId=sensor-th-p-0002;SharedAccessKey=5gId9wHgi6DWWQGiLI/iwdGIAvu/FgS8fmW/UK60i4o="
# The client object is used to interact with your Azure IoT hub.
device_client = IoTHubDeviceClient.create_from_connection_string(conn_str)

# Connect the client.
device_client.connect()

# send 2 messages with 2 system properties & 1 custom property with a 1 second pause between each message
for i in range(1, 3):
    print("sending message #" + str(i))
    msg = Message("test wind speed " + str(i))
    msg.message_id = uuid.uuid4()
    msg.correlation_id = "correlation-1234"
    msg.custom_properties["tornado-warning"] = "yes"
    msg.content_encoding = "utf-8"
    msg.content_type = "application/json"
    device_client.send_message(msg)
    time.sleep(1)

# send 2 messages with only custom property with a 1 second pause between each message
for i in range(3, 5):
    print("sending message #" + str(i))
    msg = Message("test wind speed " + str(i))
    msg.custom_properties["tornado-warning"] = "yes"
    msg.content_encoding = "utf-8"
    msg.content_type = "application/json"
    device_client.send_message(msg)
    time.sleep(1)

# send 2 messages with only system properties with a 1 second pause between each message
for i in range(5, 7):
    print("sending message #" + str(i))
    msg = Message("test wind speed " + str(i))
    msg.message_id = uuid.uuid4()
    msg.correlation_id = "correlation-1234"
    msg.content_encoding = "utf-8"
    msg.content_type = "application/json"
    device_client.send_message(msg)
    time.sleep(1)

# send 2 messages with 1 system property and 1 custom property with a 1 second pause between each message
for i in range(7, 9):
    print("sending message #" + str(i))
    msg = Message("test wind speed " + str(i))
    msg.message_id = uuid.uuid4()
    msg.custom_properties["tornado-warning"] = "yes"
    msg.content_encoding = "utf-8"
    msg.content_type = "application/json"
    device_client.send_message(msg)
    time.sleep(1)

# send only string messages
for i in range(9, 11):
    print("sending message #" + str(i))
    device_client.send_message("test payload message " + str(i))
    time.sleep(1)


# finally, shut down the client
device_client.shutdown()