#Vivaan Gupta
#11/8/2021
#Moving object

import os
import pygame as py

os.system('cls')

#first thing
py.init()

WIDTH = 800
HEIGHT = 800

boulder=py.Rect(WIDTH-300,HEIGHT-300,100,300)

#create window
height= 700
width = 800
colors = {'red':(150,0,0),'green':(0,200,0), 'blue':(0,0,255), 'purple':(150, 0, 150), 'white':(255,255,255), 'black':(0,0,0) }
screen=py.display.set_mode((width, height))
myColor= colors.get('purple')
boulderColor = colors.get('blue')
screen.fill(myColor)
py.display.set_caption("Moving Square")
py.display.flip()
bg=py.image.load("Images\\bgSmaller.jpg")
#parameters to define our square
x=width/2
y=height/2
wbox=25
hbox=25
#creating out object square
square=py.Rect(x,y,wbox, hbox )
#draw object
objColor=colors.get('red')
py.draw.rect(screen, objColor, square)
py.draw.rect(screen,boulderColor,boulder)
screen.blit(bg,(0,0))
py.display.update()
#create speed to move the object on the screen
speed = 7
run=True #Variable to control the main loop
#boolean to check for jump
Jumping=False
jumpCount=10
while run:
    py.time.delay(50) #milliseconds
    for anyThing in py.event.get():
        if anyThing.type == py.QUIT:
            run =False
            
    keyPressed= py.key.get_pressed()
    
    if keyPressed[py.K_RIGHT] and square.x <WIDTH-wbox-speed :
        if square.colliderect(boulder):
            square.x-=3
        else:
            square.x += speed     
    if keyPressed[py.K_LEFT] and square.x>speed-3:
        if square.colliderect(boulder):
            square.x+=3
        else:
            square.x -= speed

    if not(Jumping):
        if keyPressed[py.K_DOWN] and square.y <HEIGHT-hbox-speed:
            if square.colliderect(boulder):
                square.y-=3
            else:
                square.y += speed
        if keyPressed[py.K_UP] and square.y>speed-3:
            square.y -= speed
        if keyPressed[py.K_SPACE]:
            Jumping = True

    else:
        if jumpCount >= -10:
            square.y -= jumpCount*abs(jumpCount)*0.5
            jumpCount -= 1
        else:
            jumpCount = 10
            Jumping = False

    # if(py.Rect.collidepoint(boulder,(square.x+wbox/2,square.y))):
    #     move=False
    #     square.x = square.x-wbox
    #     move=True

    screen.blit(bg,(0,0))
    py.draw.rect(screen,boulderColor,boulder)
    py.draw.rect(screen, objColor, square)
    py.display.flip()
py.quit()
