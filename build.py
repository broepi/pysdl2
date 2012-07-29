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
builddir = os.path.join (thisdir, "build")

os.chdir (thisdir)

if not os.path.isdir (builddir):
	os.mkdir (builddir)

print "\nSDL repo is copied into a seperate build dir SDL_build"
if yesno ():
	shutil.copytree ("3rd/SDL", "build/SDL", ignore=shutil.ignore_patterns(".hg*"))

print "\nThe SDL lib will now be build."
if yesno ():
	os.chdir ("build/SDL")
	print "./autogen.sh"
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
	os.chdir ("..")
	print "SDL build successful!"
	os.chdir (thisdir)

print "\ncopy libSDL2.so to build dir"
shutil.copy (builddir+"/SDL/build/.libs/libSDL2.so", builddir+"/libSDL2.so")

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
res = call ("python "+thirddir+"/ctypeslib/xml2py.py "+builddir+"/newSDL.xml -o "+builddir+"/SDL_ctypes.py -l "+builddir+"/libSDL2.so -r \"SDL.*\"", shell=True)

print "\nsome transformations ..."

fs = open (builddir+"/SDL_ctypes.py", "r")
content = fs.read ()
fs.close ()

content = content.replace ("_libraries['"+builddir+"/libSDL2.so']", "lib")
content = re.sub (r"__all__ = \[[^\]]*\]", "", content, 1)
content = content.replace ("CDLL('"+builddir+"/libSDL2.so')", "CDLL(os.path.dirname(os.path.realpath(__file__))+\"/libSDL2.so\")")
content = "import os\n\n" + content
print "'"+builddir+"/libSDL2.so'"

fs = open (builddir+"/SDL_ctypes.py", "w")
fs.write (content)
fs.close ()

print "\nput all into final dir"
if not os.path.isdir ("final"):
	os.mkdir ("final")
shutil.copy (builddir+"/libSDL2.so", thisdir+"/final/libSDL2.so")
shutil.copy (builddir+"/SDL_ctypes.py", thisdir+"/final/SDL2.py")

