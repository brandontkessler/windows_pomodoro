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

        # Await toaster completion
        while self.toaster.notification_active():
            time.sleep(0.1)
        return
    

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
        
        # Await toaster completion
        while self.toaster.notification_active():
            time.sleep(0.1)
        return


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

        # Await toaster completion
        while self.toaster.notification_active():
            time.sleep(0.1)
        return


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

        # Await toaster completion
        while self.toaster.notification_active():
            time.sleep(0.1)
        return
        

if __name__=='__main__':
    pomodoro = Pomodoro()
    pomodoro.task(2)
    pomodoro.short_break(1)
