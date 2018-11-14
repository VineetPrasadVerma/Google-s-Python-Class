 #!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them
def specialFilePath(dirname):
  specialFilePathNamesList = []

  filenames = os.listdir(dirname)
  for filename in filenames:
    match = re.search(r'__(\w+)__', filename)
    if match:
      path = os.path.join(dirname, filename)
      specialFilePathNamesList.append(os.path.abspath(path))

  return specialFilePathNamesList

def copy_to(specialFilePaths , todir):
  if not os.path.exists(todir):
    os.mkdir(todir)

  for path in specialFilePaths:
    fname = os.path.basename(path)
    shutil.copy(path, os.path.join(to_dir, fname))

def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  specialFilePaths = []
  for directory in args:
    specialFilePaths.extend( specialFilePath(directory))
  if todir:
    copy_to(specialFilePaths, todir)
  else:
    print '\n'.join(specialFilePaths)
  
if __name__ == "__main__":
  main()
