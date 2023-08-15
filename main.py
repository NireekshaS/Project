import os
import pygame
import tkinter as tk
from tkinter import filedialog

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("500x300")
        self.root.config(bg= 'black')
        # Initialize Pygame
        pygame.init()

        # Music Player Variables
        self.music_file = None
        self.playing = False

        # Create GUI Elements
        self.load_button = tk.Button(self.root, text="Load Song", command=self.load_song)
        self.load_button.pack()

        self.play_button = tk.Button(self.root, text="Play", command=self.play_music)
        self.play_button.pack()

        self.pause_button = tk.Button(self.root, text="Pause", command=self.pause_music)
        self.pause_button.pack()

        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop_music)
        self.stop_button.pack()

        self.volume_slider = tk.Scale(self.root, from_=0, to=1, resolution=0.1, orient=tk.HORIZONTAL, label="Volume", command=self.set_volume)
        self.volume_slider.pack()

        self.song_info_label = tk.Label(self.root, text="No song loaded.")
        self.song_info_label.pack()

    def load_song(self):
        self.music_file = filedialog.askopenfilename(defaultextension=".mp3", filetypes=[("MP3 Files", "*.mp3"), ("All Files", "*.*")])
        if self.music_file:
            pygame.mixer.music.load(self.music_file)
            self.song_info_label.config(text=os.path.basename(self.music_file))

    def play_music(self):
        if self.music_file:
            pygame.mixer.music.play()
            self.playing = True

    def pause_music(self):
        if self.playing:
            pygame.mixer.music.pause()
            self.playing = False

    def stop_music(self):
        if self.playing:
            pygame.mixer.music.stop()
            self.playing = False

    def set_volume(self, volume):
        pygame.mixer.music.set_volume(float(volume))


if __name__ == "__main__":
    root = tk.Tk()
    music_player = MusicPlayer(root)
    root.mainloop()
