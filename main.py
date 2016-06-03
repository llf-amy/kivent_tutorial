from kivy.app import App
from kivy.uix.widget import Widget
import kivent_core ## add this import statement to kivent

class TestGame(Widget):
    pass

class YourAppNameApp(App):
    def build(self):
        pass
    
if __name__ == '__main__':
    YourAppNameApp().run()