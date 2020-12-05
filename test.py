import viscaip.controller as vip
import time

cam = vip.Controller("192.168.1.129")

def pulpit():
    cam.moveToAbsolute(6, -980, -64)
    cam.zoomSet(11000)

def chapel():
    cam.zoomSet(0)
    cam.moveToAbsolute(9, -850, 10)

presets = [pulpit, chapel]
for preset in presets:
    print(preset.__name__)

while True:
    input_preset = input("Enter a preset name: ")
    found = False
    for preset in presets:
        if preset.__name__ == input_preset:
            found = True
            preset()
    if not found:
        print("Preset not found")


