#showCalendar
def showCalendar(params):
	data = {}
	data["method"] = "showCalendar"

#addCalendarEntry
#
#@name
#@date
def addCalendarEntry(params):
	data = {}
	data["method"] = "addCalendarEntry"
	data["name"] = params["name"]
	data["date"] = params["date"]
	print("Adding the following entry:")
	print(params["name"])
	print(params["date"])
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
	return data

def exit(params):
	data = {}
	data["method"] = "exit"
	return data