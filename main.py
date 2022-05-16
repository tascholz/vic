from PySide6.QtCore import QSize, Qt, Signal, QObject
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QWidget, QVBoxLayout, QGridLayout
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

		#Test
		self.module = ""

		self.app = QApplication(sys.argv)
		
		self.app.setStyleSheet(self.stylesheet)

		self.window = MainWindow()
		
		self.window.show()

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

			cmd, params = self.bot.run()
			print(params)
			self.module = getattr(sys.modules[__name__], cmd["module"])()
			method_to_call = getattr(self.module, cmd["method"])
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
			else:
				method_to_call(params)

	def cycleBG(self):
		index = 0
		allfiles = [f for f in listdir("images/") if isfile(join("images/", f))]
		while True:
			if index >= len(allfiles):
				index = 0

			print(allfiles[index])
			
			self.stylesheet = "MainWindow { background-image: url(images/" + allfiles[index] + "); background-repeat: no-repeat; background-position: center;}"
			self.app.setStyleSheet(self.stylesheet)
			index += 1
			sleep(10)



class Communicate(QObject):
	calendar = Signal()
	shoppingList = Signal()
	toDo = Signal()
	back = Signal()

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

main = Main()