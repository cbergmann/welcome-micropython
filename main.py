#Imports go at the top
from microbit import *
import radio
import music
import audio

def on_gesture_screen_down():
    if mode == "s":
        radio.send("i XMAS")
    effect = audio.SoundEffect(waveform=audio.SoundEffect.WAVEFORM_SINE,freq_start=849,freq_end=1,vol_start=255,vol_end=0,duration=1000,fx=audio.SoundEffect.FX_NONE,shape=audio.SoundEffect.SHAPE_LINEAR)
    audio.play(effect,wait=True)
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
    if mode == "s":
        radio.send("l "
        "00900:"
        "00900:"
        "99999:"
        "00900:"
        "00900")
    display.show(Image(
        "09090:"
        "00000:"
        "00000:"
        "99999:"
        "00000"))
    effect = audio.SoundEffect(waveform=audio.SoundEffect.WAVEFORM_SINE,freq_start=3041,freq_end=3923,vol_start=59,vol_end=255,duration=500,fx=audio.SoundEffect.FX_WARBLE,shape=audio.SoundEffect.SHAPE_LINEAR)
    audio.play(effect,wait=False)
    display.show(Image(
        "09090:"
        "00000:"
        "09990:"
        "90009:"
        "09990"))
    display.show(Image(
        "09090:"
        "00000:"
        "00000:"
        "99999:"
        "00000"))

def switch_mode(newmode: str):
    global mode
    mode = newmode
    if mode == "s":
        music.stop()
        set_volume(0)
        display.scroll(mode)
    else:
        set_volume(127)
        audio.play(Sound.HELLO, wait=False)
        display.show(Image.HEART)

def on_button_pressed_ab():
    if display.read_light_level() > 50:
        music.play(music.POWER_UP, wait=False)
        display.show(Image(
            "90909:"
            "09990:"
            "99999:"
            "09990:"
            "90909"))
    else:
        music.play(music.POWER_DOWN, wait=False)
        display.show(Image(
            "00990:"
            "00099:"
            "00099:"
            "00099:"
            "00990"))

def on_received_string(receivedString):
    audio.play(Sound.GIGGLE,wait=False)
    #basic.show_icon(IconNames[receivedString[2:]])
    if receivedString[0:2] == "i ":
        image_const = receivedString[2:]
        if hasattr(Image,image_const):
            display.show(getattr(Image,image_const))
    elif receivedString[0:2] == "l ":
        display.show(Image(receivedString[2:50]))
    else:
      display.scroll(receivedString)

def on_button_pressed_b():
    if mode == "s":
        radio.send("Xmas")
    audio.play(Sound.SAD,wait=False)
    display.show(Image.SAD)

def on_pin_pressed_p1():
    switch_mode("s")

#Switch between modes r = recieve, s = send

mode = "r"
radio.on()
radio.config(group=1)
pin1.set_touch_mode(pin1.CAPACITIVE)
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
    elif accelerometer.was_gesture("face down"):
        on_gesture_screen_down()
    elif accelerometer.was_gesture("shake"):
        on_gesture_shake()
        
    sleep(100)