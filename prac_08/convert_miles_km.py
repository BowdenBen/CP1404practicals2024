"""
CP1404/CP5632 Practical
Converts miles to kilometres.
Benjamin Bowden
Started 14/11/2024, completion time 1 hour
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

KMS_IN_MILE = 1.60934

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
            kilometres = miles * KMS_IN_MILE
            self.root.ids.output_label.text = str(kilometres)
        except ValueError:
            self.root.ids.input_number.text = "0"

    def handle_up(self, value):
        """ handle incrementing miles up by 1"""
        try:
            miles = float(value)
            miles += 1
            self.root.ids.input_number.text = str(miles)
            self.handle_calculate(self.root.ids.input_number.text)  # Trigger recalculation
        except ValueError:
            self.root.ids.input_number.text = "0"

    def handle_down(self, value):
        """ handle incrementing miles down by 1"""
        try:
            miles = float(value)
            miles -= 1
            self.root.ids.input_number.text = str(miles)
            self.handle_calculate(self.root.ids.input_number.text)  # Trigger recalculation
        except ValueError:
            self.root.ids.input_number.text = "0"

ConvertMilesKm().run()