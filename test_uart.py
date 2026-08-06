import pytest
from uart import PySerialDeviceMock

@pytest.fixture
def device():
    mock_device = PySerialDeviceMock()
    yield mock_device
    mock_device.close()

def test_ping_command(device):
    response = device.send_command("PING")
    assert response == "PONG"

def test_status(device):
    response = device.send_command("STATUS")
    assert response == "STATUS_OK"

def test_overheating(device):
    response = device.send_command("OVERHEAT")
    assert response == "STATUS_NOT_OK_OVERHEATING"

def test_normal_state(device):
    response = device.send_command("NORMAL_STATE")
    assert response == "STATUS_OK"

def test_unknown_command(device):
    response = device.send_command("BANNANA")
    assert response == "ERROR_UNKNOWN"