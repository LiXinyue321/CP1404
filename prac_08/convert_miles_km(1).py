
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934


class ConvertToMilesApp(App):
    output_km = StringProperty()

    def build(self):
        """Build the app and load the kv file for the UI"""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self, text):
        """Convert input miles to number and update result"""
        miles = self.convert_to_number(text)
        self.update_result(miles)

    def handle_increment(self, text, change):
        """Increment miles and update text input"""
        miles = self.convert_to_number(text) + change
        self.root.ids.input_miles.text = str(miles)

    def update_result(self, miles):
        """Update the result label with calculated km"""
        self.output_km = str(miles * MILES_TO_KM)

    @staticmethod
    def convert_to_number(text):
        """Convert text to float, handle invalid input"""
        try:
            return float(text)
        except ValueError:
            return 0.0


ConvertToMilesApp().run()
