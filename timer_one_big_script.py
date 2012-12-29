# Simple script to act as a timer in the terminal

import datetime

# build functions here
def display_help():
	print "s: start"
	print "p: stop"
	print "r: refresh"
	print "q: quit"
	print "?: show help"


# main program
var = 1
while var == 1:
	com = raw_input("Command: ")
	if com == 's':
		start_time = datetime.datetime.now()
		print "start time = %s" % str(start_time)
	elif com == 'p':
		stop_time = datetime.datetime.now()
		print "stop time = %s" % str(stop_time)
		elapsed_time = stop_time - start_time
		print "ran for %s" % str(elapsed_time)
	elif com == 'r':
		start_time = 0
		stop_time = 0
		elapsed_time = 0
	elif com == 'q':
		print "quitting timer"
		var = 2
	elif com == '?':
		display_help()
	else:
		print "I'm not sure I can do that, Dave."
 