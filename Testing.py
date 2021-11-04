#Vivaan Gupta
#10/25/2021
#Learning Fonts and Blit

import os, pygame, random

from pygame.constants import MOUSEBUTTONDOWN
os.system('cls')

pygame.init()

MainMenu = True
Instructions = False
Level1 = False
Level2 = False
Settings = False
Scoreboard = False
ScreenSize = False
BackColor = False
ObjColor = False
counter = 0

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

Setting_messages = ["SCREEN SIZE", "BACKGROUND COLOR","OBJECT COLOR","SOUNDS (ON/OFF)"]    #Setting Messages
menu_messages=["INTRUCTIONS","LEVEL 1","LEVEL 2", "SETTINGS","SCOREBOARD", "EXIT"]

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

count = 0
mouse_pos = (0,0)
run = True
pygame.display.flip()
while run:
    print("asdjas")
    pygame.time.delay(10)
    for eve in pygame.event.get():
        if eve.type == pygame.QUIT:
            run=False
            pygame.quit()

    if eve.type == pygame.MOUSEBUTTONDOWN:
        mouse_pressed=pygame.mouse.get_pressed()
        if mouse_pressed[0]:
            mouse_pos = pygame.mouse.get_pos()

            
    
        if MainMenu:
            win.fill(currentBackColor)
            displayTitle("MENU")
            displayMenu(menu_messages)
            if mouse_pos[0]>=70 and mouse_pos[0]<=230 and mouse_pos[1]>=y_min and mouse_pos[1]<=y_max:
                MainMenu = False
                Instructions = True
                

            elif mouse_pos[0]>=70 and mouse_pos[0]<=230 and mouse_pos[1]>=y_min+100 and mouse_pos[1]<=y_max+100:
                MainMenu = False
                Level1 = True
                

            elif mouse_pos[0]>=70 and mouse_pos[0]<=230 and mouse_pos[1]>=y_min+200 and mouse_pos[1]<=y_max+200:
                MainMenu = False
                Level2 = True
                

            elif mouse_pos[0]>=70 and mouse_pos[0]<=230 and mouse_pos[1]>=y_min+300 and mouse_pos[1]<=y_max+300:
                MainMenu = False
                Settings = True
                

            elif mouse_pos[0]>=70 and mouse_pos[0]<=230 and mouse_pos[1]>=y_min+400 and mouse_pos[1]<=y_max+400:
                MainMenu = False
                Scoreboard = True
                

            elif mouse_pos[0]>=70 and mouse_pos[0]<=230 and mouse_pos[1]>=y_min+500 and mouse_pos[1]<=y_max+500:
                pygame.quit()
                run=False

        if Instructions:
            win.fill(currentBackColor)
            displayTitle("INSTRUCTIONS")
            displayBack()
            print("as")
            for eve in pygame.event.get():
                if eve.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pressed=pygame.mouse.get_pressed()
                    if mouse_pressed[0]:
                        Ins_mouse_pos = pygame.mouse.get_pos()
                        if Ins_mouse_pos[0]>=50 and Ins_mouse_pos[0]<=200 and Ins_mouse_pos[1]>=720 and Ins_mouse_pos[1]<=y_max+800:
                            Instructions = False
                            MainMenu = True

pygame.quit()