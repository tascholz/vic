import sys
from PySide6.QtWidgets import QWidget, QCalendarWidget, QLabel, QApplication, QGraphicsOpacityEffect, QVBoxLayout
from PySide6.QtCore import QDate
import json

class Calendar(QWidget):
	def __init__(self):
		super().__init__()
		with open('modules/data.json', 'r') as f:
			self.data = json.load(f)["dates"]
		self.layout = QVBoxLayout()

		print(self.data)
		for entry in self.data:
			dateLabel = QLabel(entry + ": " + self.data[entry])
			self.layout.addWidget(dateLabel)
		self.setLayout(self.layout)


def main():
	app = QApplication()
	ex = Calendar()
	sys.exit(app.exec())

if __name__ == '__main__':
	main()
