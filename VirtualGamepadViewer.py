#Imports
import os 
import sys
import glob
import pickle
from tkinter import filedialog, messagebox
import tkinter as tk
import pygame
import keyboard

#Set up tkinter for alerts and directy grabber
root = tk.Tk()
root.withdraw()
root.iconphoto(False, tk.PhotoImage(file='icon.png'))
                                
#Quit function
def quit():
	keyboard.unhook_all()
	pygame.display.quit()
	pygame.quit()
	sys.exit()


#Main Loop
while True:
	#initializer Pygame, this will reset pygame when switching skings
	pygame.init() 

	#Setting icon
	icon = pygame.image.load("icon.png")
	pygame.display.set_icon(icon)


	#Loading a skin
	try:
		#skin directory is stored in pickle attempt to open
		path = pickle.load(open("save.p", "rb"))
		#attempt to load the background image
		bg = pygame.image.load(path + '/background.png')

	#if either of these fail ask the user to select a new directory	
	except (OSError, IOError, pygame.error, TypeError) as e:
		#Get the current skins directory
		tempPath = filedialog.askdirectory(initialdir=os.getcwd() + "\\Skins\\",)
		#if they click cancel close the program
		if(tempPath is  ""):
			path = os.getcwd() + "\\Skins\\NES\\"
		else:
			path = tempPath
			
		#save the directory in a pickle
		pickle.dump(path, open( "save.p", "wb" ) ) 
		try:
			#attempt again to load background
			bg = pygame.image.load(path + '/background.png')
		except (OSError, IOError, pygame.error) as e:
			#alert the user that they have chosen a bad directory and close the program
			messagebox.showinfo("Error", "Bad Directory: Couldn't find background.png")
			quit()

	#Set up the main window
	mainDisplay = pygame.display.set_mode(bg.get_size())
	pygame.display.set_caption('Virtual Gamepad Viewer')

	bg = bg.convert()
	mainDisplay.blit(bg, (0,0))
	pygame.display.flip()

	#This array stores all the .png images along with their keycodes
	#example:
	#images[0][0] = [[43], [12,54]] keycodes that activate the image
	#images[0][1] will be the pygame image object
	images = []

	#search for every png file in the chose directory
	for file in glob.glob(path + "/*.png"):
		#remove the file extensions and parse into nested array
		#"37-37+38-35" -> [[37],[37,38],[35]]
		keysToBePressed = file[len(path)+1:-4].split("-")
		keysToBePressed = [i.split("+") for i in keysToBePressed] 
		try:
			#try and conver each str to an int, which will be the keycode to show the image
			keysCodesToBePressed = [list(map(int, i)) for i in keysToBePressed]
			#if this suceeds load the coresponding image and add it to the list
			tempObj = [keysCodesToBePressed, pygame.image.load(file).convert_alpha()]
			images.append(tempObj)
		except(ValueError):
			#this is incase there are any improperly formatted images
			#background.png will also trigger this but this is intended
			pass

	#Iintialize the boolean and font for showing keycode
	printingCodes = False
	font = pygame.font.Font(pygame.font.get_default_font(), int(bg.get_rect().size[1]/6))

	#function that is called on a keyboard event(Key up or key down)
	def drawImage(e):
		#redraw the background
		mainDisplay.blit(bg, (0,0))

		#for each image and keycode pair

		for imageObject in images:
			#example:
			# imageObject[0] = [[37],[48,49]]
			#check to see if 37 or (48 and 49) are pressed
			for i in imageObject[0]:
				pressed = True
				for j in i:
					if(not keyboard.is_pressed(j)):
						pressed = False
				#if any required key combo is pressed display the image
				if(pressed):
					mainDisplay.blit(imageObject[1], (0,0))
		
		#if printing codes
		if(printingCodes):
			#grab every currently pressed key
			line = ', '.join(str(code) for code in keyboard._pressed_events)
			#render and display the text
			textsurface = font.render(line, False, (0, 0, 0), (255,255,255))
			mainDisplay.blit(textsurface,(0,0))

		#update the display
		pygame.display.flip()

	#add drawImage to the keyboard hook
	keyboard.hook(drawImage)

	

	#Initalize clock this will limit the framerate
	clock = pygame.time.Clock();

	#program restarts right before a new skin is selected
	restarting = False
	while not restarting:
		#limit framerate to 60fps
		clock.tick(60) 

		#main pygame event loop
		for event in pygame.event.get():

			#if the X button is pressed exit the game
			if event.type == pygame.QUIT:
				#unhook keyboard and quit pygame, and python
				quit()

			#pygame mouse input
			if event.type == pygame.MOUSEBUTTONUP:
				#chose new skin on right click
				if event.button == 3:
					#set path to none and overwrite current pickle
					#this will cause a type error on restart
					#which will bring up the choose directory dialouge
					path = None
					pickle.dump(path, open( "save.p", "wb" ) )
					restarting = True

				#on left cklick toggle printing keycodes
				if event.button == 1:
					printingCodes = not printingCodes
