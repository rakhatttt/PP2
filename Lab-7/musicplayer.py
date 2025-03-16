import pygame
import os

pygame.init()

screen= pygame.display.set_mode((400,300))

music_file=["/Users/admin/Downloads/Қайрат Нұртас - Сен менің адамымсың (OST Брат или Брак 3).mp3","/Users/admin/Downloads/sadraddin-zhauap-bar-ma_(muzzonas.ru).mp3"]

track=0

pygame.mixer.music.load(music_file[track])

def play_m():
    pygame.mixer.music.play()

def stop_m():
    pygame.mixer.music.stop()

def next():
    global track

    track = (track+1)%len(music_file)
    pygame.mixer.music.load(music_file[track])
    play_m()

def prev():
    global track 
    track = (track-1)%len(music_file)
    pygame.mixer.music.load(music_file[track])
    play_m()

run=True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                play_m()
            elif event.key == pygame.K_s:
                stop_m()
            if event.key == pygame.K_n:
                next()
            if event.key == pygame.K_b:
                prev()

pygame.quit()
