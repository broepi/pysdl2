
import re, os

thisdir = os.path.dirname (os.path.realpath (__file__))
thirddir = os.path.join (thisdir, "3rd")
builddir = os.path.join (thisdir, "build")

fs = open (builddir+"/SDL.xml", "r")
cont = fs.read ()
fs.close ()

cont = re.sub ("<Unimplemented[a-zA-Z0-9_ =\"]*/>", "", cont)

fs = open (builddir+"/newSDL.xml", "w")
fs.write (cont)
fs.close ()
