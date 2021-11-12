#Vivaan Gupta
#11/11/2021
#Character moving
import os
import pygame as py

os.system('cls')
py.init()

win = py.display.set_mode((800,700))
py.display.set_caption("My Window")

bg=py.image.load("Images\\bgSmaller.jpg")
walkRight = [py.image.load('Images\Pygame-Tutorials-master\Game\\R1.png'), py.image.load('Images\Pygame-Tutorials-master\Game\\R2.png'), py.image.load('Images\Pygame-Tutorials-master\Game\\R3.png'), py.image.load('Images\Pygame-Tutorials-master\Game\\R4.png'), py.image.load('Images\Pygame-Tutorials-master\Game\\R5.png'), py.image.load('Images\Pygame-Tutorials-master\Game\\R6.png'), py.image.load('Images\Pygame-Tutorials-master\Game\\R7.png'), py.image.load('Images\Pygame-Tutorials-master\Game\\R8.png'), py.image.load('Images\Pygame-Tutorials-master\Game\\R9.png')]
walkLeft = [py.image.load('Images\Pygame-Tutorials-master\Game\\L1.png'), py.image.load('Images\Pygame-Tutorials-master\Game\\L2.png'), py.image.load('Images\Pygame-Tutorials-master\Game\\L3.png'), py.image.load('Images\Pygame-Tutorials-master\Game\\L4.png'), py.image.load('Images\Pygame-Tutorials-master\Game\\L5.png'), py.image.load('Images\Pygame-Tutorials-master\Game\\L6.png'), py.image.load('Images\Pygame-Tutorials-master\Game\\L7.png'), py.image.load('Images\Pygame-Tutorials-master\Game\\L8.png'), py.image.load('Images\Pygame-Tutorials-master\Game\\L9.png')]
char = py.image.load('Images\Pygame-Tutorials-master\Game\\standing.png')
x = 50
y = 380
width = 40
height = 60
vel = 5
ObsX = [129,194,236,300,391]
BorX = 50
BorX2 = ObsX[0]
PlatY = 356-height
PlatY2 = 254-height


clock = py.time.Clock()

isJump = False
jumpCount = 10

left = False
right = False
walkCount = 0

def redrawGameWindow():
    global walkCount
    
    win.blit(bg, (0,0))  
    if walkCount + 1 >= 27:
        walkCount = 0
        
    if left:  
        win.blit(walkLeft[walkCount//3], (x,y))
        walkCount += 1                          
    elif right:
        win.blit(walkRight[walkCount//3], (x,y))
        walkCount += 1
    else:
        win.blit(char, (x, y))
        walkCount = 0
        
    py.display.update() 
    
count = 0
count1 = 1
count2 = 2

run = True

while run:
    clock.tick(27)
    print(py.mouse.get_pos())

    for event in py.event.get():
        if event.type == py.QUIT:
            run = False

    keys = py.key.get_pressed()
    
    if keys[py.K_LEFT] and x > vel: 
        if x > BorX:
            x -= vel
            left = True
            right = False

    elif keys[py.K_RIGHT] and x < 500 - vel - width:  
        if x < BorX2 - width or isJump==True:
            x += vel
            left = False
            right = True
        
    else: 
        left = False
        right = False
        walkCount = 0
        
    if not(isJump):
        if keys[py.K_SPACE]:
            isJump = True
            left = False
            right = False
            walkCount = 0
    else:
        if jumpCount >= -10:
            y -= (jumpCount * abs(jumpCount)) * 0.25
            jumpCount -= 1
            if x>ObsX[count] and y >= PlatY:
                isJump = False
                jumpCount = 10
                BorX = ObsX[count1]
                BorX2 = ObsX[count2]
                count+=1
                count1+=1
                count2+=1
                PlatY = PlatY2
        else: 
            jumpCount = 10
            isJump = False

    redrawGameWindow() 
    
    
py.quit()