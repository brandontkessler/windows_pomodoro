from win10toast import ToastNotifier
import time

class Pomodoro:
    def __init__(self):
        self.toaster = ToastNotifier()
        

    def task(self, timing=1500):
        print("starting task...")
        time.sleep(timing)
        self.toaster.show_toast(
            "POMODORO", 
            "Your task has completed!", 
            threaded=True, 
            icon_path=None, 
            duration=3
        )
    
    def short_break(self, timing=300):
        print("starting break...")
        time.sleep(timing)
        self.toaster.show_toast(
            "POMODORO", 
            "Short break is over!", 
            threaded=True, 
            icon_path=None, 
            duration=3
        )

    def medium_break(self, timing=1800):
        print("starting break...")
        time.sleep(timing)
        self.toaster.show_toast(
            "POMODORO", 
            "Medium break is over!", 
            threaded=True, 
            icon_path=None, 
            duration=3
        )

    def long_break(self, timing=3600):
        print("starting break...")
        time.sleep(timing)
        self.toaster.show_toast(
            "POMODORO", 
            "Long break is over!", 
            threaded=True, 
            icon_path=None, 
            duration=3
        )

if __name__=='__main__':
    pomodoro = Pomodoro()
    pomodoro.task()
    pomodoro.short_break()
