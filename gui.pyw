from tkinter import *
from tkinter.ttk import *
from viscaip import controller

class MainWindow:
    def __init__(self):
        self.root = Tk()
        self.root.title("VISCA-IP")
        self.root.geometry("500x400")
        self.icon = "iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAABEElEQVRYR"\
                    "+2WSxLCIAxA6RncuvRCXIWDcBUu5NKtZ9CBMQ4EAklKbR3trlPa9/IhZT"\
                    "E7X8vOfPO1Ag8ic+KAJC9QUKqKrG9zFknBWKjLGAmshYMMyekJqOH38yW"\
                    "BT7drno0mixJYDQfySOKQAuroIWqiBM1+aGWAJWCtLbo9hMAdqgUTC6jg"\
                    "QNZIiAVw5BHunDPe++TBlHhzpwjkEr8rIOwDfQkiqNUHgvrHpaRAfKjaC"\
                    "czaF/Dq5pVGlgB30zfWdecArN9Kohp80/8Fg8ywBdi9ICiF6Hc8uxSfPZ"\
                    "BIDqyH7YG0C/KBI9jnKQHEu6wmrOB4zI4mYet5FsBwDrAF4KMAxPd5L0w"\
                    "XwCWJEn8BTQae7e2JIXhnMdgAAAAASUVORK5CYII="
        self.root.iconphoto(False, PhotoImage(data=self.icon))

    def run(self):
        self.root.mainloop()

gui = MainWindow()
gui.run()
