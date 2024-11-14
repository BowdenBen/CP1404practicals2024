"""
CP1404/CP5632 Practical
Converts miles to kilometres.
Benjamin Bowden
Started 14/11/2024, completion time 1 hour
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class ConvertMilesKm(App):
    """ ConvertMilesKm is a Kivy App for converting miles to kilometres. """
    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (400, 150)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self, value):
        """ handle calculation for miles to kilometres """
        try:
            miles = float(value)
            kilometres = miles * 1.60934
            self.root.ids.output_label.text = str(kilometres)
        except ValueError:
            pass


ConvertMilesKm().run()