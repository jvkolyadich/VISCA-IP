from tkinter import *
from tkinter.ttk import *
from viscaip.controller import Controller

class MainWindow:
    def __init__(self):

        self.cam = Controller("192.168.1.129")
        self.move_speed = 7
        
        self.root = Tk()
        self.root.title("VISCA-IP")
        #self.root.geometry("500x400")
        self.icon = "iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAABEElEQVRYR"\
                    "+2WSxLCIAxA6RncuvRCXIWDcBUu5NKtZ9CBMQ4EAklKbR3trlPa9/IhZT"\
                    "E7X8vOfPO1Ag8ic+KAJC9QUKqKrG9zFknBWKjLGAmshYMMyekJqOH38yW"\
                    "BT7drno0mixJYDQfySOKQAuroIWqiBM1+aGWAJWCtLbo9hMAdqgUTC6jg"\
                    "QNZIiAVw5BHunDPe++TBlHhzpwjkEr8rIOwDfQkiqNUHgvrHpaRAfKjaC"\
                    "czaF/Dq5pVGlgB30zfWdecArN9Kohp80/8Fg8ywBdi9ICiF6Hc8uxSfPZ"\
                    "BIDqyH7YG0C/KBI9jnKQHEu6wmrOB4zI4mYet5FsBwDrAF4KMAxPd5L0w"\
                    "XwCWJEn8BTQae7e2JIXhnMdgAAAAASUVORK5CYII="
        self.root.iconphoto(False, PhotoImage(data=self.icon))
        

        main_frame = Frame(self.root)

        power_frame = Frame(main_frame)

        turn_on = Button(power_frame, text="Turn on", command=self.cam.powerOn)
        turn_on.grid(row=1, column=1)
        
        turn_off = Button(power_frame, text="Turn off", command=self.cam.powerOff)
        turn_off.grid(row=1, column=2)

        power_frame.pack(side=TOP, padx=15, pady=15)

        pt_frame = Frame(main_frame)

        up_left = Button(pt_frame, text="↖", width=2)
        up_left.bind("<ButtonPress>", lambda _: self.cam.moveUpLeft(self.move_speed))
        up_left.bind("<ButtonRelease>", lambda _: self.cam.moveStop())
        up_left.grid(row=1, column=1)

        up = Button(pt_frame, text="↑", width=2)
        up.bind("<ButtonPress>", lambda _: self.cam.moveUp(self.move_speed))
        up.bind("<ButtonRelease>", lambda _: self.cam.moveStop())
        up.grid(row=1, column=2)

        up_right = Button(pt_frame, text="↗", width=2)
        up_right.bind("<ButtonPress>", lambda _: self.cam.moveUpRight(self.move_speed))
        up_right.bind("<ButtonRelease>", lambda _: self.cam.moveStop())
        up_right.grid(row=1, column=3)

        left = Button(pt_frame, text="←", width=2)
        left.bind("<ButtonPress>", lambda _: self.cam.moveLeft(self.move_speed))
        left.bind("<ButtonRelease>", lambda _: self.cam.moveStop())
        left.grid(row=2, column=1)

        stop = Button(pt_frame, text="■", width=2)
        stop.bind("<ButtonPress>", lambda _: self.cam.moveStop())
        stop.grid(row=2, column=2)

        right = Button(pt_frame, text="→", width=2)
        right.bind("<ButtonPress>", lambda _: self.cam.moveRight(self.move_speed))
        right.bind("<ButtonRelease>", lambda _: self.cam.moveStop())
        right.grid(row=2, column=3)

        down_left = Button(pt_frame, text="↙", width=2)
        down_left.bind("<ButtonPress>", lambda _: self.cam.moveDownLeft(self.move_speed))
        down_left.bind("<ButtonRelease>", lambda _: self.cam.moveStop())
        down_left.grid(row=3, column=1)

        down = Button(pt_frame, text="↓", width=2)
        down.bind("<ButtonPress>", lambda _: self.cam.moveDown(self.move_speed))
        down.bind("<ButtonRelease>", lambda _: self.cam.moveStop())
        down.grid(row=3, column=2)

        down_right = Button(pt_frame, text="↘", width=2)
        down_right.bind("<ButtonPress>", lambda _: self.cam.moveDownRight(self.move_speed))
        down_right.bind("<ButtonRelease>", lambda _: self.cam.moveStop())
        down_right.grid(row=3, column=3)

        pt_frame.pack(side=TOP, padx=15, pady=15)
        
        main_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    def run(self):
        self.root.mainloop()

gui = MainWindow()
gui.run()
