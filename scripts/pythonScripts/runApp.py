import os.path
import commands
import sys

'''
@author: Sean Wareham
Created on September 10, 2013
'''


# Full top level path where ".app"s are located
dir = "/Applications/"

def isApp(fileName):
	if (fileName[-4:] == ".app"):
		return True
	else:
		return False
		
def containsDot(inputString):
	for c in inputString:
		if c == ".":
			return True
	return False

# Removes  .app from a filename
def cleanName(inputString):
	if (isApp(inputString)):
		return inputString[:-4]
# 		These values will never be called (presumably) but need placeholders in case
	else:
		return "false"
		
#executes desired command with bash. There probably is a better / safer way
def executeCommand(inputString):
	commands.getoutput(inputString)
	
# Create the Command using MacOSX "open" to open an application
def makeOpenCommand(inputStringFilePath):
	command = "open " + inputStringFilePath
	return command

#Turn application name back into 
def makeFullPath(applicationName):
	return dir + applicationName	

def run():
	files = os.listdir(dir)
	args = [arg for arg in sys.argv]
# 	Remove first argument as it is the filepath of this python script
	args = args[1:]
	#dictionary of lowercase app_name mapped to full file path of the app
	dict ={}
	
	for file in files:
		if (isApp(file)):
			dict[cleanName(file).lower()] = os.path.join(dir,file)
		else:
		#eliminate junk files
			if (containsDot(file)):
				continue
			#If is a folder, examine its contents
			folderPath = os.path.join(dir,file)
			folderApps = os.listdir(folderPath)
			for nestedApp in folderApps:
				if isApp(nestedApp):
					dict[cleanName(nestedApp).lower()] = os.path.join( folderPath, nestedApp)
	for arg in args:
		arg = arg.strip(" ")
		# Do not remember best practice for .lower() so likely circuitous 
		cleanArg = arg[:]
		cleanArg = cleanArg.lower()
#       If this appname occurred in our top level directory or in any of its sub directories
		if (cleanArg in dict):
			fullPath = dict[cleanArg]
			inQuotes = "\"" + fullPath + "\""
			open = makeOpenCommand(inQuotes)
			print "Executing: " + open
			executeCommand(open)
		
if (__name__ == "__main__"):
	run()
