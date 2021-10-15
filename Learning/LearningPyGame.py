#Vivaan Gupta
#10/15/2021
#Learning display
#Learning opening windows
#Learning chagning window size
#Learning basic game loop

import pygame, os
os.system('cls')
#First thing to do is initialize pygame

pygame.init()
check = True
height = ""
width = ""
colors = {'black':(0,0,0), 'red':(255,0,0), 'green':(0,255,0), 'blue':(0,0,255), 'white':(255,255,255), 'purple':(150,0,150)}
while check:
    height = input("Height of the window (100-1000): ")
    width = input("Width of the window (100-1000): ")
    color = input("What color do you want? (Black, Red, Green, Blue, White, Purple): ")

    try: 
        height = int(height)
        width = int(width)
        if (height>= 0 and height <=1000) and (width>= 0 and width <=1000):
            check = False
    except ValueError:
        print("Try again")
        check = True

color = color.lower()
color = colors.get(str(color))
window=pygame.display.set_mode((height,width))   #Set up color
window.fill(color)
window= pygame.display.flip()   #Refresh window with new color

#Change title of window
pygame.display.set_caption("My Game Window")
window= pygame.display.flip()

run=True

#Main loop for the game:
while run:
    pygame.time.delay(1000)
    for case in pygame.event.get():
        if case.type == pygame.QUIT:
            run=False

pygame.quit()