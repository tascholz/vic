import json

#showCalendar
def showCalendar(params):
	data = {}
	data["method"] = "showCalendar"
	return data

#addCalendarEntry
#
#@name
#@date
def addCalendarEntry(params):
	data = {}
	data["method"] = "addCalendarEntry"
	data["name"] = params["name"]
	data["date"] = params["date"]

	with open('modules/data.json', 'r') as f:
		dict = json.load(f)["dates"]
	
	dict["dates"][data["date"]] = data["name"]
	
	with open('modules/data.json', 'w') as f:
		json.dump(dict, f)
	#TODO conversion data["date"] to date
	return data

#showToDoList
def showToDoList(params):
	data = {}
	data["method"] = "showToDoList"
	return data

#addToDoItem
#
#@name
#@person
def addToDoItem(params):
	data = {}
	data["method"] = "addToDoItem"
	data["name"] = params["name"]
	data["person"] = params["person"]

	with open('/modules/data.json', 'r') as f:
		dict = json.load(f)
	todoItems["toDoItems"][data["name"]] = data["person"]

	with open('/modules/data.json', 'w') as f:
		json.dump(dict, f)

	return data

#showShoppingList
def showShoppingList(params):
	data = {}
	data["method"] = "showShoppingList"
	return data

#addShoppingListEntry
#
#@name
def addShoppingListEntry(params):
	data = {}
	data["method"] = "addShoppingListEntry" 
	data["name"] = params["name"]

	with open('modules/data.json', 'r') as f:
		dict = json.load(f)
	dict["shoppingItems"].append(data["name"])
	with open('modules/data.json', 'w') as f:
		json.dump(dict, f)	

	return data

def exit(params):
	data = {}
	data["method"] = "exit"
	return data