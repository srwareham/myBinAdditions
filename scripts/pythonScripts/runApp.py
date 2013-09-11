import os.path
import commands
import sys

'''
@author: Sean Wareham
Created on September 10, 2013
'''


# Full Path where ".app"s are located
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
# 		These values will never be called (presumably) but need  placeholders
	else:
		return "false"
		
#executes desired command with bash. Probably a better / safer way
def executeCommand(inputString):
	commands.getoutput(inputString)
	
# Create the Command using MacOSX "open" to open an application
def openCommand(inputStringFilePath):
	command = "open " + inputStringFilePath
	return command

#Turn application name back into 
def makeFullPath(applicationName):
	return dir + applicationName	

def run():
	apps = os.listdir(dir)
	args = [arg for arg in sys.argv]
	args = args[1:]
	
	dict ={}
	
	for app in apps:
		if (isApp(app)):
			dict[cleanName(app).lower()] = os.path.join(dir,app)
		else:
		#eliminate junk files
			if (containsDot(app)):
				continue
# 			folder =
			folderPath = os.path.join(dir,app)
			folderApps = os.listdir(folderPath)
			for nestedApp in folderApps:
				if isApp(nestedApp):
					dict[cleanName(nestedApp).lower()] = os.path.join( folderPath, nestedApp)
	for arg in args:
		arg = arg.strip(" ")
		cleanArg = arg[:]
		cleanArg = cleanArg.lower()
		if (cleanArg in dict):
			fullPath = dict[cleanArg]
			inQuotes = "\"" + fullPath + "\""
			open = openCommand(inQuotes)
			print "Running: " + open
			executeCommand(open)

			
if (__name__ == "__main__"):
	run()
