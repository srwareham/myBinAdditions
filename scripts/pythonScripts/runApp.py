import os.path
import commands
import sys

'''
@author: Sean Wareham
Created on September 10, 2013
'''


# Full Path where ".app"s are located
dir = "/Applications/"

# Removes  .app from a filename
def cleanName(inputString):
	if (inputString[-4:] == ".app"):
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
	
def main():
	apps = os.listdir(dir)	
	args = [arg for arg in sys.argv]
# 	Eliminates the first argument because that is the path to this .py file
	args = args[1:]
# 	List of appnames without .app filextensions and in all lowercase
	cleanApps = []
	
	for app in apps:
		cleanApps.append(cleanName(app).lower())
		
	for arg in args:
# 		Probably dont care if working on clone or original, but why not clone just in case
		cleanArg = arg[:]
		
# 		Dont care about case sensitivity, only want to check if user inputs 
#   	The name of the desired app to launch
		cleanArg = cleanArg.lower()
		
# 		Check if this argument passed into runApp.py exists (case insensitive) in the
# 		List of .apps in dir
		if (cleanArg in cleanApps):
# 			fullpath found by examining original filenames found from os call
			fullPath = makeFullPath(apps[cleanApps.index(cleanArg)])
# 			Need the command in all quotes to account for spaces in app names
			inQuotes = "\"" + fullPath + "\""
# 			Generate desired command syntax
			open = openCommand(inQuotes)
			print "Running: " + open
			executeCommand(open)
# 	for app in cleanApps:
# 		print app
			
if __name__ == "__main__":
	main()
	
