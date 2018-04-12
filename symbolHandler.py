# converts asm symbols into primary asm commands

import predefinedSymbolTable

# CLASSES
class SymbolHandler():
	def __init__ (self, commands):
		self.commands = commands
		self.symbolTable = predefinedSymbolTable.symbolTable

	def isLabel(self, command):
		if '(' in command:
			return True
		else:
			return False

	def storeLabels(self):
		labelCount = 0
		for (index, command) in enumerate(self.commands):
			if self.isLabel(command):
				labelStart = command.find("(") + 1
				labelEnd = command.find(")")
				label = command[labelStart:labelEnd]
				self.symbolTable[label] = (index - labelCount)
				labelCount += 1

	def isSymbol(self, command):
		if (command[0] == '@'):
			try:
				int(command[1:])
				return False
			except:
				return True
		else:
			return False

	def storeVariables(self):
		RAMLocation = 16
		for command in self.commands:
			if self.isSymbol(command):
				symbol = command[1:]
				try:
					self.symbolTable[symbol]
				except:
					self.symbolTable[symbol] = RAMLocation
					RAMLocation += 1

	def getConvertedCommands(self):		
		self.storeLabels()
		self.storeVariables()

		convertedCommands = []
		for command in self.commands:
			if self.isSymbol(command):
				symbol = command[1:]
				convertedCommands.append('@' + str(self.symbolTable[symbol]))
			elif self.isLabel(command):
				pass
			else:
				convertedCommands.append(command)
		return convertedCommands

