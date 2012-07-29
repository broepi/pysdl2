#!/usr/bin/python

import sys, os, glob, shutil

thisdir = os.path.dirname (os.path.realpath (__file__))
thirddir = os.path.join (thisdir, "3rd")
builddir = os.path.join (thisdir, "build")
finaldir = os.path.join (thisdir, "final")

os.chdir (thisdir)

for item in glob.glob ("*.pyc"):
	os.remove (item)

for item in glob.glob (builddir+"/*"):
	if os.path.isfile (item):
		os.remove (item)

if "--full" in sys.argv:
	shutil.rmtree (thirddir)
	shutil.rmtree (builddir)
	shutil.rmtree (finaldir)

