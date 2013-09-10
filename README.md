myBinAdditons
=============

A collection of my additions to the Mac OS X Terminal
NOTE: All of these programs are stored in a custom ~/bin directory.  This directory
has been added to the PATH in my .bash_profile (you may need to add it to .bash_rc if you
are not running OS X).  Too add a directory to the PATH, edit the file ~/.bash_rc
to include the line: "PATH=${PATH}:/Users/srwareham/bin"


Programs from others:
	trash: Command line move to trash. Is a useful replacement for "rm" when you might 
		later discover you needed that file.
		
	eject: Eject a mounted volume by name or ID from command line.
	
	webs: Print out a read-friendly list of what apps are connected to the internet.
		"COMMANDS" is just a header and is to be ignored.
	
	
My Programs:
	run:  uses bash / python logic to open an application in /Applications/
		called as: run "google chrome" ; run "Google ChRoMe" ; run firefox 
		Is case insensitive by design. Multi-word apps require quotes.
		
	des: quickly cd to the desktop.  Must be invoked with ". des" (quotes not necessary)
		could just have added an alias to .bash_profile but I didn't want to clutter it.


Aliases in ~/.bash_rc:
	PATH=${PATH}:/Users/<your_username>/bin
		adds my custom bin to the PATH
	
	alias ls="ls -G"
		overloads ls to default to "ls -G" which outputs result in color.
