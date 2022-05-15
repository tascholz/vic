import sys
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
import json

class ShoppingList(QWidget):
	def __init__(self):
		super().__init__()
		with open('modules/data.json', 'r') as f:
			self.data = json.load(f)["shoppingItems"]
		self.layout = QVBoxLayout()

		for entry in self.data:
			itemLabel = QLabel(entry)
			self.layout.addWidget(itemLabel)
		self.setLayout(self.layout)