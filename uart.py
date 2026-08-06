import serial

class PySerialDeviceMock:
    status = "STATUS_OK"
    def __init__(self):
        self.connection = serial.serial_for_url("loop://", timeout = 1)

    def send_command(self, command = str) -> str:
        payload = (command.strip() + "\n").encode("utf-8")
        self.connection.write(payload)
        recived_bytes = self.connection.readline()
        recived_text = recived_bytes.decode("utf-8").strip()
        if recived_text == "PING":
            return "PONG"
        elif recived_text == "OVERHEAT":
            self.status = "STATUS_NOT_OK_OVERHEATING"
            return self.status
        elif recived_text == "STATUS":
            return self.status
        elif recived_text == "NORMAL_STATE":
            self.status = "STATUS_OK"
            return self.status
        return "ERROR_UNKNOWN"

    def close(self):
        self.connection.close()
        return "Connection closed"