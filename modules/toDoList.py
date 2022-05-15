import sys
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
import json

class ToDoList(QWidget):
	def __init__(self):
		super().__init__()
		with open('modules/data.json', 'r') as f:
			self.data = json.load(f)["tasks"]
		self.layout = QVBoxLayout()

		for entry in self.data:
			toDoLabel = QLabel(entry + ": " + self.data[entry])
			self.layout.addWidget(toDoLabel)
		self.setLayout(self.layout)