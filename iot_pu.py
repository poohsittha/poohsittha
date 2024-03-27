import pyfirmata

comport='COM3'

board=pyfirmata.Arduino(comport)

led_1=board.get_pin('d:2:o')

def led(fingerUp):
    if fingerUp==[0,1,0,0,0]:
        led_1.write(0)
        

    elif fingerUp==[0,1,1,0,0]:
        led_1.write(1)
    
    