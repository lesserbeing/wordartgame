#!/usr/bin/python2.7

###Things seem to get rendered into the loop at call time.  Watch
### The stacking that may occur. 


import pygame #imports the primary module
from pygame.locals import * #imports the entire locals library from pygame locals

def main():
	#1 Initialize Screen
	
	pygame.init() #Initializes the pygame
	screen = pygame.display.set_mode((150,150)) # Sets te display parameters
	pygame.display.set_caption("Basic Pygame Program") #Sets the caption for the header
	
	#2 Fill Background
	background = pygame.Surface(screen.get_size()) # sets up screen size
	background = background.convert() # not sure 
	background.fill((250,250,250)) # Sets the color of the background fill 
	
	#3 Display some text
	font = pygame.font.Font(None, 36) # sets the font style and name
	text = font.render("Hello World", 1, (50,10,250)) # Sets text body, position, and color
	textpos = text.get_rect() # instantiates the rectangle which encloses the text (Kind of like HTML?)
	textpos.centerx = background.get_rect().centerx #sets the text to the center
	background.blit(text,textpos) # refreshes the rendering surface
	
	#4 Blit everything to the screen
	screen.blit(background, (0,0)) #refreshes and draws the background
	pygame.display.flip() # Updates the contents of the entire display
	
	#5 Event Loop
	while 1: #main loop
			for event in pygame.event.get(): # extracts EVENTS from a growing and shrinking event array
				if event.type == QUIT: # event check 
					return # ends loop if the event is the QUIT
					
				screen.blit(background, (0,0)) #refreshes the screen and draws the background
				pygame.display.flip() # rerenders the entire thing.  
				
if __name__ == "__main__":
	main() # sets the loop. 

