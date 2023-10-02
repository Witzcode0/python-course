import pygame
import os
import random

musics_list = os.listdir("musics")

def playMusic(music_file):
    # Initialize pygame
    pygame.init()

    # Create a pygame mixer object
    pygame.mixer.init()
    pygame.mixer.music.load(music_file)

    # Set the volume (optional)
    pygame.mixer.music.set_volume(1)  # Adjust the volume between 0.0 and 1.0

    # Start playing the music
    pygame.mixer.music.play()

    # Keep the script running to let the music play
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    # Clean up when done
    pygame.quit()

def loop():
    while True:
        for music in musics_list:
            # Load the music file you want to play
            music_file = "musics/" + music  # Replace with the path to your music file
            playMusic(music_file)

def shuffle_():
    random.shuffle(musics_list)
    for music in musics_list:
        if music.endswith(".mp3"):
            music_file = "musics/" + music
            playMusic(music_file)
        else:
            print("There is not avaialable mp3 files")

shuffle_()