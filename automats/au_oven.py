#!/usr/bin/env python3.7

# States const
Z_OFF  = 1    # Power off
Z_HEAT = 2    # Heat 
Z_WAIT = 3    # Waitinig status

# Actions const
X_TURN_0 = 1  # Turn to 0 degree
X_TURN_T = 2  # Turn to not 0 degree
X_OP_CL = 3   # Open/close door

# Lamps const
L_OFF = 0
L_ON  = 1

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 


class Lamp:
    status = L_OFF
    name = 'default lamp'
    def __init__(self, name, status = L_OFF):
        self.name = name
        self.status = status

    def __str__(self):
        status = ''
        if self.status == L_OFF:
           status = ': off'
        else:
            status = ': on'
        return self.name + status 

    def set_status(self, status):
        self.status = status

class Oven:
    z = Z_OFF
    l_work   = Lamp('Work indicator')
    l_heat   = Lamp('Heat indicator')
    l_inside = Lamp('Inside lamp')
    is_door_open = 0

    def __str__(self):
        z_str = {
            self.z == Z_OFF  : 'Oven is off       ',
            self.z == Z_HEAT : 'Oven is heating...',
            self.z == Z_WAIT : 'Oven is waiting...'
        }[1]
        door_str = ''
        if self.is_door_open == 0:
            door_str = 'Door closed'
        else:
            door_str = 'Door opened'

        return (
            f"{z_str}\n"
            f"{door_str}\n"
            f"{self.l_work.__str__()}\n"
            f"{self.l_heat.__str__()}\n"
            f"{self.l_inside.__str__()}\n"
        )

    def set_state(self, z):
        self.z = z


    def set_door_status(self):
        if self.is_door_open:
            self.is_door_open = 0
        else:
            self.is_door_open = 1
 

    def get_action(self, x):
        if x == X_TURN_0:
            self.l_work.set_status(L_OFF)
            self.l_heat.set_status(L_OFF)
            self.set_state(Z_OFF) 
            print(self)
        elif x == X_TURN_T and self.z != Z_WAIT:
            self.l_work.set_status(L_ON)
            self.l_heat.set_status(L_ON)
            self.set_state(Z_HEAT)
            print(self)
        elif x == X_OP_CL:
            if self.z == Z_WAIT:
                self.set_door_status()
                self.l_heat.set_status(L_ON)
                self.set_state(Z_HEAT)
                self.l_inside.set_status(L_OFF)
                print(self)
            else:
                self.set_door_status()
                self.l_heat.set_status(L_OFF)
                self.set_state(Z_WAIT)
                self.l_inside.set_status(L_ON)
                print(self)

def main():
    oven = Oven()
    print(
          f"Actions:\n"
          f"turn to 0 degree:     {X_TURN_0}\n"
          f"turn to not 0 degree: {X_TURN_T}\n"
          f"Open/close door:      {X_OP_CL}\n" 
          )
    while(1):
        x = int(input('\nEnter action: '))
        if x == 42:
            break
        oven.get_action(x)
main()
