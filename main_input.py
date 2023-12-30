from microbit import *

def vibrate():
  pin12.write_analog(512)
  sleep(100)
  pin12.write_analog(0)

pin13.set_pull(pin13.PULL_DOWN)
pin15.set_pull(pin13.PULL_DOWN)

display.clear()
while True:
    y = abs(pin2.read_analog() - 512)
    x = abs(pin1.read_analog() - 512)

    if y < 32:
       y = 0
    
    if x < 32:
       x = 0

    pin12.write_analog(min(x+y,1023))

    if button_a.is_pressed():
        display.show(Image.HAPPY)
    elif button_b.is_pressed():
        display.show(Image.SAD)
    else:
        pin8.set_pull(pin8.PULL_DOWN)
        display.show(pin8.read_digital())