#Vivaan Gupta
#10/25/2021
#Learning Fonts and Blit

import os, pygame, random
os.system('cls')

pygame.init()

black = (0,0,0)
white=(255,255,255)
width=800
height = 800
win = pygame.display.set_mode((width,height))
pygame.display.set_caption("Setting Window")

#title_font=pygame.font.SysFont(name, size, bold=False, italic=False)
title_font=pygame.font.SysFont('comicsans',80)
sub_title=pygame.font.SysFont('comicsans',40, italic=True)

def displayTitle(title):
    pygame.time.delay(100)
    text = title_font.render(title,1,white)
    #win.blit(text,(width/2-text.get_width()/2, height/2-text.get_height()/2))
    win.blit(text,(width/2-text.get_width()/2,30))
    pygame.display.update()
    pygame.time.delay(100)

def displaySub(subTitle,ySub):
    pygame.time.delay(100)
    text = title_font.render(subTitle,1,white)
    win.blit(text,(30,ySub))
    pygame.display.update()
    pygame.time.delay(100)

run=True
while run:
    pygame.time.delay(10)
    for eve in pygame.event.get():
        if eve.type == pygame.QUIT:
            run=False
            pygame.quit()
    displayTitle("SETTINGS")
    pygame.time.delay(300)
    ySub = 150
    displaySub("Window Size", ySub)
    ySub+=150
    displaySub("Background Color", ySub)
    ySub+=150
    displaySub("Object Colors", ySub)
    ySub+=150
    displaySub("SOUNDS ON/OFF", ySub)
    #Print Window Size, Background color, Object Colors, ON/OFF

pygame.quit()