"""
ACTIVEEVENT
ANYFORMAT
ASYNCBLIT
AUDIO_S16
AUDIO_S16LSB
AUDIO_S16MSB
AUDIO_S16SYS
AUDIO_S8
AUDIO_U16
AUDIO_U16LSB
AUDIO_U16MSB
AUDIO_U16SYS
AUDIO_U8
BIG_ENDIAN
BLEND_ADD
BLEND_MAX
BLEND_MIN
BLEND_MULT
BLEND_RGBA_ADD
BLEND_RGBA_MAX
BLEND_RGBA_MIN
BLEND_RGBA_MULT
BLEND_RGBA_SUB
BLEND_RGB_ADD
BLEND_RGB_MAX
BLEND_RGB_MIN
BLEND_RGB_MULT
BLEND_RGB_SUB
BLEND_SUB
BUTTON_X1
BUTTON_X2
Color
DOUBLEBUF
FULLSCREEN
GL_ACCELERATED_VISUAL
GL_ACCUM_ALPHA_SIZE
GL_ACCUM_BLUE_SIZE
GL_ACCUM_GREEN_SIZE
GL_ACCUM_RED_SIZE
GL_ALPHA_SIZE
GL_BLUE_SIZE
GL_BUFFER_SIZE
GL_DEPTH_SIZE
GL_DOUBLEBUFFER
GL_GREEN_SIZE
GL_MULTISAMPLEBUFFERS
GL_MULTISAMPLESAMPLES
GL_RED_SIZE
GL_STENCIL_SIZE
GL_STEREO
GL_SWAP_CONTROL
HAT_CENTERED
HAT_DOWN
HAT_LEFT
HAT_LEFTDOWN
HAT_LEFTUP
HAT_RIGHT
HAT_RIGHTDOWN
HAT_RIGHTUP
HAT_UP
HWACCEL
HWPALETTE
HWSURFACE
IYUV_OVERLAY
JOYAXISMOTION
JOYBALLMOTION
JOYBUTTONDOWN
JOYBUTTONUP
JOYHATMOTION
KEYDOWN
KEYUP
KMOD_ALT
KMOD_CAPS
KMOD_CTRL
KMOD_LALT
KMOD_LCTRL
KMOD_LMETA
KMOD_LSHIFT
KMOD_META
KMOD_MODE
KMOD_NONE
KMOD_NUM
KMOD_RALT
KMOD_RCTRL
KMOD_RMETA
KMOD_RSHIFT
KMOD_SHIFT
K_0
K_1
K_2
K_3
K_4
K_5
K_6
K_7
K_8
K_9
K_AMPERSAND
K_ASTERISK
K_AT
K_BACKQUOTE
K_BACKSLASH
K_BACKSPACE
K_BREAK
K_CAPSLOCK
K_CARET
K_CLEAR
K_COLON
K_COMMA
K_DELETE
K_DOLLAR
K_DOWN
K_END
K_EQUALS
K_ESCAPE
K_EURO
K_EXCLAIM
K_F1
K_F10
K_F11
K_F12
K_F13
K_F14
K_F15
K_F2
K_F3
K_F4
K_F5
K_F6
K_F7
K_F8
K_F9
K_FIRST
K_GREATER
K_HASH
K_HELP
K_HOME
K_INSERT
K_KP0
K_KP1
K_KP2
K_KP3
K_KP4
K_KP5
K_KP6
K_KP7
K_KP8
K_KP9
K_KP_DIVIDE
K_KP_ENTER
K_KP_EQUALS
K_KP_MINUS
K_KP_MULTIPLY
K_KP_PERIOD
K_KP_PLUS
K_LALT
K_LAST
K_LCTRL
K_LEFT
K_LEFTBRACKET
K_LEFTPAREN
K_LESS
K_LMETA
K_LSHIFT
K_LSUPER
K_MENU
K_MINUS
K_MODE
K_NUMLOCK
K_PAGEDOWN
K_PAGEUP
K_PAUSE
K_PERIOD
K_PLUS
K_POWER
K_PRINT
K_QUESTION
K_QUOTE
K_QUOTEDBL
K_RALT
K_RCTRL
K_RETURN
K_RIGHT
K_RIGHTBRACKET
K_RIGHTPAREN
K_RMETA
K_RSHIFT
K_RSUPER
K_SCROLLOCK
K_SEMICOLON
K_SLASH
K_SPACE
K_SYSREQ
K_TAB
K_UNDERSCORE
K_UNKNOWN
K_UP
K_a
K_b
K_c
K_d
K_e
K_f
K_g
K_h
K_i
K_j
K_k
K_l
K_m
K_n
K_o
K_p
K_q
K_r
K_s
K_t
K_u
K_v
K_w
K_x
K_y
K_z
LIL_ENDIAN
MOUSEBUTTONDOWN
MOUSEBUTTONUP
MOUSEMOTION
NOEVENT
NOFRAME
NUMEVENTS
OPENGL
OPENGLBLIT
PREALLOC
QUIT
RESIZABLE
RLEACCEL
RLEACCELOK
Rect
SCRAP_BMP
SCRAP_CLIPBOARD
SCRAP_PBM
SCRAP_PPM
SCRAP_SELECTION
SCRAP_TEXT
SRCALPHA
SRCCOLORKEY
SWSURFACE
SYSWMEVENT
TIMER_RESOLUTION
USEREVENT
UYVY_OVERLAY
VIDEOEXPOSE
VIDEORESIZE
YUY2_OVERLAY
YV12_OVERLAY
YVYU_OVERLAY
__builtins__
__doc__
__file__
__name__
__package__
color
"""



"""

				if keys[K_SPACE] and keys[K_RCTRL]: #Checks to see of there's a button press
					go = True						# sets the switch to True
					while go == True:				# checks for switch 
						print "Wooo"				# Output
						time.sleep(.05)				# sleeps for a second to allow the input register to think
						for event in pygame.event.get():   # event checking 
							if event.type == KEYUP:		# event type  check
								go = False
"""