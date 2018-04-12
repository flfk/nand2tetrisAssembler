# translates ASM code to Machine Code

import parser
import CInstructionTables

# Classes

class Translator():
	def __init__ (self, commands):
		self.commands = commands

	def getCommandCategories(self):
		commandsCategorised = []
		for command in self.commands:
			if '@' in command:
				commandsCategorised.append(ACommand(command))
			else:
				commandsCategorised.append(CCommand(command))
		return commandsCategorised

	def getTranslatations(self):
		commandsCategorised = self.getCommandCategories()
		commandsTranslated = []
		for command in commandsCategorised:
			commandsTranslated.append(command.translate())
		return commandsTranslated

class ACommand():
	def __init__ (self, line):
		self.line = line
		self.type = "A"
		self.address = self.line[1:]

	def translate(self):
		addressBinary = get15BitBinary(self.address)
		translation = '0' + addressBinary
		return translation

class CCommand():
	def __init__ (self,line):
		self.line = line
		self.type = "C"
		if '=' in self.line:
			self.jump = 'null'
			splitLine = self.line.split('=')
			self.dest = splitLine[0]
			self.comp = splitLine[1]
		else:
			self.dest = 'null'
			splitLine = self.line.split(';')
			self.comp = splitLine[0]
			self.jump = splitLine[1]

	def translate(self):
		destDict = CInstructionTables.dest
		compDict = CInstructionTables.comp
		jumpDict = CInstructionTables.jump
		
		dest = destDict[self.dest]
		comp = compDict[self.comp]
		jump = jumpDict[self.jump]

		# print((self.dest, self.comp, self.jump) + (dest, comp, jump))

		translation = '111' + dest + comp + jump
		return translation

def get15BitBinary(decimal):
	bitsRequired = 15
	rawBinary = bin(int(decimal))[2:]
	padding= ''
	for i in range(bitsRequired - len(rawBinary)):
		padding = '0' + padding
	return padding + rawBinary

filename = "tests/parserTest.asm"
commands = parser.getCommands(filename)
translator = Translator(commands)
commandsTranslated = translator.getTranslatations()

for command in commandsTranslated:
	print(command)

# binary = getBinary('4')
# paddedBinary = get15BitBinary(binary)
# print(paddedBinary)
