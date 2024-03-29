from ttkbootstrap.constants import *
from PIL import Image
import tkinter as tk
from ttkbootstrap import Style, Meter
import RPi.GPIO as GPIO
import time
Image.CUBIC= Image.BICUBIC



BEAM_PIN = 18
count = 0

def break_beam_callback(channel):
    global count
    if GPIO.input(BEAM_PIN):
        time.sleep(0.1)
    else:
        count += 1
        if count != 0:
            meter["amountused"] = count
        time.sleep(0.2)

def restart_counter():
    global count
    count = 0
    meter["amountused"] = count

GPIO.setmode(GPIO.BCM)
GPIO.setup(BEAM_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(BEAM_PIN, GPIO.BOTH, callback=break_beam_callback)

window = tk.Tk()
window.title("SCOTT FARM'S CASE COUNTER")
window.geometry("1080x720")
window.wm_overrideredirect(False)
window.state("normal")

style = Style(theme="superhero")

meter = Meter(
    window,
    metersize=400,
    padding=250,
    amountused=count,
    metertype="semi",
    textfont="size 35 italic bold",
    subtext="TOTAL CASES",
    subtextfont="size 15",
    subtextstyle="info",
    meterthickness=50,
    bootstyle="info",
    arcrange=270,
    interactive=False)

meter.pack()

# restart button
restart_button = tk.Button(window, text="Restart", command=restart_counter)
restart_button.pack()

try:

    window.mainloop()
except KeyboardInterrupt:
    pass

# Cleanup GPIO when the program exits
GPIO.cleanup()



