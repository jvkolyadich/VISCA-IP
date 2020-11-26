import viscaip.controller as vip
import time

cam = vip.Controller("192.168.1.129")

def pulpit():
    duration = 2
    cam.moveToAbsolute(17, -980, -64)
    cam.zoomSet(12000)
    time.sleep(duration)

def chapel():
    duration = 2
    cam.zoomSet(0)
    cam.moveToAbsolute(17, -850, 10)
    time.sleep(duration)

presets = [pulpit, chapel]
print(presets)
while True:
    input_preset = input("Enter a preset name: ")
    found = False
    for preset in presets:
        if preset.__name__ == input_preset:
            found = True
            preset()
    if not found:
        print("Preset not found")

