from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen

class main(MDApp):
    ventanaPrincipal = ObjectProperty()

    def build(self):
        screen = MDScreen()

        return screen

main().run()