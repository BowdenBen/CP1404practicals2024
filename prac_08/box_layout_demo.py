from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    """Kivy application demonstrating a simple BoxLayout GUI with greeting functionality."""

    def build(self):
        """Builds the Kivy application by setting the window title and loading the Kv file.
        Returns:
            The root widget created from the Kv file.
        """
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Handles the greet action by updating the output label with a greeting message.
        Sets the output label text to "Hello" followed by the name entered in the input field.
        """
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def handle_clear(self):
        """Clears the greeting text in the output label."""
        self.root.ids.output_label.text = " "


BoxLayoutDemo().run()
