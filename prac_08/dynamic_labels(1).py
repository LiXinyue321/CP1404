from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Label


NAMES = ("Bob Brown", "Cat Cyan", "Oren Ochre")


class DynamicWidgetsApp(App):

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.main()
        return self.root

    def main(self):
        """Create labels dynamically from list of names"""
        for name in NAMES:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)


DynamicWidgetsApp().run()
