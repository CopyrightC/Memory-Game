import pygame
import random
from pygame import mixer
import sys

pygame.init()

screen = pygame.display.set_mode((1260,900))
pygame.display.set_caption('MEMORY GAME')

run = True

clock = pygame.time.Clock()
dis_txt = "You will shown some random number and you'll"
dis_txt2 = 'be given 10 seconds to memorise them.'
dis_txt3 = 'Then enter the number which you had memorised'
time_strt = 6000
score = 0

input_num_Str = ''
rand_time = 5000
mixer.music.load('music.mp3')
start = True
re = False
randm = True
input_usr = False
over = False
inp_rect = pygame.Rect(500 , 390 , 160 , 40)
num1 = 1
num2 = 10
#colors

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
grey = pygame.Color('grey12')

mus = True
class functions():

    def __init__(self):
        pass

    def screen_text(self,text,color,x,y,size):
        global txt
        font = pygame.font.Font('freesansbold.ttf',size)
        txt = font.render(text,True,color)
        screen.blit(txt, (x,y))

    def game_started(self):

        global start
        global time_strt
        global re

        while start:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            time_strt -= clock.tick(60)

            if time_strt <= 0:
                re = True
                start = False

            shourya.screen_text(dis_txt, grey, 260, 410, 34)
            shourya.screen_text(dis_txt2, grey, 320, 450, 34)
            shourya.screen_text(dis_txt3, grey, 240, 490, 34)
            pygame.display.update()

    def ready(self):

        global re
        ready = 2000

        while re:
            screen.fill(white)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            shourya.screen_text('Ready?',black,610,450,34)

            ready -= clock.tick(60)
            if ready <= 0:
                re = False
            pygame.display.update()

    def random_number(self,n1,n2):

        global randm
        global input_usr
        global rand_time
        global num
        num = random.randint(n1,n2)
        while randm:
            screen.fill(white)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            rand_time -= clock.tick(60)
            if rand_time <= 0:
                input_usr = True
                randm = False

            shourya.screen_text(str(num),black,630,450,33)
            pygame.display.update()
            clock.tick(60)

    def usr_input(self):

        global input_usr
        global inp_rect
        global input_num_Str
        global randm
        global num
        global num1
        global num2
        global rand_time
        global over
        global score

        while input_usr:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        input_num_Str = input_num_Str[:-1]
                    elif event.key == pygame.K_RETURN:
                        if input_num_Str == str(num):
                            num1 *= 10
                            num2 *= 10
                            score += 1
                            randm = True
                            input_usr = False
                            rand_time = 5000
                            input_num_Str = ''
                        else:
                            over = True
                            input_usr = False

                    else:
                        input_num_Str += event.unicode

            screen.fill(white)
            shourya.screen_text('Score : '+str(score),black,20,20,40)
            pygame.draw.rect(screen,(100,100,200),inp_rect,2)

            shourya.screen_text('ENTER THE NUMBER', black, 470, 230, 34)

            txt1 = pygame.font.Font('freesansbold.ttf',32)
            here = txt1.render(input_num_Str,True,black)
            screen.blit(here,(inp_rect.x + 10 ,inp_rect.y+5))
            inp_rect.w = here.get_width() + 16


            pygame.display.update()


    def game_over(self):

        global mus
        global num

        mixer.music.set_volume(0)

        if mus:
            mixer.Sound('gameover.wav').play()

            mus = False
        screen.fill(white)
        shourya.screen_text('GAME OVER',(200,0,0),420,400,63)
        shourya.screen_text('Score : ' + str(score), black, 540, 480, 40)

        pygame.display.update()
        clock.tick(60)





shourya = functions()

while run:

    mixer.music.play(-1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(white)
    shourya.game_started()
    shourya.ready()
    shourya.random_number(num1,num2)
    shourya.usr_input()
    if over:
        shourya.game_over()
    pygame.display.update()
    clock.tick(60)