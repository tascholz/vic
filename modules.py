import sys
from PySide6.QtCore import QObject, Signal 
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QGridLayout, QGraphicsOpacityEffect
from PySide6.QtGui import QPixmap
import json

datapath = 'modules/data.json'

class Communicate(QObject):
	calendar = Signal(object)
	shoppingList = Signal(object)
	toDo = Signal(object)


class Module(QWidget):
	def __init__(self):
		super().__init__()
		with open(datapath, 'r') as f:
			self.dict = json.load(f)
		self.layout = QVBoxLayout()
		

		#Test
		op = QGraphicsOpacityEffect(self)
		op.setOpacity(0.70)
		self.setGraphicsEffect(op)
		self.setAutoFillBackground(True)

	def buildModule(self):
		pass

	def storeData(self, params):
		pass

	def dumpJson(self):
		with open(datapath, 'w') as f:
			json.dump(self.dict, f)

class Calendar(Module):
	def __init__(self):
		super().__init__()

	def buildModule(self, signal):
		print("Kalender wird angezeigt")
		for entry in self.dict["dates"]:
			label = QLabel(entry + ": " + self.dict["dates"][entry])
			self.layout.addWidget(label)
			print(entry)
		self.setLayout(self.layout)
		signal.calendar.emit(self)

	def storeData(self, params):
		data = {}
		data["method"] = "addCalendarEntry"
		data["name"] = params["name"]
		data["date"] = params["date"]

		self.dict["dates"][data["date"]] = data["name"]
		self.dumpJson()

		return data
		
class ShoppingList(Module):
	def __init__(self):
		super().__init__()

	def buildModule(self):
		print("Einkaufsliste wird angezeigt")
		for entry in self.dict["shoppingItems"]:
			print(entry)
			label = QLabel(entry)
			self.layout.addWidget(label)
		self.setLayout(self.layout)
		self.comm.shoppingList.emit()
	def storeData(self, params):
		data = {}
		data["method"] = "addShoppingListEntry"
		data["name"] = params["name"]

		dict["shoppingItems"].append(data["name"])
		self.dumpJson()


class ToDoList(Module):
	def __init__(self):
		super().__init__()

	def buildModule(self):
		print("ToDO wird angezeigt")
		for entry in self.dict["tasks"]:
			label = QLabel(entry + ": " + self.dict["tasks"][entry])
			self.layout.addWidget(label)
		self.setLayout(self.layout)
		self.comm.toDo.emit()

	def storeData(self, data):
		data = {}
		data["method"] = "addToDoItem"
		data["name"] = params["name"]
		data["person"] = params["person"]

		self.dict["tasks"][data["name"]] = data["person"]
		self.dumpJson()

class DiaShow(Module):
	def __init__(self):
		super().__init__()

	def buildModule(self):
		self.im = QPixmap("images/img.jpg")
		self.label = QLabel()
		self.label.setPixmap(self.im)

		self.grid = QGridLayout()
		self.grid.addWidget(self.label, 1, 1)
		self.setLayout(self.grid)
		