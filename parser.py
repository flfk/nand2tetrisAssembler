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

class ACommand():
	def __init__ (self, line):
		self.line = line
		self.address = self.line[1:]


# class CCommand():


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

test = "@100"
aCommand = ACommand(test)
print(aCommand.line)
print(aCommand.address)


print(parsedLines)


# for parsedLine in parsedLines:
# 	print(parsedLine.line)

