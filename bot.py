from inputOutput import Input, OAudio
import json
import commands
import base64


class Bot():
	def __init__(self):
		self.input = Input()
		self.output = OAudio()
		self.readyForCommand = False
		with open('./CDict.json', 'r') as f:
			self.cdict = json.load(f)
		# print(self.cdict)

	def run(self):
		while True:
			print("waiting...")
			self.waitForUser()
			cmd = self.getCommand()
			method, params = self.buildCommand(cmd)
			self.executeCommand(method, params)

	def waitForUser(self):
		while True:
			if self.input.listen() == 'befehl':
				print('Ready for Command...')
				return

	def getCommand(self):
		self.output.say("was kann ich für dich tun?")
		while True:
			userInput = self.input.listen()
			for entry in self.cdict:
				if self.cdict[entry]["key"] in userInput:
					return self.cdict[entry]
			
		self.buildCommand(userInput)

	def buildCommand(self, cmd):
		parameter = {}
		if cmd["params"] == "":
			return cmd["method"], ""
		else:
			for param in cmd["params"]:
				self.output.say(cmd["params"][param])
				parameter[param] = self.input.listen()
			return cmd["method"], parameter

	def executeCommand(self, method, params):
		method_to_call = getattr(commands, method)
		data = method_to_call(params)
		print(data)
		b64Json = base64.urlsafe_b64encode(json.dumps(data).encode()).decode()
		print (b64Json)
		
		


def startBot():
	bot = Bot()
	bot.run()

if __name__ == '__main__':
    startBot()