
__version__ = "1.0.0"

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class R2App(App):
    def build(self):
        layout = BoxLayout(
            orientation="vertical",
            padding=25,
            spacing=20
        )

        self.message = Label(
            text="به R² خوش آمدی!",
            font_size="24sp"
        )

        button = Button(
            text="شروع",
            font_size="22sp",
            size_hint=(1, 0.3)
        )
        button.bind(on_press=self.start_app)

        layout.add_widget(self.message)
        layout.add_widget(button)
        return layout

    def start_app(self, instance):
        self.message.text = "اولین برنامه من!"

R2App().run()
