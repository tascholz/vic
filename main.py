from PySide6.QtCore import QSize, Qt, Signal, QObject
#Todo module entfernen
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QGridLayout
from PySide6.QtGui import QPixmap
import sys
from os import listdir
from os.path import isfile, join
from time import sleep
from bot import Bot
import threading

from modules import Calendar, ToDoList, ShoppingList, DiaShow, Communicate	

class Main():
	def __init__(self):
		self.running = True
		self.bot = Bot()
		self.stylesheet = """
			MainWindow {
				background-image: url(images/img.jpg);
				background-repeat: no-repeat;
				background-position: center;
			}
		"""
		self.module = ""

		#setting up the application and main window
		self.app = QApplication(sys.argv)
		self.app.setStyleSheet(self.stylesheet)
		self.window = MainWindow()
		self.window.show()

		#setting up the signals for communication between the widgets
		self.comm = Communicate()
		self.comm.calendar.connect(self.window.showCalendar)
		self.comm.shoppingList.connect(self.window.showShoppingList)
		self.comm.toDo.connect(self.window.showToDoList)
		self.comm.back.connect(self.window.goBack)

		#Bot Thread
		thread = threading.Thread(target=self.runBot)
		thread.setDaemon(True)
		thread.start()

		#Background Thread
		thread = threading.Thread(target=self.cycleBG)
		thread.setDaemon(True)
		thread.start()

		self.app.exec_()

	def runBot(self):
		while self.running:
			#listening for user command and retrieving parameters
			cmd, params = self.bot.run()
			print(params)

			self.module = getattr(sys.modules[__name__], cmd["module"])()
			method_to_call = getattr(self.module, cmd["method"])
			
			#when command is show
			if params == "":
				method_to_call()
				if cmd["module"] == "Calendar":
					self.comm.calendar.emit()
				elif cmd["module"] == "ToDoList":
					self.comm.toDo.emit()
				elif cmd["module"] == "ShoppingList":
					self.comm.shoppingList.emit()
				elif cmd["module"] == "DiaShow":
					self.comm.back.emit()

			#when command is create
			else:
				method_to_call(params)

	def cycleBG(self):
		index = 0
		allfiles = [f for f in listdir("images/") if isfile(join("images/", f))]
		while True:
			if index >= len(allfiles):
				index = 0
			
			self.stylesheet = "MainWindow { background-image: url(images/" + allfiles[index] + "); background-repeat: no-repeat; background-position: center;}"
			self.app.setStyleSheet(self.stylesheet)
			index += 1
			sleep(10)

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setWindowTitle("My App")	
		self.setFixedSize(800, 400)

	def showShoppingList(self):
		shoppingList = ShoppingList()
		shoppingList.buildModule()
		self.setCentralWidget(shoppingList)

	def showCalendar(self):
		cal = Calendar()
		cal.buildModule()
		self.setCentralWidget(cal)

	def showToDoList(self):
		toDoList = ToDoList()
		toDoList.buildModule()
		self.setCentralWidget(toDoList)

	def goBack(self):
		self.setCentralWidget(None)

class Communicate(QObject):
	calendar = Signal()
	shoppingList = Signal()
	toDo = Signal()
	back = Signal()

main = Main()