# Koch snowflake


import pygame
import math
black = (0,0,0)
screen = pygame.display.set_mode((650,650))
screen.fill(black)
angle = 0
#global angle
#def centerscreen(wt=500,ht=500):
#	x = (wt/2)
#	y = (ht/2)
#	return (x,y)
centrx = 650/2
centry = 650/2
#def init_angle(angle):
#	global angle
#	return (angle)
def line_draw(screen,(x1,y1),(x2,y2)):
	white = (255,255,255)
	pygame.draw.line(screen,white,(x1,y1),(x2,y2),1)
	
def fwrd(forward):
	global centrx
	global centry
	x1 = centrx
	y1 = centry
#	start = x1 , y1
	x2 = centrx + (math.cos((math.pi* angle)/180)*forward)

	y2 = centry + (math.sin((math.pi* angle)/180)*forward)
#	end = x2, y2
	line_draw(screen,(x1,y1),(x2,y2))
	centrx = x2
	centry = y2
def right(angle1):
	global angle
	angle =  angle + angle1
def left(angle1):
	right(-1*angle1)

def Koch_snowflake(length,angle1):
	fwrd(length)
	right(angle1)
	fwrd(length)
	left(angle1*2)
	fwrd(length)
	right(angle1)
	fwrd(length)
#def snow_flake(screen,range, angle1):
#3	if range == 0:
#		Koch_snowflake(2,angle1)
#	else:
#		snow_flake(screen,range-1,angle1)
#		right(angle1)
#		snow_flake(screen,range-1,angle1)
#		left(angle1*2)
#		snow_flake(screen,range-1,angle1)
#		right(angle1)
#		snow_flake(screen,range-1,angle1)

def koch(screen,range1,angle1):
	if range1 == 0:
		Koch_snowflake(1,angle1)
	else:
		for angle in [60, -120, 60, 0]:
			koch(screen, range1-1, angle1)
			right(angle)
def snow_flake_full(screen,range1,angle1):
	
	for i in range(4):	
		koch(screen,range1,angle1)
		left(angle1*2)

def main():
	wt = 1000
	ht = 1000
	pygame.init()
#	black = pygame.Color(0,0,0)
#	screen = pygame.display.set_mode((wt,ht))
#	screen.fill(black)
	snow_flake_full(screen,4,60)
	pygame.display.update()
	wait = raw_input("press any key to quit...")
	pygame.quit()

main()		
