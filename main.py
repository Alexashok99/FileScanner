


from gui.gui import AppGUI
# from src.scanner import Scanner

class MainApp:
    def __init__(self):
        self.app = AppGUI()

    def gui_run(self):
        self.app.mainloop()


if __name__ == "__main__":
    MainApp().gui_run()
