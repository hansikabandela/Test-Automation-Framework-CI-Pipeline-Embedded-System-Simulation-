
from platform_model import Machine

def test_machine_begins():
    machine = Machine()
    res = machine.start()
    assert res == "System set up"
    assert machine.condition == "ACTIVE"

def test_machine_invalid_command():
    machine = Machine()
    machine.start()
    res = machine.direct_command("INVALID")
    assert res == "Invalid command"
    assert machine.condition == "ERROR"

def test_machine_reboot():
    machine = Machine()
    machine.start()
    machine.direct_command("RESTART")
    assert machine.condition == "INACTIVE"


