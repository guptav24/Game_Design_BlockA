#Vivaan Gupta
#10/25/2021
#Learning Fonts and Blit

import os, pygame, random

from pygame.constants import MOUSEBUTTONDOWN, K_w
os.system('cls')

#Files:

#Images
arrow_up = pygame.image.load("Images\\arrow_up.png")
arrow_down = pygame.image.load("Images\\arrow_down.png")
arrow_left = pygame.image.load("Images\\arrow_left.png")
arrow_right = pygame.image.load("Images\\arrow_right.png")
bg = pygame.image.load("Images\\background_big.jpg")
check_mark = pygame.image.load("Images\\check.png")
x_mark = pygame.image.load("Images\\x.png")
arrows = [arrow_up,arrow_down,arrow_left,arrow_right]   #Array for all the arrows
arrow_check = []    #Empty array that becomes the chosen arrows
arrow_type_check = []

maxScore = 0
maxScore2 = 0

#Instructions file
myInstructions = open('instructions.txt','w')   #Opening file
#Text in the file
myInstructions.write("The game will flash you a couple images of images. Memorize these.\nAfter, use the arrow keys on the keyboard and retype what you saw.\nAnother set of arrows will flash. Repeat until you get it incorrect.\nThe different levels change the amount of time the arrows are displayed.")
myInstructions.close()  

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
arrow_type1 = 9
arrow_type2 = 0
next = 10
arrow_typeup = False
arrow_typedown = False
arrow_typeleft= False
arrow_typeright=False

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
currentBackColor = black

#Square values
hbox = 25
wbox = 25
mouse_pos = 0
y_min = 190
y_max = 215

#List of what to display on different menus
Setting_messages = ["SCREEN SIZE", "BACKGROUND COLOR"]  
menu_messages=["INTRUCTIONS","LEVEL 1","LEVEL 2", "SETTINGS","SCOREBOARD", "EXIT"]
size_messages = ["800x800","700x700","600x600"]
backColor_messages=["RED", "BLUE","GREEN","BLACK"]

#Game variables
round = 1
counter = 0
score = 0
score2 = 0

#Functions:

def updateScores(): #Funvtion to update scores
    myScoreboard=open('scoreboard.txt','w')
    myScoreboard.write('High Score (LVL1): '+str(maxScore)+'\n High Score (LVL2): '+str(maxScore2))
    myScoreboard.close()


def level1_game():
    win.blit(bg,(0,0))
    pygame.display.set_caption("Memory Game")
    pygame.display.flip()

def level2_game():
    win.blit(bg,(0,0))
    pygame.display.set_caption("Memory Game")
    pygame.display.flip()

#Title print function
def displayTitle(title):    
    pygame.time.delay(100)
    text = title_font.render(title,1,white)
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
        text = subtitle_font.render(word,1,white)
        win.blit(text,(x+wbox+10, y-10))
        pygame.display.flip()
        pygame.time.delay(100)
        y +=100
        square.y = y

#Display back text 
def displayBack():  
    pygame.time.delay(100)
    text = subtitle_font.render("BACK",1,white)
    win.blit(text,(50,height-80))
    pygame.display.update()
    pygame.time.delay(100)

def displayScoreboard():
    height = 170
    myScoreboard=open('scoreboard.txt','r')
    for line in myScoreboard.readlines():
        text = subtitle_font.render(line,1,white)
        win.blit(text, (width/2-text.get_width()/2,height))
        pygame.display.update()
        pygame.time.delay(100)
        height+=60
    myScoreboard.close()

def displayInstructionText():
    height = 170
    myInstructions=open('instructions.txt','r')
    for line in myInstructions.readlines():
        text = instruction_font.render(line,1,white)
        win.blit(text, (40,height))
        pygame.display.update()
        pygame.time.delay(100)
        height+=60
    myInstructions.close()

