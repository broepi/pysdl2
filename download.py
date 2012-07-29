#!/usr/bin/python

from subprocess import call, PIPE
import shutil, os, re

def yesno ():

	while True:
		res = raw_input ("Do that (or skip?) [Y/n]: ")
		if res == "":
			res = "y"
		res = res.lower ()
		if res in "yn":
			break
	return res == "y"

thisdir = os.path.dirname (os.path.realpath (__file__))
thirddir = os.path.join (thisdir, "3rd")

os.chdir (thisdir)

if not os.path.isdir (thirddir):
	os.mkdir (thirddir)

os.chdir (thirddir)

res = call ("svn --version", shell=True, stdout=PIPE)
if res == 127:
	raise Exception ("Please install subversion!")

res = call ("hg --version", shell=True, stdout=PIPE)
if res == 127:
	raise Exception ("Please install mercurial!")

print "\nThe ctypeslib will now be downloaded into 3rd."
if yesno ():
	res = call ("svn checkout http://svn.python.org/projects/ctypes/trunk/ctypeslib/", shell=True)
	if res != 0:
		raise Exception ("Something went wrong with the checkout.")
	print "\nDo some patching ..."
	fs = open (thirddir+"/ctypeslib/ctypeslib/codegen/gccxmlparser.py", "r")
	c = fs.read ()
	fs.close ()
	a = c.split ("\n")
	a [69-1] = r"""
        try:
            mth = getattr(self, name)
        except AttributeError:
            print "Warning: GCCXML_Parser object has no attribute",name
            return"""
	c = "\n".join (a)
	fs = open (thirddir+"/ctypeslib/ctypeslib/codegen/gccxmlparser.py", "w")
	fs.write (c)
	fs.close ()

print "\nNow copying the scripts from ctypeslib/ctypeslib/ to ctypeslib/ ..."
shutil.copy2 ("ctypeslib/ctypeslib/h2xml.py", "ctypeslib/h2xml.py")
shutil.copy2 ("ctypeslib/ctypeslib/xml2py.py", "ctypeslib/xml2py.py")


print "\nThe SDL library repository will now be checked out into 3rd."
if yesno ():
	res = call ("hg clone http://hg.libsdl.org/SDL", shell=True)
	if res != 0:
		raise Exception ("Something went wrong with the checkout.")

