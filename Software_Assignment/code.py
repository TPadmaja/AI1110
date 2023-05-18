import random
import os
import pygame

def list_songs(directory):
    playlist = []
    for file in os.listdir(directory):
        if file.endswith(".mp3"):
            song_path = os.path.join(directory, file)
            playlist.append(song_path)

    random.shuffle(playlist)
    return playlist

def play_song(song):
    pygame.mixer.music.load(song)
    pygame.mixer.music.play()

def main():
    pygame.mixer.init()
    while True:
        playlist = list_songs("Audios")
        paused = 0 
        for song in playlist:
            play_song(song)
            while (pygame.mixer.music.get_busy() or paused): #paused need to be added otherwise if paused getbusy becomes false and it goes to next song
                command = input("Enter command (p: pause, r: resume, q: quit, n: next song): ")
                if command == 'p':
                    pygame.mixer.music.pause()
                    paused = 1 
                elif command == 'r':
                    pygame.mixer.music.unpause()
                elif command == 'q':
                    pygame.mixer.music.stop()
                    return
                elif command == 'n':
                    pygame.mixer.music.stop()
                    break
                else :
                    print("you have entered an undefined command")

main()

