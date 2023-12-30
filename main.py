# Imports go at the top
from microbit import *
import music
import radio
from audio import SoundEffect

def on_gesture_screen_down():
    audio.play(SoundEffect(waveform=SoundEffect.WAVEFORM_SINE,freq_start=849,freq_end=1,vol_start=255,vol_end=0,duration=1000,fx=SoundEffect.FX_NONE,shape=SoundEffect.SHAPE_LINEAR),wait=True)
    display.show(Image.ASLEEP)

def on_logo_touched():
    #record.set_mic_gain(record.AudioLevels.LOW)
    #record.start_recording(record.BlockingState.NONBLOCKING)
    while input.logo_is_pressed():
        display.scroll(microphone.sound_level())
        sleep(5)
    music.stop()
    display.clear()
    #record.play_audio(record.BlockingState.BLOCKING)

def on_button_pressed_a():
    if mode == "s":
        radio.send("Leo")
    audio.play(Sound.SPRING, wait=False)
    display.show(Image.HAPPY)

def on_pin_pressed_p2():
    switch_mode("r")

def on_gesture_shake():
    display.show(Image("""
        . # . # .
        . . . . .
        . . . . .
        # # # # #
        . . . . .
        """))
    audio.play(SoundEffect(waveform=SoundEffect.WAVEFORM_SINE,freq_start=3041,freq_end=3923,vol_start=59,vol_end=255,duration=500,fx=SoundEffect.FX_WARBLE,shape=SoundEffect.SHAPE_LINEAR),wait=False)
    display.show(Image("""
        . # . # .
        . . . . .
        . # # # .
        # . . . #
        . # # # .
        """))
    display.show(Image("""
        . # . # .
        . . . . .
        . . . . .
        # # # # #
        . . . . .
        """))

def switch_mode(newmode: str):
    global mode
    mode = newmode
    if mode == "s":
        music.stop()
        speaker.off()
    else:
        speaker.on()
    display.scroll(mode)
    sleep(500)
    start()

def on_button_pressed_ab():
    if input.light_level() > 50:
        music.play(music.POWER_UP, wait=False)
        display.show(Image("""
            # . # . #
            . # # # .
            # # # # #
            . # # # .
            # . # . #
            """))
    else:
        music.play(music.POWER_DOWN, wait=False)
        display.show(Image("""
            . . # # .
            . . . # #
            . . . # #
            . . . # #
            . . # # .
            """))

def on_received_string(receivedString):
    audio.play(Sound.GIGGLE,wait=False)
    # basic.show_icon(IconNames[receivedString[2:]])
    if receivedString.substr(0, 2) == "i ":
        # TODO: decode image enum name
        pass
    elif receivedString.substr(0, 2) == "l ":
        display.show(Image(receivedString.substr(2,50)))
    else:
        display.scroll(receivedString)

def on_button_pressed_b():
    if mode == "s":
        radio.send("Xmas")
    audio.play(Sound.SAD,wait=False)
    display.show(Image.SAD)

def on_pin_pressed_p1():
    switch_mode("s")

def start():
    audio.play(Sound.HELLO, wait=False)
    display.show(Image.HEART)

# Switch between modes r = recieve, s = send

mode = "r"
radio.on()
radio.config(group=1)
pin1.set_touch_mode(pin0.CAPACITIVE)
pin2.set_touch_mode(pin2.CAPACITIVE)
pin_logo.set_touch_mode(pin_logo.CAPACITIVE)
if button_a.is_pressed():
    switch_mode("s")
else:
    switch_mode("r")

while True:
    message = radio.receive()

    if message:
        on_received_string(message)
    elif pin1.is_touched():
        on_pin_pressed_p1()
    elif pin2.is_touched():
        on_pin_pressed_p2()
    elif pin_logo.is_touched():
        on_logo_touched()
    elif button_a.is_pressed() and button_b.is_pressed():
        on_button_pressed_ab()
    elif button_a.was_pressed():
        on_button_pressed_a()
    elif button_b.was_pressed():
        on_button_pressed_b()
    elif accelerometer.was_gesture('face_down'):
        on_gesture_screen_down()
    elif accelerometer.was_gesture('shake'):
        on_gesture_shake()
        
    sleep(100)