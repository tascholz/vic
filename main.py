from PySide6.QtCore import QSize, Qt, Signal, QObject
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QWidget, QVBoxLayout
import sys
from bot import Bot
import threading

class Main():
	def __init__(self):
		self.running = True
		self.bot = Bot()

		self.app = QApplication(sys.argv)
		self.window = MainWindow()
		self.window.show()

		self.comm = Communicate()
		self.comm.calendar.connect(self.window.showCalendar)
		self.comm.sL.connect(self.window.showShoppingList)

		thread = threading.Thread(target=self.runBot)
		thread.setDaemon(True)
		thread.start()
		self.app.exec_()

	def runBot(self):
		while self.running:
			data = self.bot.run()
			if data["method"] == "showCalendar":
				self.comm.calendar.emit()
			if data["method"] == "showShoppingList":
				self.comm.sL.emit()

class Communicate(QObject):
	calendar = Signal()
	sL = Signal()

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("My App")

		self.diaButton = QPushButton("DiaShowButton")
		self.diaButton.clicked.connect(self.showShoppingList)

		self.calButton = QPushButton("CalendarButton")
		self.calButton.clicked.connect(self.showCalendar)
		
		self.showShoppingList()

	def showShoppingList(self):
		self.dia = Dia(self)
		self.setCentralWidget(self.dia)

	def showCalendar(self):
		self.cal = Calendar(self)
		self.setCentralWidget(self.cal)

class Dia(QWidget):
	def __init__(self, parent):
		super().__init__()
		layout = QVBoxLayout()
		self.label = QLabel("EinkaufsListe")

		self.button = QPushButton("Calendar")
		self.button.clicked.connect(parent.showCalendar)
		layout.addWidget(self.label)
		layout.addWidget(self.button)
		self.setLayout(layout)

class Calendar(QWidget):
	def __init__(self, parent):
		super().__init__()
		layout = QVBoxLayout()
		self.label = QLabel("Kalender")

		self.button = QPushButton("Dia")
		self.button.clicked.connect(parent.showShoppingList)
		layout.addWidget(self.label)
		layout.addWidget(self.button)
		self.setLayout(layout)

main = Main()