# SIMPLE CALCULATOR ANDROID APP USING KIVY PACKAGE.

# Importing the necessary libraries.
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import kivy

# Checking the minimum version required to run a kivy application.
kivy.require('1.9.0')


# Designing the UI root element using kivy.
class MyRoot(BoxLayout):

    def __int__(self):
        super(MyRoot, self).__init__()

    # Creating a function that displays the appropriate symbol, number or operator.
    def calc_symbol(self, symbol):
        self.calc_field.text += symbol

    # Creating a function that is used to clear the contents of the text window.
    def clear(self):
        self.calc_field.text = ""

    # Creating a function that is used to delete the last character of the text window.
    def clear_last(self):
        self.calc_field.text = self.calc_field.text[:-1]

    # Creating a function that is used to compute the final result each of the operations.
    def get_result(self):
        self.calc_field.text = str(eval(self.calc_field.text))


# Creating the App itself.
class MyCalculator(App):

    def build(self):
        return MyRoot()


# In order to have the app running.
mycalculator = MyCalculator()
mycalculator.run()
