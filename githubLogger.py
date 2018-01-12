import sys, os, subprocess, datetime

print('LOGGER')

tracker_File_Path = "./tracker.txt"
changes = sys.argv[1]
contribution_date = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

with open(tracker_File_Path, 'a') as the_tracker_file:
    the_tracker_file.write("\n")
    the_tracker_file.write(contribution_date)
    the_tracker_file.write("\n")
    the_tracker_file.write('Created a private contribution on a bitbucket repository.')
    the_tracker_file.write("\n")
    the_tracker_file.write( changes )
    the_tracker_file.write("\n")

subprocess.call(["git", "add", "."])
subprocess.call(["git", "commit", "-m", "Made a private contribution, check tracker.txt for details"])
subprocess.call(["git", "push", "origin", "master"])
