#Vivaan Gupta
#10/25/2021
#Learning Fonts and Blit

import os, pygame, random

from pygame.constants import MOUSEBUTTONDOWN
os.system('cls')

#Constants:

#Page values
MainMenu = 1
Instructions = 2
Level1 = 3
Level2 = 4
Settings = 5
Scoreboard = 6
ScreenSize = 7
BackColor = 8


page = MainMenu

#Colors and their values
red=(255,0,0)
green=(0,255,0) 
blue=(0,0,255)
purple=(150,0,150) 
orange=(255,128,0) 
yellow=(255,255,0)
black = (0,0,0)
white=(255,255,255)
width=800
height = 800
currentBackColor = white

#Square values
hbox = 25
wbox = 25
mouse_pos = 0
y_min = 190
y_max = 215

#List of what to display on different menus
Setting_messages = ["SCREEN SIZE", "BACKGROUND COLOR"]  
menu_messages=["INTRUCTIONS","LEVEL 1","LEVEL 2", "SETTINGS","SCOREBOARD", "EXIT"]

#Functions:

#Title print function
def displayTitle(title):    
    pygame.time.delay(100)
    text = title_font.render(title,1,black)
    #win.blit(text,(width/2-text.get_width()/2, height/2-text.get_height()/2))
    win.blit(text,(width/2-text.get_width()/2,30))
    pygame.display.update()
    pygame.time.delay(100)

#Subtitle print function
def displayMenu(specific_menu):  
    pygame.time.delay(100)
    x = 70
    y = 190
    square.x = x
    square.y = y
    for i in range (0, len(specific_menu)):
        word = specific_menu[i]
        pygame.draw.rect(win, orange, square)
        text = subtitle_font.render(word,1,black)
        win.blit(text,(x+wbox+10, y-10))
        pygame.display.flip()
        pygame.time.delay(100)
        y +=100
        square.y = y

#Display back text 
def displayBack():  
    pygame.time.delay(100)
    text = subtitle_font.render("BACK",1,black)
    win.blit(text,(50,720))
    pygame.display.update()
    pygame.time.delay(100)

#Display a certain page, and whether or not to display back also
def printPage(title,back):  
    win.fill(currentBackColor)
    displayTitle(title)
    if back:
        displayBack()

#Pygame initialize:

#Set up window
pygame.init()
win = pygame.display.set_mode((width,height))
pygame.display.set_caption("Game")

#Fonts 
title_font=pygame.font.SysFont('comicsans',80)
subtitle_font=pygame.font.SysFont('comicsans',30, italic=True)

#Square Draw
square = pygame.Rect(10,10, wbox, hbox)

#Initialize mouse_pos
mouse_pos = (0,0)

#Update window
pygame.display.flip()

#Display Menu at start
win.fill(currentBackColor)
displayTitle("MENU")
displayMenu(menu_messages)

#Main loop
run = True
while run:

    #If you click the X on the window
    pygame.time.delay(10)
    for eve in pygame.event.get():
        if eve.type == pygame.QUIT:
            run = False
        
        #If you clicked
        if eve.type == pygame.MOUSEBUTTONDOWN:
            mouse_pressed = pygame.mouse.get_pressed()
            if mouse_pressed[0]:
                mouse_pos = pygame.mouse.get_pos()

    #Main Menu Navigation
    if page == MainMenu:
        if mouse_pos[0]>=70 and mouse_pos[0]<=230 and mouse_pos[1]>=y_min and mouse_pos[1]<=y_max:
            printPage("INSTRUCTIONS",True)
            page = Instructions
        elif mouse_pos[0]>=70 and mouse_pos[0]<=230 and mouse_pos[1]>=y_min+100 and mouse_pos[1]<=y_max+100:
            printPage("LEVEL 1",True)
            page = Level1
        elif mouse_pos[0]>=70 and mouse_pos[0]<=230 and mouse_pos[1]>=y_min+200 and mouse_pos[1]<=y_max+200:
            printPage("LEVEL 2",True)
            page = Level2
        elif mouse_pos[0]>=70 and mouse_pos[0]<=230 and mouse_pos[1]>=y_min+300 and mouse_pos[1]<=y_max+300:
            printPage("SETTINGS",True)
            displayMenu(Setting_messages)
            page = Settings
        elif mouse_pos[0]>=70 and mouse_pos[0]<=230 and mouse_pos[1]>=y_min+400 and mouse_pos[1]<=y_max+400:
            printPage("SCOREBOARD",True)
            page = Scoreboard
        elif mouse_pos[0]>=70 and mouse_pos[0]<=230 and mouse_pos[1]>=y_min+500 and mouse_pos[1]<=y_max+500:
            break

        #Reset the mouse position
        mouse_pos = (0,0)

    #If you click back when the previous page was Main Menu
    if (page == Instructions or page == Level1 or page == Level2  or page==Scoreboard or page==Settings):
        if mouse_pos[0]>=50 and mouse_pos[0]<=200 and mouse_pos[1]>=720 and mouse_pos[1]<=y_max+800:
            printPage("MENU",False)
            page = MainMenu
            displayMenu(menu_messages)

    #Settings navigation
    if page==Settings:
        if mouse_pos[0]>=70 and mouse_pos[0]<=230 and mouse_pos[1]>=y_min and mouse_pos[1]<=y_max:
            printPage("SCREEN SIZE",True)
            page = ScreenSize
        elif mouse_pos[0]>=70 and mouse_pos[0]<=230 and mouse_pos[1]>=y_min+100 and mouse_pos[1]<=y_max+100:
            printPage("BACKGROUND",True)
            page = BackColor
         
        #Reset the mosue position
        mouse_pos = (0,0)

    #If you click back when Settings was the previous page
    if page == ScreenSize or page == BackColor:
        if mouse_pos[0]>=50 and mouse_pos[0]<=200 and mouse_pos[1]>=720 and mouse_pos[1]<=y_max+800:
            printPage("SETTINGS",True)
            page = Settings
            displayMenu(Setting_messages)

    #Reset the mouse position
    mouse_pos = (0,0)            

pygame.quit()