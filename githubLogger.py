import sys
import os
import subprocess


tracker_File_Path = "./tracker.txt"

with open(tracker_File_Path, 'a') as the_tracker_file:
    the_tracker_file.write('New line test')
    the_tracker_file.write("\n")

subprocess.call(["git", "add", "."])
subprocess.call(["git", "commit", "-m", "Test commit made with python"])
# subprocess.call(["git", "push origin master"])