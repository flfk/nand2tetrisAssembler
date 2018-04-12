# Parses each line of an assembly language text file, removes the white space and categorises lines into A or C Commands

# CLASSES
class LineParser():
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

# FUNCTIONS
def getCommands(filename):
	"""Returns list of strings representing asm commands from input file"""

	file = open(filename, 'r')
	lines = file.readlines()

	parsedFile = []
	for line in lines:
		lineParser = LineParser(line)

		lineParser.removeSpaces()
		lineParser.removeComments()
		lineParser.removeNewlineChar()

		if not lineParser.isBlank():
			parsedFile.append(lineParser.line)

	return parsedFile
