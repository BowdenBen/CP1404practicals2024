"""
Kivy example for CP1404, IT@JCU
Dynamically create labels
Benjamin Bowden
est. time: 1 hour
Actual time: 30 minutes
"""


from kivy.app import App
from kivy.uix.label import Label
from kivy.lang import Builder


class DynamicLabelsApp(App):
    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]  # Data

    def build(self):
        """Load the Kivy layout and populate dynamic labels."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')  # Load layout
        for name in self.names:  # Loop through the names
            label = Label(text=name)  # Create a label for each name
            self.root.ids.main.add_widget(label)  # Add the label to the layout
        return self.root

    def create_labels(self):
        """Create Label widgets dynamically and add to the main layout."""
        for name in self.names:
            self.root.ids.main.add_widget(Label(text=name))


if __name__ == '__main__':
    DynamicLabelsApp().run()