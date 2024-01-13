from kivy.app import App
from kivy.uix.widget import Widget

class AppLayout(Widget):
    def set_time(self, time):
        self.ids.time_picker.set_time(time)

class Alarm(App):
    def build(self):
        return AppLayout()

if __name__ == "__main__":
    Alarm().run()