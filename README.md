pysdl2
======

A python ctypes binding generator for the Simple Direct Media 2.0 library

This script aims to be a fully automated generator to create a working ctypes-binding for SDL 2
while SDL 2 is still in development. Before the generation, the SDL development-repository is
downloaded so it's as up-to-date as it can be.

requirements
------------

* Building operating system: Unix
* Running operating system: Unix, Windows
* Python 2.x

for downloading of ctypeslib and sdl
* Mercurial
* Subversion

howto
-----

the whole generation process is done by `make.py`. It simply calls `download.py` and `build.py`

`download.py` downloads ctypeslib and SDL from their dev-repositories

`build.py` builds SDL and the binding

`clean.py` will clean the top directory from .pyc files and the "build" directory from auto
generated files. Pass `--full` to clean really all (also downloaded dependencies and the "final"
directory)

