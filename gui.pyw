import tkinter as tk
from tkinter.ttk import *
from viscaip.controller import Controller

class MainWindow:
    def __init__(self):

        self.cam = Controller("127.0.0.1")
        self.move_speed = 7
        
        self.root = tk.Tk()
        self.root.title("VISCA-IP")
        self.icon = "iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAABEElEQVRYR"\
                    "+2WSxLCIAxA6RncuvRCXIWDcBUu5NKtZ9CBMQ4EAklKbR3trlPa9/IhZT"\
                    "E7X8vOfPO1Ag8ic+KAJC9QUKqKrG9zFknBWKjLGAmshYMMyekJqOH38yW"\
                    "BT7drno0mixJYDQfySOKQAuroIWqiBM1+aGWAJWCtLbo9hMAdqgUTC6jg"\
                    "QNZIiAVw5BHunDPe++TBlHhzpwjkEr8rIOwDfQkiqNUHgvrHpaRAfKjaC"\
                    "czaF/Dq5pVGlgB30zfWdecArN9Kohp80/8Fg8ywBdi9ICiF6Hc8uxSfPZ"\
                    "BIDqyH7YG0C/KBI9jnKQHEu6wmrOB4zI4mYet5FsBwDrAF4KMAxPd5L0w"\
                    "XwCWJEn8BTQae7e2JIXhnMdgAAAAASUVORK5CYII="
        self.root.iconphoto(False, tk.PhotoImage(data=self.icon))

        main_frame = Frame(self.root)

        power_frame = Frame(main_frame)

        turn_on = Button(power_frame, text="Turn on", command=self.cam.powerOn)
        turn_on.grid(row=1, column=1)
        
        turn_off = Button(power_frame, text="Turn off", command=self.cam.powerOff)
        turn_off.grid(row=1, column=2)

        power_frame.grid(row=1, column=1, columnspan=3, padx=15, pady=15)

        zoom_frame = Frame(main_frame)

        stop_zoom_on_release = tk.BooleanVar(zoom_frame, True)

        zoom_speed_label = Label(zoom_frame, text="Zoom:")
        zoom_speed_label.grid(row=1, column=1)

        zoom_speed_val = tk.StringVar()
        zoom_speed_val.set("0")

        zoom_speed_info = Label(zoom_frame, textvariable=zoom_speed_val)
        zoom_speed_info.grid(row=2, column=1)

        def processZoom(speed):
            if int(zoom_speed_val.get()) != speed:
                zoom_speed_val.set(speed)
                if speed > 0:
                    self.cam.zoomIn(speed)
                elif speed < 0:
                    self.cam.zoomOut(speed * -1)
                else:
                    self.cam.zoomStop()

        def resetZoom(slider):
            if stop_zoom_on_release.get():
                slider.set("0")

        zoom_speed_slider = Scale(zoom_frame, orient=tk.VERTICAL, from_=7, to=-7, value=0, command=lambda val: processZoom(int(float(val))))
        zoom_speed_slider.bind("<ButtonRelease-1>", lambda _: resetZoom(zoom_speed_slider))
        zoom_speed_slider.grid(row=3, column=1)

        zoom_frame.grid(row=2, column=1, padx=15, pady=15)

        move_speed_frame = Frame(main_frame)

        move_speed_label = Label(move_speed_frame, text="Movement speed:")
        move_speed_label.grid(row=1, column=1)

        move_speed_val = tk.StringVar()
        move_speed_val.set("8")

        move_speed_info = Label(move_speed_frame, textvariable=move_speed_val)
        move_speed_info.grid(row=2, column=1)

        move_speed_slider = Scale(move_speed_frame, orient=tk.VERTICAL, from_=17, to=1, value=8, command=lambda val: move_speed_val.set(int(float(val))))
        move_speed_slider.grid(row=3, column=1)

        move_speed_frame.grid(row=2, column=2, padx=15, pady=15)

        pt_frame = Frame(main_frame)

        stop_move_on_release = tk.BooleanVar(pt_frame, True)

        class PTButton(Button):
            def __init__(self, master=pt_frame, size=30, **kwargs):
                self.img = tk.PhotoImage()
                tk.Button.__init__(self, master, image=self.img, compound=tk.CENTER, width=size, height=size, **kwargs)

        def stopMoving(event):
            if stop_move_on_release.get():
                self.cam.moveStop()
        
        up_left = PTButton(text="↖")
        up_left.bind("<ButtonPress>", lambda _: self.cam.moveUpLeft(int(move_speed_val.get())))
        up_left.bind("<ButtonRelease>", stopMoving)
        up_left.grid(row=1, column=1)

        up = PTButton(text="↑")
        up.bind("<ButtonPress>", lambda _: self.cam.moveUp(int(move_speed_val.get())))
        up.bind("<ButtonRelease>", stopMoving)
        up.grid(row=1, column=2)

        up_right = PTButton(text="↗")
        up_right.bind("<ButtonPress>", lambda _: self.cam.moveUpRight(int(move_speed_val.get())))
        up_right.bind("<ButtonRelease>", stopMoving)
        up_right.grid(row=1, column=3)

        left = PTButton(text="←")
        left.bind("<ButtonPress>", lambda _: self.cam.moveLeft(int(move_speed_val.get())))
        left.bind("<ButtonRelease>", stopMoving)
        left.grid(row=2, column=1)

        stop = PTButton(text="■")
        stop.bind("<ButtonPress>", lambda _: self.cam.moveStop())
        stop.grid(row=2, column=2)

        right = PTButton(text="→")
        right.bind("<ButtonPress>", lambda _: self.cam.moveRight(int(move_speed_val.get())))
        right.bind("<ButtonRelease>", stopMoving)
        right.grid(row=2, column=3)

        down_left = PTButton(text="↙")
        down_left.bind("<ButtonPress>", lambda _: self.cam.moveDownLeft(int(move_speed_val.get())))
        down_left.bind("<ButtonRelease>", stopMoving)
        down_left.grid(row=3, column=1)

        down = PTButton(text="↓")
        down.bind("<ButtonPress>", lambda _: self.cam.moveDown(int(move_speed_val.get())))
        down.bind("<ButtonRelease>", stopMoving)
        down.grid(row=3, column=2)

        down_right = PTButton(text="↘")
        down_right.bind("<ButtonPress>", lambda _: self.cam.moveDownRight(int(move_speed_val.get())))
        down_right.bind("<ButtonRelease>", stopMoving)
        down_right.grid(row=3, column=3)

        pt_frame.grid(row=2, column=3, padx=15, pady=15)

        options_frame = Frame(main_frame)

        stop_zoom = Checkbutton(options_frame, onvalue=True, offvalue=False, variable=stop_zoom_on_release)
        stop_zoom.grid(row=1, column=1)

        stop_zoom_label = Label(options_frame, text="Stop zooming on release")
        stop_zoom_label.grid(row=1, column=2)

        stop_move = Checkbutton(options_frame, onvalue=True, offvalue=False, variable=stop_move_on_release)
        stop_move.grid(row=2, column=1)

        stop_move_label = Label(options_frame, text="Stop moving on release")
        stop_move_label.grid(row=2, column=2)

        options_frame.grid(row=3, column=1, columnspan=3, padx=15, pady=15)

        presets_section_frame = Frame(main_frame)

        presets_label = Label(presets_section_frame, text="Presets:")
        presets_label.grid(row=1, column=1, pady=10)

        presets_frame = Frame(presets_section_frame)

        should_set = tk.BooleanVar(presets_section_frame, False)

        class Preset():
            def __init__(self, cam, preset_num, name):
                self.cam = cam
                self.num = preset_num
                self.name = tk.StringVar(value=name)
                self.button = Button(presets_frame, textvariable=self.name, command=self.preset_action)

            def preset_action(self):
                if should_set.get():
                    self.cam.presetSet(self.num)
                    preset_set_button.configure(background="SystemButtonFace")
                    should_set.set(False)
                else:
                    self.cam.presetRecall(self.num)

        preset_rows = 8
        preset_num = 1
        for i in range(preset_rows):
            for j in range(3):
                gui_preset = Preset(self.cam, preset_num, f"Preset {preset_num}")
                gui_preset.button.grid(row=i+1, column=j+1)
                preset_num += 1

        def preset_set(set_button):
            if not should_set.get():
                set_button.configure(background="#007bd9")
                should_set.set(True)
            else:
                set_button.configure(background="SystemButtonFace")
                should_set.set(False)

        preset_set_button = tk.Button(presets_frame, text="Store position", command=lambda: preset_set(preset_set_button))
        preset_set_button.grid(row=i+2, column=1, columnspan=j+1, sticky="NESW", pady=2)

        presets_frame.grid(row=2, column=1, pady=10)
                
        presets_section_frame.grid(row=4, column=1, columnspan=3, padx=15, pady=15)
        
        main_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.root.update()
        self.root.minsize(main_frame.winfo_width()+20, main_frame.winfo_height())

    def run(self):
        self.root.mainloop()

gui = MainWindow()
gui.run()
