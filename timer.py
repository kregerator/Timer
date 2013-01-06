#! /usr/bin/env python

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

# There is a status var that saves the current status of the time
# 0 = initialized and waiting
# 1 = running
# 2 = paused

	def __init__(self):
		self.refresh_timer()

	# display the menu of commands
	def display_help(self):
		print "s: start"
		print "p: pause"
		print "e: end timer"
		print "d: display current elapsed time"
		print "r: refresh"
		print "q: quit"
		print "?: show help"

	# starts the clock running and print the sart time to the screen
	def start_timer(self):
		if self.status == 1: #already running
			print "Timer is already running."
		else:
			self.status = 1 # set status to running
			self.start_time = datetime.datetime.now()
			print "start time = %s" % str(self.start_time)
			

	# stop the timer and print the elapsed time to the screen
	def stop_timer(self):
		self.stop_time = datetime.datetime.now()
		print "Stop time = %s" % str(self.stop_time)
		# need to check if some time is already on elapsed time
		# if already has elapsed time on the timer, make sure to
		# add that in
		if self.status == 1: # timer is running currently
			if self.elapsed_time == 0:	
				self.elapsed_time = self.stop_time - self.start_time
			else:
				self.elapsed_time += (self.stop_time - self.start_time)
		# if timer wasn't running, elapsed time is already stored.
		print "Ran for %s" % str(self.elapsed_time)
		self.refresh_timer()

	# pause the timer and add the current elapsed time to the 
	# elapsed_time variable
	def pause_timer(self):
		if self.status == 2:
			print "Timer is already paused."
		else:
			self.status = 2 # set status to paused
			tmp = datetime.datetime.now()
			if self.elapsed_time == 0:	
				self.elapsed_time = tmp - self.start_time
			else:
				self.elapsed_time += (tmp - self.start_time)
			print "Timer is paused. %s saved to elapsed time.\n" % str(tmp - self.start_time)
			print "Total elapsed time is now: %s" % str(self.elapsed_time)
			print "To start timer again type 's'."
			

	# refresh the timer variables to start over
	# also used to initialized when the object is created
	def refresh_timer(self):
		self.start_time = 0
		self.stop_time = 0
		self.elapsed_time = 0
		self.status = 0
		print "Timer is initialized."

	def display_current_elapsed(self):
		#don't update elapsed_time but just display current value in
		#elapsed_time + (stop_time - start_time)
		
		if self.start_time == 0:
			print "Timer is not started."
		elif self.status == 1: #currently running
			print "Current elapsed time is : %s" % str(datetime.datetime.now() - 
				self.start_time)
			if self.elapsed_time != 0:
				print "Stored Elapsed time is : %s" % str(self.elapsed_time)
		elif self.status == 2: 
			print "Not running. Current elapsed time is %s" % str(self.elapsed_time)
		else:
			print "Something happened in display such that none of the criteria was met."
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
	elif com == 'e':
		my_timer.stop_timer()
	elif com == 'p':
		my_timer.pause_timer()
	elif com == 'r':
		my_timer.refresh_timer()
	elif com == 'q':
		# if currently running, call stop_timer
		if my_timer.status == 1:
			my_timer.stop_timer()
		print "Quitting . . . "
		var = 0
	elif com == 'd':
		my_timer.display_current_elapsed()
	elif com == '?':
		my_timer.display_help()
	else:
		print "I'm not sure I can do that, Dave."
 