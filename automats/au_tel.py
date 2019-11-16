#!/usr/bin/env python3.7

# TV automata

# States const
Z_OFF = 0
Z_CH1 = 1 
Z_CH2 = 2

# Actions const
X_SET_POWER = 1
X_SET_CHAN  = 2

# Lamp states const
L_OFF = 0
L_ON  = 1

# # # # # # # # # # # # # # # # # # # # # # #

class Lamp:
    l = L_OFF
    name = 'default lamp' 
    def __init__(self, name):
        self.name = name
    def __str__(self):
        str_status = ''
        if self.l == L_OFF:
            str_status = ': off'
        else:
            str_status = ': on'
        return self.name + str_status
    def set_state(self, state):
        self.l = state

class TV:
    z = Z_OFF
    l = Lamp('TV lamp')
    def __str__(self):
        str_z = ''
        if self.z == Z_OFF:
            str_z = 'TV is off'
        elif self.z == Z_CH1:
            str_z = 'TV showing channel 1'
        elif self.z == Z_CH2:
            str_z = 'TV showing channel 2'
        return (
            f"{str_z}\n"
            f"{self.l.__str__()}\n"
        )
    def set_power(self):
        if self.z == Z_OFF:
            self.z = Z_CH1
            self.l.set_state(L_ON)
        else:
            self.z = Z_OFF
            self.l.set_state(L_OFF)
    
    def set_chan(self):
        if self.z == Z_CH1:
            self.z = Z_CH2
        elif self.z == Z_CH2:
            self.z = Z_CH1

    def get_action(self, x):
        if x == X_SET_POWER:
           self.set_power()
        else:
            self.set_chan()
        print(self)

print(
    f"Actions:\n"
    f"Set power:   {X_SET_POWER}\n"
    f"set channel: {X_SET_CHAN}\n"
)

tv = TV()
while(1):
    x = int(input('Enter action: '))
    if x == 42:
        break
    tv.get_action(x)

