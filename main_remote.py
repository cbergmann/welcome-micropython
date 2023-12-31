from microbit import *
import radio

pin13.set_pull(pin13.NO_PULL)
pin14.set_pull(pin14.NO_PULL)
pin15.set_pull(pin15.NO_PULL)
pin16.set_pull(pin16.NO_PULL)
pin8.set_pull(pin16.NO_PULL)

display.clear()
radio.on()
radio.config(group=1)
while True:
    y = pin2.read_analog() - 512
    x = pin1.read_analog() - 512

    send = ""
       
    if button_a.is_pressed():
        send += "A"
    
    if button_b.is_pressed():
        send += "B"
    
    if pin15.read_digital() == 0:
        send += "E"
    
    if pin13.read_digital() == 0:
        send += "C"
    
    if pin16.read_digital() == 0:
        send += "F"
    
    if pin14.read_digital() == 0:
        send += "D"
    
    if pin8.read_digital() == 0:
        send += "Z"
    
    if abs(y) > 32:
        if y < 0:
            send += "y"
        else:
            send += "Y"
        send += "{0:03d}".format(abs(y))
    
    if abs(x) > 32:
        if x < 0:
            send += "x"
        else:
            send += "X"
        send += "{0:03d}".format(abs(x))

    message = radio.receive()
    if message:
        display.scroll(message)
    if send == "":
        display.clear()
    else:
        display.scroll(send)

    radio.send(send)

    sleep(100)
