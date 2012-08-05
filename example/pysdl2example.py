"""
A first rudimentary sample using the pysdl2 binding
"""

import sys, os
sys.path.append (os.path.dirname (os.path.realpath (__file__))+"/../final")

from SDL2 import *

res = SDL_Init (SDL_INIT_VIDEO)
if res != 0:
	raise Exception ("SDL Init failed: "+str(SDL_GetError()) )

win = SDL_CreateWindow ("Hello World", 0, 0, 800, 600, SDL_WINDOW_SHOWN)
renderer = SDL_CreateRenderer (win, -1, 0)

SDL_SetRenderDrawColor (renderer, 0, 0, 255, 255)
SDL_RenderClear (renderer)
SDL_RenderPresent (renderer)
SDL_Delay (5000)

SDL_Quit ()
