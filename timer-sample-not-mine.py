#!/usr/bin/env python
 
'''
A timeclock.
https://github.com/enure/timer/blob/master/timer.py
'''
 
import os, string, time, re, datetime
 
# file system vars
home = os.path.expanduser("~")
khronosHome = os.path.join(home, ".khronos/")
khronosHomeArchive = os.path.join(khronosHome, "archive/")
khronosHomeTrash = os.path.join(khronosHome, "trash/")
 
# Places a title at the top of each screen
def title():
    os.system("clear")
    print "Khronos 3000\n"
 
# Lists all projects
def printProjects(): # FIXME this should say if there are no projects.
    print "> Choose a Project or Enter A New Project"
    projects = [f for f in os.listdir(khronosHome) if os.path.isfile(os.path.join(khronosHome, f))] # http://www.faqs.org/docs/diveintopython/apihelper_filter.html
    for project in projects:
        print " ", project
 
# Users selects or creates a new project
def setProject():
    # Wait for it
    action = raw_input("? ")
    action = string.strip(action)
    if action == "q":
        quit()
    if action == "":
        goHome()
    else:
        title()
        myProjectName = action.replace(" ", "_")
        workOnProject(projectName=myProjectName)
 
def workOnProject(projectName="default"):
    title()
    print "> " + projectName
    print " "
    print "[s]tart, [v]iew    [a]rchive [d]elete"
    print " "
    action = raw_input("? ")
    action = string.strip(action)
    if action == "s": # start
        timer(0, projectName)
    if action == "v": # view
        viewProjectSessions(projectName)
    if action == "a": # archive
        archiveProject(projectName)
    if action == "d": # delete
        deleteProject(projectName)
    if action == "q": # quit
        quit()
    else:
        workOnProject(projectName)
 
def viewProjectSessions(projectName):
    title()
    # list sessions for a particular project
    file = os.path.join(khronosHome, projectName)
    if os.path.isfile(file):
        f=open(file, "r")
        print "> Project:", projectName, "\n"
        for line in f:
            if line:
                line = re.search("^(\\d+)(.+)$", line)
                print secondsToHMS(int(line.group(1))), line.group(2)
    print " "
    print "[b]ack  [q]uit"
    print " "
    action = raw_input("? ")
    if action == "b":
        workOnProject(projectName)
    if action == "q":
        quit()
    else:
        viewProjectSessions(projectName)
 
def archiveProject(projectName):
    os.system("mv " + khronosHome + projectName + " " + khronosHome + "archive/")
    title()
    print "Project", projectName, "archived"
    time.sleep(2)
    goHome()
 
def deleteProject(projectName):
    os.system("mv " + khronosHome + projectName + " " + khronosHome + "trash/")
    title()
    print "Project", projectName, "trashed"
    time.sleep(2)
    goHome()
 
# The timer, which can be started, stopped, and 
# when prompted will give the elapsed time
def timer(timeElapsed=0, projectName="default"):
    title()
    file = khronosHome + projectName
    timeStart = time.time()
    print "Timer running...\n"
    print "[s]top  [e]lapsed\n"
    action = raw_input("? ")
    action = string.strip(action)
 
    # stop
    if action == "s": 
        timeStop = time.time()
        timeTotal = (int(timeStop - timeStart) + timeElapsed)
        title()
        print "Saving Session...\n"
        print "Time:", secondsToHMS(timeTotal)
        print "\n"
        print "What did you do?"
        sessionNote = raw_input("? ")
        today = datetime.datetime.now().strftime("%d/%m/%Y")
        f = open(file, "a")
        session = ("%d" % timeTotal) + "\t" + string.strip(sessionNote) + "\t" + today + "\n"
        f.write(session)
        f.close()
        goHome()
    # elapsed
    if action == "e":
        timeStop = time.time()
        timeElapsed = (timeStop - timeStart) + timeElapsed
        title()
        print secondsToHMS(timeElapsed) + " have elapsed..."
        time.sleep(2)
        timer(timeElapsed, projectName)
    if action == "q":
        quit()
    # invalid input
    else:
        title()
        print "Timer running...\n"
        timeStop = time.time()
        timeElapsed = (timeStop - timeStart) + timeElapsed
        timer(timeElapsed)
 
def makeKhronosHomeDir():
    if os.path.isdir(khronosHome):
        pass
    elif os.path.isfile(khronosHome):
        print "A file with the name", khronosHome, "exists. You'll need to fix this."
    else:
        os.system("mkdir " + khronosHome)
        os.system("mkdir " + khronosHome + "/trash")
        os.system("mkdir " + khronosHome + "/archive")
 
def secondsToHMS(seconds):
    # convert seconds into hours, minutes and seconds
    mins, secs = divmod(seconds,60)
    hours, mins = divmod(mins, 60)
    if int(mins) == 0:
        HMS = "%s%s" % (int(secs), "s")
    if int(hours) == 0:
        HMS = "%s%s %s%s" % (int(mins), "m", int(secs), "s")
    else:
        HMS = "%s%s %s%s %s%s" % (int(hours), "h", int(mins), "m", int(secs), "s")
    return HMS # without return, this function can sometimes return "None"
 
def quit():
    title()
    print "Bye\n"
    exit()
 
def goHome():
    title() # set the title
    makeKhronosHomeDir() # make ~/.khronos if not already present
    printProjects() # show projects
    setProject() # let the user choose/create a project
 
goHome()