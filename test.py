import viscaip.controller as vip

cam = vip.Controller("192.168.1.129")
print(cam.moveToAbsolute(10, -2000, 100))
