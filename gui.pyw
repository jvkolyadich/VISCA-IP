from tkinter import *
from tkinter.ttk import *

class MainWindow:
    def __init__(self):
        self.root = Tk()
        self.icon = "iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAABEElEQVRYR+"\
                    "2WSxLCIAxA6RncuvRCXIWDcBUu5NKtZ9CBMQ4EAklKbR3trlPa9/IhZTE7"\
                    "X8vOfPO1Ag8ic+KAJC9QUKqKrG9zFknBWKjLGAmshYMMyekJqOH38yWBT7"\
                    "drno0mixJYDQfySOKQAuroIWqiBM1+aGWAJWCtLbo9hMAdqgUTC6jgQNZI"\
                    "iAVw5BHunDPe++TBlHhzpwjkEr8rIOwDfQkiqNUHgvrHpaRAfKjaCczaF/"\
                    "Dq5pVGlgB30zfWdecArN9Kohp80/8Fg8ywBdi9ICiF6Hc8uxSfPZBIDqyH"\
                    "7YG0C/KBI9jnKQHEu6wmrOB4zI4mYet5FsBwDrAF4KMAxPd5L0wXwCWJEn"\
                    "8BTQae7e2JIXhnMdgAAAAASUVORK5CYII="
        self.root.iconphoto(False, PhotoImage(data=self.icon))

    def run(self):
        self.root.mainloop()

gui = MainWindow()
gui.run()
