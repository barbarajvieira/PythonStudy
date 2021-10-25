#Faça um programa em python que abra e reproduza o audio de um arquivo MP3
# copiar o arquivo mp3 p pycharm (tem q estar na msm pasta)

import pygame
pygame.init()
pygame.mixer.music.load('ex21.mp3')
pygame.mixer.music.play()
pygame.ecent.wait()



