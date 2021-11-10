#Vivaan Gupta
#10/25/2021
#Learning Fonts and Blit

import os, pygame, random

from pygame.constants import MOUSEBUTTONDOWN
os.system('cls')

pygame.init()

#Page values
MainMenu = 1
Instructions = 2
Level1 = 3
Level2 = 4
Settings = 5
Scoreboard = 6
ScreenSize = 7
BackColor = 8
ObjColor = 9
Sounds = 10

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


#List of what to display on different menus
Setting_messages = ["SCREEN SIZE", "BACKGROUND COLOR","OBJECT COLOR","SOUNDS"]  
menu_messages=["INTRUCTIONS","LEVEL 1","LEVEL 2", "SETTINGS","SCOREBOARD", "EXIT"]
Menu_sels = [Instructions, Level1, Level2, Settings, Scoreboard]
Settings_sels = [ScreenSize, BackColor, ObjColor, Sounds]


#Set up window
win = pygame.display.set_mode((width,height))
pygame.display.set_caption("Game")

#Fonts 
title_font=pygame.font.SysFont('comicsans',80)
subtitle_font=pygame.font.SysFont('comicsans',30, italic=True)

#Square
hbox = 25
wbox = 25
mouse_pos = 0
y_min = 190
y_max = 215
square = pygame.Rect(10,10, wbox, hbox)

#Initialize mouse_pos
mouse_pos = (0,0)

def displayTitle(title):    #Title print function
    pygame.time.delay(100)
    text = title_font.render(title,1,black)
    #win.blit(text,(width/2-text.get_width()/2, height/2-text.get_height()/2))
    win.blit(text,(width/2-text.get_width()/2,30))
    pygame.display.update()
    pygame.time.delay(100)

def displayMenu(specific_menu):  #Subtitle print function
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

def displayBack():  #Display back text 
    pygame.time.delay(100)
    text = subtitle_font.render("BACK",1,black)
    win.blit(text,(50,720))
    pygame.display.update()
    pygame.time.delay(100)

def printPage(title,back):  #Display a certain page, and whether or not to display back also
    win.fill(currentBackColor)
    displayTitle(title)
    if back:
        displayBack()

def pageClicks(menu,sel,mouse_pos):
    page = MainMenu
    if mouse_pos[0]>=70 and mouse_pos[0]<=230 and mouse_pos[1]>=y_min and mouse_pos[1]<=y_max:
            printPage((menu_messages[0]),True)
            page = sel[0]
    elif mouse_pos[0]>=70 and mouse_pos[0]<=230 and mouse_pos[1]>=y_min+100 and mouse_pos[1]<=y_max+100:
        printPage((menu_messages[1]),True)
        page = sel[1]
    elif mouse_pos[0]>=70 and mouse_pos[0]<=230 and mouse_pos[1]>=y_min+200 and mouse_pos[1]<=y_max+200:
        printPage((menu_messages[2]),True)
        page = sel[2]
    elif mouse_pos[0]>=70 and mouse_pos[0]<=230 and mouse_pos[1]>=y_min+300 and mouse_pos[1]<=y_max+300:
        printPage((menu_messages[3]),True)
        if menu == menu_messages:
            menu = Setting_messages
            sel = Settings_sels
            displayMenu(Setting_messages)
        page = sel[3]
    elif mouse_pos[0]>=70 and mouse_pos[0]<=230 and mouse_pos[1]>=y_min+400 and mouse_pos[1]<=y_max+400:
        printPage((menu_messages[4]),True)
        page = sel[4]
    elif mouse_pos[0]>=70 and mouse_pos[0]<=230 and mouse_pos[1]>=y_min+500 and mouse_pos[1]<=y_max+500:
        printPage((menu_messages[5]),True)
        page = sel[5]
        if menu == menu_messages:
            pygame.quit()
    return page

run = True

#Update window
pygame.display.flip()

#Display Menu at start
win.fill(currentBackColor)
displayTitle("MENU")
displayMenu(menu_messages)

while run:

    #If you click the X on the window
    pygame.time.delay(10)
    for eve in pygame.event.get():
        if eve.type == pygame.QUIT:
            run=False
            pygame.quit()
        
        #If you clicked
        if eve.type == pygame.MOUSEBUTTONDOWN:
            mouse_pressed = pygame.mouse.get_pressed()
            if mouse_pressed[0]:
                mouse_pos = pygame.mouse.get_pos()

    #Main Menu Navigation
    if page == MainMenu:
        page = pageClicks(menu_messages, Menu_sels, mouse_pos)

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
        page = pageClicks(Setting_messages, Settings_sels, mouse_pos)
         
        #Reset the mosue position
        mouse_pos = (0,0)

    #If you click back when Settings was the previous page
    if page == ScreenSize or page == BackColor or page == ObjColor or page == Sounds:
        if mouse_pos[0]>=50 and mouse_pos[0]<=200 and mouse_pos[1]>=720 and mouse_pos[1]<=y_max+800:
            printPage("SETTINGS",True)
            page = Settings
            displayMenu(Setting_messages)

    #Reset the mouse position
    mouse_pos = (0,0)
            

pygame.quit()