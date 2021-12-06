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

BorList = [50,129,194,236,300,391,484,570,653,762]
BorLeft = BorList[0]
BorRight = BorList[1]
platforms = [356-height, 254-height,202-height,158-height]


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
    
count1 = 1
count2 = 2
count_plat = 0

run = True

while run:
    clock.tick(27)
    print(py.mouse.get_pos())

    for event in py.event.get():
        if event.type == py.QUIT:
            run = False

    keys = py.key.get_pressed()
    
    if keys[py.K_LEFT] and x > vel: 
        if x > BorLeft or isJump==True:
            x -= vel
            left = True
            right = False

    elif keys[py.K_RIGHT] and x < 500 - vel - width:  
        if x < BorRight - width or isJump==True:
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
            if x>BorRight and y >= platforms[count_plat]:
                isJump = False
                jumpCount = 10
                BorLeft = BorList[count1]
                BorRight = BorList[count2]
                count1+=1
                count2+=1
                count_plat+=1
        else: 
            jumpCount = 10
            isJump = False
        
            

    redrawGameWindow() 
    
    
py.quit()