#!/usr/bin/env python3
import numpy as np
import sounddevice as sd
import pynput.mouse
import pynput.keyboard

duration = 10  # in seconds

volume = 0

released = False

keyboard = pynput.keyboard.Controller()
mouse = pynput.mouse.Controller()


def audio_callback(indata, frames, time, status):
    global volume
    volume_norm = np.linalg.norm(indata) * 10
    volume = volume_norm


stream = sd.InputStream(callback=audio_callback)
with stream:
    while True:
        if volume > 5:
            # keyboard.press('L')
            # keyboard.press(pynput.keyboard.Key.space)
            if released:
                mouse.press(pynput.mouse.Button.left)
                released = False

                print("                  doing it")

        else:
            # keyboard.release('L')
            # keyboard.release(pynput.keyboard.Key.space)
            if not released:
                mouse.release(pynput.mouse.Button.left)
                released = True

                print("stopped")
