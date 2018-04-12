# converts .asm file to .hack output file
# Usage: assembler.py <file.asm>

import symbolHandler
import sys
import parser
import translator

# FUNCTIONS
def main():

	# Ensure single command line argument provided
	if (len(sys.argv) != 2):
		print("Usage: assembler.py <file.asm>")
		exit(1)

	# Retrieve input file details
	inputFile = sys.argv[1]
	inputFileName = inputFile.split('.')[0]
	inputExtension = inputFile.split('.')[1]

	# Ensure .asm file provided
	if not (inputExtension == 'asm'):
		print("Usage: assembler.py <file.asm>")
		exit(1)

	# Open output file
	outputExtension = ".hack"
	outputFile = inputFileName + outputExtension
	output = open(outputFile, 'w')

	# Parse input file
	commands = parser.getCommands(inputFile)

	# Convert symbols
	symbolConverter = symbolHandler.SymbolHandler(commands)
	convertedCommands = symbolConverter.getConvertedCommands()

	# Translate commands
	codeTranslator = translator.Translator(convertedCommands)
	commandsTranslated = codeTranslator.getTranslatations()

	# Write to ourput file
	for command in commandsTranslated:
		output.write(command + '\n')

	output.close()

# MAIN
if __name__ == "__main__":
	main()