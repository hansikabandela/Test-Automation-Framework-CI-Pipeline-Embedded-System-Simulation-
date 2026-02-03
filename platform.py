# lets create the embedded platform

class Machine:
   def __init__(system):
       system.condition = "INACTIVE"
   
   def start(system):
       if system.condition == "INACTIVE":
          system.condition = "ACTIVE"
          return "System set up"
       return "System started running"

   def stop(system):
       if system.condition == "ACTIVE":
          system.condition = "IDLE"
          return "System stopped"
       return "System disabled"
   
   def direct_command(system, command):
       if command not in ["PLAY", "PAUSE", "RESTART"]:
          system.condition = "ERROR"
          return "Invalid command"
       if command == "RESTART":
          system.condition = "INACTIVE"
          return "System reboot"

       return f"{command} is accomplished"

# For testing purpose

if __name__ == "__main__":
     m = Machine()
     print(m.start())
     print(m.direct_command("PLAY"))
     print(m.direct_command("ERROR"))
     print(m.stop())
     print(m.direct_command("RESTART"))

