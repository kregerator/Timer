# 2012.12.28
# Simple script to act as a timer in the terminal
# It has been quite a while since I've done any programming
# object oriented or otherwise, so there may be better ways to
# do these things. For now, I'm using it at a learning exercise.

import datetime

class Timer:
# The Timer class holds the three vairables needed for the timer 
# (start.time, stop.time, and elapsed_time) as well as the functions
# (display_help, start_timer, stop_timer, refresh_timer, quit_timer,
# and display_current_elapsed) that are needed to run a timer.

	def __init__(self):
		self.refresh_timer()

	# display the menu of commands
	def display_help(self):
		print "s: start"
		print "p: stop"
		print "d: display current elapsed time"
		print "r: refresh"
		print "q: quit"
		print "?: show help"

	# starts the clock running and print the sart time to the screen
	def start_timer(self):
		self.start_time = datetime.datetime.now()
		print "start time = %s" % str(self.start_time)

	# stop the timer and print the elapsed time to the screen
	def stop_timer(self):
		self.stop_time = datetime.datetime.now()
		print "stop time = %s" % str(self.stop_time)
		self.elapsed_time = self.stop_time - self.start_time
		print "ran for %s" % str(self.elapsed_time)

	# refresh the timer variables to start over
	# also used to initialized when the object is created
	def refresh_timer(self):
		self.start_time = 0
		self.stop_time = 0
		self.elapsed_time = 0

	def display_current_elapsed(self):
		#don't update elapsed_time but just display current value in
		#elapsed_time + (stop_time - start_time)
		print "Current elapsed time is : %s" % str(datetime.datetime.now() - 
			self.start_time)
		# This will have to bet updated when 'p' command is turned more into
		# a pause feature instead of just stop

# main program driving by a simple while loop
# var is used to keep running through the loop, to quit it is set to 0
var = 1
my_timer = Timer()
print "type '?' for help"
while var == 1:
	com = raw_input("Command: ")
	if com == 's':
		my_timer.start_timer()
	elif com == 'p':
		my_timer.stop_timer()
	elif com == 'r':
		my_timer.refresh_timer()
	elif com == 'q':
		print "Quitting . . . "
		var = 0
	elif com == 'd':
		my_timer.display_current_elapsed()
	elif com == '?':
		my_timer.display_help()
	else:
		print "I'm not sure I can do that, Dave."
 