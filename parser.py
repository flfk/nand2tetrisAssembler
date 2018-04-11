# Parses assembly language text file line by line, removes white space and categorises line

filename = "tests/noComments.asm"

def removeSpaces(lines):
	"""removes spaces from array of strings"""
	linesNoSpaces = []
	for line in lines:
		cleanedLine = line.replace(" ","")
		linesNoSpaces.append(cleanedLine)
	return linesNoSpaces

def removeEmptyLines(lines):
	linesNoEmpties = []
	for line in lines:
		if not ("\n"):
			linesNoEmpties.append(line)


file = open(filename, 'r')
lines = file.readlines()
countLines = len(lines)

linesNoSpaces = removeSpaces(lines)
linesNoEmpties = removeEmptyLines(linesNoSpaces)

print(linesNoEmpties)