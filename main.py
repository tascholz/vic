from PySide6.QtCore import QSize, Qt, Signal, QObject
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QWidget, QVBoxLayout
import sys
from bot import Bot
import threading

from modules.calendar import Calendar
from modules.toDoList import ToDoList
from modules.shoppingList import ShoppingList	

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
		self.comm.toDo.connect(self.window.showToDoList)

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
			if data["method"] == "showToDoList":
				self.comm.toDo.emit()

class Communicate(QObject):
	calendar = Signal()
	sL = Signal()
	toDo = Signal()

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("My App")		
		self.showShoppingList()

	def showShoppingList(self):
		self.shoppingList = ShoppingList()
		self.setCentralWidget(self.shoppingList)

	def showCalendar(self):
		self.cal = Calendar()
		self.setCentralWidget(self.cal)
	def showToDoList(self):
		self.toDoList = ToDoList()
		self.setCentralWidget(self.toDoList)

main = Main()