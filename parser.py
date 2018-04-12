# Parses each line of an assembly language text file, removes the white space and categorises lines into A or C Commands

filename = "tests/parserTest.asm"

class Parser():
	def __init__ (self, line):
		self.line = line

	def removeSpaces(self):
		self.line = self.line.replace(' ', '')

	def removeComments(self):
		splitLine = self.line.split("//", 1)
		self.line = splitLine[0]

	def removeNewlineChar(self):
		splitLine = self.line.split('\n', 1)
		self.line = splitLine[0]

	def isBlank(self):
		if self.line == '':
			return True
		else:
			return False

	def getCommand

class ACommand():
	def __init__ (self, line):
		self.line = line
		self.address = self.line[1:]


class CCommand():
	def __init__ (self,line):
		self.line = line
		if '=' in self.line:
			self.isJump = False
			self.jump = False
			splitLine = self.line.split('=')
			self.dest = splitLine[0]
			self.comp = splitLine[1]
		else:
			self.isJump = True
			self.dest = False
			splitLine = self.line.split(';')
			self.comp = splitLine[0]
			self.jump = splitLine[1]
			




file = open(filename, 'r')
lines = file.readlines()

parsedLines = []
for line in lines:
	lineParser = Parser(line)

	lineParser.removeSpaces()
	lineParser.removeComments()
	lineParser.removeNewlineChar()

	if not lineParser.isBlank():
		parsedLines.append(lineParser.line)

print(parsedLines)

commands = []
for line in parsedLines:
	getCommand
# test = "0;JMP"
# cCommand = CCommand(test)
# print(cCommand.line)
# print(cCommand.isJump)
# print(cCommand.dest)
# print(cCommand.comp)
# print(cCommand.jump)





# for parsedLine in parsedLines:
# 	print(parsedLine.line)

