#Vivaan Gupta
#10/15/2021
#Learning display
#Learning opening windows
#Learning chagning window size
#Learning basic game loop

import pygame, os, random
os.system('cls')
#First thing to do is initialize pygame

pygame.init()
check = True
height = 600
width = 700

colors = {                  #Colors and their values
          'red':(255,0,0), 
          'green':(0,255,0), 
          'blue':(0,0,255), 
          'purple':(150,0,150), 
          'orange':(255,128.0), 
          'yellow':(255,255,0)
          }
colorNames = ['red','green','blue','purple','orange','yellow']
randColor = random.choice(colorNames)   #Picks a random color

# while check:
#     height = input("Height of the window (100-1000): ")
#     width = input("Width of the window (100-1000): ")

#     try: 
#         height = int(height)
#         width = int(width)
#         if (height< 100 or height >1000) or (width< 100 or width >1000):    #Makes sure he dimensions are correct
#             print("The numbers have to be between 100-1000")
#             check = True
#         else:
#             check = False
#     except ValueError:
#         print("Try again")
#         check = True

# color = colors.get(str(randColor))  #Make the color the random color
color = random.choice(list(colors.keys()))
window=pygame.display.set_mode((width,height))   #Set up color
window.fill(color)
pygame.display.flip()   #Refresh window with new color

#Change title of window
pygame.display.set_caption("My Game Window")    #Name of the window
pygame.display.flip()
hbox=50
wbox=50    #Dimensions of box
rspeed=20 #Speed of moving rectangle
cspeed = 20
randx=int(random.randrange(0,width))
randy=int(random.randrange(0,height))
yc = width/2
xc = height/2
rcircle = hbox/2
rect=pygame.Rect(randx, randy, wbox, hbox) #Places rectangle
pygame.draw.rect(window, (0,0,0), rect)    #Draws rectangle
pygame.draw.circle(window, (255,255,255),(xc, yc), rcircle)
pygame.display.flip()

run=True

#Main loop for the game:
while run==True:
    pygame.time.delay(100) #Delay of starting the game
    for case in pygame.event.get():
        if case.type == pygame.QUIT:    #Quits program if window closed
            run=False
    #How to get position of the mouse
    #x,y=pygame.mouse.get_pos()
    #print("( "+str(x)+" , "+str(y)+" )")
    keyPressed = pygame.key.get_pressed()
    #Sees key presses and moves
    if keyPressed[pygame.K_UP]:
        if rect.y < 0:
            rect.y = height
        else:
            rect.y -= rspeed
    if keyPressed[pygame.K_DOWN]:
        if rect.y>height:
            rect.y = 0
        else:
            rect.y += rspeed
    if keyPressed[pygame.K_LEFT]:
        if rect.x < 0:
            rect.x=width
        else:
            rect.x -= rspeed
    if keyPressed[pygame.K_RIGHT]:
        if rect.x>width:
            rect.x=0
        else:
            rect.x += rspeed

    if keyPressed[pygame.K_w] and yc>rcircle:
            yc -= cspeed
    if keyPressed[pygame.K_s] and yc<height-rcircle:
            yc += cspeed
    if keyPressed[pygame.K_a] and xc>rcircle:
            xc -= cspeed
    if keyPressed[pygame.K_d] and xc<width-rcircle:
            xc += cspeed   
    window.fill(color)

    point = (xc,yc)     #Collide point
    collide = rect.collidepoint(point)  #Sees if it is collides
    if collide:
        rcircle = rcircle+(hbox/2)
        randx=int(random.randrange(0,width))
        randy=int(random.randrange(0,height))
        rect=pygame.Rect(randx, randy, wbox, hbox)      #Resets the square
        cspeed-=2   #Decreases circle speed
    pygame.draw.rect(window, (0,0,0), rect)
    pygame.draw.circle(window, (255,255,255),(xc, yc), rcircle)
    pygame.display.flip()
    if rcircle == hbox*2+hbox:
        pygame.quit
        print("CIRCLE WINS!")
        break

pygame.quit()