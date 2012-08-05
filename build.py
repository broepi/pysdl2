#!/usr/bin/python

from subprocess import call, PIPE
import shutil, os, re

def yesno (msg = "Do that (or skip?) [Y/n]: "):

	while True:
		res = raw_input (msg)
		if res == "":
			res = "y"
		res = res.lower ()
		if res in "yn":
			break
	return res == "y"

thisdir = os.path.dirname (os.path.realpath (__file__))
thirddir = os.path.join (thisdir, "3rd")
builddir = os.path.join (thisdir, "build")

os.chdir (thisdir)

if not os.path.isdir (builddir):
	os.mkdir (builddir)

print "\nSDL repo is copied into a seperate build dir SDL_build"
if yesno ():
	shutil.copytree ("3rd/SDL", "build/SDL", ignore=shutil.ignore_patterns(".hg*"))

print "\nA Linux shared object will be build, you can also cross-build a Windows DLL."
if yesno ("Yes = Linux , No = Windows [Y/n]: "):
	platf = "linux"
	libfilename = "libSDL2.so"
else:
	platf = "win"
	libfilename = "SDL2.dll"

print "\nThe SDL lib will now be build."
if yesno ():
	os.chdir ("build/SDL")
	print "./autogen.sh"
	if platf == "linux":
		res = call ("./autogen.sh", shell=True)
		if res != 0:
			raise Exception ("./autogen.sh failed!")
		print "./configure"
		res = call ("./configure", shell=True)
		if res != 0:
			raise Exception ("./configure failed!")
		print "make"
		res = call ("make", shell=True)
		if res != 0:
			raise Exception ("make failed!")
	elif platf == "win":
		print "./cross-configure.sh"
		res = call ("./cross-configure.sh", shell=True)
		if res != 0:
			raise Exception ("./configure failed!")
		print "./cross-make.sh"
		res = call ("./cross-make.sh", shell=True)
		if res != 0:
			raise Exception ("make failed!")
	os.chdir ("..")
	print "SDL build successful!"
	os.chdir (thisdir)

print "\ncopy "+libfilename+" to build dir"
shutil.copy (builddir+"/SDL/build/.libs/"+libfilename, builddir+"/"+libfilename)

print "\nheader => XML"
res = call ("python "+thirddir+"/ctypeslib/h2xml.py "+builddir+"/SDL/include/SDL.h -o "+builddir+"/SDL.xml -c", shell=True)
if res != 0:
	raise Exception ("Something went wrong with h2xml")

print "\nstrip <Unimplemented ...>"
res = call ("python stripunimpl.py", shell=True)
if res != 0:
	raise Exception ("Something went wrong while stripping Unimplemented tags.")

print "\nXML => python-module"
# -l specifies the library (shared object) and -r is a regular expression for which symbols to include
if platf == "linux":
	res = call ("python "+thirddir+"/ctypeslib/xml2py.py "+builddir+"/newSDL.xml -o "+builddir+"/SDL_ctypes.py -l "+builddir+"/"+libfilename+" -r \"SDL.*\"", shell=True)
elif platf == "win":
	res = call ("wine python "+thirddir+"/ctypeslib/xml2py.py "+builddir+"/newSDL.xml -o "+builddir+"/SDL_ctypes.py -l "+builddir+"/"+libfilename+" -r \"SDL.*\"", shell=True)
if res != 0:
	raise Exception ("Something went wrong while compiling XML to python-binding.")

print "\nsome transformations ..."

fs = open (builddir+"/SDL_ctypes.py", "r")
content = fs.read ()
fs.close ()

content = content.replace ("_libraries['"+builddir+"/"+libfilename+"']", "lib")
content = re.sub (r"__all__ = \[[^\]]*\]", "", content, 1)
content = content.replace ("CDLL('"+builddir+"/"+libfilename+"')", "CDLL(os.path.dirname(os.path.realpath(__file__))+\"/"+libfilename+"\")")
content = "import os\n\n" + content
print "'"+builddir+"/"+libfilename+"'"

fs = open (builddir+"/SDL_ctypes.py", "w")
fs.write (content)
fs.close ()

print "\nput all into final dir"
if not os.path.isdir ("final"):
	os.mkdir ("final")
shutil.copy (builddir+"/"+libfilename, thisdir+"/final/"+libfilename)
shutil.copy (builddir+"/SDL_ctypes.py", thisdir+"/final/SDL2.py")