#Change screen size
def changeScreenSize(width_new,height_new):
    global width 
    width= width_new
    global height
    height = height_new
    win = pygame.display.set_mode((width_new,height_new))
    win.fill(currentBackColor)
    printPage("SCREEN SIZE",True)
    displayMenu(size_messages)
    pygame.display.update
    

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
instruction_font = pygame.font.SysFont('comicsans',20)

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
check = 1

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
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            arrow_typeleft = True
            arrow_typeup = False
            arrow_typedown = False
            arrow_typeright=False
        if keys[pygame.K_RIGHT]:
            arrow_typeright = True
            arrow_typeup = False
            arrow_typedown = False
            arrow_typeleft= False
        if keys[pygame.K_DOWN]:
            arrow_typedown = True
            arrow_typeup = False
            arrow_typeleft= False
            arrow_typeright=False
        if keys[pygame.K_UP]:
            arrow_typeup = True
            arrow_typedown = False
            arrow_typeleft= False
            arrow_typeright=False

        #Main Menu Navigation
        if page == MainMenu:
            if mouse_pos[0]>=70 and mouse_pos[0]<=230 and mouse_pos[1]>=y_min and mouse_pos[1]<=y_max:
                printPage("INSTRUCTIONS",True)
                page = Instructions
            elif mouse_pos[0]>=70 and mouse_pos[0]<=230 and mouse_pos[1]>=y_min+100 and mouse_pos[1]<=y_max+100:
                level1_game()
                page = Level1
                displayBack()
            elif mouse_pos[0]>=70 and mouse_pos[0]<=230 and mouse_pos[1]>=y_min+200 and mouse_pos[1]<=y_max+200:
                level2_game()
                displayBack()
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

        #Level 1 Game
        if page==Level1 and check == 1:
            check += 1
            x = 0
            for i in range (round): #How many times it prints arrows
                rand_arrow = random.choice(arrows)  #Chooses random arrow
                arrow_check.append(rand_arrow)  #Puts that arrow into the check array
                win.blit(rand_arrow,((width/(round*2))-50+x,height/2-50)) #Places the arrows centered based on how many arrows there are
                x+=width/round
            pygame.display.flip()
            pygame.time.delay(1000)
            win.blit(bg,(0,0))
            displayBack()
            pygame.display.flip()
            x=0
            page = arrow_type1   #Next page to type and check arrows

        #Level 2 Game
        if page == Level2 and check==1:
            check += 1
            x = 0
            for i in range (round): #How many times it prints arrows
                rand_arrow = random.choice(arrows)  #Chooses random arrow
                arrow_check.append(rand_arrow)  #Puts that arrow into the check array
                win.blit(rand_arrow,((width/(round*2))-50+x,height/2-50)) #Places the arrows centered based on how many arrows there are
                x+=width/round
            pygame.display.flip()
            pygame.time.delay(600)
            win.blit(bg,(0,0))
            displayBack()
            pygame.display.flip()
            x=0
            page = arrow_type2   #Next page to type and check arrows

        if page == arrow_type1:
            win.blit(bg,(0,0))
            displayBack()
            pygame.display.flip()
            if counter<round:
                if arrow_typeup==True:
                    arrow_type_check.append(arrow_up)
                    win.blit(arrow_up,(width/2-50,height/2-50))
                    pygame.display.flip()
                    pygame.time.delay(200)
                    counter+=1
                if arrow_down==True:
                    arrow_type_check.append(arrow_down)
                    win.blit(arrow_down,(width/2-50,height/2-50))
                    pygame.display.flip()
                    pygame.time.delay(200)
                    counter+=1
                if arrow_left==True:
                    arrow_type_check.append(arrow_left)
                    win.blit(arrow_left,(width/2-50,height/2-50))
                    pygame.display.flip()
                    pygame.time.delay(200)
                    counter+=1
                if arrow_right==True:
                    arrow_type_check.append(arrow_right)
                    win.blit(arrow_right,(width/2-50,height/2-50))
                    pygame.display.flip()
                    pygame.time.delay(200)
                    counter+=1
            if counter == round:
                if arrow_type_check == arrow_check:
                    score+=1
                    win.blit(bg, (0,0))
                    win.blit(check_mark,(width/2-250,height/2-250))
                    next_text = subtitle_font.render("NEXT",1,white)
                    win.blit(next_text,(width-150,height-80))
                    pygame.display.update()
                    page = next
                if arrow_type_check != arrow_check:
                    round = 1
                    check = 1
                    counter = 0
                    win.blit(bg, (0,0))
                    arrow_type_check.clear()
                    arrow_check.clear()
                    win.blit(x_mark,(width/2-250,height/2-250))
                    pygame.display.update()
                    pygame.time.delay(1000)
                    win.blit(bg,(0,0))
                    score_text = subtitle_font.render("YOUR SCORE: " + str(score),1,white)
                    win.blit(score_text,(width/2-score_text.get_width()/2,height/2))
                    pygame.display.update()
                    pygame.time.delay(1500)
                    printPage("MENU",False)
                    page = MainMenu
                    displayMenu(menu_messages)
                    if score>=maxScore:  #Checks high score
                        maxScore = score
                        updateScores()
                    myScoreboard=open('scoreboard.txt','w')
                    myScoreboard.write('High Score (LVL1): '+str(maxScore)+'\n High Score (LVL2): '+str(maxScore2))
                    myScoreboard.close()
                    score = 0
        
        if page == arrow_type2:
            win.blit(bg,(0,0))
            displayBack()
            pygame.display.flip()
            if counter<round:
                if arrow_typeup==True:
                    arrow_type_check.append(arrow_up)
                    win.blit(arrow_up,(width/2-50,height/2-50))
                    pygame.display.flip()
                    pygame.time.delay(200)
                    counter+=1
                if arrow_down==True:
                    arrow_type_check.append(arrow_down)
                    win.blit(arrow_down,(width/2-50,height/2-50))
                    pygame.display.flip()
                    pygame.time.delay(200)
                    counter+=1
                if arrow_left==True:
                    arrow_type_check.append(arrow_left)
                    win.blit(arrow_left,(width/2-50,height/2-50))
                    pygame.display.flip()
                    pygame.time.delay(200)
                    counter+=1
                if arrow_right==True:
                    arrow_type_check.append(arrow_right)
                    win.blit(arrow_right,(width/2-50,height/2-50))
                    pygame.display.flip()
                    pygame.time.delay(200)
                    counter+=1
            if counter == round:
                if arrow_type_check == arrow_check:
                    score2+=1
                    win.blit(bg, (0,0))
                    win.blit(check_mark,(width/2-250,height/2-250))
                    next_text = subtitle_font.render("NEXT",1,white)
                    win.blit(next_text,(width-150,height-80))
                    pygame.display.update()
                    page = next
                if arrow_type_check != arrow_check:
                    round = 1
                    check = 1
                    counter = 0
                    win.blit(bg, (0,0))
                    arrow_type_check.clear()
                    arrow_check.clear()
                    win.blit(x_mark,(width/2-250,height/2-250))
                    pygame.display.update()
                    pygame.time.delay(1000)
                    win.blit(bg,(0,0))
                    score2_text = subtitle_font.render("YOUR SCORE: " + str(score),1,white)
                    win.blit(score2_text,(width/2-score2_text.get_width()/2,height/2))
                    pygame.display.update()
                    pygame.time.delay(1500)
                    printPage("MENU",False)
                    page = MainMenu
                    displayMenu(menu_messages)
                    if score2>=maxScore2:  #Checks high score
                        maxScore2 = score2
                        updateScores()
                    myScoreboard=open('scoreboard.txt','w')
                    myScoreboard.write('High Score (LVL1): '+str(maxScore)+'\nHigh Score (LVL2): '+str(maxScore2))
                    myScoreboard.close()
                    score2 = 0



        if page == next:
            if mouse_pos[0]>=width-200 and mouse_pos[0]<=width and mouse_pos[1]>=height-80 and mouse_pos[1]<=y_max+height:
                level1_game()
                if round <7:
                    round+=1
                check = 1
                counter = 0
                arrow_type_check.clear()
                arrow_check.clear()
                win.blit(bg,(0,0))
                displayBack()
                pygame.display.flip()
                pygame.time.delay(1000)
                page = Level1
                


        #If you click back when the previous page was Main Menu
        if (page == Instructions or page == Level1 or page == Level2  or page==Scoreboard or page==Settings or page==arrow_type1 or page==arrow_type2):
            if mouse_pos[0]>=50 and mouse_pos[0]<=200 and mouse_pos[1]>=height-80 and mouse_pos[1]<=y_max+height:
                printPage("MENU",False)
                page = MainMenu
                displayMenu(menu_messages)

        #Show the Instructions
        if page==Instructions:
            displayInstructionText()

        if page==Scoreboard:
            displayScoreboard()

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
            if mouse_pos[0]>=50 and mouse_pos[0]<=200 and mouse_pos[1]>=height-80 and mouse_pos[1]<=y_max+height:
                printPage("SETTINGS",True)
                page = Settings
                displayMenu(Setting_messages)

        #Screen Size Menu
        if page== ScreenSize:
            displayMenu(size_messages)
            if mouse_pos[0]>=70 and mouse_pos[0]<=230 and mouse_pos[1]>=y_min and mouse_pos[1]<=y_max:
                changeScreenSize(800,800)
            elif mouse_pos[0]>=70 and mouse_pos[0]<=230 and mouse_pos[1]>=y_min+100 and mouse_pos[1]<=y_max+100:
                changeScreenSize(700,700)
            elif mouse_pos[0]>=70 and mouse_pos[0]<=230 and mouse_pos[1]>=y_min+200 and mouse_pos[1]<=y_max+200:
                changeScreenSize(600,600)

        #Background Color Menu
        if page == BackColor:
            displayMenu(backColor_messages)
            if mouse_pos[0]>=70 and mouse_pos[0]<=230 and mouse_pos[1]>=y_min and mouse_pos[1]<=y_max:
                currentBackColor = red
                printPage("BACKGROUND",True)
            elif mouse_pos[0]>=70 and mouse_pos[0]<=230 and mouse_pos[1]>=y_min+100 and mouse_pos[1]<=y_max+100:
                currentBackColor = blue
                printPage("BACKGROUND",True)
            elif mouse_pos[0]>=70 and mouse_pos[0]<=230 and mouse_pos[1]>=y_min+200 and mouse_pos[1]<=y_max+200:
                currentBackColor = green
                printPage("BACKGROUND",True)
            elif mouse_pos[0]>=70 and mouse_pos[0]<=230 and mouse_pos[1]>=y_min+300 and mouse_pos[1]<=y_max+300:
                currentBackColor = black
                printPage("BACKGROUND",True)

        #Reset the mouse position
        mouse_pos = (0,0)     

        arrow_typeup = False
        arrow_typedown = False
        arrow_typeleft= False
        arrow_typeright=False       

updateScores()
pygame.quit()