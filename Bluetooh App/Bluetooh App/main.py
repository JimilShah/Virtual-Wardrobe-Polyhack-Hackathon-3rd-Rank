from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivymd.app import MDApp
from kivymd.uix.textfield import MDTextField

Window.size = (400, 600)
screen_helper = """
Screen:
    MDNavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'Terminal'
                        left_action_items: [['menu', lambda x: nav_drawer.set_state('toggle')]]
                        right_action_items: [["connection", lambda x: app.callback()],["delete", lambda x: app.callback_2()], ["dots-vertical", lambda x: app.callback_3()]]
                        elevation:5
                    Widget:
        MDNavigationDrawer:
            id:nav_drawer 

            BoxLayout:
                orientation:'vertical'
                spacing:'8dp'
                padding:'8dp'
                Image:
                    source:'Loop.jpg'
                    text:'Serial Bluetooth Terminal'
                    font_style:'Subtitle1'
                    size_hint_y: None
                MDLabel:
                    text:'Bluetooth Serial Terminal'
                    font_style:'Subtitle1'
                    size_hint_y: None
                    height: self.texture_size[1]
                ScrollView:
                    MDList:
                        OneLineListItem:
                            text:'Terminal'

                        OneLineListItem:
                            text:'Devices'

                        OneLineListItem:
                            text:'Settings'

                        OneLineListItem:
                            text:'Info'
"""


class DemoApp(MDApp):

    def build(self):
        screen = Builder.load_string(screen_helper)
        username = MDTextField(text='', icon_right="send", pos_hint={'x': 0.0, 'center_y': 0.05})
        self.theme_cls.primary_palette = "Blue"
        layout = GridLayout(cols=7, row_force_default=True, row_default_height=10, size_hint=(None, None),
                            size=(400, 75))
        btn1 = Button(text='M1')
        btn2 = Button(text='M2')
        btn3 = Button(text='M3')
        btn4 = Button(text='M4')
        btn5 = Button(text='M5')
        btn6 = Button(text='M6')
        btn7 = Button(text='M7')

        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)
        layout.add_widget(btn4)
        layout.add_widget(btn5)
        layout.add_widget(btn6)
        layout.add_widget(btn7)
        screen.add_widget(layout)
        screen.add_widget(username)
        return screen

    def nav_drawer(self):
        print("NAVIGATION")

    def callback(self):
        pass

    def callback_2(self):
        pass

    def callback_3(self):
        pass


DemoApp().run()
