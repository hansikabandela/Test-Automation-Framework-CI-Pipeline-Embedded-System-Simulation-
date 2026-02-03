
from platform_model import Machine

def machine_begins():
    machine = Machine()
    res = machine.start()
    assert res == "System has started"
    assert machine.condition == "ACTIVE"

def machine_invalid_command():
    machine = Machine()
    machine.start()
    res = machine.direct_command("INVALID")
    assert res == "Inaccurate command passed"
    assert machine.condition == "ERROR"

def machine_reboot():
    machine = Machine()
    machine.start()
    machine.direct_command("RESTART")
    assert machine.condition == "INACTIVE"


