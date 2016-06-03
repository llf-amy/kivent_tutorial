from kivy.app import App
from kivy.uix.widget import Widget
import kivent_core
from kivent_core.managers.resource_managers import texture_manager
from random import randint, choice
from kivy.core.window import Window
from kivy.clock import Clock
from kivent_core.gameworld import GameWorld
from kivent_core.systems.position_systems import PositionSystem2D
from kivent_core.systems.renderers import Renderer
from kivent_core.managers.resource_managers import texture_manager
from kivy.properties import StringProperty

## load the atlas with our sprites
texture_manager.load_atlas('assets/background_objects.atlas')

class TestGame(Widget):
    def __init__(self, **kwargs):
        super(TestGame, self).__init__(**kwargs)
        self.gameworld.init_gameworld(['position', 'renderer'], callback = self.init_game)

    def init_game(self):
        self.setup_states()
        self.set_state()
        self.load_models()
        self.draw_some_stuff()

    def setup_states(self):
        ## add 'renderer' here to make sure the canvas knows about it and is unpaused
        self.gameworld.add_state(state_name='main',
                                 systems_added = ['renderer'],
                                 systems_removed = [],
                                 systems_paused = [],
                                 systems_unpaused = ['renderer'],
                                 screenmanager_screen = 'main')
    def set_state(self):
        self.gameworld.state = 'main'

    def load_models(self):
        ### load a model of the 'star1' texture with 2 different sizes (7., 7.) and (10., 10.).
        model_manager = self.gameworld.model_manager
        model_manager.load_textured_rectangle('vertex_format_4f', 7., 7., 'star1', 'star1-4')
        model_manager.load_textured_rectangle('vertex_format_4f', 10., 10., 'star1', 'star1-4-2')

    def draw_some_stuff(self):
        init_entity = self.gameworld.init_entity
        for x in range(1000):
            pos = randint(0, Window.width), randint(0, Window.height)
            model_key = choice(['star1-4', 'star1-4-2'])
            ## create_dict will dictate the order to create components
            create_dict = {
                'position':pos,
                'renderer': {'texture': 'star1', 'model_key': model_key}}
            ent = init_entity(create_dict, ['position', 'renderer'])

class DebugPanel(Widget):
    fps = StringProperty(None)

    def __init__(self, **kwargs):
        super(DebugPanel, self).__init__(**kwargs)
        Clock.schedule_once(self.update_fps)

    def update_fps(self,dt):
        self.fps = str(int(Clock.get_fps()))
        Clock.schedule_once(self.update_fps, .05)

class YourAppNameApp(App):
    def build(self):
        pass

if __name__ == '__main__':
    YourAppNameApp().run()
