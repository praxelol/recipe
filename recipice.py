import requests
import random
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
import sys

api_key = "9fea5a0cae1f4d078645627cc8d22f18"
response = requests.get("https://api.spoonacular.com/recipes/random?apiKey={}".format(api_key))


recipe_data = response.json()


random_recipe = random.choice(recipe_data["recipes"])


app = QApplication([])


widget = QWidget()

# Set the title of the widget
widget.setWindowTitle(random_recipe["title"])

# Create a label for the recipe image


# Create a label for the recipe instructions
recipe_instructions = QLabel(random_recipe["instructions"])
recipe_instructions.setWordWrap(True)



# Create the refresh button
refresh_button = QPushButton("Refresh")

# Create the layout for the widget
layout = QVBoxLayout()

# Add the refresh button to the layout
layout.addWidget(refresh_button)

# Set the layout for the widget




# Define a function that fetches a new random recipe and updates the widget's content
def refresh():
    # Fetch a new random recipe
    response = requests.get("https://api.spoonacular.com/recipes/random?apiKey={}".format(api_key))
    recipe_data = response.json()
    random_recipe = random.choice(recipe_data["recipes"])

    # Update the widget's title
    widget.setWindowTitle(random_recipe["title"])

    # Update the recipe image
    

    # Update the recipe instructions
    recipe_instructions.setText(random_recipe["instructions"])

# Connect the clicked signal of the refresh button to the refresh function
refresh_button.clicked.connect(refresh)

# Add the labels to the widget
widget.setLayout(layout)

widget.layout().addWidget(recipe_instructions)
widget.setStyleSheet("background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 #ee9ca7, stop: 1 #ffdde1);")

recipe_instructions.setStyleSheet("font-size: 18px; color:#734b6d;")
refresh_button.setStyleSheet("background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 #de6262, stop: 1 #ffb88c);")

# creating a QGraphicsDropShadowEffect object
shadow = QGraphicsDropShadowEffect()

# setting blur radius (optional step)
shadow.setBlurRadius(15)

# adding shadow to the label
refresh_button.setGraphicsEffect(shadow)

# Show the widget
widget.show()

# Run the application loop
app.exec_()
