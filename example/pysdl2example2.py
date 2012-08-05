"""
A first rudimentary sample using the pysdl2 binding
"""

import sys, os
sys.path.append (os.path.dirname (os.path.realpath (__file__))+"/../final")

from SDL2 import *

if SDL_Init (SDL_INIT_AUDIO|SDL_INIT_VIDEO) < 0:
	raise Exception ("SDL konnte nicht initialisiert werden:"+SDL_GetError())

mainwnd = SDL_CreateWindow ("Hello World!-Window", 100, 100, 640, 480, 0)
event = SDL_Event ()

running = True
while running:
	SDL_WaitEvent (pointer(event))
	
	if event.type == SDL_QUIT:
		running = False
	elif event.type == SDL_MOUSEMOTION:
		print "mouse was moved to (",event.motion.x,";",event.motion.y,")"

SDL_Quit ()
